---
title: Defining Quality Control Standards for Single-Cell Proteomics by Inter-Laboratory Benchmarking
authors:
  - Sam van Puyenbroeck
  - Tine Claeys
  - Anjali Seth
  - Jeewan Babu Rijal
  - Charline Keller
  - Lavender Lin
  - Rupert Mayer
  - Manuel Matzinger
  - Isaac Han
  - Pedro Aragón Fernández
  - Valdemaras Petrosius
  - Benjamin Furtwängler
  - Brian Boyle
  - Keith Rivera
  - Guilhem Tourniaire
  - Florian A. Rosenberger
  - Lennart Martens
  - Steven A. Carr
  - Zhen Dong
  - Ákos Végvári
  - Christine Carapito
  - Ryan Kelly
  - Karl Mechtler
  - Bogdan Budnik
  - Erwin M. Schoof
  - Claudia Ctortecka
aliases:
  - 
tags:
  - literature
  - paper
  - proteomics
  - single-cell
  - quality-control
category: literature
date_created: 2026-07-20
Journal: bioRxiv
Year: 2026
---

# Defining Quality Control Standards for Single-Cell Proteomics by Inter-Laboratory Benchmarking

## Citation

> [!cite] Reference
> **Title**：Defining Quality Control Standards for Single-Cell Proteomics by Inter-Laboratory Benchmarking
> **Authors**: Sam van Puyenbroeck et al.
> **Year**: 2026
> **Journal**: bioRxiv
> **DOI**: 10.64898/2026.07.13.738155

## Abstract

Single-cell proteomics (SCP) can quantify thousands of proteins, yet the absence of community-wide quality control limits interpretability. The HUPO Single Cell Initiative presents the first inter-laboratory benchmarking study across seven laboratories using standardized 384-well plates acquired on [[Orbitrap Astral]] and [[timsTOF Ultra2]] instruments. Centralized analysis across six [[DIA]] software tools revealed that software choice impacts identification depth and quantitative accuracy more than instrument vendor. A multi-layered quality control framework enabled the detection of technical failures including cell-leakage, column degradation, and pipetting errors. The study demonstrates that instrument-vendor harmonization is insufficient for inter-laboratory reproducibility without rigorous batch correction. Sequential correction for plate identity and well position allowed for clean cell-type separation and confident downstream differential expression analysis.

## Key Points

- Software choice is the primary determinant of identification depth and quantitative accuracy in SCP, often exceeding instrument-level variation.
- A standardized, multi-tier QC framework (including quantitative mixtures, qualitative standards, and processing/sorting controls) is essential to deconvolve technical variability from biological heterogeneity.
- Cross-laboratory data integration for SCP requires explicit batch correction of plate-level and position-based effects to resolve biological signal.
- The use of standardized control samples allows researchers to identify and exclude data influenced by chromatography, instrument drift, or sample preparation anomalies.

## Methods

### Sample Preparation
- Method used: [[cellenONE]] picolitre dispensing, [[DDM]] lysis, [[Trypsin]]/[[Lys-C]] dual-protease digestion.
- Cell type: [[HEK293T]] and [[K562]].
- Number of cells: 108 single cells per cell type (216 total) per plate.

### Data Analysis
- Software: [[Spectronaut]], [[DIA-NN]], [[CHIMERYS]], [[PEAKS]], [[FragPipe]], [[alphaDIA]].
- Downstream: [[msqrob2]] for differential expression analysis, [[scplainer]] for variance partitioning, [[omicsGMF]] for dimensionality reduction.

## Results

### Main Findings
1. Software benchmarking identified significant differences in precursor identification counts and quantitative error; [[Spectronaut]] generally yielded higher identification numbers, whereas [[FragPipe]] showed lower quantitative error.
2. The four-tier QC framework (chromatographic stability, plate integrity, longitudinal acquisition trends, and data completeness) effectively flagged acquisition failures and systematic biases.
3. Batch correction (specifically targeting plate identity and well-position effects) is critical to remove technical noise, allowing for the successful identification of differentially expressed proteins between cell types across different laboratories and instruments.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Overview of the centralized sample preparation and standardized LC-MS/MS workflow. |
| Fig 2 | Comparison of quantitative accuracy and peptide sequence overlap across six DIA software tools. |
| Fig 3 | Quantitative and qualitative performance across instruments and sample types. |
| Fig 4 | Multi-tier QC evaluation including retention time stability and feature completeness. |
| Fig 5 | Intra- and inter-laboratory quantitative reproducibility and batch effect correction using latent factor representation. |
| Fig 6 | Cross-laboratory differential expression analysis between HEK293T and K562 single cells. |

## Discussion

### Strengths
- Unprecedented scale of inter-laboratory benchmarking for single-cell proteomics.
- Systematic deconvolution of instrument vs. software contributions.
- Provides a practical, data-driven framework for future SCP studies.

### Limitations
- The use of specific cell types ([[HEK293T]] and [[K562]]) may not fully capture the complexity of all primary/patient samples.
- The study highlights high site-to-site variability, necessitating complex batch correction methods which may not be accessible to all users.

### Future Work
- Investigation into whether the observed software-dependency persists with future algorithm updates.
- Standardization of the multi-tier QC framework for routine application in clinical SCP pipelines.

## Personal Notes



## Related Papers

- Gatto, L. et al. "Initial recommendations for performing, benchmarking and reporting single-cell proteomics experiments." *Nat Methods* (2023).
- Ctortecka, C. et al. "Automated single-cell proteomics providing sufficient proteome depth to study complex biology beyond cell type classifications." *Nat Commun* (2024).