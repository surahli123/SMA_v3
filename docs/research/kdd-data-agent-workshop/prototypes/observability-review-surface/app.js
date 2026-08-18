// PROTOTYPE / THROWAWAY — synthetic, read-only, no backend or mutations.
const ROUTES = ["review", "claims", "verify", "trace"];
const CASE = {
  id: "CASE A-017",
  title: "Search experiment miss",
  revision: "packet rev 5",
  verdict: "Suspected",
  readiness: "Blocked",
  sha: "9f71c2e",
  artifact: "blend_weights.bin v73"
};

const evidence = {
  "EV-DEP-17": { title: "Deployed blend artifact", type: "Validated support", source: "Synthetic Deploy Registry", scope: "search-web / prod-usw2 / treatment", interval: "2026-08-10 17:42 UTC", authorization: "read:deploy-metadata", receipt: "rcpt_deploy_8f21", validator: "sha-reachability/v3 · PASS", freshness: "current", invalidation: "none", locator: "src/ranking/blend.py:118–126" },
  "EV-MET-19": { title: "Mobile contradiction", type: "High-risk contradiction", source: "Synthetic Metric Warehouse", scope: "mobile / all locales", interval: "2026-08-11 01:03 UTC", authorization: "aggregate-only", receipt: "rcpt_query_91c2", validator: "segment-contrast/v2 · PASS", freshness: "7 h", invalidation: "unresolved; blocks confirmation", locator: "metrics/search/2026-08-11/ev-met-19" },
  "EV-IDX-02": { title: "Stale corpus gap", type: "Stale / incomplete", source: "Synthetic Index Registry", scope: "global corpus", interval: "2026-07-28 08:00 UTC", authorization: "metadata-only", receipt: "rcpt_index_77bf", validator: "freshness/v1 · FAIL", freshness: "14 d; review limit 24 h", invalidation: "recompute required", locator: "corpus-index@idx-2026.07.28" },
  "EV-ACL-04": { title: "Permission-redacted authorization", type: "Authorization fact", source: "Synthetic ACL Registry", scope: "treatment corpus", interval: "2026-08-10 17:40 UTC", authorization: "metadata-only", receipt: "rcpt_acl_31ae", validator: "scope-match/v2 · PASS", freshness: "current", invalidation: "raw principals require authorized expansion", locator: "acl:search-v42 · principals [REDACTED]" }
};

const competingClaims = {
  "C-17": {
    title: "Blend overweight",
    state: "Suspected",
    question: "Did the deployed per-feature blend weights contribute to the search experiment miss?",
    basis: "Deployed code supports the mechanism, while the flat mobile segment contradicts a confirmed causal reading.",
    support: "EV-DEP-17",
    contradiction: "EV-MET-19",
    coverage: "Incomplete; EV-IDX-02 is stale.",
    nextReview: "Verify deployed artifact authority and recompute the stale corpus snapshot.",
    locator: "claim://CASE-A-017/C-17?revision=5"
  },
  "C-09": {
    title: "Index coverage",
    state: "Inconclusive",
    question: "Did incomplete index coverage contribute to the observed experiment miss?",
    basis: "The available corpus snapshot predates the experiment and cannot resolve this claim.",
    support: "None receipted",
    contradiction: "None receipted",
    coverage: "Incomplete; EV-IDX-02 requires recomputation.",
    nextReview: "Recompute the authorized corpus snapshot before reassessing this claim.",
    locator: "claim://CASE-A-017/C-09?revision=5"
  },
  "C-22": {
    title: "Metric pipeline bias",
    state: "Ruled out",
    question: "Did a metric-pipeline defect create the observed segment contrast?",
    basis: "The synthetic segment validator passed and no receipted pipeline defect is linked to this packet.",
    support: "None receipted",
    contradiction: "EV-MET-19 validator PASS",
    coverage: "Sufficient for this packet revision only.",
    nextReview: "Reopen only if a new receipted pipeline defect is attached.",
    locator: "claim://CASE-A-017/C-22?revision=5"
  }
};
const competingClaimOrder = ["C-17", "C-09", "C-22"];

const query = () => new URLSearchParams(location.search);
const route = () => ROUTES.includes(query().get("view")) ? query().get("view") : "review";
const demoState = () => query().get("state") || "ready";
function navigate(view, extra = {}) {
  const url = new URL(location.href);
  url.searchParams.set("view", view);
  Object.entries(extra).forEach(([key, value]) => url.searchParams.set(key, value));
  history.pushState({}, "", url);
  render();
}

function icon(name) {
  const paths = {
    review: '<rect x="4" y="4" width="16" height="16" rx="1"/><path d="M8 9h8M8 13h8M8 17h5"/>',
    claims: '<circle cx="6" cy="12" r="2"/><circle cx="18" cy="6" r="2"/><circle cx="18" cy="18" r="2"/><path d="m8 11 8-4M8 13l8 4"/>',
    verify: '<path d="M12 3 4.5 6v5c0 4.8 3 8.2 7.5 10 4.5-1.8 7.5-5.2 7.5-10V6L12 3Z"/><path d="m9 12 2 2 4-5"/>',
    trace: '<path d="M5 4v5M5 15v5M12 4v8M12 18v2M19 4v2M19 12v8"/><circle cx="5" cy="12" r="2"/><circle cx="12" cy="15" r="2"/><circle cx="19" cy="9" r="2"/>'
  };
  return `<svg viewBox="0 0 24 24" aria-hidden="true">${paths[name]}</svg>`;
}

function routeRail() {
  const caseNav = `<section class="rail-group"><h2>CASE</h2>${[["Overview","⌂"],["Artifacts","□","14"],["Evidence","▧","23"],["Analyses","⌁","17"],["Timeline","◇"]].map(item=>`<button><b>${item[1]}</b><span>${item[0]}</span><em>${item[2]||""}</em></button>`).join("")}</section>`;
  if (route() === "claims") {
    return `${caseNav}<section class="rail-group rail-claims"><h2>CLAIMS</h2>${competingClaimOrder.map((id,index)=>{ const item = competingClaims[id]; return `<button data-claim="${id}" class="${index===0?"active":""}"><b>${index===0?"△":"○"}</b><span><strong>${id}</strong>${item.title}<small>${item.state}</small></span></button>`; }).join("")}</section>`;
  }
  if (route() === "review" || route() === "verify") {
    return `<section class="rail-case"><h2>CASE</h2><strong>${CASE.id}</strong><span>${CASE.title}</span></section><section class="rail-path"><h2>EVIDENCE PATH</h2>${[["Verdict","Suspected"],["Contradiction","CT-17"],["Deployed Proof","DP-3 · This view"]].map((item,index)=>`<div class="${index===2?"current":""}"><i></i><strong>${item[0]}</strong><span>${item[1]}</span>${index===2?"<small>Exact deployed authority</small>":""}</div>`).join("")}</section><section class="rail-facts"><div><b>Case Owner</b><span>platform-forensics</span></div><div><b>Severity</b><span class="accent">High</span></div><div><b>Status</b><span>Open</span></div></section>`;
  }
  return `${caseNav}<section class="rail-group routes"><h2>WORKSPACE</h2>${ROUTES.map(view=>`<button data-route="${view}" class="${route()===view?"active":""}" ${route()===view?'aria-current="page"':""}>${icon(view)}<span>${view[0].toUpperCase()+view.slice(1)}</span><kbd>F${ROUTES.indexOf(view)+1}</kbd></button>`).join("")}</section>`;
}

function mobileRoutes() {
  return `<section class="mobile-routes">${ROUTES.map(view=>`<button data-route="${view}" class="${route()===view?"active":""}" ${route()===view?'aria-current="page"':""}>${icon(view)}<span>${view[0].toUpperCase()+view.slice(1)}</span></button>`).join("")}</section>`;
}

function shell(content) {
  return `<a class="skip" href="#workspace">Skip to workspace</a>
  <div class="app-shell">
    <aside class="context-rail">
      <div class="case-lockup"><a href="?view=review" class="mark" aria-label="Forensic Observability home"><span>F</span><i></i></a><div><strong>${CASE.id}</strong><span>${CASE.title}</span></div></div>
      ${routeRail()}
      <footer><strong>READ-ONLY PROTOTYPE</strong><span>SYNTHETIC CASE DATA</span></footer>
    </aside>
    <div class="app-body">
      <header class="topbar">
        <nav aria-label="Review modes">${ROUTES.map(view=>`<button data-route="${view}" class="${route()===view?"active":""}" ${route()===view?'aria-current="page"':""}>${icon(view)}<span>${view[0].toUpperCase()+view.slice(1)}</span></button>`).join("")}</nav>
        <dl><div><dt>Cause verdict</dt><dd>${CASE.verdict}</dd></div><div><dt>Recommendation readiness</dt><dd>${CASE.readiness}</dd></div></dl>
      </header>
      <div class="mobile-case"><strong>${CASE.id}</strong><span>${CASE.title} · ${CASE.revision}</span></div>
      <main id="workspace">${content}${stateTray()}</main>${mobileRoutes()}
    </div>
  </div>`;
}

function stateTray() {
  const messages = {
    loading: "Loading receipted evidence…",
    empty: "No evidence matches this scope. Coverage remains incomplete; absence is not negative evidence.",
    error: "Receipt retrieval failed. This record cannot affect the verdict.",
    permission: "Fail closed: raw rows are permission-redacted. Aggregate evidence remains available."
  };
  const state = demoState();
  return `<details class="state-tray" ${state!=="ready"?"open":""}><summary>Prototype states</summary><div>${["ready","loading","empty","error","permission"].map(value=>`<button data-state="${value}" aria-pressed="${state===value}">${value}</button>`).join("")}</div>${messages[state]?`<p role="status" class="${state}">${messages[state]}</p>`:""}</details>`;
}

function reviewView() {
  const proofLines = [
    ["118","def apply_blend_weight(scores, weights):","9f71c2e","blend_weights.bin v73"],
    ["119",'    """Apply per-feature blend weights to scores."""',"9f71c2e","blend_weights.bin v73"],
    ["120","    if weights is None:","9f71c2e","blend_weights.bin v73"],
    ["121","        return scores","9f71c2e","blend_weights.bin v73"],
    ["122","    blended = [0.0] * len(scores)","9f71c2e","blend_weights.bin v73"],
    ["123","    for i, w in enumerate(weights):","9f71c2e","blend_weights.bin v73"],
    ["124","        blended[i] = scores[i] * w","9f71c2e","blend_weights.bin v73"],
    ["125","    return blended","9f71c2e","blend_weights.bin v73"]
  ];
  return shell(`<div class="review-layout">
    <section class="review-core">
      <header class="conclusion-strip"><div><span>Current conclusion</span><strong>Blend weight is a plausible contributor, not yet confirmed.</strong></div><dl><div><dt>Deployed SHA</dt><dd>${CASE.sha}</dd></div><div><dt>Artifact</dt><dd>${CASE.artifact}</dd></div><div><dt>Environment</dt><dd>prod-usw2</dd></div></dl></header>
      <div class="evidence-matrix">
        <article><header><strong>Strongest support</strong><span>EV-DEP-17 · Validated</span></header><button data-evidence="EV-DEP-17"><b>Deployed code applies per-feature blend weights</b><pre>118  def apply_blend_weight(scores, weights):
119      if weights is None:
120          return scores
123      for i, w in enumerate(weights):
124          blended[i] = scores[i] * w</pre><footer><span>src/ranking/blend.py:118–126 · ${CASE.sha}</span><em>PASS</em></footer></button></article>
        <article class="contradiction"><header><strong>Strongest contradiction</strong><span>EV-MET-19</span></header><button data-evidence="EV-MET-19"><b>Mobile does not follow the expected movement</b><div class="metric-table"><span>Segment</span><span>Observed</span><span>Expected</span><span>All traffic</span><code>declined</code><code>declined</code><span>Mobile</span><code>flat</code><code>declined</code></div><p>The segment contrast blocks a confirmed causal reading.</p><footer><span>segment-contrast/v2 · mobile / all locales</span><em>PASS</em></footer></button></article>
        <article><header><strong>Stale corpus gap</strong><span>EV-IDX-02</span></header><button data-evidence="EV-IDX-02"><b>Corpus snapshot predates the experiment</b><dl class="mini-facts"><div><dt>Index built</dt><dd>2026-07-28 08:00 UTC</dd></div><div><dt>Age at review</dt><dd>14 d</dd></div><div><dt>Freshness limit</dt><dd>24 h</dd></div><div><dt>Impact</dt><dd>Coverage remains incomplete</dd></div></dl><footer><span>corpus-index@idx-2026.07.28</span><em class="warn">FAIL</em></footer></button></article>
        <article class="next-action"><header><strong>Next safe action</strong><span>Read-only</span></header><button data-route="verify"><b>Verify deployed artifact against source</b><dl class="mini-facts"><div><dt>Target</dt><dd>${CASE.sha} · ${CASE.artifact}</dd></div><div><dt>Proof</dt><dd>file / symbol / lines / receipt</dd></div><div><dt>Boundary</dt><dd>No deployment or mutation</dd></div></dl><span class="action-link">Open deployed proof <i>→</i></span></button></article>
      </div>
    </section>
    <aside class="case-inspector"><h2>CASE FACTS</h2>${[["Case ID",CASE.id],["Cause verdict",CASE.verdict],["Recommendation readiness",CASE.readiness],["Packet","revision 5"],["Deployed SHA",CASE.sha],["Artifact",CASE.artifact],["Coverage","incomplete"],["Owner","platform-forensics"]].map(row=>`<div><b>${row[0]}</b><span>${row[1]}</span></div>`).join("")}<h2>REVIEW BOUNDARY</h2><p>No view can mutate source facts, verdict, readiness, or production state.</p></aside>
  </div>
  <section class="proof-dock"><header><h2>PERSISTENT PROOF DOCK</h2><span>Exact deployed authority · src/ranking/blend.py:118–126</span></header><div class="proof-head"><span>LINE</span><span>SOURCE CODE</span><span>DEPLOYED SHA</span><span>ARTIFACT</span><span>STATUS</span><span>RECEIPT</span><span>VALIDATOR</span></div>${proofLines.map(row=>`<button data-route="verify"><code>${row[0]}</code><code>${row[1]}</code><code>${row[2]}</code><code>${row[3]}</code><span>Exact</span><code>rcpt_deploy_8f21</code><span>PASS</span></button>`).join("")}</section>`);
}

const graphNodes = [
  ["metric mobile-path path-answer path-evidence","EV-MET-19","Metric miss","Mobile contradiction",3,5],["surface mobile-path path-evidence","EV-SRF-11","Surface","Mobile SERP",27,5],["query mobile-path path-evidence","EV-QR-21","Query / result","Packet 5 miss set",51,5],["acl mobile-path path-evidence","EV-ACL-04","ACL / corpus","Permission-redacted",75,5],
  ["deploy mobile-path path-answer path-evidence","EV-DEP-17","Deployed change","SHA 9f71c2e · v73",3,29],["artifact path-evidence","EV-ART-01","Artifact","blend_weights.bin v73",27,29],["environment path-evidence","EV-ENV-02","Environment","prod-usw2",51,29],["runtime mobile-path path-evidence","EV-PL-08","Pipeline / runtime","CI deploy pipeline",75,29],
  ["judgment path-answer path-evidence","EV-JDG-17","Blend judgment","Plausible contributor",3,53],["conflict mobile-path path-answer path-evidence","EV-MET-19","Contradiction","Mobile stayed flat",27,53],["verification mobile-path path-answer path-evidence","EV-VER-17","Verification","Exact deployed match",51,53],["recommend mobile-path path-evidence","EV-REC-03","Recommendation","Blocked",75,53],
  ["claim mobile-path path-answer path-evidence","C-17","Blend overweight","Suspected",3,78],["claim","C-09","Index coverage","Inconclusive",36,78],["claim","C-22","Metric pipeline bias","Ruled out",69,78]
];
function graphStage() {
  const paths = ["M18 11H28","M42 11H52","M66 11H76","M18 35H28","M42 35H52","M66 35H76","M18 59H28","M42 59H52","M66 59H76","M12 18V29","M36 18V29","M60 18V29","M84 18V29","M12 42V53","M36 42V53","M60 42V53","M84 42V53","M12 66V78","M36 66V78","M60 66V78"];
  return `<div class="graph-stage" data-graph><div class="band observation"><span>OBSERVATION</span></div><div class="band authority"><span>AUTHORITY</span></div><div class="band judgment"><span>JUDGMENT</span></div><div class="band conclusion"><span>CLAIM / CONCLUSION</span></div><svg viewBox="0 0 100 100" preserveAspectRatio="none"><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10Z"/></marker></defs>${paths.map((d,index)=>`<path class="${[7,13,17].includes(index)?"risk":""}" d="${d}" marker-end="url(#arrow)"/>`).join("")}</svg>${graphNodes.map(node=>{ const record = node[1].startsWith("EV-") ? `data-evidence="${node[1]}"` : `data-claim="${node[1]}"`; return `<button class="graph-node ${node[0]} ${node[1]==="EV-MET-19"?"selected":""}" style="--x:${node[4]}%;--y:${node[5]}%" ${record}><small>${node[1]}</small><b>${node[2]}</b><span>${node[3]}</span></button>`; }).join("")}<div class="edge-labels"><span style="--x:20%;--y:11%">produces</span><span style="--x:44%;--y:11%">observed on</span><span style="--x:68%;--y:11%">scoped by</span><span style="--x:20%;--y:35%">deployed as</span><span style="--x:44%;--y:59%">conflicted by</span><span style="--x:68%;--y:59%">blocks</span></div></div>`;
}

function evidenceInspector(id="EV-MET-19") {
  const item = evidence[id];
  if (!item) return `<aside class="evidence-inspector" data-inspector><header><h2>EVIDENCE INSPECTOR</h2><button aria-label="Close inspector">×</button></header><div class="inspector-title"><span>Unavailable</span><strong>${id}</strong><p>No synthetic Evidence record exists for this identifier.</p></div></aside>`;
  const rows = values => `<dl>${values.map(row=>`<div><dt>${row[0]}</dt><dd>${row[1]}</dd></div>`).join("")}</dl>`;
  return `<aside class="evidence-inspector" data-inspector><header><h2>EVIDENCE INSPECTOR</h2><button aria-label="Close inspector">×</button></header><div class="inspector-title"><span>${item.type}</span><strong>${id}</strong><p>${item.title}</p></div>${rows([["Source",item.source],["Scope",item.scope],["Interval",item.interval]])}<h3>AUTHORIZATION</h3>${rows([["Decision",item.authorization],["Scope",item.scope]])}<h3>RECEIPT / PROVENANCE</h3>${rows([["Receipt",item.receipt],["Validator",item.validator]])}<h3>FRESHNESS / INVALIDATION</h3>${rows([["Freshness",item.freshness],["Invalidation",item.invalidation]])}<h3>EXACT LOCATOR</h3><code class="exact-locator">${item.locator}</code><button class="inspector-action" data-route="verify">Open in proof viewer <span>↗</span></button></aside>`;
}

function claimInspector(id="C-17") {
  const item = competingClaims[id];
  if (!item) return `<aside class="evidence-inspector" data-inspector><header><h2>CLAIM INSPECTOR</h2><button aria-label="Close inspector">×</button></header><div class="inspector-title"><span>Unavailable</span><strong>${id}</strong><p>No synthetic Claim record exists for this identifier.</p></div></aside>`;
  const rows = values => `<dl>${values.map(row=>`<div><dt>${row[0]}</dt><dd>${row[1]}</dd></div>`).join("")}</dl>`;
  return `<aside class="evidence-inspector claim-inspector" data-inspector><header><h2>CLAIM INSPECTOR</h2><button aria-label="Close inspector">×</button></header><div class="inspector-title"><span>Competing claim · ${item.state}</span><strong>${id}</strong><p>${item.title}</p></div>${rows([["Review question",item.question],["Current basis",item.basis],["Support records",item.support],["Contradiction",item.contradiction]])}<h3>COVERAGE / NEXT REVIEW</h3>${rows([["Coverage",item.coverage],["Next review",item.nextReview]])}<h3>CLAIM LOCATOR</h3><code class="exact-locator">${item.locator}</code><p class="claim-boundary">This Claim record is a review judgment. It is not Evidence and cannot mutate the verdict.</p></aside>`;
}

function claimsView() {
  return shell(`<div class="claims-layout"><section class="graph-workbench"><header class="graph-title"><div><h1>Evidence Graph</h1><p>Competing claims and typed evidence paths</p></div><div><button data-path="answer" aria-pressed="false">Show answer path</button><button data-path="evidence" aria-pressed="false">Show evidence path</button></div></header><div class="graph-controls"><button data-action="risk" aria-pressed="false">Contradictions</button><label>Group by<select disabled title="Only Layer grouping is available in this prototype"><option>Layer only</option></select></label><label>Collapse<select data-action="collapse"><option>None</option><option>Context</option></select></label><label>Layout<select disabled title="Only left-to-right layout is available in this prototype"><option>Left → Right only</option></select></label><button data-action="relayout">Re-layout</button><p class="graph-path-status" data-path-status aria-live="polite">All typed paths visible.</p></div>${graphStage()}<footer class="graph-legend"><div><b>Node types</b><span>□ Observation</span><span>□ Authority</span><span>□ Judgment</span><span>□ Claim</span></div><div><b>Edge types</b><span>→ derives / produces</span><span class="risk">→ contradicts / blocks</span><span>⇢ references</span></div></footer></section>${evidenceInspector()}</div>`);
}

const deployedCode = `118  def apply_blend_weight(scores, weights):
119      """Apply per-feature blend weights to scores."""
120      if weights is None:
121          return scores
122      blended = [0.0] * len(scores)
123      for i, w in enumerate(weights):
124          blended[i] = scores[i] * w
125      return blended
126`;
const candidateCode = `118  def apply_blend_weight(scores, weights):
119      """Apply normalized blend weights to scores."""
120      if not weights:
121          return scores
122      total_w = sum(weights)
123      if total_w == 0:
124          return scores
125      return [s * (w / total_w) for s, w in zip(scores, weights)]
126`;
function codePane(value, candidate=false) {
  return `<div class="code-pane" data-code-pane>${value.split("\n").map(line=>{
    const match = line.match(/^(\d+)\s(.*)$/);
    const number = match ? match[1] : "";
    const content = match ? match[2] : line;
    const changed = candidate && ["122","123","124","125"].includes(number);
    return `<code class="${changed ? (number === "125" ? "added" : "removed") : ""}"><span>${number}</span>${content}</code>`;
  }).join("")}</div>`;
}
function verifyView() {
  const authority = [["Deployed SHA",CASE.sha],["Repository","search-ranking"],["File","src/ranking/blend.py"],["Symbol","apply_blend_weight"],["Lines","118–126"],["Artifact",CASE.artifact],["Environment","prod-usw2"],["Deployed at","2026-08-10 17:42Z"]];
  return shell(`<div class="verify-layout"><section class="verify-workspace"><nav class="breadcrumb">Verdict <span>›</span> Contradiction CT-17 <span>›</span> Deployed proof DP-3 · revision 5</nav><div class="authority-strip">${authority.map(row=>`<div><span>${row[0]}</span><code>${row[1]}</code></div>`).join("")}</div><nav class="verify-tabs" aria-label="Verify projections"><button class="active" data-verify-target="verify-code" aria-pressed="true">Code</button><button disabled title="A separate Config projection is unavailable in this prototype">Config <small>Unavailable</small></button><button data-verify-target="verify-diff" aria-pressed="false">Diff</button><button data-verify-target="verify-receipts" aria-pressed="false">Receipts</button><label>View<select disabled title="Only deployed-versus-candidate comparison is available"><option>Deployed vs Candidate only</option></select></label></nav><p class="verify-control-status" data-verify-status aria-live="polite">Code comparison active.</p><div class="code-compare" id="verify-code" tabindex="-1"><article><header><strong>Deployed (${CASE.sha})</strong><span class="applied">OBSERVED · APPLIED</span></header><div class="code-location"><code>src/ranking/blend.py:118–126</code><span>lines 118–126 of 512</span></div>${codePane(deployedCode)}<footer><div><span>Artifact observed</span><code>${CASE.artifact}</code></div><div><span>Receipt</span><code>rcpt_deploy_8f21</code></div></footer></article><article class="candidate"><header><strong>Candidate (a3b4d5e)</strong><span>PROPOSED · not_applied</span></header><div class="code-location"><code>src/ranking/blend.py:118–126</code><span>lines 118–126 of 512</span></div>${codePane(candidateCode, true)}<footer><div><span>Artifact proposed</span><code>blend_weights.bin v74</code></div><div><span>Status</span><code>not_applied</code></div></footer></article></div><div class="verification-log"><div><span>Deployed commit</span><code>${CASE.sha}</code><small>Observed through CI Deploy Pipeline</small></div><div><span>Candidate commit</span><code>a3b4d5e</code><small>Proposal only · not_applied</small></div></div><div class="diff-status" id="verify-diff" tabindex="-1"><strong>Diff status: <code>not_applied</code></strong><span>Candidate change was not included in deployed artifact v73.</span></div></section><aside class="provenance" id="verify-receipts" tabindex="-1"><h2>RECEIPTS / PROVENANCE</h2>${[["Validator Receipt","sha-reachability/v3","PASS"],["Artifact Receipt","artifact-integrity/v2","PASS"]].map(row=>`<section class="receipt"><header><strong>${row[0]}</strong><em>${row[2]}</em></header><div><b>Validator</b><code>${row[1]}</code></div><div><b>Receipt ID</b><code>vr_9f71c2e_20260810</code></div><div><b>Generated</b><code>2026-08-10 17:42:28Z</code></div><div><b>Result</b><code>${row[2]}</code></div></section>`).join("")}<section class="acl"><h3>ACL / AUTHORIZATION</h3>${[["Authorizer","synthetic deploy-bot"],["Policy","deploy:prod-usw2"],["Scope","repo:search-ranking"],["Decision","ALLOWED"],["Evidence","EV-ACL-04"]].map(row=>`<div><b>${row[0]}</b><code>${row[1]}</code></div>`).join("")}</section><section class="redacted"><h3>EVIDENCE (PERMISSION-REDACTED)</h3><code>s3://artifacts-prod/**/blend_weights.bin</code><p>Raw principals require authorized expansion.</p><button disabled title="Authorized expansion is unavailable in this static prototype">Expansion unavailable</button></section></aside></div>`);
}

const traceEvents = [
  ["Query planned","Identify candidate ranking artifacts","00:51:03.212","412 ms","Completed","Planner","—","ok"],
  ["ACL checked","Verify access to artifact paths","00:51:03.624","186 ms","Completed","Security","EV-ACL-04","ok"],
  ["Corpus fetched","Collect synthetic corpus snapshot","00:51:04.071","3.842 s","Completed","Collector","—","selected"],
  ["Metric computed","Calculate segment contrast","00:51:08.512","621 ms","Completed","Analytics","EV-MET-19","ok"],
  ["Deployment metadata read","Read deployment manifest","00:51:09.140","128 ms","Error","System","—","error"],
  ["Trace gap","No events captured","00:51:11.301","12.000 s","Gap","—","—","gap"],
  ["Deployment metadata retry","Retry after trace gap","00:51:23.301","1.284 s","Completed","System","EV-DEP-17","retry"],
  ["Metric computed (superseded)","Alternate window replaced","00:51:24.822","540 ms","Superseded","Analytics","—","superseded"],
  ["Validator completed","Evidence package validated","00:51:25.494","287 ms","Completed","Validation","EV-DEP-17","ok"]
];
const traceOutput = `2026-08-11T00:51:04Z INFO start search-ranking collection
case=CASE-A-017 packet_rev=5
artifact=blend_weights.bin v73 sha=9f71c2e
acl=OK linked_evidence=EV-ACL-04
fetch=10432 docs permission_redacted=1284
metric=segment-contrast linked_evidence=EV-MET-19
deploy_metadata=ERROR timeout
trace_gap=12.000s
deploy_metadata=OK retry linked_evidence=EV-DEP-17
validator=PASS
exit_code=0`;
const traceFilterState = { time: "all", status: "all", tool: "all", evidence: "all", search: "" };
function traceView() {
  return shell(`<div class="trace-layout"><section class="trace-workspace"><header class="trace-warning"><span>△</span><div><h1>Execution Trace — not Evidence</h1><p>Events reconstruct what ran, when, and with what results. Only linked validated Evidence can affect the verdict.</p></div></header><div class="trace-controls"><button data-trace-reset disabled>Reset filters</button><button data-trace-filter="time" aria-pressed="false">Time: All</button><button data-trace-filter="status" aria-pressed="false">Status: All</button><button data-trace-filter="tool" aria-pressed="false">Tool category: All</button><button data-trace-filter="evidence" aria-pressed="false">Evidence link: All</button><label><input data-trace-search aria-label="Search events" placeholder="Search events…"></label></div><div class="trace-table"><header><span>EVENT</span><span>TIME (UTC)</span><span>DURATION</span><span>STATUS</span><span>TOOL CATEGORY</span><span>EVIDENCE LINK</span></header>${traceEvents.map((event,index)=>`<button class="trace-row ${event[7]}" data-trace-index="${index}" data-time="${index>=4?"after-error":"early"}" data-status="${event[4].toLowerCase()}" data-tool="${event[5].toLowerCase()}" data-linked="${event[6]!=="—"}"><span class="event"><i></i><b>${event[0]}</b><small>${event[1]}</small></span><code>${event[2]}</code><code>${event[3]}</code><span class="status">${event[4]}</span><span>${event[5]}</span><span class="evidence-link">${event[6]}</span></button>`).join("")}</div><p class="trace-empty" data-trace-empty hidden>No trace events match the current synthetic filters.</p><footer class="trace-footer"><span><b data-trace-count>9</b> events</span><div><i class="ok"></i>Completed <i class="warn"></i>Warning <i class="bad"></i>Error <i class="gap"></i>Gap <i class="retry"></i>Retry</div></footer></section><aside class="trace-inspector"><header><div><h2>Corpus fetched</h2><span>Event ID: EVT-CORPUS-06</span></div><button aria-label="Close inspector">×</button></header><div class="not-evidence"><strong>Tool output is not evidence</strong><span>Raw results and logs cannot affect the verdict.</span></div><section><h3>EVENT DETAILS</h3>${[["Time (UTC)","2026-08-11 00:51:04.071"],["Duration","3.842 s"],["Status","Completed"],["Tool category","Collector"],["Tool","search-ranking"],["Host","synthetic runner"]].map(row=>`<div class="detail-row"><b>${row[0]}</b><code>${row[1]}</code></div>`).join("")}</section><section><h3>TOOL OUTPUT (TRUNCATED)</h3><pre data-code-pane>${traceOutput}</pre></section><section class="linked-evidence"><h3>LINKED EVIDENCE</h3><button data-route="claims"><strong>EV-MET-19</strong><span>Open validated record in Evidence Graph</span></button></section><button class="back-to-graph" data-route="claims">Back to evidence in graph <span>↗</span></button></aside></div><footer class="trace-facts"><span>Case: ${CASE.id}</span><span>Cause verdict: ${CASE.verdict}</span><span>Recommendation readiness: ${CASE.readiness}</span><span>Deployed SHA: ${CASE.sha}</span><span>Artifact: ${CASE.artifact}</span></footer>`);
}

function bindReplacedInspector() {
  document.querySelector("[data-inspector] [data-route]")?.addEventListener("click", event => navigate(event.currentTarget.dataset.route));
  document.querySelector("[data-inspector] [aria-label='Close inspector']")?.addEventListener("click", event => { event.currentTarget.closest("[data-inspector]").hidden = true; });
}

function replaceInspector(content) {
  const inspector = document.querySelector("[data-inspector]");
  if (!inspector) return;
  inspector.outerHTML = content;
  bindReplacedInspector();
}

function applyTraceFilters() {
  const rows = [...document.querySelectorAll(".trace-row")];
  if (!rows.length) return;
  const needle = traceFilterState.search.trim().toLowerCase();
  let visible = 0;
  rows.forEach(row => {
    const matches = (traceFilterState.time === "all" || row.dataset.time === "after-error")
      && (traceFilterState.status === "all" || row.dataset.status !== "completed")
      && (traceFilterState.tool === "all" || row.dataset.tool === "system")
      && (traceFilterState.evidence === "all" || row.dataset.linked === "true")
      && (!needle || row.innerText.toLowerCase().includes(needle));
    row.hidden = !matches;
    if (matches) visible += 1;
  });
  const labels = {
    time: traceFilterState.time === "all" ? "Time: All" : "Time: After error",
    status: traceFilterState.status === "all" ? "Status: All" : "Status: Attention",
    tool: traceFilterState.tool === "all" ? "Tool category: All" : "Tool category: System",
    evidence: traceFilterState.evidence === "all" ? "Evidence link: All" : "Evidence link: Linked"
  };
  document.querySelectorAll("[data-trace-filter]").forEach(button => {
    const key = button.dataset.traceFilter;
    button.textContent = labels[key];
    button.setAttribute("aria-pressed", String(traceFilterState[key] !== "all"));
  });
  const reset = document.querySelector("[data-trace-reset]");
  if (reset) reset.disabled = Object.values(traceFilterState).every(value => value === "all" || value === "");
  const count = document.querySelector("[data-trace-count]");
  if (count) count.textContent = String(visible);
  const empty = document.querySelector("[data-trace-empty]");
  if (empty) empty.hidden = visible !== 0;
}

function bind() {
  document.querySelectorAll("[data-route]").forEach(element => element.addEventListener("click", () => navigate(element.dataset.route)));
  document.querySelectorAll("[data-state]").forEach(element => element.addEventListener("click", () => navigate(route(), { state: element.dataset.state })));
  document.querySelectorAll("[data-evidence]").forEach(element => element.addEventListener("click", () => {
    const id = element.dataset.evidence;
    if (route() === "claims") {
      replaceInspector(evidenceInspector(id));
      document.querySelectorAll("[data-evidence]").forEach(node => node.classList.toggle("selected", node.dataset.evidence === id));
      document.querySelectorAll("[data-claim]").forEach(node => { node.classList.remove("selected"); node.classList.remove("active"); });
    } else navigate(id === "EV-DEP-17" ? "verify" : "claims");
  }));
  document.querySelectorAll("[data-claim]").forEach(element => element.addEventListener("click", () => {
    const id = element.dataset.claim;
    replaceInspector(claimInspector(id));
    document.querySelectorAll("[data-claim]").forEach(node => { node.classList.toggle("selected", node.dataset.claim === id); node.classList.toggle("active", node.dataset.claim === id); });
    document.querySelectorAll("[data-evidence]").forEach(node => node.classList.remove("selected"));
  }));
  document.querySelectorAll("[data-path]").forEach(element => element.addEventListener("click", () => {
    const mode = element.dataset.path;
    const active = element.getAttribute("aria-pressed") !== "true";
    document.querySelectorAll("[data-path]").forEach(button => button.setAttribute("aria-pressed", String(active && button === element)));
    const graph = document.querySelector("[data-graph]");
    graph?.classList.remove("path-answer", "path-evidence");
    if (active) graph?.classList.add(`path-${mode}`);
    const status = document.querySelector("[data-path-status]");
    if (status) status.textContent = active ? (mode === "answer" ? "Answer path highlighted · 6 review nodes." : "Evidence path highlighted · metric-to-claim chain.") : "All typed paths visible.";
  }));
  document.querySelector("[data-action=risk]")?.addEventListener("click", event => {
    const active = document.querySelector("[data-graph]")?.classList.toggle("risk-only") || false;
    event.currentTarget.setAttribute("aria-pressed", String(active));
  });
  document.querySelector("[data-action=relayout]")?.addEventListener("click", () => document.querySelector("[data-graph]")?.classList.toggle("relayout"));
  document.querySelector("select[data-action=collapse]")?.addEventListener("change", event => document.querySelector("[data-graph]")?.classList.toggle("collapsed", event.target.value === "Context"));
  document.querySelectorAll("[data-verify-target]").forEach(element => element.addEventListener("click", () => {
    document.querySelectorAll("[data-verify-target]").forEach(button => { button.classList.toggle("active", button === element); button.setAttribute("aria-pressed", String(button === element)); });
    const target = document.querySelector(`#${element.dataset.verifyTarget}`);
    target?.focus({ preventScroll: true });
    target?.scrollIntoView({ block: "start", behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
    const status = document.querySelector("[data-verify-status]");
    if (status) status.textContent = `${element.textContent.trim()} projection focused.`;
  }));
  document.querySelectorAll("[data-trace-filter]").forEach(element => element.addEventListener("click", () => {
    const key = element.dataset.traceFilter;
    const activeValue = { time: "after-error", status: "attention", tool: "system", evidence: "linked" }[key];
    traceFilterState[key] = traceFilterState[key] === "all" ? activeValue : "all";
    applyTraceFilters();
  }));
  document.querySelector("[data-trace-reset]")?.addEventListener("click", () => {
    Object.assign(traceFilterState, { time: "all", status: "all", tool: "all", evidence: "all", search: "" });
    const search = document.querySelector("[data-trace-search]");
    if (search) search.value = "";
    applyTraceFilters();
  });
  document.querySelector("[data-trace-search]")?.addEventListener("input", event => { traceFilterState.search = event.target.value; applyTraceFilters(); });
  document.querySelectorAll("[aria-label='Close inspector']").forEach(element => element.addEventListener("click", event => { event.currentTarget.closest("[data-inspector], .trace-inspector")?.setAttribute("hidden", ""); }));
  applyTraceFilters();
}
function render() {
  document.querySelector("#app").innerHTML = ({ review: reviewView, claims: claimsView, verify: verifyView, trace: traceView })[route()]();
  bind();
}
addEventListener("popstate", render);
addEventListener("keydown", event => {
  const match = /^F([1-4])$/.exec(event.code);
  if (match) { event.preventDefault(); navigate(ROUTES[Number(match[1]) - 1]); }
});
if (query().has("variant")) history.replaceState({}, "", `${location.pathname}?view=review`);
render();
