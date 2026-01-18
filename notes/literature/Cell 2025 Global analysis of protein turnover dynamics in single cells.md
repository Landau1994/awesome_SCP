---
title: Global analysis of protein turnover dynamics in single cells
aliases:
   - Global analysis of protein turnover dynamics in single cells
   - Sabatier et al., 2025
   - SC-pSILAC paper
tags:
  - literature
  - paper
category: literature
date_created: 2025-05-01
Journal: Cell
Year: 2025
authors:
  - Pierre Sabatier
  - Maico Lechner
  - Ulises H. Guzmán
  - Christian M. Beusch
  - Xinlei Zeng
  - Longteng Wang
  - Fabiana Izaguirre
  - Anjali Seth
  - Olga Gritsenko
  - Sergey Rodin
  - Karl-Henrik Grinnemo
  - Zilu Ye
  - Jesper V. Olsen
---

# Global analysis of protein turnover dynamics in single cells

## Citation

> [!cite] Reference
>**Title**：Global analysis of protein turnover dynamics in single cells
> **Authors**: Pierre Sabatier, Maico Lechner, Ulises H. Guzmán, et al.
> **Year**: 2025
> **Journal**: Cell
> **DOI**: 10.1016/j.cell.2025.03.002

## Abstract

Single-cell proteomics (SCPs) has advanced significantly, yet it remains largely unidimensional, focusing primarily on protein abundances. In this study, the authors employed a pulsed stable isotope labeling by amino acids in cell culture ([[pSILAC]]) approach to simultaneously analyze protein abundance and turnover in single cells ([[SC-pSILAC]]). Using a state-of-the-art SCP workflow involving the [[Orbitrap Astral]], they demonstrated that two SILAC labels are detectable from ~4,000 proteins in single [[HeLa]] cells. They performed a large-scale time-series SC-pSILAC analysis of undirected differentiation of human induced pluripotent stem cells ([[iPSCs]]) encompassing 6 sampling times over 2 months and analyzed >1,000 cells. Protein turnover dynamics highlighted differentiation-specific co-regulation of protein complexes with core histone turnover, discriminating dividing and non-dividing cells. Lastly, correlating cell diameter with the abundance of individual proteins showed that histones and some cell-cycle proteins do not scale with cell size.

## Key Points

- Development of [[SC-pSILAC]] to measure both protein abundance and turnover at the single-cell level.
- Identification of treatment-specific effects on protein turnover using drugs like [[Bortezomib]], [[Cycloheximide]], and [[CHIR99021]].
- Core histone turnover dynamics can distinguish between dividing and non-dividing cell populations in complex differentiation models.

## Methods

### Sample Preparation
- Method used: [[SC-pSILAC]] (Pulsed Stable Isotope Labeling by Amino Acids in Cell Culture) combined with [[ProteoCHIP]] based sample preparation.
- Cell type: [[HeLa]], [[HEK293T]], [[hFF-1]] (human foreskin fibroblasts), and [[hi12]] (human iPSCs) undergoing embryoid body (EB) differentiation.
- Number of cells: >1,000 single cells for the iPSC differentiation dataset; smaller cohorts for drug treatment validations.

### Data Analysis
- Software: [[Spectronaut]] (v18/v19) using [[directDIA+]], [[R]], [[RStudio]].
- Downstream: [[DAPAR]], [[Pracma]], [[ComplexHeatmap]], [[clusterProfiler]], [[Seurat]]-based workflow for clustering.

## Results

### Main Findings
1. **Feasibility of SC-pSILAC**: The method successfully quantified light and heavy labels for ~3,000-4,000 proteins in single cells, with turnover ratios correlating well (0.8) with bulk protein half-life measurements.
2. **Differentiation Dynamics**: During iPSC differentiation, protein turnover analysis revealed cell-specific markers and co-regulation of complexes (e.g., proteasome, ribosomes) that abundance data alone missed.
3. **Cell Cycle Insights**: Turnover rates of core histones (e.g., [[H4]]) served as a robust marker to distinguish actively dividing cells (fast turnover/high label incorporation) from non-dividing/contact-inhibited cells (slow turnover), a distinction not possible with bulk analysis.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Workflow of [[SC-pSILAC]], validation in [[HeLa]] cells, and correlation with bulk half-life in [[hFF]]. |
| Fig 2 | Impact of [[Bortezomib]] (proteasome inhibitor) and [[Cycloheximide]] (translation inhibitor) on turnover in [[HEK293T]] cells. |
| Fig 3 | Analysis of [[HeLa]] cells treated with GSK3 inhibitor [[CHIR99021]], showing [[Beta-catenin]] accumulation. |
| Fig 4 | Large-scale time-series analysis of [[iPSC]] differentiation into embryoid bodies (EBs) over 2 months. |
| Fig 5 | Cell-type specific marker expression and co-regulation of protein complexes (proteasome, histones) during differentiation. |
| Fig 6 | Histone turnover distinguishes dividing from non-dividing cells and correlates with cell diameter. |
| Fig 7 | Comparison of different modes of cell-cycle arrest (contact inhibition vs. serum deprivation) using histone turnover. |

## Discussion

### Strengths
- **Multidimensionality**: Provides an orthogonal layer of biological information (turnover) alongside abundance.
- **Sensitivity**: Capitalizes on the [[Orbitrap Astral]] to detect split signals (light/heavy) in single cells without excessive data loss.
- **Functional Insight**: Capable of identifying non-dividing subpopulations and drug mechanism of actions that abundance data might obscure.

### Limitations
- **Relative Quantification**: Can only measure relative turnover (ratio of light/heavy) at a single time point per cell, not absolute synthesis/degradation rates.
- **Sample Restrictions**: Requires metabolic labeling, making it difficult to apply directly to clinical tissue samples or organisms that cannot easily incorporate amino acid analogs.
- **Throughput**: Multiplexing reduces signal intensity, potentially increasing missing values for low-abundance proteins.

### Future Work
- Application of SC-pSILAC to cancer research to study dormant cancer cell populations.
- Investigation of scaling laws between protein concentration and cell size for cell-cycle regulators.
- Enhancing sensitivity and throughput to apply the method to more complex biological contexts.

## Personal Notes



## Related Papers

- Sabatier et al., 2021 (Nat. Commun.) - *Integrative proteomics method identifies a regulator of translation.*
- Ye et al., 2025 (Nat. Methods) - *Chip-Tip workflow enabling deep single-cell proteomics.*
- Schwanhäusser et al., 2011 (Nature) - *Global quantification of mammalian gene expression control (Bulk SILAC turnover).*