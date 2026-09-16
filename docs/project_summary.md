# DisasterSense Project Summary

## Overview

DisasterSense is a deep learning project focused on disaster image classification. The goal is to automatically recognize disaster categories from visual data and compare different model architectures for performance and robustness.

## Problem

Emergency response systems require rapid detection of disasters from imagery. Accurate classification helps teams react faster, allocate resources, and improve situational awareness.

## Objective

The project evaluates how well different deep learning architectures classify disaster images and identifies the most effective model for the task.

## Models compared

1. CNN baseline
2. CNN with patch-based decomposition
3. Vision Transformer with self-attention

## Results

| Model | Accuracy | Precision | Recall | F1-Score |
| --- | ---: | ---: | ---: | ---: |
| CNN | 93.33% | 93.99% | 93.33% | 93.31% |
| CNN + Patches | 90.00% | 91.03% | 90.00% | 89.98% |
| Vision Transformer | 98.33% | 98.41% | 98.33% | 98.33% |

## Key insight

Patches alone reduced the performance of the CNN model, but adding self-attention allowed the Vision Transformer to model relationships between image regions effectively. This led to the best overall result and demonstrated why attention-based models excel on visual disaster detection tasks.

## Technologies used

- Python
- PyTorch
- Torchvision
- Transformers
- NumPy
- Pandas
- Matplotlib
- Seaborn
- scikit-learn

## Future extensions

- larger and more diverse datasets
- real-time streaming detection
- geospatial integration
- mobile or web deployment
- multi-label detection for combined disaster events

## Conclusion

DisasterSense demonstrates the value of modern vision architectures for disaster recognition. The Vision Transformer proved to be the strongest model and provides a strong foundation for future disaster monitoring and response systems.
