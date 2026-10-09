# Synthetic skin-classifier weights (demonstration only)

This repository contains **random, untrained** weights for an illustrative two-layer neural network. These values are **not learned from skin images** and must **never** be used for diagnosis, health decisions, or model performance claims.

## Files
- `mpox.safetensors`: four synthetic tensors; input=4 features, hidden=8, output=3 demonstration categories.
- `inspect_weights.py`: loads and prints tensor names and shapes.
- `model_info.json`: architecture details and disclaimer.

## Inspect
`pip install safetensors numpy`

`python inspect_weights.py`

These are not compatible with ResNet, ViT, or image-based skin classifiers. For meaningful image classification, supply a suitable model architecture, labeled training data, evaluation, preprocessing and licensed trained weights.
