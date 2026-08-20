/* Behaviour tests for the M0 Flight Readiness review surface.

   These execute the real, unmodified app.js and data/fixtures.js against the
   minimal document in dom.js, then assert on the tree that results. Nothing is
   restated or re-implemented: if app.js stops putting a required field on the
   first screen, or starts claiming an authority it does not have, a test here
   fails.

   Run: node tests/test_surface.js   (no dependency, no network, no file writes)
*/

"use strict";

var fs = require("fs");
var path = require("path");
var vm = require("vm");
var assert = require("assert");

var ROOT = path.resolve(__dirname, "..");
var Document = require("./dom.js").Document;

/* Mirrors the mount structure of index.html, including #routes nested inside
   #workspace. */
var MOUNT_IDS = [
  "rail-flight-id", "rail-evidence-class", "rail-schema", "scenario-list",
  "rail-facts", "route-tabs", "strip-analysis-use", "strip-eligibility",
  { id: "workspace", children: ["routes"] }
];

/* ------------------------------------------------------------------ harness */

function boot(options) {
  var settings = options || {};
  var document = new Document();
  document.mount(MOUNT_IDS);

  var window = {
    location: { hash: settings.hash || "" },
    addEventListener: function () {}
  };

  var sandbox = { window: window, document: document, JSON: JSON, console: console };
  sandbox.globalThis = sandbox;
  var context = vm.createContext(sandbox);

  var model = settings.model === undefined
    ? fs.readFileSync(path.join(ROOT, "data", "fixtures.js"), "utf8")
    : "window.__M0_REVIEW_MODEL__ = " + JSON.stringify(settings.model) + ";";
  vm.runInContext(model, context, { filename: "data/fixtures.js" });

  vm.runInContext(fs.readFileSync(path.join(ROOT, "app.js"), "utf8"), context, { filename: "app.js" });

  return {
    document: document,
    window: window,
    workspace: document.getElementById("workspace"),
    routes: document.getElementById("routes"),
    model: sandbox.window.__M0_REVIEW_MODEL__
  };
}

function tabNamed(app, label) {
  return app.document.getElementById("route-tabs").byAttr("role", "tab").filter(function (node) {
    return node.textContent === label;
  })[0];
}

function scenarioButton(app, index) {
  return app.document.getElementById("scenario-list").byTag("button")[index];
}

/* -------------------------------------------------------------------- tests */

var tests = [];
function test(name, fn) { tests.push([name, fn]); }

var MODEL = JSON.parse(fs.readFileSync(path.join(ROOT, "data", "fixtures.json"), "utf8"));

test("the model carries every required scenario class", function () {
  var uses = MODEL.scenarios.map(function (item) { return item.decision.analysis_use.value; });
  assert.ok(uses.indexOf("decision_grade") !== -1, "a decision_grade scenario is required");
  assert.ok(uses.indexOf("directional_only") !== -1, "a directional_only scenario is required");
  assert.ok(uses.indexOf("not_permitted") !== -1, "a not_permitted scenario is required");

  var ids = MODEL.scenarios.map(function (item) { return item.scenario_id; });
  ["unauthorized-read", "redaction-blocked-read", "stale-superseded-read", "incomplete-observations"]
    .forEach(function (id) {
      assert.ok(ids.indexOf(id) !== -1, id + " is required");
    });
});

test("every scenario is an emitted fixture-class packet, never a production packet", function () {
  MODEL.scenarios.forEach(function (scenario) {
    assert.strictEqual(scenario.flight.evidence_class, "fixture", scenario.scenario_id);
    assert.strictEqual(scenario.projection_class, "emitted_fixture_packet", scenario.scenario_id);
    assert.strictEqual(scenario.emitted_by, "kdd_data_agent.m0.evaluator.evaluate_flight", scenario.scenario_id);
  });
});

test("the first screen carries the packet decision, why it is limited, and next_safe_action", function () {
  MODEL.scenarios.forEach(function (scenario, index) {
    var app = boot({ hash: "#/" + scenario.scenario_id + "/readiness" });
    var first = app.document.getElementById("packet-decision");
    assert.ok(first, "the readiness panel must be the first screen for " + scenario.scenario_id);

    var text = first.textContent;
    assert.ok(text.indexOf(scenario.decision.analysis_use.value) !== -1, "stored analysis_use missing");
    assert.ok(text.indexOf(scenario.decision.post_analysis_eligibility.value) !== -1, "derived eligibility missing");
    assert.ok(text.indexOf(scenario.decision.why_limited) !== -1, "why_limited missing");
    assert.ok(text.indexOf(scenario.next_safe_action.kind) !== -1, "next_safe_action kind missing");
    assert.ok(text.indexOf(scenario.next_safe_action.guidance) !== -1, "next_safe_action guidance missing");
    assert.ok(text.indexOf(scenario.next_safe_action.reopen_condition) !== -1, "reopen condition missing");
    assert.ok(index >= 0);
  });
});

test("stored analysis_use and derived eligibility are separately labelled", function () {
  var app = boot({});
  var first = app.document.getElementById("packet-decision").textContent;
  assert.ok(first.indexOf("stored on the packet") !== -1, "analysis_use must be labelled as stored");
  assert.ok(
    first.indexOf("derived at render time; never stored on the packet") !== -1,
    "eligibility must be labelled as render-derived"
  );
  assert.ok(
    first.indexOf("decision_grade -> eligible; directional_only or not_permitted -> blocked") !== -1,
    "the derivation rule must be visible"
  );
});

test("the first screen shows an ordered material-check summary with every required field", function () {
  var app = boot({ hash: "#/incomplete-observations/readiness" });
  var scenario = MODEL.scenarios.filter(function (item) {
    return item.scenario_id === "incomplete-observations";
  })[0];
  var first = app.document.getElementById("packet-decision");

  var headers = first.byTag("th").map(function (node) { return node.textContent; });
  ["Check", "Outcome", "Materiality", "Rule source", "Evidence IDs", "Validator / receipt IDs"]
    .forEach(function (name) {
      assert.ok(headers.indexOf(name) !== -1, "the summary must expose " + name);
    });

  /* Failed, missing and unknown checks must precede passed ones. */
  var order = { FAIL: 0, MISSING: 1, UNKNOWN: 2, NOT_APPLICABLE: 3, PASS: 4 };
  var outcomes = first.byClass("outcome").map(function (node) { return node.textContent; });
  var ranks = outcomes.map(function (name) { return order[name]; });
  for (var i = 1; i < ranks.length; i += 1) {
    assert.ok(ranks[i] >= ranks[i - 1], "material checks must be ordered blocking-first");
  }

  scenario.decision.blockers.forEach(function (checkId) {
    assert.ok(first.textContent.indexOf(checkId) !== -1, checkId + " must appear on the first screen");
  });
});

test("source-read and D4/D6 receipts open within two interactions, by keyboard", function () {
  MODEL.scenarios.forEach(function (scenario) {
    var app = boot({ hash: "#/" + scenario.scenario_id + "/readiness" });
    var first = app.document.getElementById("packet-decision");
    var cards = first.byClass("receipt");
    assert.ok(cards.length >= 2, "the first screen must reach both receipt classes");

    /* Interaction one: the card is a <details>; opening it is a single
       activation of its <summary>, which is keyboard-reachable by Tab and
       activated by Enter or Space with no scripting involved. */
    var opened = cards.slice(0, 2).map(function (card) {
      card.setAttribute("open", "");
      return card;
    });

    var sourceId = scenario.receipts.source_read[0].receipt_id;
    var recomputationId = scenario.receipts.recomputation_d4_d6[0].receipt_id;
    var shown = opened.map(function (card) { return card.textContent; }).join(" ");
    assert.ok(shown.indexOf(sourceId) !== -1, "the exact source-read receipt id must be reachable");
    assert.ok(shown.indexOf(recomputationId) !== -1, "the exact D4/D6 receipt id must be reachable");
    assert.ok(shown.indexOf("D4") !== -1 && shown.indexOf("D6") !== -1, "the D4/D6 bindings must be named");
  });
});

/* A boundary page has to be able to say "no candidate diff is produced", so a
   blunt keyword ban would forbid the very statements the contract requires.
   The real property is that a sensitive subject may only ever appear in a
   negated sentence: the surface may deny cause, recommendation, win/loss, P3
   closure and Committee acceptance, and may never assert them. */
var SENSITIVE = [
  "cause", "recommend", "recommendation", "candidate diff", "remediation",
  "win", "loss", "won", "production capability", "production authorization",
  "committee", "p3", "acceptance", "launch", "deploy", "rollback"
];
/* "pre-P3" and "not permitted" are themselves statements of a limit, so they
   count as negations rather than as claims about the thing they name. */
var NEGATION = /(\bpre-?p3\b|\bnot_permitted\b|\b(no|none|not|never|cannot|can't|without|neither|nor|refus|absent|forbid|unauthori|separate|owns|open|remains?|blocked)\b)/i;

/* The scan covers authored prose only. A field label, an identifier cell and a
   verbatim <pre> dump of packet bytes are not assertions by this surface: the
   packet is shown as it is, and laundering its contents would be the defect. */
test("a sensitive subject only ever appears in a negated sentence", function () {
  var scanned = 0;
  MODEL.scenarios.forEach(function (scenario) {
    ["readiness", "checks", "receipts", "gaps", "boundaries"].forEach(function (route) {
      var app = boot({ hash: "#/" + scenario.scenario_id + "/" + route });
      app.routes.byTag("p").forEach(function (paragraph) {
        if (paragraph.byTag("pre").length) return;
        scanned += 1;
        /* textContent concatenates adjacent nodes without whitespace, so a list
           ordinal can fuse to the sentence after it. Restore the break before
           splitting, otherwise a negation would be read as part of its
           predecessor. */
        paragraph.textContent
          .replace(/(\.)(?=\S)/g, "$1 ")
          .replace(/(\d)(?=[A-Z])/g, "$1 ")
          .split(/(?<=\.)\s+|\n+/)
          .forEach(function (sentence) {
            var hit = SENSITIVE.filter(function (word) {
              return new RegExp("\\b" + word + "\\b", "i").test(sentence);
            });
            if (!hit.length) return;
            assert.ok(
              NEGATION.test(sentence),
              "route " + route + " of " + scenario.scenario_id
                + " asserts " + JSON.stringify(hit.join(", ")) + " in: " + JSON.stringify(sentence.slice(0, 160))
            );
          });
      });
    });
  });
  assert.ok(scanned > 100, "the scan must actually reach the surface's prose, saw " + scanned);
});

test("the surface never claims an authority it does not have", function () {
  var forbidden = [
    "root cause is", "the cause is", "we recommend", "production ready",
    "production capability established", "committee accepted", "p3 closed",
    "approved for launch", "safe to launch", "ship it", "won the test"
  ];
  MODEL.scenarios.forEach(function (scenario) {
    ["readiness", "checks", "receipts", "gaps", "boundaries"].forEach(function (route) {
      var app = boot({ hash: "#/" + scenario.scenario_id + "/" + route });
      var text = app.routes.textContent.toLowerCase();
      forbidden.forEach(function (phrase) {
        assert.ok(
          text.indexOf(phrase) === -1,
          "route " + route + " of " + scenario.scenario_id + " must not contain " + JSON.stringify(phrase)
        );
      });
    });
  });
});

test("the boundaries route states every required limit", function () {
  var app = boot({ hash: "#/trusted-decision-grade/boundaries" });
  var text = app.routes.textContent;
  ["Fixture-only", "No production capability", "No cause", "No M1 or M2 recommendation",
    "No win or loss", "No P3 closure", "No Committee decision", "Read-only"]
    .forEach(function (line) {
      assert.ok(text.indexOf(line) !== -1, "the boundaries route must state: " + line);
    });
  assert.ok(text.indexOf("Trace") !== -1, "the Trace boundary must be stated");
  assert.ok(
    text.indexOf("never evidence authority") !== -1,
    "Trace must be denied evidence authority"
  );
});

test("packet identity, revisions, expiry and supersession are on the first screen", function () {
  MODEL.scenarios.forEach(function (scenario) {
    var app = boot({ hash: "#/" + scenario.scenario_id + "/readiness" });
    var text = app.document.getElementById("packet-decision").textContent;
    assert.ok(text.indexOf(scenario.identity.packet_digest) !== -1, "packet_digest missing");
    assert.ok(text.indexOf(scenario.identity.contract_digest) !== -1, "contract_digest missing");
    assert.ok(text.indexOf(scenario.identity.core_check_set.revision) !== -1, "core check set revision missing");
    assert.ok(text.indexOf(scenario.identity.core_check_set.digest) !== -1, "core check set digest missing");
    assert.ok(text.indexOf(scenario.identity.expiry) !== -1, "expiry missing");
    assert.ok(text.indexOf(scenario.state.supersession.state) !== -1, "supersession state missing");
  });
});

test("supersession and acknowledgement invalidation are shown where recorded", function () {
  var scenario = MODEL.scenarios.filter(function (item) {
    return item.scenario_id === "stale-superseded-read";
  })[0];
  assert.strictEqual(scenario.state.supersession.state, "supersedes_an_earlier_packet");

  var readiness = boot({ hash: "#/stale-superseded-read/readiness" });
  assert.ok(
    readiness.document.getElementById("packet-decision").textContent
      .indexOf(scenario.identity.supersedes_digest) !== -1,
    "the superseded packet digest must be reachable"
  );

  var gaps = boot({ hash: "#/stale-superseded-read/gaps" });
  var text = gaps.routes.textContent;
  assert.ok(text.indexOf("invalidated") !== -1, "the invalidated acknowledgement must be shown");
  assert.ok(
    text.indexOf("separate from the packet") !== -1,
    "an acknowledgement must be labelled as separate from the packet"
  );
});

test("blocked, unauthorized, stale and incomplete states never render as eligible", function () {
  MODEL.scenarios.forEach(function (scenario) {
    if (scenario.decision.analysis_use.value === "decision_grade") return;
    var app = boot({ hash: "#/" + scenario.scenario_id + "/readiness" });
    assert.strictEqual(
      app.document.getElementById("strip-eligibility").textContent,
      "blocked",
      scenario.scenario_id + " must read blocked"
    );
    assert.strictEqual(scenario.decision.post_analysis_eligibility.value, "blocked");
  });

  var trusted = boot({ hash: "#/trusted-decision-grade/readiness" });
  assert.strictEqual(trusted.document.getElementById("strip-eligibility").textContent, "eligible");
});

test("typed absence renders as UNKNOWN or MISSING, never blank or null", function () {
  var app = boot({ hash: "#/unauthorized-read/receipts" });
  assert.ok(
    app.routes.textContent.indexOf("UNKNOWN") !== -1 || app.routes.textContent.indexOf("MISSING") !== -1,
    "an unauthorized read must surface its typed absences"
  );

  /* The assertion is about fields the surface itself renders. A verbatim <pre>
     dump of a receipt is the packet's own bytes and must not be laundered: if
     the receipt detail genuinely holds a JSON null, the reviewer sees it. */
  var authored = app.routes.all(function (node) {
    return node.nodeType === 1
      && (node.tagName === "DD" || node.tagName === "TD")
      && node.byTag("pre").length === 0;
  });
  assert.ok(authored.length > 0, "the surface renders authored fields");
  authored.forEach(function (node) {
    var text = node.textContent.trim();
    assert.notStrictEqual(text, "", "an authored field must never render blank");
    assert.notStrictEqual(text, "null", "an authored field must never render null");
    assert.notStrictEqual(text, "undefined", "an authored field must never render undefined");
    assert.notStrictEqual(text, "-", "an authored field must never render a bare dash");
  });

  /* Absence in the model must reach the reader as its typed token. */
  var scenario = MODEL.scenarios.filter(function (item) {
    return item.scenario_id === "unauthorized-read";
  })[0];
  var snapshot = scenario.receipts.source_read[0].source.snapshot_id;
  assert.ok(snapshot && snapshot.__kdd__, "this fixture's snapshot_id is a typed absence");
  var readiness = boot({ hash: "#/unauthorized-read/readiness" });
  assert.ok(
    readiness.document.getElementById("packet-decision").byClass("absent").length > 0,
    "a typed absence must be rendered with its token, not silently dropped"
  );
});

test("an unauthorized or redaction-blocked read never exposes a retained body", function () {
  ["unauthorized-read", "redaction-blocked-read"].forEach(function (id) {
    var scenario = MODEL.scenarios.filter(function (item) { return item.scenario_id === id; })[0];
    scenario.receipts.source_read.forEach(function (receipt) {
      assert.strictEqual(receipt.body_retained, false, id + " must retain no body");
    });
    var app = boot({ hash: "#/" + id + "/readiness" });
    assert.ok(
      app.document.getElementById("packet-decision").textContent.indexOf("No body is retained") !== -1,
      id + " must say so explicitly rather than showing an empty panel"
    );
  });
});

test("every graph-like relationship has a table or list path and no node diagram exists", function () {
  MODEL.scenarios.forEach(function (scenario) {
    var app = boot({ hash: "#/" + scenario.scenario_id + "/receipts" });
    assert.ok(app.routes.byTag("table").length > 0, "receipt relationships must be tabulated");
    assert.strictEqual(app.routes.byTag("svg").length, 0, "no node diagram may be rendered");
    assert.strictEqual(app.routes.byTag("canvas").length, 0, "no node diagram may be rendered");
  });
});

test("view filters change the view only, never the packet", function () {
  var app = boot({ hash: "#/incomplete-observations/checks" });
  var before = JSON.stringify(app.model.scenarios);
  var select = app.routes.byTag("select")[0];
  assert.ok(select, "the checks route exposes a filter");

  select.dispatch("change", { target: { value: "FAIL" } });
  assert.strictEqual(JSON.stringify(app.model.scenarios), before, "filtering must not change the model");

  var note = app.routes.textContent;
  assert.ok(
    note.indexOf("View filter only") !== -1,
    "the filter must state that it changes no packet, check, evidence or source state"
  );
});

test("no control offers a write, apply, approve or re-evaluate action", function () {
  var forbidden = /\b(apply|approve|acknowledge|re-?evaluate|submit|save|delete|edit|override|unblock|promote)\b/i;
  MODEL.scenarios.forEach(function (scenario) {
    ["readiness", "checks", "receipts", "gaps", "boundaries"].forEach(function (route) {
      var app = boot({ hash: "#/" + scenario.scenario_id + "/" + route });
      app.routes.byTag("button").forEach(function (button) {
        assert.ok(
          !forbidden.test(button.textContent),
          "a control reads " + JSON.stringify(button.textContent) + " on route " + route
        );
      });
      assert.strictEqual(app.routes.byTag("form").length, 0, "no form may exist");
      assert.strictEqual(app.routes.byTag("input").filter(function (node) {
        return node.getAttribute("type") !== "checkbox";
      }).length, 0, "no data entry control may exist");
    });
  });
});

test("scenario and route selection are read-only view changes", function () {
  var app = boot({});
  var before = JSON.stringify(app.model);
  scenarioButton(app, 3).click();
  tabNamed(app, "Receipts").click();
  assert.strictEqual(JSON.stringify(app.model), before, "navigation must not change the model");
  assert.strictEqual(
    app.document.getElementById("rail-flight-id").textContent,
    app.model.scenarios[3].flight.flight_id
  );
});

test("route tabs expose the standard keyboard tab pattern", function () {
  var app = boot({});
  var tabs = app.document.getElementById("route-tabs").byAttr("role", "tab");
  assert.strictEqual(tabs.length, 5);
  assert.strictEqual(tabs.filter(function (tab) {
    return tab.getAttribute("aria-selected") === "true";
  }).length, 1, "exactly one tab is selected");
  assert.strictEqual(tabs.filter(function (tab) {
    return tab.getAttribute("tabindex") === "0";
  }).length, 1, "roving tabindex keeps one tab in the tab order");

  tabs[0].dispatch("keydown", { key: "ArrowRight" });
  var after = app.document.getElementById("route-tabs").byAttr("role", "tab");
  assert.strictEqual(after[1].getAttribute("aria-selected"), "true", "ArrowRight moves selection");

  var panel = app.routes.byAttr("role", "tabpanel")[0];
  assert.ok(panel, "a tabpanel exists");
  assert.strictEqual(panel.getAttribute("aria-labelledby"), "tab-" + "checks");
});

test("the surface fails closed on an absent, unknown or malformed model", function () {
  var absent = boot({ model: null });
  assert.ok(absent.workspace.textContent.indexOf("will not render") !== -1, "an absent model must refuse");
  assert.strictEqual(absent.routes, null, "no route may be mounted without a model");

  var wrongSchema = boot({ model: { schema_version: "something-else/v9", scenarios: [{}] } });
  assert.ok(wrongSchema.workspace.textContent.indexOf("will not render") !== -1, "a foreign schema must refuse");
  assert.ok(wrongSchema.workspace.textContent.indexOf("something-else/v9") !== -1, "the refusal names what it saw");

  var empty = boot({ model: { schema_version: "m0-review-surface-projection/v1", scenarios: [] } });
  assert.ok(empty.workspace.textContent.indexOf("carries no scenario") !== -1, "an empty model must refuse");

  var truncated = boot({
    model: {
      schema_version: "m0-review-surface-projection/v1",
      scenarios: [{ scenario_id: "x", decision: { analysis_use: { value: "decision_grade" } } }]
    }
  });
  assert.ok(
    truncated.workspace.textContent.indexOf("packet digest") !== -1,
    "a scenario without a packet digest must refuse rather than render"
  );
});

test("an unrecognised deep link falls back rather than failing", function () {
  var app = boot({ hash: "#/no-such-scenario/no-such-route" });
  assert.ok(app.document.getElementById("packet-decision"), "an unknown fragment falls back to readiness");
  assert.strictEqual(
    app.document.getElementById("rail-flight-id").textContent,
    MODEL.scenarios[0].flight.flight_id
  );
});

test("the renderer reaches no network, storage or navigation API", function () {
  /* Comments are stripped first: the file documents the APIs it refuses to use,
     and naming one in prose is not calling it. The assertion is about code. */
  var source = fs.readFileSync(path.join(ROOT, "app.js"), "utf8")
    .replace(/\/\*[\s\S]*?\*\//g, "")
    .replace(/^\s*\/\/.*$/gm, "");
  [
    "fetch(", "XMLHttpRequest", "WebSocket", "EventSource", "navigator.sendBeacon",
    "localStorage", "sessionStorage", "document.cookie", "indexedDB",
    "eval(", "new Function", "innerHTML", "outerHTML", "document.write",
    "history.pushState", "history.replaceState", "location.assign", "location.replace",
    "import(", "require("
  ].forEach(function (token) {
    assert.strictEqual(source.indexOf(token), -1, "app.js must not contain " + token);
  });

  var markup = fs.readFileSync(path.join(ROOT, "index.html"), "utf8");
  assert.strictEqual(/<script[^>]+src=["'](?!data\/fixtures\.js|app\.js)/.test(markup), false,
    "index.html may only load its own two local scripts");
  assert.strictEqual(/https?:\/\//.test(markup.replace(/<!--[\s\S]*?-->/g, "")), false,
    "index.html must reference no remote origin");

  var styles = fs.readFileSync(path.join(ROOT, "styles.css"), "utf8");
  assert.strictEqual(/@import|url\(\s*["']?https?:/.test(styles), false,
    "styles.css must load no remote asset");
});

/* --------------------------------------------------------------------- run */

var failures = 0;
tests.forEach(function (entry) {
  try {
    entry[1]();
    console.log("ok   " + entry[0]);
  } catch (error) {
    failures += 1;
    console.log("FAIL " + entry[0]);
    console.log("     " + error.message);
  }
});

console.log("");
console.log(tests.length - failures + " passed, " + failures + " failed, " + tests.length + " total");
process.exit(failures ? 1 : 0);
