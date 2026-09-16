# DisasterSense

## One-page project overview

DisasterSense is a disaster image classification project built to compare different deep learning models for identifying disaster categories from visual data. The goal is to improve automated emergency response support by detecting patterns in disaster imagery faster and more accurately.

### Dataset
- 300 total images
- 3 classes: earthquakes, floods, wildfires
- 80/20 train-test split
- Preprocessed and augmented for training

### Models evaluated
- CNN baseline
- CNN with patches
- Vision Transformer

### Performance summary
- CNN: 93.33% accuracy
- CNN + Patches: 90.00% accuracy
- Vision Transformer: 98.33% accuracy

### Main finding
The Vision Transformer produced the strongest performance because self-attention helps the model understand long-range relationships across image regions. Patch-based processing alone did not help enough, but the attention mechanism significantly improved the model's ability to detect disaster patterns.

### Why this matters
This system can support rapid disaster response, better resource planning, and improved situational awareness in emergency scenarios.

### Tools used
Python, PyTorch, Torchvision, Transformers, scikit-learn, Matplotlib, Seaborn.

### Project status
Research project completed and packaged with documentation, presentation assets, and repository-ready files.
