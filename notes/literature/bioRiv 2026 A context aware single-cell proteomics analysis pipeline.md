---
title: A Context-Aware Single-Cell Proteomics Analysis pipeline
authors:
  - Carla Salomó Coll
  - Agata N Makar
  - Alejandro J Brenes
  - Joseph Inns
  - Matthias Trost
  - Neil Rajan
  - Simon Wilkinson
  - Alex von Kriegsheim
aliases:
  - CASPA
tags:
  - literature
  - paper
  - single-cell-proteomics
  - bioinformatics
  - LLM
category: literature
date_created: 2026-04-09
Journal: bioRxiv
Year: 2026
---

# A Context-Aware Single-Cell Proteomics Analysis pipeline

## Citation

> [!cite] Reference
> **Title**: A Context-Aware Single-Cell Proteomics Analysis pipeline.
> **Authors**: Carla Salomó Coll, Agata N Makar, Alejandro J Brenes, Joseph Inns, Matthias Trost, Neil Rajan, Simon Wilkinson, Alex von Kriegsheim
> **Year**: 2026
> **Journal**: bioRxiv
> **DOI**: 10.64898/2026.04.03.716382

## Abstract

Single-cell proteomics (SCP) by mass spectrometry can now quantify hundreds to thousands of proteins per cell, but the field still lacks standardised analytical pipelines that accommodate the diversity of instruments, sample preparation workflows and biological contexts encountered in practice. Existing workflows, largely adapted from single-cell transcriptomics, do not account for the informative missingness, pervasive ambient protein contamination and limited feature space that distinguish proteomic from transcriptomic data. In addition, cell type annotation remains a manual bottleneck that is subjective, difficult to reproduce and hard to scale. Here we present an end-to-end pipeline that integrates adaptive quality control, entropy-guided iterative batch correction, multi-modal marker discovery that exploits detection patterns unique to proteomics, and context-aware annotation by large language models (LLMs) coupled to structured contradiction reasoning and orthogonal data-driven validation. 

## Key Points

- Introduces Context-Aware Single-Cell Proteomics Analysis ([[CASPA]]), a fully automated end-to-end pipeline for SCP data.
- Employs adaptive quality control, iterative batch correction (via [[Harmony]]), and multi-modal marker discovery tailored for SCP (incorporating missingness and intensity metrics).
- Utilizes a novel three-round context-aware [[LLM]] annotation architecture to interpret ambiguous cell states (e.g., phagocytosis, lytic cell death) while minimizing hallucination and misclassification of ambient proteins.
- Validated across diverse tissues (human brain, GBM neutrophils, skin tumor, injured pancreas) showing high concordance with FACS ground truth and orthogonal IHC validation.

## Methods

### Sample Preparation
- Method used: [[CellenONE]] single-cell isolation, [[diaPASEF]], [[timsTOF]] SCP mass spectrometer.
- Cell type: Developing human brain cells, glioblastoma tumor-associated neutrophils, CYLD cutaneous syndrome skin tumor cells, and caerulein-injured mouse pancreas cells.
- Number of cells: 819 (brain), 330 (neutrophils), 249 (skin tumor), 234 (pancreas).

### Data Analysis
- Software: [[DIA-NN]], [[Spectronaut]], [[FragPipe]], [[Snakemake]], [[Python]], [[scanpy]], [[scikit-learn]], [[Claude Sonnet]], [[GPT-5.2]].
- Downstream: [[Harmony]] (adaptive batch correction), [[Leiden]] clustering, AUCell pathway scoring, scplainer (LME model), PanglaoDB validation, Multi-modal marker mining.

## Results

### Main Findings
1. The adaptive pipeline efficiently resolved batch effects dynamically using a dual-modality PCA (intensity and detection patterns) combined with an entropy-guided Harmony loop.
2. A three-round structured LLM annotation successfully decoded complex cellular states that typically confuse standard analyses, such as distinguishing true ambient contamination from phagocytosed cargo in neutrophils and macrophages.
3. Held-out validation on skin tumors and orthogonal tissue validation (IHC/IF) on injured pancreas demonstrated that automated annotations closely matched FACS-sorted ground truth and physiological cellular distributions.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Robust end-to-end pipeline for single-cell proteomics analysis, detailing QC, batch correction, marker discovery, and 3-tier LLM annotation. |
| Fig 2 | Benchmarking against the developing human brain single-cell proteome, showing resolution of lineages and batch correction efficacy. |
| Fig 3 | Benchmarking on glioblastoma tumor-associated neutrophils, highlighting LLM capability in resolving functional states over pure lineages. |
| Fig 4 | Prompt engineering architecture and model comparison between GPT-5.2 and Claude Sonnet 4.6 across failure-mode targets. |
| Fig 5 | Held-out validation on CCS skin tumor with FACS ground truth, showing 90.8% annotation concordance at the single-cell level. |
| Fig 6 | Pipeline validation with v3 annotation architecture on caerulein-injured mouse pancreas, outlining specific pathway signatures and cell states. |
| Fig 7 | Orthogonal tissue validation of pipeline annotations in caerulein-injured mouse pancreas using IHC and IF to confirm cellular localizations and phagocytic uptake. |

## Discussion

### Strengths
- Uniquely leverages "informative missingness" and multi-modal protein evidence instead of relying purely on abundance, which is crucial for SCP data.
- The 3-round LLM contextual prompt engineering overcomes common pitfalls of naive LLM annotations, explicitly dealing with biological phenomena like phagocytosis and ambient carryover.
- Fully automated workflow built on [[Snakemake]], ensuring reproducibility.

### Limitations
- Annotation heavily depends on commercial LLM APIs, which introduces cost and availability constraints.
- Clustering resolution and dual-modality embeddings were used as defaults but not exhaustively benchmarked against all alternative parameterizations.
- Performance relies on the quality of the experimental context provided to the LLM (Round 0).

### Future Work
- Broader blinded replication across additional and open-source model families to draw stronger conclusions about LLM reasoning capacities.
- Testing on substantially larger SCP datasets to identify and address any scaling constraints not captured in the 200-800 cell range tested.

## Personal Notes
The pipeline uses Python 3.10+ with scanpy (1.9+), harmony-pytorch, scikit-learn, scipy, and statsmodels. Visualisation uses matplotlib (3.7+). Marker statistics use scipy.stats (Fisher’s exact, Wilcoxon rank-sum) with statsmodels for multiple testing correction. AUCell pathway scoring uses the decoupler package with MSigDB Hallmark gene sets. All code is available at https://github.com/vonkriegsheim/CASPA.


## Related Papers

- Wu T, et al. Single-cell proteomic landscape of the developing human brain. Nat Biotechnol, (2026).
- Sadiku P, et al. Single cell proteomic analysis defines discrete neutrophil functional states in human glioblastoma. Nat Commun 17, 621 (2025).
- Inns J, et al. Democratised single cell proteomics uncovers tumor associated macrophage signature in CYLD cutaneous syndrome skin tumors. bioRxiv, (2026).