# Crop-disease corruption robustness

**Problem.** Classify crop disease and its severity stage (25 crop-disease-stage classes) from leaf images and IoT environmental-sensor readings.

**This repository.** TEST-only image, IoT, and paired corruption; frozen-model evaluation; bootstrap intervals and difference-of-drops analysis; classical and E3 comparison reports.

**Result.** 361 saved condition metric files. Findings depend on the model and corruption; no broad quantum robustness advantage is claimed. The train-on-corrupted scaffold is unrun.

| Code | Model |
| --- | --- |
| E0 | Image-only classifier (MobileNetV3-Large) |
| E1 | IoT-sensor-only MLP |
| E2 | Classical fusion of frozen E0/E1 embeddings |
| E3 | Hybrid fusion with a variational quantum circuit (PennyLane) |

## Start here

Read [RUN_COMMANDS.md](RUN_COMMANDS.md) for environment setup, safe verification,
artifact restoration and examples. Read [provenance/VERIFICATION.md](provenance/VERIFICATION.md)
for checks actually run and their limits.

- `corruption_study/gen/`: corruption and embedding generation.
- `corruption_study/eval/`: inference, aggregation, bootstrap statistics and plots.
- `corruption_study/results/`: preserved condition results, predictions, confusion matrices and reports.
- `common/quantum_models.py`: frozen E3 inference classes; PennyLane loads only when quantum models are requested.
- Other model folders contain frozen inference inputs, not copies of the training projects.

## Project family

- [crop-multimodal-baselines](https://github.com/Shafin-paranoid-Ahmed/crop-multimodal-baselines): classical baselines and frozen embeddings
- [crop-quantum-fusion](https://github.com/Shafin-paranoid-Ahmed/crop-quantum-fusion): hybrid quantum-classical fusion experiments
- [crop-corruption-robustness](https://github.com/Shafin-paranoid-Ahmed/crop-corruption-robustness): test-time corruption robustness study (this repository)

The baselines repository builds the frozen embeddings, kept as a local bundle (`.artifacts/embeddings-v1.zip`) that is not published. Quantum fusion consumes those embeddings, while robustness evaluates frozen models from both projects.
Each repository includes versioned copies of the small helpers it needs. No submodule
or implicit sibling-directory lookup is required. [COMPANIONS.json](COMPANIONS.json)
lists the family; [ARTIFACTS.json](ARTIFACTS.json) records exact input hashes.

## Data and protocol

The fixed legacy split manifests contain 46,713 / 5,193 / 5,767 train/validation/test
rows and 25 combined crop-disease-stage classes. Legacy training/validation labels
are documented as pseudo/generated. These results must not be conflated with later
trusted-label HDC or QCNN protocols. Stage 0 is healthy; stages 1/2/3 are early/mid/severe.

Raw images, sensor files and regenerated corrupted inputs are not distributed here.
Provide an authorized dataset separately. Split CSVs, saved metrics, selected model
weights and predictions are included; frozen embeddings are in the local bundle.
Path fields in result files use `WORKSPACE` for the machine-specific directory the runs used; they are not runtime dependencies.

## Reproducibility

[provenance/MANIFEST.json](provenance/MANIFEST.json) holds SHA-256 hashes of the frozen code, splits and
result artifacts, and [provenance/NOTES.md](provenance/NOTES.md) records implementation notes. Historical experiment
runbooks preserve the original chronology and may contain superseded status text;
the root runbook and validation record take precedence. Canonical artifacts remain
frozen. Update shared helper copies only deliberately, with hashes and parity checks.

Related, separate research: [QCNN](https://github.com/Shafin-paranoid-Ahmed/qcnn) and
[QEMCMC](https://github.com/Shafin-paranoid-Ahmed/qemcmc). They use different protocols and are not part of this benchmark.

## Contributors

Shafin Ahmed ([@Shafin-paranoid-Ahmed](https://github.com/Shafin-paranoid-Ahmed)), with contributions from [@guardianbot1](https://github.com/guardianbot1) and [@thinkiamparanoid2](https://github.com/thinkiamparanoid2).
