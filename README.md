# Mpox Skin-Lesion Classification Using Deep Learning

## Research Overview
This repository is dedicated to research on automated recognition of mpox-associated skin lesions from clinical images. Image-based classification has been studied as a potential **screening and decision-support** approach, especially where rapid specialist assessment is difficult. A skin-image prediction is not a confirmed diagnosis: the CDC recommends real-time PCR testing of lesion material for mpox diagnosis.

## Published Research Findings
Thieme et al. (2023) developed **MPXV-CNN** and evaluated it on a collection of 139,198 skin-lesion images, including 676 mpox images. The published study reported:

| Metric | Published test-cohort result |
|---|---:|
| Sensitivity | 0.91 |
| Specificity | 0.898 |
| Area under ROC curve (AUC) | 0.966 |

The authors also reported sensitivity of 0.89 in a prospective clinical-image cohort. **These are the paper's results, not performance measurements for this repository's weight file.** The study highlights the promise of image-based classification while leaving important questions about external generalizability and clinical deployment.

## Repository Model
- **Proposed model file:** `models/mpox.safetensors`
- **Purpose:** Store model parameters for the Mpox skin-lesion classification research.
- **Model architecture, training dataset, input preprocessing, and class labels:** To be documented for the research-trained version.
- **This repository's validation metrics:** To be added from the associated experiment and paper.
- **Weight update:** The research-trained weights will be uploaded in a subsequent revision.

The current sample weight file supplied earlier in this project has **not been established as the research-trained model**. Do not associate it with the cited publication's architecture, training data, or performance until independently confirmed. When replacing it, update `model_info.json`, preprocessing instructions, and evaluation results together.

## Research Direction
The project investigates computational methods for analyzing skin-lesion images, with attention to differentiating mpox from visually similar conditions. Research evaluation should include independent test data, sensitivity, specificity, precision, recall, F1 score, AUC, confusion matrices, and analysis across varied image sources and skin tones where data permit.

## Intended Use
**Research and educational use only.** Image classification does not replace clinician assessment or confirmatory laboratory testing. No clinical validation or diagnostic authorization is claimed for the repository model.

## References
1. Thieme, A. H., Zheng, Y., Machiraju, G., et al. (2023). **A deep-learning algorithm to classify skin lesions from mpox virus infection.** *Nature Medicine, 29*, 738–747. https://doi.org/10.1038/s41591-023-02225-7
2. Centers for Disease Control and Prevention (2026). **Diagnostic Testing for Monkeypox.** https://www.cdc.gov/monkeypox/hcp/diagnosis-testing/index.html

## Citation for This Project
If you use this repository, please cite the **project's own paper** when its authors, title, publication details, and DOI are added. Reference [1] is background literature, not a claim that this repository reproduces that model.
