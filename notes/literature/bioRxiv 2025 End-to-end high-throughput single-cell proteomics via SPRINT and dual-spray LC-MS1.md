---
title: End-to-end high-throughput single-cell proteomics via SPRINT and dual-spray LC-MS
authors:
  - Zhen Liu
  - Wenbo Dong
  - Lei Gu
  - Ruicheng Ge
  - Xinlei Zeng
  - Jingwen Deng
  - Haoran Zhang
  - Zilu Ye
aliases:
   - <article>
   - <paper>
   - <literature>
tags:
  - literature
  - paper
  - single-cell_proteomics
  - mass_spectrometry
category: literature
date_created: 2024-05-22
Journal: bioRxiv (Preprint)
Year: 2025
---

# End-to-end high-throughput single-cell proteomics via SPRINT and dual-spray LC-MS

## Citation

> [!cite] Reference
> **Title**：End-to-end high-throughput single-cell proteomics via SPRINT and dual-spray LC-MS
> **Authors**: Zhen Liu, Wenbo Dong, Lei Gu, Ruicheng Ge, Xinlei Zeng, Jingwen Deng, Haoran Zhang, Zilu Ye
> **Year**: 2025
> **Journal**: bioRxiv
> **DOI**: 10.1101/2025.11.03.686420

## Abstract

Single-cell proteomics (SCP) enables direct measurement of protein heterogeneity but remains constrained by throughput and limited applicability to primary tissues. Here, the authors present an integrated workflow to address these challenges. They engineered **SPRINT**, an AI-powered bioprinting platform that prepares more than 10,000 single cells per day (tenfold faster than existing systems) while identifying over 6,000 proteins from individual HeLa cells. To expand analytical capacity, they designed a **dual-spray tandem direct injection (TDI) LC system** that parallelizes non-analytical steps, doubling MS utilization efficiency and enabling 168 label-free SCP runs per day. Combined with optimized tissue dissociation protocols, this workflow enabled the creation of the first mouse tissue-derived SCP atlas, profiling >1,000 single cells across six organs.

## Key Points

- **SPRINT Platform:** An AI-powered bioprinting system using multi-nozzle chips to dispense droplets as small as 30 pL, achieving >10,000 cell preparations/day with 100% accuracy for HeLa cells.
- **Dual-Spray TDI LC System:** Parallelizes column loading/equilibration with peptide separation, increasing MS utilization efficiency from 44.2% to 88.4%, supporting 168 label-free runs/day.
- **Multi-Organ Mouse Atlas:** The first comprehensive SCP atlas covering bone marrow, heart, intestine, kidney, lung, and lymph, identifying 5,823 unique proteins and resolving tissue-resident heterogeneity.

## Methods

### Sample Preparation
- **Method used:** SPRINT (Single-cell Proteomics Rapid INTegrator) bioprinting, using AI-guided nozzle selection and 30 pL droplet dispensing.
- **Cell type:** HeLa cells, mouse bone marrow, and primary cells from 12 mouse tissues (brain, intestine, lymph, etc.).
- **Optimization:** Systematic evaluation of master mix volume (500 nL), enzyme type (Trypsin), digestion time (1-2 h), and acidification buffer (0.1% TFA in 0.5% DMSO).
- **Tissue Dissociation:** Optimized BSA concentrations (standardized to 0.1% BSA) to balance cell viability and MS compatibility.

### Data Analysis
- **Instrumentation:** Vanquish Neo UHPLC coupled with Orbitrap Astral mass spectrometer.
- **Software:** DIA-NN (v1.9.2) and Spectronaut v19 for raw file processing (library-free directDIA).
- **Downstream:** R package Seurat (v5) for clustering/visualization; Slingshot for pseudotime trajectory analysis of neutrophil differentiation.

## Results

### Main Findings
1. **Unprecedented Throughput:** SPRINT achieves >10,000 cell preparations/day, while the dual-spray TDI system doubles MS throughput to 168 label-free samples/day without sensitivity loss.
2. **Deep Proteome Coverage:** Routine identification of ~6,000 proteins per single HeLa cell and over 7,000 proteins in 20-cell pools.
3. **Biological Resolution:** The mouse SCP atlas resolved major tissue-resident populations (e.g., cardiomyocytes, proximal tubule cells) and captured protein-level variations in neutrophil maturation that are often missed by scRNA-seq.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Overview of SPRINT platform performance, sorting efficiency, and identification depth for HeLa and bone marrow cells. |
| Fig 2 | Versatile sorting of tissue cells; comparison of "Regular" vs "High-recovery" chips for low-density samples. |
| Fig 3 | Optimization of the SCP workflow (volumes, enzymes, digestion time, and buffer conditions). |
| Fig 4 | Tissue dissociation strategy evaluation, showing the effect of BSA on cell viability and morphology across 12 tissues. |
| Fig 5 | Dual-spray TDI LC system mechanics, MS utilization efficiency comparison (88.4% vs 44.2%), and technical reproducibility. |
| Fig 6 | Mouse single-cell proteomics atlas across 6 organs, including t-SNE clusters and neutrophil differentiation pseudotime. |

## Discussion

### Strengths
- **End-to-End Scalability:** Addresses bottlenecks in both sample preparation (SPRINT) and LC-MS analysis (dual-spray TDI).
- **Label-Free Efficiency:** High-throughput achieved without the quantitative compromises or cost of multiplexing reagents.
- **Standardized Protocols:** Provides a rigorous framework for primary tissue dissociation tailored for proteomics.

### Limitations
- **Throughput Gap:** While significantly improved, SCP still lags behind scRNA-seq in terms of total cells per experiment (thousands vs. tens of thousands).
- **Debris Interference:** Primary tissue dissociation still produces significant debris, requiring AI algorithms and specific chip designs to maintain recovery.

### Future Work
- Improvement of ion source designs to push throughput toward 300–500 cells per day.
- Development of clinical-grade dissociation protocols.
- Integration of spatial dimensions to create "virtual cell" models combining proteomic, transcriptomic, and spatial data.

## Personal Notes

- The 88.4% MS utilization is a massive improvement over traditional setups where the MS spends half its time idle during column washes.
- SPRINT's use of a multi-nozzle chip (640 nozzles) is key to its speed compared to single-capillary systems like cellenONE.

## Related Papers

- Budnik et al. (2018) *SCoPE-MS* (Foundational multiplexing SCP).
- Woo et al. (2018) *nanoPOTS* (Foundational miniaturized prep).
- Ctortecka et al. (2024) *Automated single-cell proteomics* (Previous state-of-the-art benchmarks).