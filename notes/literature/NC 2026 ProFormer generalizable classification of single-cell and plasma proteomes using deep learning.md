---
title: ProFormer:generalizable classification of single-cell and plasma proteomes using deep learning
authors:
  - Karl K. Krull
  - Arlene Kühn
  - Julia Höhn
  - Syed Azmal Ali
  - Martin H. Otterbein
  - Titus J. Brinker
  - Jeroen Krijgsveld
aliases:
  - ProFormer
tags:
  - literature
  - paper
  - proteomics
  - deep-learning
  - transformer
category: literature
date_created: 2025-05-14
Journal: Nature Communications
Year: 2026
---

# ProFormer: generalizable classification of single-cell and plasma proteomes using deep learning

## Citation

> [!cite] Reference
> **Title**：ProFormer: generalizable classification of single-cell and plasma proteomes using deep learning
> **Authors**: Karl K. Krull, Arlene Kühn, Julia Höhn, Syed Azmal Ali, Martin H. Otterbein, Titus J. Brinker, Jeroen Krijgsveld
> **Year**: 2026
> **Journal**: Nature Communications
> **DOI**: 10.1038/s41467-026-78143-2

## Abstract

Proteomics is essential for defining cell identity and biomarker discovery, yet limited throughput and complex data interpretation hinder large-scale cohort studies. The authors introduce ProFormer, a transformer-based deep learning pipeline for the direct analysis of mass spectrometry (MS) data. By utilizing tabular MS1-level features (m/z, retention time, ion mobility, and intensity) through a learnable "patch merger" rather than image-based binning, ProFormer achieves superior classification accuracy and robustness against batch effects. The model demonstrates high efficacy in annotating single-cell proteomes (e.g., cell type, cycle stage, and differentiation trajectory) and identifying disease status from plasma. Furthermore, ProFormer provides single-peptide resolution explainability through SHAP (SHapley Additive exPlanation) values, linking predictions to underlying biological processes, such as complement activation in COVID-19 patients.

## Key Points

- ProFormer avoids the information loss inherent in converting MS data to "image-like" heatmaps by using a learnable patch merger to process tabular data.
- The pipeline demonstrates strong resilience to technical domain shifts (batch effects) and superior performance over existing CNN and traditional ML models in across-dataset generalization.
- The use of SHAP values enables explainable AI in proteomics, allowing for the identification of specific, biologically relevant peptide ions that drive model predictions.

## Methods

### Sample Preparation
- Method used: [[diaPASEF]] LC-MS/MS, peptide digestion using [[Trypsin]].
- Cell type: HeLa S3 cells (IFN-γ treatment experiments), various single-cell datasets (e.g., HEK-293T, K562, A549, mESC, U-2 OS), and human plasma.
- Number of cells: Ranges from bulk samples down to single-cell instances (e.g., 30,000 cells per culture for IFN-γ studies).

### Data Analysis
- Software: [[DIA-NN]], [[MaxQuant]], [[Python]], [[PyTorch]], [[Scikit-learn]], [[XGBoost]], [[Optuna]], [[SHAP]].
- Downstream: [[Principal Component Analysis]], [[t-SNE]], [[Random Forest]], [[SHAP]]-based feature importance analysis.

## Results

### Main Findings
1. ProFormer consistently outperformed 14 other architectures, including traditional ML (Logistic Regression, Random Forest, XGBoost) and various CNNs (ResNet, EfficientNet, DenseNet), in classification accuracy and batch robustness.
2. The model exhibits high sensitivity and generalization, successfully resolving dose-dependent proteome perturbations and classifying single-cell proteomes across varied biological conditions.
3. ProFormer enabled the identification of biologically meaningful peptides—such as those from C3 and C4A proteins—associated with severe COVID-19, confirming that model predictions reflect genuine clinical/biological differences rather than technical artifacts.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Conceptual design of the ProFormer pipeline using a learnable patch merger to reduce high-dimensional MS data into tokens for a transformer. |
| Fig 2 | Benchmarking ProFormer against alternative ML and DL pipelines using the in-house IFN-γ dataset; demonstrates superior AUC and robust generalization. |
| Fig 3 | Explanations of data aggregation by the patch merger, demonstrating how it focuses on non-random, biologically informative regions in feature space. |
| Fig 4 | Exploration of data attributes and model robustness; testing with varying peptide abundances, training set sizes, and artificial Gaussian noise. |
| Fig 5 | Application of ProFormer to plasma proteome classification (COVID-19 severity) and use of SHAP values to explain individual peptide ion contributions. |

## Discussion

### Strengths
- Avoids the potential loss of information and artifacts associated with binning data into image-like heatmaps.
- Robust to batch effects and capable of domain generalization.
- High interpretability at a single-peptide resolution, facilitating the discovery of biomarkers.
- Flexible input allows for the integration of additional features like ion mobility.

### Limitations
- While designed to be peptide/protein-agnostic, the current implementation relied on MS1 feature extraction informed by MS2-based identification.
- Performance in single-cell settings is heavily dependent on data quality, necessitating the filtering of low-abundance/missing-value peptide ions.

### Future Work
- Transitioning to a fully database search-free model that operates independently of MS2 information or in the complete absence of MS2 data.
- Further algorithmic development to process raw MS data directly to improve MS1 feature capture.

## Personal Notes



## Related Papers

- [[Cadow et al. 2021]] - On the feasibility of deep learning applications using raw mass spectrometry data.
- [[Seddiki et al. 2020]] - Cumulative learning enables convolutional neural network representations for small mass spectrometry data classification.
- [[Vaswani et al. 2017]] - Attention is all you need.
- [[Demichev et al. 2020]] - DIA-NN: neural networks and interference correction enable deep proteome coverage in high throughput.