# Graph Report - corruption_study  (2026-10-02)

## Corpus Check
- 384 files · ~123,405 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 733 file(s) not represented in the graph (top: .csv 730, (none) 3)

## Summary
- 259 nodes · 383 edges · 21 communities (16 shown, 5 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `da7ad651`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- run_corruption_eval.py
- Implementation Report
- corrupt_iot.py
- Corruption Robustness Study
- corrupt_images.py
- enrich_metrics_with_bootstrap.py
- ImageDataset
- generate_report_artifacts.py
- Run Commands
- generate_thesis_report.py
- bootstrap_difference_of_drops.py
- Corruption Study Checklist
- summarize_results.py
- Thesis-Style Corruption Robustness Report
- E3 Corruption Extension Summary
- TestImageDataset
- Secondary Augmented-Training Scaffold
- passthrough_sanity_check.md
- robustness_summary.md
- severity0_sanity_check.md

## God Nodes (most connected - your core abstractions)
1. `Implementation Report` - 32 edges
2. `Corruption Robustness Study` - 15 edges
3. `Run Commands` - 11 edges
4. `main()` - 10 edges
5. `main()` - 9 edges
6. `main()` - 8 edges
7. `main()` - 8 edges
8. `Corruption Study Checklist` - 8 edges
9. `Thesis-Style Corruption Robustness Report` - 8 edges
10. `main()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `predict_e2()` --calls--> `E2MatchedK`  [EXTRACTED]
  corruption_study/eval/run_corruption_eval.py → corruption_study/eval/run_corruption_eval.py  _Bridges community 6 → community 0_
- `extract_image_embeddings()` --calls--> `TestImageDataset`  [EXTRACTED]
  corruption_study/gen/regen_embeddings.py → corruption_study/gen/regen_embeddings.py  _Bridges community 15 → community 0_

## Import Cycles
- None detected.

## Communities (21 total, 5 thin omitted)

### Community 0 - "run_corruption_eval.py"
Cohesion: 0.08
Nodes (25): align_features(), build_e0(), load_checkpoint_state(), load_classes(), load_embeddings(), main(), normalize_images(), parse_args() (+17 more)

### Community 1 - "Implementation Report"
Cohesion: 0.06
Nodes (32): Bootstrap CI Checkpoint, Both-Corrupted Pairing Revision, Clean Test Metrics Found, Commands Run For Audit, Completed E3 Corruption Matrix Checkpoint, Current Status, Data And Split Counts, E2 Embedding Interface (+24 more)

### Community 2 - "corrupt_iot.py"
Cohesion: 0.17
Nodes (12): clean_reference_rows(), ensure_dir(), main(), mean_by_seed(), parse_args(), plot_curves(), align_features(), corrupt() (+4 more)

### Community 3 - "Corruption Robustness Study"
Cohesion: 0.12
Nodes (15): Bootstrap Confidence Intervals, Corruption Robustness Study, E2 Embedding Regeneration, E3 Corruption Extension, Image Corruptions, Interpretation, IoT Corruptions, Main Outputs (+7 more)

### Community 4 - "corrupt_images.py"
Cohesion: 0.21
Nodes (9): apply_corruption(), find_image(), main(), motion_blur(), output_path(), parse_args(), read_manifest(), resize_clean_geometry() (+1 more)

### Community 5 - "enrich_metrics_with_bootstrap.py"
Cohesion: 0.26
Nodes (12): bootstrap_absolute(), bootstrap_drop(), clean_reference_run(), load_json(), load_predictions(), main(), parse_args(), point_metrics() (+4 more)

### Community 6 - "ImageDataset"
Cohesion: 0.14
Nodes (5): E2Canonical128To25Head, E2MatchedK, find_image(), FusionProjectionK, ImageDataset

### Community 7 - "generate_report_artifacts.py"
Cohesion: 0.33
Nodes (9): generate_passthrough_sanity(), generate_per_class_recall(), generate_severity0_sanity(), load_json(), main(), metrics_for_run(), parse_args(), prediction_runs() (+1 more)

### Community 8 - "Run Commands"
Cohesion: 0.17
Nodes (11): 1. MVP Image Corruption Generation, 2. MVP IoT Feature-Space Corruption Generation, 3. Regenerate Clean TEST Embeddings Sanity Check, 4. Regenerate MVP Corrupted E2/E2-8 TEST Embeddings, 5. Evaluation Examples, 6. Full Matrix Later, 7. Optional E2 128-to-25 Variant, 8. Supervisor-Requested E3 Corruption Evaluation (+3 more)

### Community 9 - "generate_thesis_report.py"
Cohesion: 0.33
Nodes (9): aggregate(), both_corrupted_table(), build_curve_data(), corruption_mean_drop(), fmt(), main(), model_label(), parse_args() (+1 more)

### Community 10 - "bootstrap_difference_of_drops.py"
Cohesion: 0.36
Nodes (8): bootstrap_comparison(), load_prediction(), main(), merge_predictions(), parse_args(), prediction_path(), present_class_macro_f1(), run_name()

### Community 11 - "Corruption Study Checklist"
Cohesion: 0.22
Nodes (8): Corruption Study Checklist, E3 Corruption Extension - Supervisor Request, Phase 1 - Audit, Phase 2 - Materialization, Phase 3 - Smoke Test, Phase 4 - Full Matrix, Phase 5 - Reporting, Plan-Level Remaining Items

### Community 12 - "summarize_results.py"
Cohesion: 0.36
Nodes (6): add_clean_references(), load_metrics(), main(), make_robustness_summary(), parse_args(), write_markdown()

### Community 13 - "Thesis-Style Corruption Robustness Report"
Cohesion: 0.22
Nodes (8): Bootstrap Settings, Direct Difference-of-Drops Bootstrap, Image Corruption Degradation, Interpretation Guardrail, IoT Corruption Degradation, Output Tables, Representative Paired Stress Conditions, Thesis-Style Corruption Robustness Report

### Community 14 - "E3 Corruption Extension Summary"
Cohesion: 0.25
Nodes (7): Attack E3 Drop Minus Original E3 Drop, Clean Sanity Metrics, E3 Corruption Extension Summary, Extra Macro-F1 Drop Versus E2-8, Interpretation, Mean Robustness Drops, Output Coverage

### Community 16 - "Secondary Augmented-Training Scaffold"
Cohesion: 0.33
Nodes (5): Guardrails, Proposed Evaluation, Recommended Augmentations, Recommended First Scope, Secondary Augmented-Training Scaffold

## Knowledge Gaps
- **82 isolated node(s):** `Phase 1 - Audit`, `Phase 2 - Materialization`, `Phase 3 - Smoke Test`, `Phase 4 - Full Matrix`, `Phase 5 - Reporting` (+77 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 122 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `TestImageDataset` connect `TestImageDataset` to `run_corruption_eval.py`?**
  _High betweenness centrality (0.016) - this node is a cross-community bridge._
- **Why does `ImageDataset` connect `ImageDataset` to `run_corruption_eval.py`?**
  _High betweenness centrality (0.016) - this node is a cross-community bridge._
- **What connects `Phase 1 - Audit`, `Phase 2 - Materialization`, `Phase 3 - Smoke Test` to the rest of the system?**
  _82 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `run_corruption_eval.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0782608695652174 - nodes in this community are weakly interconnected._
- **Should `Implementation Report` be split into smaller, more focused modules?**
  _Cohesion score 0.06060606060606061 - nodes in this community are weakly interconnected._
- **Should `Corruption Robustness Study` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._
- **Should `ImageDataset` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._