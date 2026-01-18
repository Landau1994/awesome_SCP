---
title: Benchmarking informatics workflows for data-independent acquisition single-cell proteomics
authors:
  - Jianwei Wang
  - Yi Huang
  - Fanghua Lu
  - Qinqin Xu
  - Zhuo Yang
  - Yirong Jiang
  - Shaowen Shi
  - Jianzhang Pan
  - Yi Yang
  - Qun Fang
aliases:
   - informatics workflows for DIA sc-proteomics
   - scDIA benchmarking
tags:
  - literature
  - paper
category: literature
date_created: 2024-05-22
Journal: Nature Communications
Year: 2025
---

# Benchmarking informatics workflows for data-independent acquisition single-cell proteomics

## Citation

> [!cite] Reference
> **Title**：Benchmarking informatics workflows for data-independent acquisition single-cell proteomics
> **Authors**: Jianwei Wang, Yi Huang, Fanghua Lu, Qinqin Xu, Zhuo Yang, Yirong Jiang, Shaowen Shi, Jianzhang Pan, Yi Yang, Qun Fang
> **Year**: 2025
> **Journal**: Nature Communications
> **DOI**: https://doi.org/10.1038/s41467-025-65174-4

## Abstract

Single-cell proteomics (SCP) using data-independent acquisition mass spectrometry (DIA MS) has advanced rapidly, yet the impact of diverse data analysis strategies on experimental outcomes remains under-investigated. This study presents a framework for benchmarking DIA-based SCP data analysis strategies. It comprehensively evaluates popular software tools (DIA-NN, Spectronaut, and PEAKS Studio), searching strategies (library-based vs. library-free), and downstream informatics steps, including sparsity reduction, missing value imputation, normalization, batch effect correction, and differential expression analysis. Using simulated mixed-proteome samples and real spike-in single-cell samples, the authors identify high-performing method combinations and provide concrete recommendations for optimizing SCP DIA workflows.

## Key Points

- **Software Performance**: Spectronaut (directDIA) generally identifies the highest number of proteins/peptides, while DIA-NN exhibits superior quantitative accuracy and robustness across various library types.
- **Workflow Recommendations**: Sparsity reduction (targeting ~75% data completeness) is crucial. High-performing combinations for differential expression include SoftImpute, Sum normalization, ComBat-P/NP, and DESeq2.
- **Batch Effect Correction**: Batch effects are a major driver of variability even in technical replicates; correction methods like ComBat-P or limma are essential for identifying true biological differences in SCP datasets.

## Methods

### Sample Preparation
- **Method used**: Simulated single-cell samples (mixed tryptic digests of Human HeLa, Yeast, and E. coli at defined ratios) and real single-cell samples using a microfluidic PiSPA platform.
- **Cell type**: HeLa, Yeast, E. coli (simulated); MCF-7 cells treated with doxorubicin/DMSO (real).
- **Number of cells**: Single-cell equivalents (approx. 200–250 pg protein per injection).

### Data Analysis
- **Software**: DIA-NN (v1.9.2), Spectronaut (v19.5), PEAKS Studio (v12.0).
- **Downstream**: Evaluation of 4900 method combinations using metrics like Adjusted Rand Index (ARI), partial area under the ROC curve (pAUC), and F1-score. Machine learning (XGBoost/SHAP) was used to identify key drivers of performance.

## Results

### Main Findings
1. **Detection vs. Quantification**: Spectronaut excelled in protein coverage (depth), but DIA-NN provided the most accurate fold-change estimates and lower coefficient of variation (CV) for protein quantities.
2. **Library Strategies**: Sample-specific spectral libraries generally outperformed public or in-silico predicted libraries, though library-free approaches (directDIA, DIA-NN library-free) are viable alternatives.
3. **Workflow Sensitivity**: Normalization and batch correction steps were found to have a more significant impact on the final biological interpretation (ARI/pAUC) than missing value imputation.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Comparison of protein identification and quantification accuracy across DIA-NN, Spectronaut, and PEAKS using simulated samples. |
| Fig 2 | Benchmarking of ~4900 informatics combinations for batch effect correction and differential expression analysis. |
| Fig 3 | SHAP analysis identifying the "patterns" of high-performing method combinations (e.g., importance of statistical tests and normalization). |
| Fig 4 | Evaluation of high-performing workflows on real MCF-7 single-cell samples with spike-ins to assess biological insights. |
| Fig 5 | Comparison of GO and Reactome pathway enrichment results across different informatics workflows. |

## Discussion

### Strengths
- Provides a systematic and comprehensive evaluation of the entire informatics pipeline, not just the initial search software.
- Uses both ground-truth simulated data and real-world biological perturbation samples.
- Introduces an open-access framework (SCPDA) for others to perform similar benchmarking.

### Limitations
- The study primarily focuses on the timsTOF platform (diaPASEF); while applicable to others, platform-specific nuances might exist for Orbitrap or Astral instruments.
- Benchmarking is limited to a subset of available statistical methods and software versions available at the time of study.

### Future Work
- Integration of multiple workflows via a "voting model" or ensemble approach to improve the reliability of single-cell proteomic findings.
- Expanding benchmarking to newer, high-throughput mass spectrometers like the Orbitrap Astral.

## Personal Notes
- *Sparsity reduction (SR75) seems to be a sweet spot for balancing data depth and quantitative reliability.*
- *The findings highlight that software choice is just the beginning; downstream normalization and batch correction are where biological signal is often lost or found.*

## Related Papers
- Demichev, V. et al. (2020) DIA-NN: neural networks and interference correction... *Nat. Methods*.
- Brunner, A. D. et al. (2022) Ultra-high sensitivity mass spectrometry... *Mol. Syst. Biol.*
- Tran, H. T. N. et al. (2020) A benchmark of batch-effect correction methods... *Genome Biol.*