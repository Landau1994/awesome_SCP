---
title: Radiant DIA:A Fast, Sensitive, and Accurate Search Engine for Quantitative Proteomics
authors:
  - Seth Just
  - Lee S. Cantrell
  - Andrew Nichols
  - Jian Wang
  - Janos Kis
  - Iman Mohtashemi
  - Theodore Platt
  - Omid Farokhzad
  - Serafim Batzoglou
aliases:
  - Radiant DIA
tags:
  - literature
  - paper
  - proteomics
  - DIA
  - cloud-computing
category: literature
date_created: 2026-05-12
Journal: bioRxiv
Year: 2026
---

# Radiant DIA: A Fast, Sensitive, and Accurate Search Engine for Quantitative Proteomics

## Citation

> [!cite] Reference
> **Title**: Radiant DIA: A Fast, Sensitive, and Accurate Search Engine for Quantitative Proteomics
> **Authors**: Seth Just, Lee S. Cantrell, Andrew Nichols, Jian Wang, Janos Kis, Iman Mohtashemi, Theodore Platt, Omid Farokhzad, Serafim Batzoglou
> **Year**: 2026
> **Journal**: bioRxiv
> **DOI**: 10.64898/2026.04.29.721743

## Abstract

In mass spectrometry-based proteomics, robust and efficient search engines are essential for accurate peptide and protein identification and quantification. Advances in sample preparation and instrumentation have increased the demand for highly scalable processing tools, with datasets comprising hundreds or thousands of samples in single-cell and population studies. Here we present Radiant DIA, a novel Data-Independent Acquisition search engine which achieves 4x faster processing and 10x lower cloud compute costs for large experiments while ensuring rigorous control of false discovery rate (FDR) and maintaining similar sensitivity, precision, and quantitative accuracy. The Radiant DIA search engine is paired with a modular pipeline deployable on cloud and desktop environments comprising individual modules for distributed re-scoring, FDR estimation, protein inference and quantification. Unlike traditional monolithic applications, this architecture enables high-performance, cloud-scale analysis without sacrificing local usability. Together, the Radiant DIA and Fulcrum Pipeline tools enhance computational efficiency to facilitate biological discovery in large-scale proteomics, as demonstrated by analyses of real-world experiments up to thousands of MS acquisitions.

## Key Points

- Introduces [[Radiant DIA]], a fast, C++-based search engine optimized for scoring peptide-spectrum matches (PSMs) in parallel.
- Pairs the search engine with [[Fulcrum Pipeline]], a modular, Apache Spark-based pipeline for distributed post-processing (FDR, protein inference, quantification).
- Achieves 4x faster processing and 10x lower cloud computing costs compared to state-of-the-art tools like DIA-NN, scaling efficiently to datasets exceeding 2,500 runs.
- Maintains high sensitivity and precise FDR control, demonstrating robust handling of complex PTMs (e.g., deamidation) and deep quantitative reproducibility.

## Methods

### Sample Preparation
- Method used: [[DIA]] (Data-Independent Acquisition), Matrix-Matched Calibration Curve ([[MMCC]]), [[Proteograph XT]] assay for plasma.
- Cell type: HeLa, human plasma, human eye lens tissue, mixed human peptide libraries.
- Number of cells: N/A (Population and tissue cohorts up to 2,561 MS acquisitions)

### Data Analysis
- Software: [[Radiant DIA]], [[Fulcrum Pipeline]], [[DIA-NN]], [[mokapot]], [[Proffer]], [[Preppers]], [[DirectLFQ]], [[Apache Spark]], [[Skyline]]
- Downstream: Distributed re-scoring, [[MixMax]] (Blocking MixMax) for FDR estimation, linear discriminant analysis (LDA) and neural network (NN) classifiers, Match-Between-Runs ([[MBR]]), Differential Abundance (DA) analysis.

## Results

### Main Findings
1. **Computational Throughput and Scalability**: Radiant DIA and Fulcrum Pipeline successfully processed a 2,561-run dataset in under 4 hours (wall time) at roughly $111, whereas a comparable distributed DIA-NN workflow took 1.92x longer and cost 9.5x more.
2. **Robust Performance**: Radiant DIA matched DIA-NN in precursor identifications across datasets but exhibited superior run-to-run quantitative precision (lower CVs) and more conservative, accurate FDR calibration (proven via entrapment analysis). 
3. **Biological Utility and PTM Handling**: In a highly modified human eye lens dataset, Radiant DIA showed better retention-time support and dot-product match scores for deamidated peptides. In a plasma cancer cohort, it provided more stable quantitation, reducing false variance compared to DIA-NN's transferred identifications.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Comparison of parallelized cloud processing pipelines, showing the speed, cost efficiency, and desktop benchmarks of Radiant DIA/Fulcrum vs. scalable DIA-NN pipelines across cohort sizes. |
| Fig 2 | Overview of precursor identification counts from the Hour Proteome, HeLa, and Eye Lens datasets for library-free and MBR searches. |
| Fig 3 | Quantitative precision (CV distributions) and limits of detection/quantification (LoD/LoQ from MMCC) demonstrating Radiant DIA's accuracy across multiple replicate studies. |
| Fig 4 | Distribution of spectral match quality (Skyline dot product) and measured intensity for PSMs in the Eye Lens dataset, evaluating engine-specific match confidence. |
| Fig 5 | Evaluation of the cancer plasma case study, detailing nanoparticle precursor completeness, intensity distributions, and differential expression overlaps. |

## Discussion

### Strengths
- Unprecedented scalability allowing processing of massive cohorts (>2,500 runs) efficiently via distributed cloud frameworks ([[Apache Spark]]).
- Cost-effective architecture reducing computing expenditure by up to 10-fold on platforms like AWS.
- Highly modular and transparent pipeline (Fulcrum), enabling the integration of custom algorithms for re-scoring, normalization, and protein inference without rewriting monolithic codebases.
- Native support for ARM architectures, allowing for further compute cost reductions.

### Limitations
- The underlying code and precise licensing terms are subject to institutional approval and were not publicly posted at the time of the preprint.
- Maximum utility of the Fulcrum Pipeline requires familiarity with cluster computing / containerized environments (e.g., Kubernetes, Spark), which may present a learning curve for standard desktop users.

### Future Work
- Development of additional plug-in modules within the Fulcrum Pipeline to support transition refinement, interference removal, and targeted quantitative re-extraction from MS files.
- Application of the platform to next-generation MS demands like population-scale profiling, single-cell proteomics, and rapid clinical translation.

## Personal Notes



## Related Papers

- Pino, L. K., et al. (2020). Acquiring and Analyzing Data Independent Acquisition Proteomics Experiments without Spectrum Libraries. *Mol Cell Proteomics*.
- Demichev, V., et al. (2020). DIA-NN: neural networks and interference correction enable deep proteome coverage in high throughput. *Nat Methods*.
- Keich, U., et al. (2015). Improved False Discovery Rate Estimation Procedure for Shotgun Proteomics. *J Proteome Res*.
- Ammar, C., et al. (2023). Accurate Label-Free Quantification by directLFQ to Compare Unlimited Numbers of Proteomes. *Mol. Cell. Proteom*.