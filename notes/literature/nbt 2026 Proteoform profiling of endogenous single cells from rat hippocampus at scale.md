---
title: Proteoform profiling of endogenous single cells from rat hippocampus at scale
authors:
  - Pei Su
  - Michael A. R. Hollas
  - Indira Pla
  - Stanislav Rubakhin
  - Fatma Ayaloglu Butun
  - Joseph B. Greer
  - Bryan P. Early
  - Ryan T. Fellers
  - Michael A. Caldwell
  - Jonathan V. Sweedler
  - Jared O. Kafader
  - Neil L. Kelleher
aliases:
  - scPiMS
tags:
  - literature
  - paper
  - proteomics
  - single-cell
category: literature
date_created: 2024-05-23
Journal: Nature Biotechnology
Year: 2026
---

# Proteoform profiling of endogenous single cells from rat hippocampus at scale

## Citation

> [!cite] Reference
> **Title**：Proteoform profiling of endogenous single cells from rat hippocampus at scale
> **Authors**: Pei Su, Michael A. R. Hollas, Indira Pla, Stanislav Rubakhin, Fatma Ayaloglu Butun, Joseph B. Greer, Bryan P. Early, Ryan T. Fellers, Michael A. Caldwell, Jonathan V. Sweedler, Jared O. Kafader, Neil L. Kelleher
> **Year**: 2026
> **Journal**: Nature Biotechnology
> **DOI**: https://doi.org/10.1038/s41587-025-02669-x

## Abstract

Single-cell proteomics faces major challenges in throughput and intact protein characterization. This paper introduces single-cell proteoform imaging mass spectrometry ([[scPiMS]]), a high-throughput, label-free method for profiling endogenous single cells. By bypassing traditional [[proteolytic digestion]] and chromatographic separation, the researchers analyzed 10,809 cells from the rat hippocampus. Using a developed informatics workflow, they successfully assigned >93% of detected cells to three main cell types—neurons, astrocytes, and microglia—based on their specific proteoform signatures, which were further validated through optical microscopy.

## Key Points

- Development of [[scPiMS]], a platform for high-throughput, [[top-down proteomics]] at the single-cell level.
- Analysis of 10,809 hippocampal single cells across two datasets with a throughput of ~1,000 cells per day.
- Identification and classification of major cell types (neurons, astrocytes, microglia) using [[proteoform]] signatures and [[GSVA]] pathway analysis.
- The workflow utilizes an [[intact mass tag (IMT)]] approach and the [[PAScore]] algorithm for statistical assignment of proteoforms.

## Methods

### Sample Preparation
- Method used: Enzymatic ([[papain]]) and mechanical disaggregation; sample drop-cast onto [[ITO glass slides]].
- Cell type: Rat hippocampal cells (neurons, astrocytes, microglia).
- Number of cells: 10,809 (Dataset I: 5,272; Dataset II: 5,537).

### Data Analysis
- Software: [[scApp]] ([[C#]]), [[MATLAB]], [[TDValidator]], [[ProSight Native]], [[GSVA]], [[ComplexHeatmap]], [[factoextra]], [[QuPath]], [[ImageJ]].
- Downstream: [[Unsupervised clustering]], [[PCA]], [[Pathway-adjusted PAScore matrix]].

## Results

### Main Findings
1. [[scPiMS]] successfully demonstrated a high-throughput capability for [[MS-based proteomics]], achieving ~50 cells per hour with minimal signal crossover.
2. The study assigned 93% of 5,272 cells in Dataset I to major cell types: 72% neurons, 15% astrocytes, 6% microglia, and 7% unassigned.
3. Specific proteoform biomarkers were identified for cell types, such as monoacetylated [[ARP5L]] for neurons, [[ALDOA]] and [[GFAP]] for astrocytes, and [[PP5-TPR]] for microglia.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Overview of the [[scPiMS]] workflow, extraction kinetics (cellogram), and aggregated mass spectra/collector's curves. |
| Fig 2 | Cell type assignments visualized via [[PCA]] and heatmap; example mass spectra of identified cell-type-specific proteoforms. |

## Discussion

### Strengths
- Enables [[label-free]] profiling of intact proteoforms, preserving protein-level information.
- Significantly improves throughput compared to previous [[single-cell proteomics]] technologies.
- Bypasses [[proteolytic digestion]], reducing sample handling time and complexity.

### Limitations
- Dependent on a reference proteoform library for assignment.
- Requires specialized [[nano-DESI]] and [[Orbitrap]] instrumentation.
- Coverage is limited to proteoforms within the 5–70 kDa range.

### Future Work
- Scaling the approach further to identify rare cell subpopulations.
- Expanding reference proteoform databases to increase the depth of identification.

## Personal Notes



## Related Papers

- [[Su, P. et al. (2022) - Highly multiplexed, label-free proteoform imaging of tissues by individual ion mass spectrometry]]
- [[Kafader, J. O. et al. (2020) - Multiplexed mass spectrometry of individual ions improves measurement of proteoforms and their complexes]]
- [[Zeisel, A. et al. (2015) - Cell types in the mouse cortex and hippocampus revealed by single-cell RNA-seq]]