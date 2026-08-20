/* M0 Flight Readiness review surface — read-only renderer.

   This file reads the generated model in data/fixtures.js and writes the DOM.
   It performs no network request, no storage access, no navigation and no
   mutation of any kind: there is no fetch, XMLHttpRequest, WebSocket, import(),
   localStorage, cookie, form submit or eval anywhere below. Every control is a
   view control, and every value shown is read straight off an emitted
   FlightReadinessPacket projection.

   Nodes are built with createElement and textContent only. Model values never
   reach innerHTML, so a value in the data can never become markup or script.

   Fail-closed rule: an absent or unrecognised model renders a refusal, not an
   empty page; an absent field renders its typed absence token (UNKNOWN or
   MISSING), never a blank, a dash or null.
*/

(function () {
  "use strict";

  var SCHEMA = "m0-review-surface-projection/v1";
  var RESERVED = "__kdd__";

  /* ------------------------------------------------------------ DOM utils */

  function h(tag, props, children) {
    var node = document.createElement(tag);
    if (props) {
      Object.keys(props).forEach(function (key) {
        var value = props[key];
        if (value === null || value === undefined || value === false) return;
        if (key === "class") node.className = value;
        else if (key === "text") node.textContent = String(value);
        else if (key === "onclick") node.addEventListener("click", value);
        else if (key === "onkeydown") node.addEventListener("keydown", value);
        else if (key === "onchange") node.addEventListener("change", value);
        else node.setAttribute(key, value === true ? "" : String(value));
      });
    }
    (children || []).forEach(function (child) {
      if (child === null || child === undefined) return;
      node.appendChild(typeof child === "string" ? document.createTextNode(child) : child);
    });
    return node;
  }

  function clear(node) {
    while (node.firstChild) node.removeChild(node.firstChild);
  }

  /* -------------------------------------------------- typed value display */

  /* The package encodes absence under the reserved __kdd__ key. UNKNOWN and
     MISSING are different facts and are shown as different words. */
  function absentName(value) {
    if (value && typeof value === "object" && !Array.isArray(value)) {
      var keys = Object.keys(value);
      if (keys.length === 1 && keys[0] === RESERVED) return String(value[RESERVED]);
    }
    return null;
  }

  function val(value) {
    var absent = absentName(value);
    if (absent) return h("span", { class: "absent", text: absent });
    if (value === null || value === undefined) return h("span", { class: "absent", text: "not recorded" });
    if (typeof value === "boolean") return document.createTextNode(value ? "true" : "false");
    if (Array.isArray(value)) {
      if (!value.length) return h("span", { class: "absent", text: "none recorded" });
      return document.createTextNode(value.map(flat).join(", "));
    }
    if (typeof value === "object") return document.createTextNode(JSON.stringify(value));
    return document.createTextNode(String(value));
  }

  function flat(value) {
    var absent = absentName(value);
    if (absent) return absent;
    if (value === null || value === undefined) return "not recorded";
    if (typeof value === "object") return JSON.stringify(value);
    return String(value);
  }

  function interval(value) {
    if (!value || typeof value !== "object") return flat(value);
    return flat(value.start) + " → " + flat(value.end);
  }

  function kv(pairs) {
    var list = h("dl", { class: "kv" });
    pairs.forEach(function (pair) {
      if (!pair) return;
      list.appendChild(h("dt", { text: pair[0] }));
      list.appendChild(h("dd", null, [typeof pair[1] === "string" ? document.createTextNode(pair[1]) : pair[1]]));
    });
    return list;
  }

  function panel(title, meta, body) {
    var head = h("header", null, [h("h3", { text: title })]);
    if (meta) head.appendChild(h("span", { class: "meta", text: meta }));
    return h("section", { class: "panel" }, [head, body]);
  }

  function outcomeTag(outcome) {
    return h("span", { class: "outcome " + outcome, text: outcome });
  }

  /* ------------------------------------------------------------- receipts */

  /* One receipt, collapsed. Opening it is a single interaction — one click, or
     one Enter/Space with the summary focused — which is what keeps the exact
     source-read and D4/D6 receipts inside the two-interaction budget. */
  function receiptCard(receipt, title, open) {
    var summary = h("summary", { class: "receipt-summary" }, [
      h("span", { class: "title", text: title }),
      h("span", { class: "rid", text: receipt.receipt_id })
    ]);

    var inner = h("div", { class: "inner" }, [
      h("h4", { text: "Identity" }),
      kv([
        ["receipt_id", h("span", { class: "mono", text: receipt.receipt_id })],
        ["digest", h("span", { class: "mono", text: receipt.digest })],
        ["receipt_kind", receipt.receipt_kind],
        ["outcome", receipt.outcome],
        ["actor", flat(receipt.actor_id) + " (" + flat(receipt.actor_kind) + ")"],
        ["recorded_at", val(receipt.recorded_at)]
      ]),
      h("h4", { text: "Authority and scope" }),
      kv([
        ["authorization_state", receipt.authorization_state],
        ["redaction_state", receipt.redaction_state],
        ["observed_interval", interval(receipt.observed_interval)],
        ["source_id", val((receipt.source || {}).source_id)],
        ["locator", val((receipt.source || {}).locator)],
        ["snapshot_id", val((receipt.source || {}).snapshot_id)],
        ["source_owner", val((receipt.source || {}).owner)]
      ]),
      h("h4", { text: "Retained body" }),
      h("p", {
        text: receipt.body_retained
          ? "A body is retained under this authorization and redaction state. The packet exposes its digest only; the body itself is never serialized."
          : "No body is retained. The packet records the typed absence rather than an empty value."
      }),
      kv([["body_digest", val(receipt.body_digest)]])
    ]);

    if (receipt.decision_bindings && receipt.decision_bindings.length) {
      inner.appendChild(h("h4", { text: "Decision bindings" }));
      inner.appendChild(kv([
        ["decision_bindings", receipt.decision_bindings.join(", ")],
        ["independence_class", val(receipt.detail.independence_class)],
        ["comparison_rule_id", val(receipt.detail.comparison_rule_id)],
        ["comparison_matches", val(receipt.detail.comparison_matches)],
        ["comparator_digest", h("span", { class: "mono", text: flat(receipt.detail.comparator_digest) })],
        ["reported_output_digest", h("span", { class: "mono", text: flat(receipt.detail.reported_output_digest) })],
        ["recomputed_output_digest", h("span", { class: "mono", text: flat(receipt.detail.recomputed_output_digest) })]
      ]));
    }

    if (receipt.derivation_inputs && receipt.derivation_inputs.length) {
      inner.appendChild(h("h4", { text: "Derivation inputs" }));
      inner.appendChild(h("pre", { text: receipt.derivation_inputs.join("\n") }));
    }

    inner.appendChild(h("h4", { text: "Exact receipt detail" }));
    inner.appendChild(h("pre", { text: JSON.stringify(receipt.detail, null, 2) }));

    return h("details", { class: "receipt", open: open === true }, [summary, inner]);
  }

  /* --------------------------------------------------------- check tables */

  var CHECK_COLUMNS = [
    "Check", "Outcome", "Materiality", "Rule source", "Evidence IDs", "Validator / receipt IDs"
  ];

  function checkTable(checks, blockers, captionText) {
    var head = h("tr", null, CHECK_COLUMNS.map(function (name) {
      return h("th", { scope: "col", text: name });
    }));
    var body = h("tbody");

    checks.forEach(function (check, index) {
      var blocking = blockers.indexOf(check.check_id) !== -1;
      var detailId = "check-detail-" + index + "-" + check.check_id;

      var toggle = h("button", {
        type: "button",
        class: "expander",
        "aria-expanded": "false",
        "aria-controls": detailId,
        text: check.check_id
      });

      var row = h("tr", { class: blocking ? "blocking" : null }, [
        h("td", null, [
          toggle,
          h("div", { class: "mono", text: check.title })
        ]),
        h("td", null, [outcomeTag(check.outcome)]),
        h("td", { class: "mono token", text: check.materiality }),
        h("td", { class: "mono", text: check.rule_source }),
        h("td", { class: "mono" }, [val(check.evidence_ids)]),
        h("td", { class: "mono" }, [val(check.receipt_ids)])
      ]);

      var detailRow = h("tr", { class: "detail", id: detailId, hidden: true }, [
        h("td", { colspan: String(CHECK_COLUMNS.length) }, [
          kv([
            ["reason", check.reason],
            ["reopen_condition", check.reopen_condition],
            ["affected_scope", check.affected_scope],
            ["ruling_actor", check.ruling_actor],
            ["materiality_rule_id", check.materiality_rule_id],
            ["core_floor", val(check.core_floor)],
            ["result_digest", h("span", { class: "mono", text: check.result_digest })]
          ])
        ])
      ]);

      toggle.addEventListener("click", function () {
        var open = toggle.getAttribute("aria-expanded") === "true";
        toggle.setAttribute("aria-expanded", open ? "false" : "true");
        detailRow.hidden = open;
      });

      body.appendChild(row);
      body.appendChild(detailRow);
    });

    var table = h("table", null, [
      h("caption", { text: captionText }),
      h("thead", null, [head]),
      body
    ]);
    return h("div", { class: "scroll" }, [table]);
  }

  /* --------------------------------------------------------------- routes */

  function readinessRoute(scenario) {
    var decision = scenario.decision;
    var action = scenario.next_safe_action;
    var material = scenario.checks.filter(function (check) {
      return check.materiality === "material" || check.materiality === "unknown";
    });

    var conclusion = h("div", { class: "decision" }, [
      h("div", null, [
        h("p", { class: "eyebrow", text: "Packet decision" }),
        h("div", { class: "verdict" }, [
          h("span", { class: "value " + decision.analysis_use.value, text: decision.analysis_use.value }),
          h("span", { class: "origin", text: decision.analysis_use.storage + " · " + decision.analysis_use.derived_by })
        ]),
        h("div", { class: "derived" }, [
          h("p", { class: "eyebrow", text: "Derived post-analysis eligibility" }),
          h("div", { class: "verdict" }, [
            h("span", {
              class: "value " + decision.post_analysis_eligibility.value,
              text: decision.post_analysis_eligibility.value
            }),
            h("span", { class: "origin", text: decision.post_analysis_eligibility.storage })
          ]),
          h("p", { class: "rule", text: "Rule: " + decision.post_analysis_eligibility.rule })
        ]),
        h("p", { class: "why", text: decision.why_limited }),
        h("p", { class: "authority-note", text: decision.authority_note })
      ]),
      h("div", { class: "action" }, [
        h("p", { class: "eyebrow", text: "Next safe action" }),
        kv([]),
        h("dl", null, [
          h("div", null, [h("dt", { text: "kind" }), h("dd", { class: "kind", text: action.kind })]),
          h("div", null, [h("dt", { text: "guidance" }), h("dd", { text: action.guidance })]),
          h("div", null, [h("dt", { text: "reopen condition" }), h("dd", { text: action.reopen_condition })]),
          h("div", null, [
            h("dt", { text: "blockers" }),
            h("dd", null, [val(decision.blockers)])
          ])
        ])
      ])
    ]);

    var reach = h("div", { class: "pad" }, [
      h("p", {
        class: "reach",
        text: "The exact source read and the independent D4/D6 recomputation are one interaction away: "
          + "move focus to a heading below and press Enter or Space."
      }),
      receiptCard(scenario.receipts.source_read[0], "Source read — exact retained receipt", false),
      receiptCard(scenario.receipts.recomputation_d4_d6[0], "Independent recomputation — D4/D6 receipt", false)
    ]);

    /* The receipt reach sits directly under the decision, before the long
       check table: a reviewer who wants the proof should not have to scroll
       past nineteen rows to find it. */
    var core = h("div", null, [
      conclusion,
      panel("Receipt reach", "source read and D4/D6 recomputation", reach),
      panel(
        "Material check summary",
        material.length + " of " + scenario.checks.length + " checks are material or unknown",
        checkTable(
          material,
          decision.blockers,
          "Ordered failed, missing and unknown first, then not-applicable, then passed. "
            + "Expand a check identifier for its reason, reopen condition, scope and ruling actor."
        )
      )
    ]);

    return h("div", { class: "split" }, [core, inspector(scenario)]);
  }

  function inspector(scenario) {
    var identity = scenario.identity;
    var state = scenario.state;

    function stateLine(label, value, flagged, note) {
      return h("div", { class: "state-line" }, [
        h("span", { text: label }),
        h("b", { class: flagged ? "flag" : "clear", text: value }),
        note ? h("span", { text: note }) : null
      ]);
    }

    return h("aside", { class: "inspector", "aria-label": "Packet identity and state" }, [
      h("section", null, [
        h("h3", { text: "Packet identity" }),
        kv([
          ["packet_digest", h("span", { class: "mono", text: identity.packet_digest })],
          ["contract_digest", h("span", { class: "mono", text: identity.contract_digest })],
          ["frozen contract revision", flat(identity.frozen_binding.packet.revision)],
          ["frozen contract digest", h("span", { class: "mono", text: flat(identity.frozen_binding.packet.packet_digest) })],
          ["architecture revision", flat(identity.frozen_binding.architecture_revision)],
          ["core check set revision", identity.core_check_set.revision],
          ["core set digest", h("span", { class: "mono", text: identity.core_check_set.digest })],
          ["expiry", val(identity.expiry)]
        ])
      ]),
      h("section", null, [
        h("h3", { text: "Supersession" }),
        kv([
          ["state", state.supersession.state],
          ["supersedes_digest", h("span", { class: "mono" }, [val(identity.supersedes_digest)])],
          ["predecessor_digest", h("span", { class: "mono" }, [val(identity.predecessor_digest)])]
        ])
      ]),
      h("section", null, [
        h("h3", { text: "Authorization, redaction and freshness" }),
        stateLine("authorization", state.authorization_state, state.authorization_state !== "authorized"),
        stateLine(
          "redaction",
          state.redaction_state,
          state.redaction_state !== "not_required" && state.redaction_state !== "applied"
        ),
        stateLine("staleness", state.staleness.state, state.staleness.state === "stale"),
        stateLine(
          "completeness",
          state.incompleteness.state,
          state.incompleteness.state === "incomplete",
          state.incompleteness.unresolved_checks.length + " unresolved"
        ),
        h("p", { class: "rule", text: state.body_retention })
      ]),
      h("section", null, [
        h("h3", { text: "Named human state" }),
        kv([
          ["experiment owner", scenario.human.packet_human_state.experiment_owner],
          ["independent DS", scenario.human.packet_human_state.independent_ds_consultant],
          ["committee route", scenario.human.packet_human_state.committee_route],
          ["acknowledgement", scenario.human.packet_human_state.acknowledgement_state]
        ])
      ])
    ]);
  }

  function checksRoute(scenario, state) {
    var filters = state.filters;

    function select(id, label, options, current, onchange) {
      var box = h("select", { id: id, onchange: onchange });
      options.forEach(function (option) {
        var node = h("option", { value: option, text: option });
        if (option === current) node.selected = true;
        box.appendChild(node);
      });
      return h("label", { for: id }, [document.createTextNode(label), box]);
    }

    var outcomes = ["all"].concat(["FAIL", "MISSING", "UNKNOWN", "NOT_APPLICABLE", "PASS"]);
    var materialities = ["all", "material", "non_material", "unknown"];

    var visible = scenario.checks.filter(function (check) {
      if (filters.outcome !== "all" && check.outcome !== filters.outcome) return false;
      if (filters.materiality !== "all" && check.materiality !== filters.materiality) return false;
      if (filters.coreFloor && !check.core_floor) return false;
      return true;
    });

    var coreToggle = h("input", { type: "checkbox", id: "filter-core" });
    coreToggle.checked = filters.coreFloor;
    coreToggle.addEventListener("change", function () {
      filters.coreFloor = coreToggle.checked;
      render();
    });

    var bar = h("div", { class: "filters" }, [
      select("filter-outcome", "Outcome", outcomes, filters.outcome, function (event) {
        filters.outcome = event.target.value;
        render();
      }),
      select("filter-materiality", "Materiality", materialities, filters.materiality, function (event) {
        filters.materiality = event.target.value;
        render();
      }),
      h("label", { for: "filter-core" }, [coreToggle, document.createTextNode("Fixed-floor checks only")]),
      h("span", { class: "ro", text: "View filter only — no packet, check, evidence or source state changes." }),
      h("span", { class: "count", text: visible.length + " / " + scenario.checks.length + " shown" })
    ]);

    var body = visible.length
      ? checkTable(visible, scenario.decision.blockers, "The sealed nineteen-check set, filtered for viewing only.")
      : h("div", { class: "pad" }, [h("p", { class: "gap-empty", text: "No check matches this filter. The packet is unchanged." })]);

    return h("div", null, [
      bar,
      body,
      panel("Frozen check registry", "m0-core-check-set/v1", h("div", { class: "scroll" }, [
        h("table", null, [
          h("caption", { text: "Every check identifier, title, fixed-floor status and rule source carried by the sealed set." }),
          h("thead", null, [h("tr", null, ["Check", "Title", "Fixed floor", "Rule source"].map(function (name) {
            return h("th", { scope: "col", text: name });
          }))]),
          h("tbody", null, MODEL.check_registry.map(function (item) {
            return h("tr", null, [
              h("td", { class: "mono", text: item.check_id }),
              h("td", { text: item.title }),
              h("td", { class: "mono", text: item.core_floor ? "true" : "false" }),
              h("td", { class: "mono", text: item.rule_source })
            ]);
          }))
        ])
      ]))
    ]);
  }

  function receiptsRoute(scenario) {
    var receipts = scenario.receipts;

    var index = h("div", { class: "scroll" }, [
      h("table", null, [
        h("caption", { text: "Every receipt the packet carries, as a list. There is no node diagram: each relationship below is a row, and each row names its inputs." }),
        h("thead", null, [h("tr", null, ["Receipt", "Role", "Outcome", "Actor", "Derivation inputs"].map(function (name) {
          return h("th", { scope: "col", text: name });
        }))]),
        h("tbody", null, [].concat(receipts.source_read, receipts.recomputation_d4_d6, receipts.validator).map(function (receipt) {
          return h("tr", null, [
            h("td", { class: "mono", text: receipt.receipt_id }),
            h("td", { class: "mono token", text: receipt.role }),
            h("td", { class: "mono token", text: receipt.outcome }),
            h("td", { class: "mono token", text: flat(receipt.actor_id) }),
            h("td", { class: "mono" }, [val(receipt.derivation_inputs)])
          ]);
        }))
      ])
    ]);

    var sources = h("div", { class: "pad" }, receipts.source_read.map(function (receipt) {
      return receiptCard(receipt, "Source read — " + receipt.outcome, false);
    }));

    var recomputation = h("div", { class: "pad" }, [
      h("p", {
        text: "Check 14 compares the reported decision-metric output against an independent recomputation. "
          + "The independence class is recorded on the receipt: same_pipeline is not independent and yields UNKNOWN. "
          + "Sharing the immutable source snapshot is always recorded as a shared_source_snapshot Coverage Gap."
      })
    ].concat(receipts.recomputation_d4_d6.map(function (receipt) {
      return receiptCard(receipt, "Independent recomputation — D4/D6", false);
    })));

    var validators = h("div", { class: "pad" }, [
      h("p", { text: "One deterministic validator receipt per check in the sealed set." })
    ].concat(receipts.validator.map(function (receipt) {
      return receiptCard(receipt, "Validator — " + receipt.outcome, false);
    })));

    return h("div", null, [
      panel("Receipt index", "list view of every recorded relationship", index),
      panel("Source-read receipts", receipts.source_read.length + " recorded", sources),
      panel("D4/D6 recomputation receipts", receipts.recomputation_d4_d6.length + " recorded", recomputation),
      panel("Validator receipts", receipts.validator.length + " recorded", validators)
    ]);
  }

  function gapsRoute(scenario) {
    var gaps = scenario.coverage_gaps;
    var disagreements = scenario.disagreements;

    var gapBody = gaps.length
      ? h("div", { class: "scroll" }, [
          h("table", null, [
            h("caption", { text: "Every recorded absence, its materiality, the rule that classified it, and the next safe check that would close it." }),
            h("thead", null, [h("tr", null, ["Gap", "Kind", "Materiality", "Rule source", "Reason", "Next safe check", "Evidence refs"].map(function (name) {
              return h("th", { scope: "col", text: name });
            }))]),
            h("tbody", null, gaps.map(function (gap) {
              return h("tr", null, [
                h("td", { class: "mono", text: gap.gap_id }),
                h("td", { class: "mono token", text: gap.kind }),
                h("td", { class: "mono token", text: gap.materiality }),
                h("td", { class: "mono" }, [val(gap.rule_source)]),
                h("td", { text: gap.reason }),
                h("td", null, [val(gap.next_safe_check)]),
                h("td", { class: "mono" }, [val(gap.evidence_refs)])
              ]);
            }))
          ])
        ])
      : h("div", { class: "pad" }, [h("p", { class: "gap-empty", text: "No Coverage Gap is recorded on this packet." })]);

    var disagreementBody = disagreements.length
      ? h("div", { class: "pad" }, disagreements.map(function (item) {
          return h("div", { class: "receipt" }, [
            h("div", { class: "inner" }, [
              h("h4", { text: String(item.kind) }),
              kv(Object.keys(item).sort().map(function (key) {
                return [key, h("span", { class: "mono" }, [val(item[key])])];
              }))
            ])
          ]);
        }))
      : h("div", { class: "pad" }, [h("p", { class: "gap-empty", text: "No disagreement is recorded on this packet." })]);

    var stateBody = h("div", { class: "pad" }, [
      h("p", { text: "Staleness, invalidation and supersession are read off the packet. A state the packet does not carry is reported as not_recorded rather than inferred." }),
      kv([
        ["staleness", scenario.state.staleness.state],
        ["contract analysis window", interval(scenario.state.staleness.contract_analysis_window)],
        ["supersession", scenario.state.supersession.state],
        ["supersedes_digest", h("span", { class: "mono" }, [val(scenario.state.supersession.supersedes_digest)])],
        ["completeness", scenario.state.incompleteness.state],
        ["unresolved checks", scenario.state.incompleteness.unresolved_checks.length
          ? scenario.state.incompleteness.unresolved_checks.map(function (item) { return item.check_id; }).join(", ")
          : h("span", { class: "absent", text: "none recorded" })]
      ])
    ]);

    if (scenario.state.staleness.detail.length) {
      stateBody.appendChild(h("h4", { text: "Reads outside the contract window" }));
      stateBody.appendChild(h("pre", {
        text: scenario.state.staleness.detail.map(function (item) {
          return item.receipt_id + "  outcome=" + item.outcome + "  observed=" + interval(item.observed_interval);
        }).join("\n")
      }));
    }

    var ack = scenario.human.acknowledgement_record;
    var ackBody = h("div", { class: "pad" }, ack
      ? [
          h("p", { text: ack.object + ". A reviewer acknowledgement is a separate record; superseding the acknowledged packet invalidates it without rewriting history." }),
          kv([
            ["acknowledged packet", h("span", { class: "mono", text: ack.acknowledged_packet_digest })],
            ["reviewer", ack.reviewer],
            ["state before", ack.state_before],
            ["state after", ack.state_after],
            ["invalidated by", h("span", { class: "mono" }, [val(ack.invalidated_by_packet_digest)])]
          ])
        ]
      : [h("p", {
          class: "gap-empty",
          text: "No acknowledgement record exists for this packet. Its packet human state is "
            + scenario.human.packet_human_state.acknowledgement_state + "."
        })]
    );

    /* State first, then the long gap list. This route's question is which
       packet is current and what happened to the earlier acknowledgement, and
       that answer must not sit below twenty gap rows. */
    return h("div", null, [
      panel("Staleness, invalidation and supersession", scenario.state.supersession.state, stateBody),
      panel("Acknowledgement record", ack ? ack.state_after : "none recorded", ackBody),
      panel("Disagreements", disagreements.length + " recorded", disagreementBody),
      panel("Coverage Gaps", gaps.length + " recorded", gapBody)
    ]);
  }

  function boundariesRoute(scenario) {
    var list = h("ol", { class: "boundaries" }, MODEL.boundaries.map(function (line, index) {
      return h("li", null, [
        h("span", { class: "no", text: String(index + 1) }),
        h("span", { text: line })
      ]);
    }));

    var provenance = MODEL.provenance;

    var bindings = h("div", { class: "scroll" }, [
      h("table", null, [
        h("caption", { text: "The exact inputs this projection is bound to. A byte change to any of them invalidates it." }),
        h("thead", null, [h("tr", null, ["Role", "Path", "Revision", "SHA-256"].map(function (name) {
          return h("th", { scope: "col", text: name });
        }))]),
        h("tbody", null, provenance.file_bindings.map(function (item) {
          return h("tr", null, [
            h("td", { text: item.role }),
            h("td", { class: "mono", text: item.path }),
            h("td", { class: "mono", text: item.revision }),
            h("td", { class: "mono", text: item.sha256 })
          ]);
        }).concat([
          h("tr", null, [
            h("td", { text: "Accepted M0 package" }),
            h("td", { class: "mono", text: ".agents/skills/kdd_data_agent/ (" + provenance.accepted_package_file_count + " files)" }),
            h("td", { class: "mono", text: provenance.accepted_package_verdict }),
            h("td", { class: "mono", text: provenance.accepted_package_aggregate_sha256 })
          ])
        ]))
      ])
    ]);

    return h("div", null, [
      panel("What this surface is not", "explicit boundaries", h("div", { class: "pad" }, [list])),
      panel("Trace", "not present in M0", h("div", { class: "pad" }, [
        h("p", { text: "M0 collects no Trace store, and this surface renders none. If a later milestone adds one, it is a separately collected diagnostic projection, never evidence authority: when Trace and canonical Evidence diverge, Evidence controls and the divergence is recorded as a Coverage Gap." })
      ])),
      panel("Provenance", "exact input bindings", h("div", { class: "pad" }, [
        h("p", { text: "Aggregate recipe: " + provenance.aggregate_recipe }),
        bindings
      ])),
      panel("Accepted package projection", "kdd_data_agent.m0.packet.synthetic_review_projection", h("div", { class: "pad" }, [
        h("p", { text: "The accepted package emits its own pre-P3 projection for this packet. It is shown verbatim so the surface can be checked against it rather than trusted." }),
        h("pre", { text: JSON.stringify(scenario.accepted_package_projection, null, 2) })
      ]))
    ]);
  }

  var ROUTES = [
    { id: "readiness", label: "Readiness", build: readinessRoute },
    { id: "checks", label: "Checks", build: checksRoute },
    { id: "receipts", label: "Receipts", build: receiptsRoute },
    { id: "gaps", label: "Gaps & state", build: gapsRoute },
    { id: "boundaries", label: "Boundaries", build: boundariesRoute }
  ];

  /* ----------------------------------------------------------- fail closed */

  function refuse(reason) {
    var main = document.getElementById("workspace");
    if (!main) return;
    clear(main);
    main.appendChild(h("section", { class: "notice", role: "alert" }, [
      h("h1", { text: "This surface will not render" }),
      h("p", { text: reason }),
      h("p", { text: "Nothing is shown rather than something unverified. Regenerate the model from the accepted M0 package with tools/build_fixtures.py and reload." })
    ]));
  }

  /* --------------------------------------------------------------- runtime */

  var MODEL = window.__M0_REVIEW_MODEL__;
  var STATE = {
    scenario: 0,
    route: "readiness",
    filters: { outcome: "all", materiality: "all", coreFloor: false }
  };

  function currentScenario() {
    return MODEL.scenarios[STATE.scenario];
  }

  function renderRail(scenario) {
    document.getElementById("rail-flight-id").textContent = scenario.flight.flight_id;
    document.getElementById("rail-evidence-class").textContent = "evidence_class = " + scenario.flight.evidence_class;
    document.getElementById("rail-schema").textContent = MODEL.schema_version;

    var list = document.getElementById("scenario-list");
    clear(list);
    /* The rail carries the stored decision only. Eligibility is mechanically
       derived from it and is already on the authority strip; repeating it on
       every row would spend the accent colour on a fact the reader has, and
       turn seven rows into a wall of identical badges. */
    MODEL.scenarios.forEach(function (item, index) {
      var use = item.decision.analysis_use.value;
      var button = h("button", {
        type: "button",
        "aria-current": index === STATE.scenario ? "true" : "false"
      }, [
        h("span", { class: "name", text: item.title }),
        h("span", { class: "use " + use, text: use })
      ]);
      button.addEventListener("click", function () {
        STATE.scenario = index;
        render();
      });
      list.appendChild(h("li", null, [button]));
    });

    var facts = document.getElementById("rail-facts");
    clear(facts);
    /* The review question is a sentence, not a field: it gets its own line
       rather than being squeezed into the label/value grid. */
    var question = document.getElementById("rail-question");
    if (question) question.textContent = scenario.review_question;
    [
      ["Scenario", scenario.scenario_id],
      ["Emitted by", scenario.emitted_by],
      ["Window", interval(scenario.flight.analysis_window)],
      ["Runtime", scenario.flight.observed_runtime_units + " / " + scenario.flight.planned_runtime_units + " units"],
      ["Decision metric", scenario.flight.decision_metric.metric_id],
      ["Source", scenario.flight.source.source_id],
      ["Tenant", scenario.flight.tenant_scope]
    ].forEach(function (pair) {
      facts.appendChild(h("div", null, [
        h("dt", { text: pair[0] }),
        h("dd", null, [typeof pair[1] === "string" ? document.createTextNode(pair[1]) : pair[1]])
      ]));
    });
  }

  function renderStrip(scenario) {
    var use = document.getElementById("strip-analysis-use");
    var eligibility = document.getElementById("strip-eligibility");
    use.textContent = scenario.decision.analysis_use.value;
    use.className = scenario.decision.analysis_use.value;
    eligibility.textContent = scenario.decision.post_analysis_eligibility.value;
    eligibility.className = scenario.decision.post_analysis_eligibility.value;
  }

  function renderTabs() {
    var tabs = document.getElementById("route-tabs");
    clear(tabs);
    ROUTES.forEach(function (route) {
      var selected = route.id === STATE.route;
      var tab = h("button", {
        type: "button",
        role: "tab",
        id: "tab-" + route.id,
        "aria-selected": selected ? "true" : "false",
        "aria-controls": "panel-" + route.id,
        tabindex: selected ? "0" : "-1",
        text: route.label
      });
      tab.addEventListener("click", function () {
        STATE.route = route.id;
        render();
      });
      tab.addEventListener("keydown", function (event) {
        var index = ROUTES.findIndex(function (item) { return item.id === STATE.route; });
        var next = null;
        if (event.key === "ArrowRight") next = (index + 1) % ROUTES.length;
        else if (event.key === "ArrowLeft") next = (index - 1 + ROUTES.length) % ROUTES.length;
        else if (event.key === "Home") next = 0;
        else if (event.key === "End") next = ROUTES.length - 1;
        if (next === null) return;
        event.preventDefault();
        STATE.route = ROUTES[next].id;
        render();
        var target = document.getElementById("tab-" + STATE.route);
        if (target) target.focus();
      });
      tabs.appendChild(tab);
    });
  }

  function render() {
    var scenario = currentScenario();
    renderRail(scenario);
    renderStrip(scenario);
    renderTabs();

    var routes = document.getElementById("routes");
    clear(routes);
    var definition = ROUTES.filter(function (item) { return item.id === STATE.route; })[0];
    var panelNode = h("section", {
      class: "route",
      role: "tabpanel",
      id: "panel-" + definition.id,
      "aria-labelledby": "tab-" + definition.id,
      tabindex: "0"
    }, [definition.build(scenario, STATE)]);

    if (definition.id === "readiness") panelNode.id = "packet-decision";
    routes.appendChild(panelNode);

    if (scenario.projection_note) {
      routes.appendChild(h("section", { class: "panel" }, [
        h("div", { class: "pad" }, [h("p", { text: scenario.projection_note })])
      ]));
    }
  }

  /* Read-only deep link: #/<scenario_id>/<route_id> selects a view on load and
     on back/forward. The hash is only ever read, never written, so this surface
     records no navigation state and mutates nothing. An unrecognised fragment
     falls back to the first scenario's readiness view rather than failing. */
  function applyHash() {
    var parts = String(window.location.hash || "").replace(/^#\/?/, "").split("/");
    var scenarioIndex = -1;
    if (parts[0]) {
      MODEL.scenarios.forEach(function (item, index) {
        if (item.scenario_id === parts[0]) scenarioIndex = index;
      });
    }
    if (scenarioIndex !== -1) STATE.scenario = scenarioIndex;
    if (parts[1] && ROUTES.some(function (item) { return item.id === parts[1]; })) STATE.route = parts[1];
  }

  function start() {
    if (!MODEL || typeof MODEL !== "object") {
      refuse("The generated model at data/fixtures.js is absent or is not an object.");
      return;
    }
    if (MODEL.schema_version !== SCHEMA) {
      refuse("The model declares schema_version " + JSON.stringify(MODEL.schema_version)
        + ", and this surface only renders " + JSON.stringify(SCHEMA) + ".");
      return;
    }
    if (!Array.isArray(MODEL.scenarios) || !MODEL.scenarios.length) {
      refuse("The model carries no scenario.");
      return;
    }
    var bad = MODEL.scenarios.filter(function (item) {
      return !item.decision || !item.decision.analysis_use || !item.identity || !item.identity.packet_digest;
    });
    if (bad.length) {
      refuse("A scenario is missing its packet decision or packet digest, so the surface cannot show what it is bound to.");
      return;
    }
    applyHash();
    if (window.addEventListener) {
      window.addEventListener("hashchange", function () {
        applyHash();
        render();
      });
    }
    render();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
