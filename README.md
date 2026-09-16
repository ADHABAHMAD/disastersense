# DisasterSense

Deep Learning for Disaster Classification using CNNs and Vision Transformers.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Research%20Project-success)

</div>

DisasterSense is a deep learning project for the automatic classification of disaster images. The system compares three architectures to determine which performs best for identifying disaster types from visual data:

- CNN baseline
- CNN with patch-based image decomposition
- Vision Transformer with self-attention

The results show a clear advantage for the Vision Transformer, which achieved the highest classification accuracy in this study.

## Highlights

- 3-class disaster classification: earthquakes, floods, and wildfires
- comparative analysis of CNN and transformer-based models
- performance evaluation using accuracy, precision, recall, and F1-score
- academic report and presentation assets included in the repository

## Key results

| Model | Accuracy | Precision | Recall | F1-Score |
| --- | ---: | ---: | ---: | ---: |
| CNN baseline | 93.33% | 93.99% | 93.33% | 93.31% |
| CNN + Patches | 90.00% | 91.03% | 90.00% | 89.98% |
| Vision Transformer | 98.33% | 98.41% | 98.33% | 98.33% |

The Vision Transformer achieved the best result with only 1 error out of 60 test images, establishing it as the strongest architecture for this task.

## Problem statement

Rapid disaster identification is crucial for emergency response, planning, and resource allocation. This project investigates whether patch-based image processing and self-attention improve classification performance on disaster imagery.

## Research questions

1. Does dividing an image into patches improve or damage CNN performance?
2. How much does self-attention improve classification quality?
3. Which model is best for disaster recognition from image data?

## Dataset

The study uses a dataset of disaster images with three classes:

- Earthquakes
- Floods
- Wildfires

Details:

- Total images: 300
- Train/test split: 80/20
- Image size: 224 × 224 RGB
- Preprocessing: resizing, normalization, augmentation

## Methodology

Three models were trained under similar conditions:

### 1. CNN baseline
A ResNet50-based full-image classifier.

### 2. CNN with patches
The image is divided into patches and processed without attention.

### 3. Vision Transformer
Image patches are converted into tokens and processed using self-attention layers.

## Main finding

The results demonstrate that:

- patch-based decomposition alone reduced performance,
- self-attention significantly improved understanding of spatial relationships,
- the Vision Transformer provided the strongest overall results.

This suggests that attention mechanisms are the key ingredient for high-quality disaster recognition from visual patterns.

## Repository layout

- [README.md](README.md) — GitHub-ready project overview
- [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) — one-page summary
- [docs/project_summary.md](docs/project_summary.md) — detailed project summary
- [disastersense/README (1).md](disastersense/README%20%281%29.md) — full project documentation
- [disastersense/PROJECT_SUMMARY.md](disastersense/PROJECT_SUMMARY.md) — project summary file
- [disastersense/DisasterSense_Report_4.docx](disastersense/DisasterSense_Report_4.docx) — full report
- [disastersense/DisasterSense_Presentation_3.pptx](disastersense/DisasterSense_Presentation_3.pptx) — presentation deck
- [examples/basic_demo.py](examples/basic_demo.py) — example script
- [tests/test_risk_engine.py](tests/test_risk_engine.py) — validation tests

## Tech stack

- Python
- PyTorch
- Torchvision
- Transformers
- NumPy
- Pandas
- Matplotlib
- Seaborn
- scikit-learn
- Jupyter Notebook

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the demo

```bash
python examples/basic_demo.py
```

## Running the tests

```bash
python -m pytest -q
```

## Future work

- larger and more diverse disaster datasets
- real-time monitoring for disaster detection
- geospatial and map-based integration
- mobile or web deployment
- multi-label disaster recognition
- edge deployment for field use

## License

This project is distributed under the MIT License.

## Acknowledgement

This project was developed as a research and academic effort focused on disaster detection using modern computer vision techniques.
