---
title: Optimization of trap column properties and loading conditions for proteome profiling of single-cell-level sample inputs
authors:
  - Siqi Huang
  - Thy Truong
  - Chao Wang
  - Xiaofeng Xie
  - H.-J. Lavender Lin
  - Ryan T. Kelly
aliases:
  - trap-colum-optimize
tags:
  - literature
  - paper
category: literature
date_created: 2026-03-25
Journal: Analytical and Bioanalytical Chemistry
Year: 2026
---

# Optimization of trap column properties and loading conditions for proteome profiling of single-cell-level sample inputs

## Citation

> [!cite] Reference
> **Title**: Optimization of trap column properties and loading conditions for proteome profiling of single-cell-level sample inputs
> **Authors**: Siqi Huang, Thy Truong, Chao Wang, Xiaofeng Xie, H.-J. Lavender Lin, Ryan T. Kelly
> **Year**: 2026
> **Journal**: Analytical and Bioanalytical Chemistry
> **DOI**: 10.1007/s00216-026-06440-2

## Abstract

Nanoflow liquid chromatography-mass spectrometry has become indispensable for profiling limited and heterogeneous biological samples, yet overall analytical sensitivity, robustness, and throughput often remain constrained by the mechanisms used to transfer samples onto the analytical column. Although trap-and-elute workflows are widely deployed to improve loading efficiency, sample cleanup, and column longevity, a systematic evaluation of how trap column properties and loading parameters influence proteome coverage, particularly under low-input and high-throughput conditions, is needed. **Here, we assess trap column inner diameter, particle size, packing material, loading flow rate, and sample concentration using both bulk-prepared digests and single cells. We demonstrate that incorporating a trap column markedly mitigates performance losses associated with large-volume loading with minimal impact on peak width, peak area, or identification depth**. Notably, variations in trap column geometry and loading speed exert only minimal influence on chromatographic quality or proteome depth, indicating that trap-and-elute workflows afford considerable flexibility in the LC system design. These findings establish practical guidelines for optimizing trap column configurations and highlight the suitability of trap-and-elute strategies for high-sensitivity, high-throughput proteomics.

## Key Points

- Trap-and-elute workflows successfully mitigate the detrimental effects of large-volume sample injections that otherwise severely impact direct-loading strategies.
- Variations in trap column geometry (inner diameter) and particle size yield minimal differences in peptide peak width, area, or total proteome coverage.
- Loading flow rates can be significantly increased (e.g., up to 10 µL/min) without compromising chromatographic performance, allowing for higher sample throughput.

## Methods

### Sample Preparation
- Method used: Automated single-cell digestion using [[Tecan UNO]] and [[Trap-and-elute]] [[nanoLC-MS]]
- Cell type: [[HeLa]] cells
- Number of cells: Bulk digests (down to 200 pg equivalents) and individually isolated single cells (15-17 µm diameter)

### Data Analysis
- Software: [[DIA-NN]] (version 2.0.2)
- Downstream: [[Python]]

## Results

### Main Findings
1. Large-volume direct injections (e.g., 10 µL) lead to significant sample loss, particularly for early-eluting hydrophilic peptides, a limitation fully mitigated by employing a trap column.
2. The use of trap columns introduces no noticeable bias in the hydrophobicity (GRAVY score) distribution of the detected peptides compared to direct injection.
3. Reducing the trap column inner diameter from 75 µm to 30 µm provides less than a 10% reduction in peak width, indicating that the analytical column rather than the trap column is the primary driver of chromatographic performance.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Schematics of valving setups for direct loading (no trap) versus trap-and-elute workflows with backflushing elution. |
| Fig 2 | Comparison of proteome and peptide coverage across multiple trap column particles and direct injection for various sample inputs (10 ng and 200 pg) and volumes (1 µL and 10 µL). |
| Fig 3 | Investigation of trap-induced biases showing Venn diagrams of identified peptides/proteins and the distribution of GRAVY scores, proving no specific classes of peptides are lost. |
| Fig 4 | Analysis of high- and low-volume direct sample injections, demonstrating the loss of early-eluting hydrophilic peptides during 10-µL direct loading. |
| Fig 5 | Evaluation of high loading flow rates (1 µL/min vs 10 µL/min), showing higher loading speeds do not negatively impact peak area, peak width, or identification coverage. |
| Fig 6 | Peak width and peak area comparisons demonstrating that different trap column particle sizes result in similar performance metrics to direct loading. |
| Fig 7 | Impact of trap column inner diameter (30 µm vs 75 µm) on proteome coverage and peak width for both standard digests and true single cells, showing minimal advantage to narrower trap columns. |

## Discussion

### Strengths
- Provides a highly systematic, multidimensional evaluation of trap column parameters that are critical yet rarely benchmarked in single-cell proteomics.
- Data are verified using both bulk dilutions and authentic single-cell samples.
- Clears up misconceptions by proving that trap columns offer extensive flexibility without sacrificing duty cycle or peak capacity.

### Limitations
- The study focuses primarily on capillary-based trap columns; other column formats were not evaluated.
- The evaluation was largely restricted to HeLa cell lysates, which may not capture the dynamic range challenges of more complex biological matrices or tissues.

### Future Work
- Evaluation of other trap column formats (e.g., monolithic or chip-based traps).
- Application of optimized trap-and-elute strategies to complex biological matrices with higher dynamic ranges, such as clinical biopsies or spatially resolved tissues.

## Personal Notes



## Related Papers

- Cong Y, et al. Improved single-cell proteome coverage using narrow-bore packed NanoLC columns and ultrasensitive mass spectrometry. Anal Chem. 2020.
- Webber KGI, et al. Open-tubular trap columns: towards simple and robust liquid chromatography separations for single-cell proteomics. Mol Omics. 2024.
- Greguš M, et al. Improved sensitivity of ultralow flow LC-MS-based proteomic profiling of limited samples using monolithic capillary columns and FAIMS technology. Anal Chem. 2020.