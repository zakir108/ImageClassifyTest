# Mpox Skin-Lesion Image Classification — Research Model

## Overview

This repository supports research on image-based classification of suspected mpox skin lesions using machine learning. The intended goal is to investigate whether computer-vision models can distinguish mpox-related lesions from other visually similar skin conditions and assist future research on screening and diagnostic decision support.

**Research-paper source:** [Add paper title, authors, publication venue, year, DOI/URL]. The specific methodology, dataset, outcomes, and limitations should be documented here once verified against the paper. No paper-specific performance claims are made in this version.

## Research workflow

The planned workflow includes preparing a labeled image dataset, choosing an image-classification architecture, training the model, and evaluating its performance on held-out data. Evaluation should report class definitions, dataset provenance and split strategy, sensitivity, specificity, precision, recall, F1 score, and confusion matrix as appropriate.

## Files

- `mpox.safetensors` — **temporary placeholder weights**. The current file contains synthetic, untrained tensors and is **not** the trained model from a research paper. Replace it with trained weights after verifying the architecture and provenance.
- `model_info.json` — metadata for the temporary demonstration tensors; update when replacing the weights.
- `inspect_weights.py` — simple utility for inspecting the current tensor file.

## Model status

**Research implementation in progress.** The trained Mpox classification weights, matching architecture, image preprocessing pipeline, and verified evaluation results have **not yet been added**. This package cannot currently make meaningful predictions from skin images.

When real weights become available, document:

1. Exact source paper and dataset, including permission and license for redistribution.
2. Model architecture, input image size, normalization, and class labels.
3. Training setup, data splits, and independent test results.
4. Weight file version, checksum, and instructions to load and run inference.
5. Known limitations, potential biases, and intended research use.

## Intended use and limitations

This project is intended for **research and education only**. Skin lesions with similar appearances may have different causes; image-based predictions alone cannot establish mpox infection. The model is not clinically validated and must not be used as a substitute for clinical examination or appropriate laboratory testing.

## Citation

[Add complete reference for the Mpox research paper and any dataset/model sources before attributing methods or findings to them.]
