# Crop-disease corruption robustness

TEST-only image, IoT, and paired corruption; frozen-model evaluation; bootstrap intervals and difference-of-drops analysis; classical and E3 comparison reports. The snapshot contains 361 saved condition metric files. Findings depend on the model and corruption; no broad quantum robustness advantage is claimed. The train-on-corrupted scaffold is unrun.

This is an independent local research snapshot extracted on 2026-10-12.
No GitHub repository or release has been created; future publication is intended to be private.
It does not require the original thesis checkout or a sibling repository for code imports.

## Start here

Read [RUN_COMMANDS.md](RUN_COMMANDS.md) for environment setup, safe verification,
artifact downloads and examples. Read [provenance/VERIFICATION.md](provenance/VERIFICATION.md)
for checks actually run and their limits.

- `corruption_study/gen/`: corruption and embedding generation.
- `corruption_study/eval/`: inference, aggregation, bootstrap statistics and plots.
- `corruption_study/results/`: preserved condition results, predictions, confusion matrices and reports.
- `common/quantum_models.py`: frozen E3 inference classes; PennyLane loads only when quantum models are requested.
- Other model folders contain frozen inference inputs, not copies of the companion training projects.

## Companion repositories

- [crop-multimodal-baselines](../crop-multimodal-baselines/README.md)
- [crop-quantum-fusion](../crop-quantum-fusion/README.md)
- [crop-corruption-robustness](../crop-corruption-robustness/README.md)

The baselines repository holds the local frozen embedding bundle in `.artifacts/embeddings-v1.zip`. Quantum fusion consumes
those embeddings, while robustness evaluates frozen models from both projects.
Each repository includes versioned copies of the small helpers it needs. No submodule
or implicit sibling-directory lookup is required. [COMPANIONS.json](COMPANIONS.json)
records the pinned companion commits; [ARTIFACTS.json](ARTIFACTS.json) records exact input hashes.

## Data and protocol

The fixed legacy split manifests contain 46,713 / 5,193 / 5,767 train/validation/test
rows and 25 combined crop-disease-stage classes. Legacy training/validation labels
are documented as pseudo/generated. These results must not be conflated with later
trusted-label HDC or QCNN protocols. Stage 0 is healthy; stages 1/2/3 are early/mid/severe.

Raw images, sensor files and regenerated corrupted inputs are not distributed here.
Provide an authorized dataset separately. Split CSVs, saved metrics, selected model
weights and predictions are retained; frozen embeddings are present locally and packaged in the local bundle.
Historical absolute paths inside result files are provenance, not runtime dependencies.

## Provenance and maintenance

Source: `yes-yes-company/THESIS`, commit `da7ad651d7e3eaebfa2216950a5f2dd0d0640a1a`.
See [NOTICE.md](NOTICE.md), [provenance/SOURCE_MANIFEST.json](provenance/SOURCE_MANIFEST.json),
and [provenance/CHANGES.md](provenance/CHANGES.md). Historical experiment runbooks preserve
the original chronology and may contain old machine paths or superseded status text;
the root runbook and verification record take precedence. Canonical artifacts remain
frozen. Update shared helper copies only deliberately, with source hashes and parity checks.

Related, separate research: [QCNN](https://github.com/Shafin-paranoid-Ahmed/qcnn) and
[QEMCMC](https://github.com/Shafin-paranoid-Ahmed/qemcmc). They use different protocols and are not part
of this benchmark. No new experiments were run as part of extraction.
