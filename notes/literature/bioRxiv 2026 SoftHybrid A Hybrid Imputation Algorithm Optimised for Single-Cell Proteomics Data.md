---
title: SoftHybrid:A Hybrid Imputation Algorithm Optimised for Single-Cell Proteomics Data
authors:
  - Yixin Shi
  - Simon Davis
  - Philip D. Charles
  - Stephen Taylor
  - Eszter Dombi
  - Georgina Berridge
  - Daniel Ebner
  - Roman Fischer
aliases:
   - SoftHybrid
   - Shi et al. 2026
tags:
  - literature
  - paper
  - single-cell-proteomics
  - imputation
  - bioinformatics
category: literature
date_created: 2026-01-14
Journal: bioRxiv
Year: 2026
---

# SoftHybrid: A Hybrid Imputation Algorithm Optimised for Single-Cell Proteomics Data

## Citation

> [!cite] Reference
> **Title**：SoftHybrid: A Hybrid Imputation Algorithm Optimised for Single-Cell Proteomics Data
> **Authors**: Yixin Shi, Simon Davis, Philip D. Charles, Stephen Taylor, Eszter Dombi, Georgina Berridge, Daniel Ebner, Roman Fischer
> **Year**: 2026
> **Journal**: bioRxiv
> **DOI**: 10.64898/2026.01.13.699212

## Abstract

Missing values (MVs) remain a significant barrier to reliable proteomics analysis, particularly in single-cell proteomics, where small amounts of starting material and limits in detection drive Missing-Not-At-Random (MNAR) sparsity. Commonly used bulk proteomic imputation approaches typically address Missing-At-Random (MAR) MVs and improve replicate consistency at the expense of sensitivity for biological variation, whereas MNAR-specific strategies preserve group differences but compromise cross-replicate reproducibility. Existing imputation methods are commonly applied to bulk data and do not offer a generalised ‘off-the shelf’ implementation that robustly addresses the significant sparsity observed in single-cell studies. Here, we introduce SoftHybrid, a continuous weighting framework that automatically balances MAR- and MNAR-oriented imputation across a dataset-derived model between missing rate and protein abundance model. Benchmarking across known ground truth samples (three-species mix) and real single-cell proteomics data showed that SoftHybrid outperforms existing methods at low inputs while meeting or exceeding previous state-of-the-art performance at the mini-bulk level. Preservation of proteomic patterns and enhanced replicate consistency improve testing significance and boost recovery of biological signals. SoftHybrid is implemented as an R package and freely available on GitHub.

## Key Points

- Introduction of **SoftHybrid**, an imputation strategy that uses a sigmoid weighting function to balance between MAR-oriented ([[Random Forest]]) and MNAR-oriented ([[minProb]]) methods based on protein missing rate and abundance.
- SoftHybrid demonstrates superior performance in low-input and single-cell settings compared to standard methods (Gaussian, KNN, RF, minProb), particularly in preserving both cluster separation and replicate consistency.
- The method is effective for both [[DDA]] and [[DIA]] acquisition modes and improves the recovery of biological signals (e.g., hypoxia pathways) without inflating false positives.

## Methods

### Sample Preparation
- Method used: [[LC-MS/MS]] (Bruker timsTOF Ultra2), [[dia-PASEF]], [[CellenONE]] (single-cell isolation), proteoCHIP EVO 96 nanowell plates.
- Cell type: E57 glioblastoma stem cells ([[GSC]]), astrocytes ([[AST]]), macrophages ([[MAC]]), microglia ([[MIC]]), and KOLF2.1S [[iPSC]]s. Three-species mix (Human, Yeast, *E. coli*).
- Number of cells: Single cells (approx. 76-106 retained after QC) and 50-cell mini-bulk aggregates.

### Data Analysis
- Software: [[DIA-NN]] (v1.8.1/2.1.0), [[FragPipe]] (v23.1, [[MSFragger]]), [[R]], [[Bioconductor]].
- Downstream: [[PCA]], [[limma]] (differential expression), [[GSEA]] (Pathway enrichment), [[Adjusted Rand Index]] (ARI).

## Results

### Main Findings
1. **Imputation Trade-offs**: Conventional methods like [[Random Forest]] (RF) and [[KNN]] compress biological heterogeneity, while [[minProb]] and [[Gaussian]] (Perseus-style) preserve group differences but reduce replicate consistency. SoftHybrid effectively bridges this gap.
2. **Benchmark Performance**: In a controlled three-species titration, SoftHybrid achieved the lowest Mean Absolute Error (MAE) and highest macro-AUC at single-cell equivalent inputs (50 pg and 100 pg) for both [[DIA]] and [[DDA]] modes.
3. **Biological Interpretability**: In a hypoxia vs. normoxia single-cell dataset, SoftHybrid recovered the strongest hypoxia signature (highest NES and statistical support) while maintaining low noise levels comparable to other methods, avoiding the spurious pathway enrichments seen with some competitors.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Overview of benchmarking workflow: datasets (three-species, single-cell), acquisition (DDA/DIA), imputation methods compared, and evaluation metrics. |
| Fig 2 | Concept of SoftHybrid: illustrates the "elbow point" in missing rates and the sigmoid weighting scheme that transitions from RF (MAR) to minProb (MNAR). |
| Fig 3 | Impact of imputation on single-cell data: PCA plots, clustering fidelity (ARI), replicate correlation, and GSEA bubble plots showing pathway activation/suppression. |
| Fig 4 | Global and species-specific Mean Absolute Error (MAE) benchmarking across different input amounts (50pg to 10ng) for DIA and DDA. |
| Fig 5 | Scatter plots of log2 intensity ratios vs. intensity at 100pg, highlighting systematic biases (red boxes) in other methods compared to SoftHybrid. |
| Fig 6 | Macro-ROC curves evaluating detection sensitivity (TPR vs FPR) for different imputation methods across input doses in DIA and DDA modes. |
| Fig 7 | Real-world single-cell performance: PCA clustering, performance scores (ARI, correlation), and specific GSEA results for the Hypoxia pathway. |

## Discussion

### Strengths
- **Hybrid Approach**: continuously interpolates between MAR and MNAR mechanisms rather than using rigid bins, adapting to the "mixed" nature of missingness in proteomics.
- **Robustness**: Perform well across varying sparsity levels, from single-cell (high MNAR) to bulk (mixed/MAR), and across acquisition modes ([[DDA]] and [[DIA]]).
- **Usability**: Implemented as an open-source [[R]] package.

### Limitations
- **Computational Cost**: Incorporating [[Random Forest]] makes the method computationally intensive compared to simpler methods; processing 76 samples took ~20 minutes.
- **Sample-Specific Effects**: The weighting scheme is protein-centric and does not explicitly model sample-specific technical failures (e.g., failed injections), though RF partially compensates for this.

### Future Work
- Potential application to other sparse proteomic datasets, such as post-translational modification (PTM) analyses, clinical samples, or immune-enrichment experiments.

## Personal Notes



## Related Papers

- [[notes/methods/MsImpute]]: "MsImpute: Estimation of Missing Peptide Intensity Data in Label-Free Quantitative Mass Spectrometry" (Ref 23)
- [[MissForest]]: "MissForest--non-parametric missing value imputation for mixed-type data" (Ref 16)
- [[Perseus]]: "The Perseus computational platform for comprehensive analysis of (prote)omics data" (Ref 13)
- [[MinProb]]: Discussed as a standard Left-censored method (Ref 17)