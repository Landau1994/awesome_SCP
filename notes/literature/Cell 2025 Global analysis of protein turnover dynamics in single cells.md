---
title: Cell 2025 Global analysis of protein turnover dynamics in single cells
aliases:
  - <article>
  - <paper>
  - <literature>
tags:
  - literature
  - paper
category: literature
date_created: 2026-01-18
Journal: Nature Communications
Year: "2025"
---
# Global analysis of protein turnover dynamics in single cells

## Citation

> [!cite] Reference
> **Authors**: Pierre Sabatier, Maico Lechner, Ulises H. Guzmán, Christian M. Beusch, Xinlei Zeng, Longteng Wang, Fabiana Izaguirre, Anjali Seth, Olga Gritsenko, Sergey Rodin, Karl-Henrik Grinnemo, Zilu Ye, and Jesper V. Olsen
> **Year**: 2025
> **Journal**: Cell
> **DOI**: https://doi.org/10.1016/j.cell.2025.03.002

## Abstract

This study introduces SC-pSILAC, a method combining single-cell proteomics (SCP) with pulsed stable isotope labeling by amino acids in cell culture (pSILAC) to simultaneously measure protein abundance and turnover dynamics in single cells. Utilizing the Orbitrap Astral mass spectrometer, the authors quantify protein turnover in thousands of proteins across single cells. The method is applied to study drug-induced turnover changes and human iPSC differentiation. A key finding reveals that core histone turnover dynamics can distinguish dividing from non-dividing cells within a population, and that histone abundance does not scale with cell size, unlike the majority of the proteome.

## Key Points

- Development of **SC-pSILAC** to measure both protein abundance and turnover (Light/Heavy ratio) in single cells.
- Demonstration that histone turnover rates can differentiate between dividing and non-dividing (contact-inhibited) cells within the same sample, which is not possible with bulk analysis.
- Discovery that while most protein abundances scale linearly with cell size, histones and specific cell-cycle proteins do not.
- Application of the method to track protein dynamics during undirected differentiation of human iPSCs into embryoid bodies over 2 months.

## Methods

### Sample Preparation
- Method used: [[SC-pSILAC]] (utilizing [[ProteoCHIP]] LF-48/EVO 96 and [[Evotips]])
- Cell type: HeLa, HEK293T, human foreskin fibroblasts (hFF), human induced pluripotent stem cells (hiPSCs), Embryoid Bodies (EBs)
- Number of cells: >1,000 single cells for the differentiation dataset; varying numbers for drug treatments (single cells, 10-cell pools, bulk).

### Data Analysis
- Software: [[Spectronaut]] (v18/v19) using directDIA
- Downstream: [[DAPAR]], [[Pracma]], [[ComplexHeatmap]], [[clusterProfiler]] (in R environment)

## Results

### Main Findings
1. **Validation and Drug Effects**: The method quantified ~4,000 proteins in single HeLa cells with both SILAC labels. It successfully detected specific turnover changes induced by Bortezomib (proteasome inhibitor) and Cycloheximide (translation inhibitor), and identified $\beta$-catenin accumulation/stabilization upon GSK3 inhibition (CHIR99021).
2. **differentiation Dynamics**: During iPSC differentiation, the study identified cell-specific markers and turnover dynamics. Protein complexes like the proteasome and ribosomes showed co-regulated turnover.
3. **Cell Cycle and Size Scaling**: Core histone turnover was identified as a robust metric to distinguish dividing from non-dividing cells. Furthermore, correlating protein abundance with cell diameter revealed that histones do not scale with cell size, maintaining a constant amount regardless of cell volume, unlike the global proteome.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Overview of the SC-pSILAC workflow, validation on HeLa cells, and correlation of single-cell turnover ratios with bulk protein half-life. |
| Fig 2 | Analysis of HEK293T cells treated with Bortezomib and Cycloheximide, showing treatment-specific protein turnover changes. |
| Fig 3 | HeLa cells treated with GSK3 inhibitor CHIR99021, highlighting the specific stabilization and accumulation of $\beta$-catenin (CTNB1). |
| Fig 4 | Large-scale time-series analysis of iPSC differentiation into Embryoid Bodies, visualizing cell subpopulations and turnover dynamics. |
| Fig 5 | Cell-type specific marker expression and co-regulation of turnover in protein complexes (proteasome, histones, ribosomes). |
| Fig 6 | Histone turnover distinguishes dividing from non-dividing cells; analysis of protein abundance scaling relative to cell diameter. |
| Fig 7 | Comparison of different modes of cell-cycle arrest (contact inhibition vs. serum deprivation) using histone turnover and proteomic signatures. |

## Discussion

### Strengths
- **Multidimensionality**: Provides orthogonal layers of information (abundance and turnover) from the same single cell.
- **Sensitivity**: Leverages the [[Orbitrap Astral]] to detect dual labels in thousands of proteins per single cell.
- **Functional Insight**: Reveals biological phenomena (e.g., non-scaling of histones, quiescent sub-populations) masked in bulk averages.

### Limitations
- **Snapshot Nature**: Provides a ratio at a single time point rather than a kinetic rate; cannot separate synthesis and degradation rates without multiple time points (impossible in destructive SC analysis).
- **Reduced Sensitivity**: Splitting the signal between Light and Heavy channels lowers the overall identification count compared to label-free SCP.
- **Computational Challenges**: Quantifying low-abundance signals for both isotopic labels in single cells is computationally demanding.

### Future Work
- Application to tissue samples and clinical studies.
- Enhancing sensitivity and throughput to allow for broader applications.
- Studying cells at different stages of differentiation and dividing rates in more complex biological systems.

## Personal Notes

## Related Papers

- [[SCoPE2]]
- [[plexDIA]]
- [[nPOP]]