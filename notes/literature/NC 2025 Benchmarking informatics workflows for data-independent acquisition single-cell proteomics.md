---
title: NC 2025 Benchmarking informatics workflows for data-independent acquisition single-cell proteomics
aliases:
  - <article>
  - <paper>
  - <literature>
tags:
  - methods
  - literature
  - paper
category: literature
url: <% tp.file.cursor(3) %>
date_created: 2026-01-18
Journal: Nature Communications
Year: "2025"
---
# Benchmarking informatics workflows for data-independent acquisition single-cell proteomics

## Citation

> [!cite] Reference
> **Authors**: Jianwei Wang, Yi Huang, Fanghua Lu, Qinqin Xu, Zhuo Yang, Yirong Jiang, Shaowen Shi, Jianzhang Pan, Yi Yang & Qun Fang
> **Year**: 2025
> **Journal**: Nature Communications
> **DOI**: https://doi.org/10.1038/s41467-025-65174-4

## Abstract
Recent years have seen a rise of single-cell proteomics by data-independent acquisition mass spectrometry (DIA MS). While diverse data analysis strategies have been reported in literature, their impact on the outcome of single-cell proteomic experiments has been rarely investigated. Here, the authors present a framework for benchmarking data analysis strategies for DIA-based single-cell proteomics. This framework provides a comprehensive comparison of popular DIA data analysis software tools and searching strategies, as well as a systematic evaluation of method combinations in subsequent informatic workflows, including sparsity reduction, missing value imputation, normalization, batch effect correction, and differential expression analysis. Benchmarking on simulated single-cell samples consisting of mixed proteomes and real single-cell samples with a spike-in scheme, recommendations are provided for the data analysis for DIA-based single-cell proteomics.

## Key Points

- A comprehensive benchmarking framework was developed to evaluate DIA analysis software and downstream bioinformatics workflows for single-cell proteomics.
- [[DIA-NN]] is recommended for its robustness across various spectral library types, while [[Spectronaut]] (directDIA) offers high identification numbers.
- The study identified optimal downstream workflows: strict sparsity reduction (>75% completeness), [[Sum normalization]] (or [[Quantile normalization]]), batch correction via [[ComBat]] or [[limma]], and differential expression analysis using [[DESeq2]].

## Methods

### Sample Preparation
- Method used: [[PiSPA]] (Pick-up Single-cell Proteomics Analysis), [[diaPASEF]]
- Cell type: [[MCF-7]] (human breast adenocarcinoma), plus digests of [[HeLa]], [[Yeast]], and *[[E. coli]]*
- Number of cells: 60 single cells (MCF-7) across 3 batches for the real-sample spike-in experiment; multiple replicates for simulated mixed-proteome samples.

### Data Analysis
- Software: [[DIA-NN]], [[Spectronaut]], [[PEAKS Studio]], [[FragPipe]], [[AlphaPeptDeep]]
- Downstream: [[SCPDA]] (custom open-source tool), [[limma]], [[DESeq2]], [[edgeR]], [[ComBat]], [[Scanorama]]

## Results

### Main Findings
1. **Software Performance**: [[DIA-NN]] demonstrated the best quantitative precision and robustness across different library types (library-free vs. library-based). [[Spectronaut]] and [[PEAKS]] performed well in identification numbers, particularly with sample-specific libraries.
2. **Workflow Optimization**: Through evaluating ~4900 method combinations, the study found that sparsity reduction is critical (removing proteins with <75% completeness). For statistical testing, count-based methods like [[DESeq2]] (adapted for proteomics) and [[limma-trend]] performed best when paired with appropriate normalization.
3. **Biological Validation**: The optimized workflows were validated on real single-cell samples (MCF-7 treated with doxorubicin vs. DMSO). The recommended pipeline successfully identified differential proteins related to [[p53]] signaling and DNA damage response, showing higher sensitivity and specificity than baseline random choices.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Performance comparison of [[DIA-NN]], [[Spectronaut]], and [[PEAKS]] on simulated single-cell samples regarding identification coverage, data completeness, and quantitative accuracy. |
| Fig 2 | Comprehensive benchmarking of downstream workflows (imputation, normalization, batch correction, DE analysis) using parallel coordinate plots and clustering to identify high-performing combinations. |
| Fig 3 | Machine learning analysis using [[XGBoost]] and [[SHAP]] values to determine the feature importance of different analysis steps, highlighting statistical tests and normalization as key drivers. |
| Fig 4 | Validation of high-performing method combinations on real single-cell spike-in samples (MCF-7 with yeast/E. coli spike-ins), assessing True Positive/False Positive rates. |
| Fig 5 | Comparison of Gene Ontology (GO) and Reactome pathway enrichment results derived from the differential proteins found by the top-performing workflows. |

## Discussion

### Strengths
- The study utilizes a "ground truth" approach using mixed-species proteomes (human, yeast, E. coli) to rigorously calculate precision and accuracy.
- It covers the entire analysis pipeline, not just the search engine, providing a holistic view of how normalization and batch correction interact with identification software.
- The authors released an open-source tool, [[SCPDA]], to facilitate ongoing benchmarking and analysis.

### Limitations
- The "Sum" normalization method worked best for simulated samples with constant total protein, but biological single-cell samples vary in size; [[Quantile normalization]] was better for real samples but assumes identical distributions.
- The study focuses on [[timsTOF]] data; while likely applicable to Orbitrap/Astral, specific parameters might need tuning for other hardware.

### Future Work
- Integration of results across different workflows (e.g., using a voting model) to improve confidence.
- Benchmarking on newer instruments like the [[Orbitrap Astral]].
- Developing normalization methods that better account for biological cell size heterogeneity without erasing true biological signal.

## Personal Notes

## Related Papers

- [[SCoPE2: mass spectrometry of single mammalian cells quantifies proteome heterogeneity during cell differentiation]]
- [[DIA-NN: neural networks and interference correction enable deep proteome coverage in high throughput]]
- [[Optimal data processing for single-cell proteomics]]