---
title: Benchmarking informatics workflows for data-independent acquisition single-cell proteomics
aliases:
   - Benchmarking informatics workflows for DIA-SCP
   - SCPDA paper
   - Wang et al. 2025
tags:
  - literature
  - paper
  - single-cell-proteomics
  - DIA-MS
  - bioinformatics
  - benchmarking
category: literature
date_created: 2023-10-25
Journal: Nature Communications
Year: 2025
---

# Benchmarking informatics workflows for data-independent acquisition single-cell proteomics

## Citation

> [!cite] Reference
> **Title**：Benchmarking informatics workflows for data-independent acquisition single-cell proteomics
> **Authors**: Jianwei Wang, Yi Huang, Fanghua Lu, Qinqin Xu, Zhuo Yang, Yirong Jiang, Shaowen Shi, Jianzhang Pan, Yi Yang & Qun Fang
> **Year**: 2025
> **Journal**: Nature Communications
> **DOI**: https://doi.org/10.1038/s41467-025-65174-4

## Abstract

Recent years have seen a rise of single-cell proteomics by data-independent acquisition mass spectrometry (DIA MS). While diverse data analysis strategies have been reported in literature, their impact on the outcome of single-cell proteomic experiments has been rarely investigated. Here, we present a framework for benchmarking data analysis strategies for DIA-based single-cell proteomics. This framework provides a comprehensive comparison of popular DIA data analysis software tools and searching strategies, as well as a systematic evaluation of method combinations in subsequent informatic workflow, including sparsity reduction, missing value imputation, normalization, batch effect correction, and differential expression analysis. Benchmarking on simulated single-cell samples consisting of mixed proteomes and real single-cell samples with a spike-in scheme, recommendations are provided for the data analysis for DIA-based single-cell proteomics.

## Key Points

- A comprehensive benchmarking framework (SCPDA) was developed to evaluate DIA analysis software and downstream bioinformatics workflows for single-cell proteomics.
- **Software Performance**: [[DIA-NN]] demonstrated robustness across various spectral library types; [[Spectronaut]] (directDIA) and [[PEAKS Studio]] performed well in library-free modes.
- **Workflow Recommendations**: Sparsity reduction (75% data completeness) is crucial. High-performing downstream combinations often included Sum or Median normalization, Batch correction (e.g., [[ComBat]]), and statistical tests like [[DESeq2]] or [[limma]].
- **Validation**: The optimized workflows were validated on real single-cell samples ([[MCF-7]] cells treated with Doxorubicin) with spike-ins, successfully revealing relevant biological pathways (e.g., p53 signaling).

## Methods

### Sample Preparation
- **Method used**: [[diaPASEF]] acquisition on a [[timsTOF Pro 2]] mass spectrometer.
    - **Simulated Samples**: Tryptic digests of [[HeLa]], [[Yeast]], and [[E. coli]] mixed in defined proportions (Mixed-proteome samples).
    - **Real Single-Cell Samples**: Prepared using the [[PiSPA]] platform (Pick-up Single-cell Proteomics Analysis) based on a microfluidic liquid handling robot.
- **Cell type**: 
    - Human [[HeLa]] cell digest (for simulation).
    - Human [[MCF-7]] adenocarcinoma cells (treated with Doxorubicin vs DMSO control).
- **Number of cells**: 
    - Mixed proteome: 200 pg injection to mimic single cells.
    - Real cells: 60 single cells across 3 batches (spiked with Yeast/E. coli digests).

### Data Analysis
- **Software**: 
    - [[DIA-NN]] (v1.9.2)
    - [[Spectronaut]] (v19.5)
    - [[PEAKS Studio]] (v12.0)
    - [[FragPipe]] (for library building)
    - [[AlphaPeptDeep]] (for predicted libraries)
- **Downstream**: 
    - **Sparsity Reduction**: [[NoSR]], [[SR66]], [[SR75]], [[SR90]].
    - **Imputation**: [[Zero]], [[KNN]], [[SoftImpute]], [[IterativeSVD]], [[MissForest]], etc.
    - **Normalization**: [[Unnormalized]], [[Median]], [[Sum]], [[QN]], [[TRQN]], [[Scanorama]].
    - **Batch Effect Correction**: [[NoBC]], [[limma]] (removeBatchEffect), [[ComBat]] (parametric/non-parametric), [[Scanorama]].
    - **Statistical Tests**: [[t-test]], [[Wilcoxon]], [[limma]] (trend/voom), [[edgeR]], [[DESeq2]].
    - **Evaluation Metrics**: Adjusted Rand Index ([[ARI]]), [[pAUC]], F1-score, [[SHAP]] values for feature importance.

## Results

### Main Findings
1.  **Software Comparison**: [[DIA-NN]] using public libraries provided high quantification accuracy. [[Spectronaut]]'s directDIA workflow detected the highest number of proteins/peptides in library-free mode. [[PEAKS Studio]] offered a balance of sensitivity and precision in library-free mode.
2.  **Workflow Optimization**: 
    - **Sparsity Reduction**: Filtering for 75% data completeness ([[SR75]]) offered the best trade-off between protein detection numbers and minimizing false positives/missing values.
    - **Normalization & Batch Effect**: Normalization was identified as the most critical step. [[Sum]] normalization combined with [[ComBat-P]] or [[ComBat-NP]] consistently performed well.
    - **Statistical Testing**: [[DESeq2]] and [[limma-trend]] were frequently part of the top-performing combinations.
3.  **Best Combination**: A specific high-performing combination identified was **[[SoftImpute]] (Imputation) + [[Sum]] (Normalization) + [[ComBat-P]] (Batch Correction) + [[DESeq2]] (Stats)**, achieving an ARI of 1.0 and F1-score of 93% on the benchmark dataset.
4.  **Biological Application**: Applied to Doxorubicin-treated [[MCF-7]] cells, the optimized workflow successfully identified up-regulation of the TP53 pathway and down-regulation of ribosomal pathways, consistent with DNA damage responses.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Performance comparison of DIA software ([[DIA-NN]], [[Spectronaut]], [[PEAKS]]) using library-based and library-free strategies on simulated mixed-proteome samples. Shows protein/peptide counts, overlap, and quantification accuracy (fold change). |
| Fig 2 | Benchmarking of downstream workflow combinations. (a) Workflow schematic. (b) Parallel coordinate plot of metrics (ARI, pAUC, F1). (c) Composition of top 1% and 5% methods. (d-f) Impact of specific methods on metrics. (g-i) Clustering and ROC analysis of the best method combination. |
| Fig 3 | Machine learning analysis using [[XGBoost]] and [[SHAP]] values to determine the importance of each analysis step and identify patterns in high-performing method combinations (e.g., interaction between normalization and statistical tests). |
| Fig 4 | Performance evaluation on real single-cell samples ([[MCF-7]] spike-ins). Shows the selection of method combinations via beam search and their performance (TPR/FPR) on spike-in proteins. |
| Fig 5 | Biological validation: [[Gene Ontology]] (GO) and [[Reactome]] pathway enrichment analysis of differential proteins found between Doxorubicin-treated and control cells using the optimized workflows. |

## Discussion

### Strengths
- **Comprehensive Framework**: The study covers the entire computational pipeline from spectral searching to differential expression, not just one part.
- **Explainable AI**: The use of [[SHAP]] values to interpret *why* certain workflows perform better adds significant value over simple ranking.
- **Dual Validation**: Uses both ground-truth simulated samples (mixed proteomes) and real single-cell experiments with spike-ins to validate findings.
- **Resource Availability**: The framework is released as an open-access tool named **SCPDA**.

### Limitations
- **Homogeneous Samples**: The study primarily used homogeneous cell lines ([[HeLa]], [[MCF-7]]). Performance might vary in highly heterogeneous tissue samples where "missingness" might be biological rather than technical.
- **Batch Effect Assumptions**: The batch effect correction evaluation assumed known technical batches; in some real-world scenarios, confounding biological variables might complicate this.
- **Software Versions**: Benchmarking results are tied to specific versions of the software, which are rapidly evolving.

### Future Work
- **Integration of Workflows**: Suggests using voting models or ensemble methods integrating results from multiple workflows/software to improve reliability.
- **Expansion to New Hardware**: The framework can be applied to optimize workflows for newer instruments like the [[Orbitrap Astral]].

## Personal Notes



## Related Papers

- [[SCoPE2]] (Specht et al., 2021) - Genome Biology
- [[DIA-NN]] (Demichev et al., 2020) - Nature Methods
- [[diaPASEF]] (Brunner et al., 2022) - Molecular Systems Biology
- [[Scanorama]] (Hie et al., 2019) - Nature Biotechnology