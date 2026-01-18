---
title: Ultra-fast label-free quantification and comprehensive proteome coverage with narrow-window data-independent acquisition
authors:
  - Ulises H. Guzman
  - Ana Martinez-Val
  - Zilu Ye
  - Eugen Damoc
  - Tabiwang N. Arrey
  - Anna Pashkova
  - Santosh Renuse
  - Eduard Denisov
  - Johannes Petzoldt
  - Amelia C. Peterson
  - Florian Harking
  - Ole Østergaard
  - Rasmus Rydbirk
  - Susana Aznar
  - Hamish Stewart
  - Yue Xuan
  - Daniel Hermanson
  - Stevan Horning
  - Christian Hock
  - Alexander Makarov
  - Vlad Zabrouskov
  - Jesper V. Olsen
aliases:
   - nDIA
   - Astral analyzer
   - Ultra-fast proteomics
tags:
  - literature
  - paper
  - proteomics
  - mass_spectrometry
category: literature
date_created: 2024-05-22
Journal: Nature Biotechnology
Year: 2024
---

# Ultra-fast label-free quantification and comprehensive proteome coverage with narrow-window data-independent acquisition

## Citation

> [!cite] Reference
> **Title**：Ultra-fast label-free quantification and comprehensive proteome coverage with narrow-window data-independent acquisition
> **Authors**: Ulises H. Guzman, Ana Martinez-Val, Zilu Ye, et al.
> **Year**: 2024
> **Journal**: Nature Biotechnology
> **DOI**: https://doi.org/10.1038/s41587-023-02099-7

## Abstract

Mass spectrometry (MS)-based proteomics aims to characterize comprehensive proteomes in a fast and reproducible manner. The authors present a **narrow-window data-independent acquisition (nDIA)** strategy. Using a quadrupole Orbitrap mass spectrometer paired with the asymmetric track lossless (**Astral**) analyzer, they achieve >200-Hz MS/MS scanning speeds with 2-Th isolation windows. This approach dissolves the traditional differences between data-dependent (DDA) and data-independent (DIA) methods. The strategy allows for profiling >100 yeast proteomes or 48 human proteomes per day, reaching depths of ~10,000 human protein groups in 30 minutes.

## Key Points

- **The nDIA Strategy**: Combines the high specificity of narrow isolation windows (2-Th, typically used in DDA) with the high throughput and reproducibility of DIA.
- **Hardware Advancement**: Utilization of the **Orbitrap Astral MS**, which features an Astral analyzer for ultra-fast, high-sensitivity MS/MS and an Orbitrap analyzer for high-resolution MS1 scans.
- **Unprecedented Throughput**: Capable of quantifying ~10,000 protein groups from human cell lysates in 30 minutes and ~7,000 proteins in just 5 minutes (180 samples per day).
- **Comprehensive Coverage**: Achieves near-complete coverage of the expressed human proteome (~12,000 proteins) in 3–4.5 hours using offline fractionation.

## Methods

### Sample Preparation
- **Method used**: Protein Aggregation Capture (PAC) for cell lysis and digestion; offline high-pH (HpH) reversed-phase peptide fractionation for deep coverage.
- **Cell types**: HEK293, HeLa, *Saccharomyces cerevisiae* (yeast), and human brain tissue (Broadmann’s area 9).
- **Loading amounts**: Ranging from single-cell levels (50 pg) to 2,000 ng for deep profiling.

### Data Analysis
- **Software**: DIA-NN (v1.8.1) and Spectronaut (v17/v18) using a library-free approach (directDIA+).
- **Downstream**: MaxLFQ algorithm for protein quantification; GSEA (Gene Set Enrichment Analysis) via clusterProfiler; R v.4.2.2 for statistical processing.

## Results

### Main Findings
1. **Astral Analyzer Performance**: Provides >200-Hz MS/MS scanning speed with low-ppm mass accuracy and high sensitivity, outperforming existing TOF and Orbitrap instruments in speed and depth.
2. **Quantitative Precision**: Demonstrated high precision in a three-species proteome mixture (Human, Yeast, *E. coli*), quantifying over 14,000 protein groups in a single 30-minute run with low CVs.
3. **Single-Cell Sensitivity**: Successfully identified ~3,000 proteins from 50 pg of HeLa digest and >4,500 proteins from individual single HeLa cells.
4. **Clinical Application**: Re-analyzed a Multiple System Atrophy (MSA) cohort, identifying biomarkers related to blood coagulation and immune response 20x faster than previous studies.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Benchmarking nDIA against DDA; hardware overview of the Orbitrap Astral MS and scan rate comparisons. |
| Fig 2 | Deep single-shot proteome coverage across various sample loads (100ng to 2000ng) and gradients. |
| Fig 3 | LFQ accuracy and precision analysis using a three-species mixture at different ratios. |
| Fig 4 | Multi-shot strategy using HpH fractionation to reach ~12,000 protein groups in under 5 hours. |
| Fig 5 | Functional genomics screen of 104 yeast knockout strains; quantification of ~4,500 proteins per strain. |
| Fig 6 | Clinical proteomics application re-analyzing MSA vs. Control brain biopsies at high throughput. |

## Discussion

### Strengths
- **Speed and Depth**: Dramatically increases the number of proteins identified per unit of time.
- **Data Completeness**: Reduces the "missing value" problem inherent in DDA while maintaining DDA-like isolation specificity.
- **Versatility**: Validated across single-cell, bulk cell line, and complex clinical tissue samples.

### Limitations
- **Ion Utilization**: Reducing the mass range with narrow windows means only a small fraction (0.5%) of the total ion beam is sampled at any given time, which could impact sensitivity for extremely low-abundance targets.
- **Instrument Access**: Requires the latest generation Orbitrap Astral MS hardware.

### Future Work
- **Ion Scheduling**: Potential for synchronized precursor release to improve sensitivity.
- **Hybrid Methods**: Combining nDIA with ion mobility (e.g., FAIMS) or intelligent window placement for low-abundance targets.

## Personal Notes
- The "nDIA" approach effectively makes the choice between DDA and DIA obsolete for most high-throughput applications, as it provides the benefits of both.
- The throughput of 180 SPD (Samples Per Day) is a significant milestone for large-scale clinical cohort studies.

## Related Papers
- Bekker-Jensen, D. B. et al. (2017) *Cell Syst.* - Optimized shotgun strategy for human proteomes.
- Demichev, V. et al. (2020) *Nat. Methods* - DIA-NN software.
- Stewart, H. I. et al. (2023) *Anal. Chem.* - Parallelized acquisition of Orbitrap and Astral analyzers.