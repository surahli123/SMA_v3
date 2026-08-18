# Enterprise Search Metric Miss / Drop: Domain-Specific Research

Date: 2026-08-11  
Scope: research-only. This document presents candidate requirements for a greenfield Data Agent; it is not an owner decision, architecture spec, or implementation plan.

## Conclusion First

The eight general categories of experiment-miss causes still apply, but they are not sufficiently granular for enterprise search. Here, the metric is affected by more than ranking code. It is also affected by the following state:

- Who is searching: tenant, user/group, locale, device, session, and query intent.
- What can be searched: ACL/security trimming, connector, source, index, schema, parser, chunk, and freshness.
- How results are retrieved: lexical, vector, hybrid, filter, synonym, rewrite, and spell correction.
- How results are ranked and presented: fusion, reranker, personalization, business rule, UI, and fallback.
- How outcomes are recorded: exposure, impression, position, click, dwell, reformulation, and success label.

Therefore, the same query string is not a stable experimental unit. The same query may have a different eligible corpus, permissions, history, and available features for different tenants/users. The Data Agent must first freeze **query context + eligible corpus + effective search pipeline**, and only then link a metric change to a production change.

The most important design implication is that production evidence cannot consist only of the repo and deploy. It must also include connector/index generation, ACL snapshot, schema/parser/analyzer, embedding/model, query pipeline, fusion/rerank, fallback/cache, and presentation/telemetry revision.

## Research Method and Evidence Labels

This research prioritizes official documentation and primary research from Microsoft, Google, Elastic, and OpenSearch. No SEO summaries were used.

- **Strong support**: Official sources directly describe a product mechanism, limitation, or observational bias.
- **Reasoned inference**: A Data Agent requirement inferred from multiple official mechanisms; it is not prescribed verbatim by a vendor.
- **Unknown**: This research found no public primary source that can establish a threshold or unified contract.
- **Transfer limitation**: Bing/web-search research can demonstrate bias mechanisms in click and session metrics, but enterprise search makes these problems more severe because of tenants, ACLs, and sparse queries/clicks; its models or thresholds cannot be copied directly.

All URLs were accessed on **2026-08-11**.

## Domain-Specific Failure Planes in Enterprise Search

### 1. Query Mix, Head/Tail, and Tenant Heterogeneity

**Strong support + reasoned inference.** Google's personal-search research finds that a personalized corpus and information need make query-document clicks extremely sparse and create selection bias. Microsoft's online-evaluation research treats documents, result lists, and sessions as different experimental units. Therefore, a single global CTR or a small number of head queries cannot represent all tenants, query classes, and tasks.

Possible failures:

- The treatment improves head/navigation queries but harms tail, acronym, people, exact-title, or long natural-language queries; the effects cancel out in aggregate.
- Large tenants or high-frequency users dominate the overall metric; severe regressions in small tenants are averaged away.
- The treatment/control mixes are imbalanced by query intent, tenant size, ACL density, content source, or locale.
- The definition of the triggered population changes, producing an apparent effect change even though ranking did not change.

Required evidence: query fingerprint/class, head/mid/tail bucket, tenant/user cohort, locale, session, trigger/exposure, eligible result count, source mix, per-slice effect, and sample size.

Falsification checks: Does the effect remain in a paired replay with fixed query/cohort/corpus? Do tenant-equal weighting and traffic weighting produce opposite conclusions? Is the triggered mix balanced between treatment and control?

Sources:

- [Google Research, Learning to Rank with Selection Bias in Personal Search](https://research.google/pubs/learning-to-rank-with-selection-bias-in-personal-search/) (accessed: 2026-08-11)
- [Microsoft Research, Online Evaluation for Information Retrieval](https://www.microsoft.com/en-us/research/publication/online-evaluation-information-retrieval/) (accessed: 2026-08-11)
- [Microsoft Search, Queries usage report](https://learn.microsoft.com/en-us/microsoftsearch/queries-usage-reports) (accessed: 2026-08-11)

### 2. ACL, Security Trimming, and Identity Propagation

**Strong support.** Official Azure and Google documentation states that enterprise results depend on caller identity, group membership, document permission metadata, and query-time enforcement. Azure also explicitly notes a timing lag before permission changes are recognized by the search system. OpenSearch explains that DLS is a query and warns that analyzing an identity containing special characters as ordinary text can cause incorrect filtering and even compromise access control.

Possible failures:

- Group/ACL sync lag suddenly makes relevant documents invisible, causing zero-result queries or a success drop.
- Errors in the identity token, group expansion, security filter, or tenant routing cause over-filtering.
- ACL under-filtering may increase CTR, but that is a security regression and cannot be treated as a search win.
- Treatment and control use inconsistent permission snapshots; the same query actually searches different corpora.
- A schema/analyzer change to permission fields causes principal mismatches.

Required evidence: request principal, tenant, group expansion receipt, ACL source version, ACL/index effective time, security filter/role/query, eligible-before/after-trim counts, denied-result audit, and security incident signal.

Falsification checks: Use authorized test identities to make allow/deny document assertions against the same index generation; compare pre-trim and post-trim candidates; reconcile source ACLs with indexed ACLs; verify whether the problem affects only a particular group/tenant.

Change attribution: Link the issue to an auth code/config/connector/data change only when identity, ACL snapshot, index generation, query filter, and affected scope all align. If permission evidence cannot be read, report only a coverage gap; do not attribute "cannot see the document" directly to the ranker.

Sources:

- [Azure AI Search, Document-level access control](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) (accessed: 2026-08-11)
- [Google Agent Search, Set up data source access control](https://cloud.google.com/generative-ai-app-builder/docs/data-source-access-control) (accessed: 2026-08-11)
- [OpenSearch, Document-level security](https://docs.opensearch.org/latest/security/access-control/document-level-security/) (accessed: 2026-08-11)

### 3. Connector, Content, Schema, Parser, Chunk, and Index Freshness

**Strong support + reasoned inference.** Elasticsearch is near-real-time: writes become searchable only after a refresh. Azure indexers and Google imports/connectors are separate long-running tasks and synchronization planes. The presence of source content does not mean that it has been successfully extracted, mapped, indexed, refreshed, and included in the current serving alias.

Possible failures:

- The connector stops, the checkpoint/high-water mark is wrong, a partial failure occurs, or a delete is not propagated.
- Source freshness, ACL freshness, and index freshness are out of sync.
- A schema field is changed from searchable/filterable; a mapping conflict or analyzer change occurs.
- A PDF/OCR/parser/chunking change loses or truncates critical title/body/table information.
- A backfill/reindex/alias switch covers only some shards, tenants, sources, or languages.
- Duplicate/stale documents change result diversity, CTR, or success.
- Indexing and queries compete for capacity; throttling or a batch partial failure prevents some documents from entering the serving corpus.

Required evidence: source snapshot/version, connector run/checkpoint, per-source success/error/skip counts, document lifecycle, schema/mapping digest, parser/chunker version, index generation, refresh/alias time, document count/freshness/duplicate/delete lag.

Falsification checks: Perform lineage sampling from source documents to indexed fields; compare old/new generations for known-item queries; check whether missing documents are present in the lexical/vector indexes and ACL metadata; reproduce with the serving generation fixed.

Change attribution: Connector config, schema/parser code, data backfill, index template, and refresh/alias changes are all typed production changes. When both the source receipt and serving generation are missing, do not jump to an application code proposal.

Sources:

- [Elastic, Near real-time search](https://www.elastic.co/guide/en/elasticsearch/reference/current/near-real-time.html) (accessed: 2026-08-11)
- [Azure AI Search, Indexers](https://learn.microsoft.com/en-us/azure/search/search-indexer-overview) (accessed: 2026-08-11)
- [Azure AI Search, Analyze performance](https://learn.microsoft.com/en-us/azure/search/search-performance-analysis) (accessed: 2026-08-11)
- [Google Agent Search, Create and manage long-running operations](https://cloud.google.com/generative-ai-app-builder/docs/long-running-operations) (accessed: 2026-08-11)

### 4. Query Understanding: Language, Analyzer, Synonym, Rewrite, and Spell

**Strong support + reasoned inference.** Azure semantic search treats query rewrite as a separate request-stage capability and can generate multiple query variants; a synonym map also enters the ranking pipeline. Analyzers in OpenSearch/Elastic behave differently from exact keywords. Therefore, the same query string does not imply the same effective query.

Possible failures:

- Stemming/tokenization/spell correction corrupts an acronym, product name, people name, or code token.
- Synonym expansion is too broad and introduces many false positives, or only part of the index is updated.
- Locale/language detection, query rewrite, or model version drifts.
- The semantics of an exact phrase, filter, negation, or quoted query change.

Required evidence: raw query, normalized/analyzed tokens, detected language, rewrite/spell/synonym expansions, query DSL, filter, pipeline/config/model revision, and per-stage candidate counts.

Falsification checks: Run an ablation that disables one transformation at a time; perform raw-versus-rewritten paired replay on a fixed index; check whether the affected query class overlaps exactly with the changed rule.

Sources:

- [Azure AI Search, Semantic ranking overview](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview) (accessed: 2026-08-11)
- [Elastic, Synonyms](https://www.elastic.co/docs/solutions/search/full-text/search-with-synonyms) (accessed: 2026-08-11)
- [OpenSearch, Analyzers](https://docs.opensearch.org/latest/analyzers/) (accessed: 2026-08-11)

### 5. Lexical, Vector, and Hybrid Retrieval and Embedding/Index Compatibility

**Strong support + reasoned inference.** Azure semantic ranker only reranks the top candidates from first-stage BM25/RRF; it cannot search the entire corpus again. OpenSearch hybrid search requires a search pipeline to normalize/combine scores from multiple subqueries and allows different weights to be configured. Therefore, a reranker cannot repair a candidate recall failure, and fusion config can independently cause a drop.

Possible failures:

- The lexical lane, vector lane, or filter does not run; candidate `k`, ef/search depth, or timeout changes.
- Document embeddings and query embeddings use inconsistent model/version/dimension/preprocessing.
- The vector backfill is incomplete; new content has only a lexical or only a vector representation.
- A change to hybrid weights, normalization, RRF/fusion, or dedupe suppresses one lane.
- The semantic rerank window is too small, so relevant documents never enter the reranker.

Required evidence: each lane's query, index/model id, candidate IDs/scores/counts/latency/error; embedding model/dimension/preprocess; fusion algorithm/weights; pre/post-fusion ranks; rerank input window and output.

Falsification checks: Replay each lane separately; enlarge the candidate/rerank window; hold candidates fixed and change only fusion/rerank; run an old/new embedding cross-matrix; use known relevant documents to check at which stage they disappear.

Change attribution: The issue can be linked to query code, pipeline/config, a model artifact, or vector data generation, but the analysis must identify whether the drop occurs at the recall, fusion, or rerank stage. A final top-k diff alone cannot localize the cause.

Sources:

- [Azure AI Search, Semantic ranking overview](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview) (accessed: 2026-08-11)
- [OpenSearch, Hybrid search](https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/index/) (accessed: 2026-08-11)
- [OpenSearch, Hybrid search explain](https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/explain/) (accessed: 2026-08-11)

### 6. Reranking, Business Rules, Personalization, and Presentation

**Strong support + reasoned inference.** Azure explicitly states that semantic ranker processes only the top 50 initial results, that input fields have priority and token limits, and that long content is truncated; a ranking-model infrastructure update may also cause small changes in score distribution. Primary research from Microsoft and Google shows that user/session context, position, result attractiveness, and prior policy affect clicks.

Possible failures:

- The reranker model/config/feature schema changes; field priority or truncation hides critical content.
- Boosts, pinned results, freshness/diversity/business rules override the model score.
- Personalization/session context leaks or is missing.
- A change to UI layout, snippet, answer card, result count, viewport, or click target changes CTR while relevance remains unchanged.

Required evidence: reranker input/output, feature/model/config revision, score/rank delta, post-rank processors, personalization/session features, rendered result list, position/viewport, and UI revision.

Falsification checks: Compare models with candidates/rerank input fixed; compare presentation with the ranked list fixed; use a no-personalization cohort, known-item queries, and unaffected locales/clients as negative controls.

Sources:

- [Azure AI Search, Semantic ranking overview](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview) (accessed: 2026-08-11)
- [Microsoft Research, An experimental comparison of click position-bias models](https://www.microsoft.com/en-us/research/publication/an-experimental-comparison-of-click-position-bias-models/) (accessed: 2026-08-11)
- [Google Research, Estimating Position Bias without Intrusive Interventions](https://research.google/pubs/estimating-position-bias-without-intrusive-interventions/) (accessed: 2026-08-11)

### 7. Search Metric, Click Bias, Zero Results, and Session Success

**Strong support; enterprise transfer is limited.** A click does not equal relevance: position and presentation change clicks; no click may be good abandonment; and a click may still leave the user dissatisfied. Microsoft also finds that query reformulation and session-level action sequences can supplement clicks, and uses utility to describe the entire search experience. In enterprise search, low-frequency queries, known-item/navigation tasks, and work spanning sessions further weaken single-query CTR.

Possible failures:

- CTR rises because results move down/up, the UI changes, or there are more low-quality clicks, rather than because success improves.
- Zero results decline because ACLs/filters are relaxed or noise is returned.
- Click logging, the impression denominator, dedupe, bot/internal traffic, or joins change.
- Session boundaries, dwell, reformulation, download, or open-in-app events are incomplete.
- Offline NDCG/recall improves, but the actual eligible corpus, query mix, latency, or user task differs, causing an online miss.
- Missing attribution token, experiment tag, user/session ID, event timestamp, or search→view/click join prevents a real behavioral change from being attributed to the treatment.
- Entity types such as File, People, Bookmark, Acronym, and external connector differ in presentation and action; combining them into a single CTR masks result-type regressions.

Required evidence: metric definition/version; impression/exposure/render/click/open/download/reformulation/session lineage; experiment tag, attribution token, event timestamp, and join receipt; rank/viewport; entity type; zero-result and eligible-result counts; offline judgment/query-set version; online slice, uncertainty, and guardrails.

Falsification checks: Check logging with the rendered list fixed; use position-aware/paired analysis; jointly examine task/session success, reformulation, time-to-content, zero-result quality, and the security guardrail; check whether the offline query set covers the affected tenants/query classes.

Sources:

- [Microsoft Research, Beyond Clicks: Query Reformulation as a Predictor of Search Satisfaction](https://www.microsoft.com/en-us/research/publication/beyond-clicks-query-reformulation-as-a-predictor-of-search-satisfaction/) (accessed: 2026-08-11)
- [Microsoft Research, Beyond Success Rate: Utility as a Search Quality Metric](https://www.microsoft.com/en-us/research/publication/beyond-success-rate-utility-as-a-search-quality-metric-for-online-experiments/) (accessed: 2026-08-11)
- [Microsoft Research, Learning to Account for Good Abandonment](https://www.microsoft.com/en-us/research/publication/learning-account-good-abandonment-search-success-metrics/) (accessed: 2026-08-11)
- [Google Research, Learning to Rank with Selection Bias in Personal Search](https://research.google/pubs/learning-to-rank-with-selection-bias-in-personal-search/) (accessed: 2026-08-11)
- [Google Agent Search, Record user events](https://cloud.google.com/generative-ai-app-builder/docs/user-events) (accessed: 2026-08-11)
- [Google Agent Search, View analytics](https://cloud.google.com/generative-ai-app-builder/docs/view-analytics) (accessed: 2026-08-11)
- [Microsoft Research, Data-driven evaluation metrics for heterogeneous SERPs](https://www.microsoft.com/en-us/research/publication/data-driven-evaluation-metrics-for-heterogeneous-search-engine-result-pages/) (accessed: 2026-08-11)

### 8. Latency, Timeout, Partial Failure, Fallback, and Cache

**Strong support + reasoned inference.** OpenSearch provides request slow logs, per-pipeline processor debug, and neural search stats; hybrid explain is itself resource-intensive and should not be used without limits in production. A timeout at any stage of the retrieval chain can degrade the system to lexical-only, stale cache, or partial results, causing a metric drop without a clear increase in the application error rate.

Possible failures:

- Silent fallback after a vector/reranker/dependency timeout.
- The cache key omits tenant, ACL, locale, flag, or model version, causing incorrect result reuse.
- A shard/replica partial failure, queue/load, or circuit breaker harms only some queries.
- Increased latency causes user abandonment, or a timeout truncates candidates and appears as a relevance drop.

Required evidence: end-to-end and per-stage latency; timeout/budget; fallback reason; cache key/hit/age/generation; partial/timed_out/shard status; dependency/cluster health; request trace; and result completeness.

Falsification checks: Break down the metric by latency/fallback/cache/shard cohort; bypass the cache; replay each stage with a fixed request; compare complete and partial requests; check whether the drop varies with load rather than deploy rollout.

Sources:

- [OpenSearch, Logs and search request slow logs](https://docs.opensearch.org/latest/install-and-configure/configuring-opensearch/logs/) (accessed: 2026-08-11)
- [OpenSearch, Debugging a search pipeline](https://docs.opensearch.org/latest/search-plugins/search-pipelines/debugging-search-pipeline/) (accessed: 2026-08-11)
- [OpenSearch, Hybrid search explain](https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/explain/) (accessed: 2026-08-11)

## Scenario A: Requirements for a Post-Experiment Metric Miss

### Enterprise-Search Causal Chain to Validate First

```text
intended search treatment
  -> assignment / trigger / exposure
  -> caller identity / tenant / locale / session
  -> effective ACL and eligible corpus
  -> connector / content / schema / parser / chunk / index generation
  -> query analysis / rewrite / synonym / spell / filters
  -> lexical and vector candidate lanes
  -> fusion / dedupe
  -> rerank / business rules / personalization
  -> fallback / cache / complete response
  -> rendered list / position / snippet / answer surface
  -> interaction and session events
  -> primary metric / mechanism metrics / guardrails
```

The Agent should locate the "first stage that differs from expectations." It should proceed to a patch-ready proposal only when the break occurs in production implementation/config/model/data and change identity, scope, time, and mechanism all align.

### Evidence / Falsifier Matrix for A

| Candidate cause | Required evidence | Minimum falsifier / validation | Can it be linked to a production change? |
|---|---|---|---|
| Invalid experiment/query mix | SRM, trigger, query/tenant/ACL-density slices, sample/power | Conclusion after reweighting/stratification; AA or same-window control | No production proposal when validity fails |
| Treatment did not actually reach the request | request flag, pipeline id, runtime/config/model, per-stage trace | Whether the treatment request and control path actually differ | Only with an effective runtime receipt |
| ACL/eligible corpus changed | principal/group, ACL/index snapshot, pre/post-trim count | Fixed identity/corpus replay | Can link to auth/config/data; blocked without ACL evidence |
| Ingestion/index drift | connector checkpoint, schema/parser/index generation | source-to-index lineage + old/new generation replay | Can link to connector/schema/data/index config |
| Query understanding failed | tokens, rewrite/synonym/spell, locale, DSL | per-transform ablation | Can link to code/config/model |
| Recall/fusion/rerank failed | per-stage candidates/scores/model/weights | stage isolation; where the known relevant document disappears | Can link to code/config/model/data; final top-k is insufficient |
| Presentation/metric bias | ranked list, render, position, events, metric version | fixed-list UI/logging test; session metrics | Can link to UI/telemetry; must not be misattributed to ranking |
| Latency/fallback | trace, timeout, fallback/cache/partial status | complete vs degraded cohort; bypass cache | Can link to serving config/code/dependency |
| Product hypothesis is false | entire chain is correct, mechanism metric did not move, valid experiment | independent rerun/segment check; alternative mechanism | Must not invent a code root cause |

### Hard Stop for A

Do not provide a production change proposal while any of the following remains unresolved:

- Assignment/SRM/exposure or critical metric lineage is invalid.
- Caller identity, tenant, or effective ACL/corpus cannot be verified.
- Treatment/control use different index generations or an unexpected search pipeline, and the difference cannot be isolated.
- The click/impression denominator or a position/presentation change cannot be explained.
- Deployed runtime, pipeline, model, or data/index identity is uncertain.

## Scenario B: Requirements for a SEV Metric Drop

B should not begin by searching for the "most recent commit." It should first determine which evidence plane contains the drop, then search only typed changes with time × scope × runtime overlap.

| Failure plane | Primary production evidence | Falsifier / safe validation | Change attribution rule |
|---|---|---|---|
| Signal/metric | raw events, definition, freshness, join, render/click lineage | independent recompute; adjacent signals | Do not attribute to search code until telemetry/data issues are excluded |
| Traffic/query/tenant | query mix, tenant, locale, ACL density, load | stable-cohort metric; reweight | A traffic/systemic cause is possible even without a deployed change |
| ACL/identity | token/group/ACL/index snapshot, trim counts | authorized identities + known docs | A security issue is independently high-risk; do not evaluate it only with a relevance metric |
| Connector/index | run/checkpoint/errors, schema/parser, generation/alias | source-index lineage; old generation replay | Data/config/code are all possible; must bind to the serving generation |
| Query pipeline | raw/effective query, transform trace, pipeline revision | transformation ablation | Bind to the exact rule/config/model/symbol |
| Retrieval/ranking | lane candidates, fusion, rerank input/output, models | stage isolation, paired replay | Identify the stage where the document disappears; do not provide only the final rank |
| Serving degradation | stage latency, timeout, fallback/cache/shards | complete/degraded cohort, bypass cache | A dependency/config/runtime change can constitute a candidate_group |
| Presentation/session | ranked list vs rendered list, UI revision, events | fixed list/render replay | Do not attribute a UI/telemetry effect to the ranker |

In addition to repo/file/symbol/line, B's rollback-ready packet should include the effective search pipeline, index generation/alias, ACL revision, embedding/reranker model, fusion/rewrite/synonym config, and fallback/cache state. If the cause is a managed vendor model or external connector change, there may be no code line; in that case, an exact artifact/config/source receipt is more important than inventing a line.

## When a Finding Can and Cannot Be Tied to a Code/Config/Flag/Model/Data Change

### Minimum Conditions for Entering `action-ready`

1. The affected query/tenant/user/locale/session scope is fixed.
2. The ACL/eligible corpus, index generation, and search pipeline that were effective at the time are fixed.
3. The typed change took effect before the effect and actually covered that scope.
4. The per-stage trace shows the predicted break: for example, a relevant document disappears at the recall, fusion, rerank, filter, or render stage.
5. At least one discriminating validation supports that mechanism; key alternative explanations have been checked.
6. The proposal points to repo/file/symbol/line in the deployed revision, or to an exact config/flag/model/data/index artifact.

### Cases That Must Remain `suspected` / `blocked`

- The only evidence is temporal proximity between an aggregate CTR/drop and a recent deploy.
- Caller permission or the eligible corpus is unknown.
- Connector/index/embedding/backfill coverage is incomplete.
- Treatment/control or before/after use different corpora/index generations.
- There is only a final result diff, without per-stage candidates and pipeline identity.
- Concurrent changes to position/UI/logging/metric definition have not been excluded.
- A vendor-managed ranking/model update has no version/change receipt.
- Tail-query or small-tenant sample size is insufficient; absence of evidence is misrepresented as no effect.
- Timeout/fallback/cache/partial results have no telemetry.

## Recommendations for Extending the Eight Confirmed Cause Categories

The following are only **research recommendations**, not owner decisions.

The original eight categories should not be removed. Each category should require checks across eight enterprise-search planes:

1. `cohort_plane`: query class, head/tail, tenant, identity, locale, session.
2. `permission_plane`: ACL, group, security filter, eligible corpus.
3. `content_plane`: source, connector, freshness, delete, schema, parser, chunk.
4. `query_plane`: analyzer, rewrite, synonym, spell, filter.
5. `retrieval_plane`: lexical, vector, embedding/index compatibility, candidate recall.
6. `ranking_plane`: fusion, dedupe, rerank, business rule, personalization.
7. `serving_plane`: latency, timeout, fallback, cache, partial failure.
8. `experience_measurement_plane`: render, position, click/session instrumentation, metric definition.

The general causal chain should be extended to the full search chain in this document, and each `Claim` should explicitly state:

- Which stage's break it explains.
- Which planes provide supporting / contradicting evidence.
- Which planes are not covered.
- Which category the proposed change belongs to among `code | config | flag | model | data | index | connector | permission | presentation | telemetry | external_dependency`.

If the original shared inventory includes only `code | config | flag | model | data`, `index/connector/permission/presentation/telemetry` should be represented as explicit subtypes or first-class types. The specific schema still requires a later design decision.

## Still Unknown and Not for This Research to Decide on the Owner's Behalf

- Unified bucket boundaries for head/tail, tenant size, and ACL density.
- The minimum sample, confidence, or promotion threshold for each query class.
- How much per-stage trace an A/B test must retain to balance privacy, cost, and reproducibility.
- Whether a managed vendor ranking/model change without a version receipt may enter `action-ready`.
- The exact risk policy when a security regression conflicts with a relevance improvement.
- Whether the final enterprise-search success metric should use task success, session utility, time-to-content, CTR, or a combination; public sources provide no unified answer across enterprises.

## Sources

- Azure AI Search, [Semantic ranking overview](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview) (accessed: 2026-08-11)
- Azure AI Search, [Document-level access control](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) (accessed: 2026-08-11)
- Azure AI Search, [Indexers](https://learn.microsoft.com/en-us/azure/search/search-indexer-overview) (accessed: 2026-08-11)
- Google Agent Search, [Set up data source access control](https://cloud.google.com/generative-ai-app-builder/docs/data-source-access-control) (accessed: 2026-08-11)
- Google Agent Search, [Long-running operations](https://cloud.google.com/generative-ai-app-builder/docs/long-running-operations) (accessed: 2026-08-11)
- Elastic, [Near real-time search](https://www.elastic.co/guide/en/elasticsearch/reference/current/near-real-time.html) (accessed: 2026-08-11)
- Elastic, [Synonyms](https://www.elastic.co/docs/solutions/search/full-text/search-with-synonyms) (accessed: 2026-08-11)
- OpenSearch, [Hybrid search](https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/index/) (accessed: 2026-08-11)
- OpenSearch, [Hybrid search explain](https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/explain/) (accessed: 2026-08-11)
- OpenSearch, [Debugging a search pipeline](https://docs.opensearch.org/latest/search-plugins/search-pipelines/debugging-search-pipeline/) (accessed: 2026-08-11)
- OpenSearch, [Document-level security](https://docs.opensearch.org/latest/security/access-control/document-level-security/) (accessed: 2026-08-11)
- Microsoft Research, [An experimental comparison of click position-bias models](https://www.microsoft.com/en-us/research/publication/an-experimental-comparison-of-click-position-bias-models/) (accessed: 2026-08-11)
- Microsoft Research, [Beyond Clicks](https://www.microsoft.com/en-us/research/publication/beyond-clicks-query-reformulation-as-a-predictor-of-search-satisfaction/) (accessed: 2026-08-11)
- Microsoft Research, [Beyond Success Rate](https://www.microsoft.com/en-us/research/publication/beyond-success-rate-utility-as-a-search-quality-metric-for-online-experiments/) (accessed: 2026-08-11)
- Microsoft Research, [Data-driven evaluation metrics for heterogeneous SERPs](https://www.microsoft.com/en-us/research/publication/data-driven-evaluation-metrics-for-heterogeneous-search-engine-result-pages/) (accessed: 2026-08-11)
- Microsoft Search, [Queries usage report](https://learn.microsoft.com/en-us/microsoftsearch/queries-usage-reports) (accessed: 2026-08-11)
- Google Research, [Estimating Position Bias without Intrusive Interventions](https://research.google/pubs/estimating-position-bias-without-intrusive-interventions/) (accessed: 2026-08-11)
- Google Research, [Learning to Rank with Selection Bias in Personal Search](https://research.google/pubs/learning-to-rank-with-selection-bias-in-personal-search/) (accessed: 2026-08-11)
- Google Agent Search, [Record user events](https://cloud.google.com/generative-ai-app-builder/docs/user-events) (accessed: 2026-08-11)
- Google Agent Search, [View analytics](https://cloud.google.com/generative-ai-app-builder/docs/view-analytics) (accessed: 2026-08-11)
