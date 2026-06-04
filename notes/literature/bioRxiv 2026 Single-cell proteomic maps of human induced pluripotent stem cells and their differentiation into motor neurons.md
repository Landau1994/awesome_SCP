---
title: Single-cell proteomic maps of human induced pluripotent stem cells and their differentiation into motor neurons
authors:
  - Vladimir A. Zhemkov
  - Aleksandra Binek
  - Ali Haghani
  - Edo Israely
  - Shaughn Bell
  - Alba Sansa
  - George Lawless
  - Jennifer Van Eyk
  - Clive N. Svendsen
aliases:
  - 
tags:
  - literature
  - paper
category: literature
date_created: 2026-06-04
Journal: bioRxiv
Year: 2026
---

# Single-cell proteomic maps of human induced pluripotent stem cells and their differentiation into motor neurons

## Citation

> [!cite] Reference
> **Title**：Single-cell proteomic maps of human induced pluripotent stem cells and their differentiation into motor neurons
> **Authors**: Vladimir A. Zhemkov, Aleksandra Binek, Ali Haghani, Edo Israely, Shaughn Bell, Alba Sansa, George Lawless, Jennifer Van Eyk, Clive N. Svendsen
> **Year**: 2026
> **Journal**: bioRxiv
> **DOI**: 10.64898/2026.05.29.728893

## Abstract

This paper presents the first single-cell proteomic maps of human induced pluripotent stem cells (iPSCs) and their differentiation into motor neurons (MNs). By utilizing a high-sensitivity [[MS-SCP]] (single-cell proteomics) approach, the study identifies proteomes of individual cells, effectively resolving iPSC and MN states, as well as their metabolic and organellar heterogeneity. The authors demonstrate significant, stage-specific discordance between the transcriptome and the proteome in differentiated neurons, suggesting that final cell states are largely defined by their dynamic protein composition rather than RNA.

## Key Points

- Establishment of high-sensitivity [[MS-SCP]] maps for characterizing iPSC pluripotency and motor neuron development.
- Discovery of distinct iPSC subclusters (0-Hi, 1-Lo, 2-Dif) and a specific motor neuron-enriched cluster ("4-MN") that are otherwise obscured by bulk methods.
- Demonstration of cell-type-specific RNA-protein discordance, revealing that mRNA levels often fail to accurately predict protein abundance during neuronal differentiation.
- Integration of [[snRNA-seq]] with [[MS-SCP]] to validate cell identity and investigate regulatory dynamics.

## Methods

### Sample Preparation
- Method used: [[FACS]] sorting into 384-well plates, "one-pot" [[MS-SCP]] protocol, and [[nano-DTSC]] (nanoflow dual-trap single-column) liquid chromatography.
- Cell type: Human iPSCs and iPSC-derived motor neurons (d7 to d60).
- Number of cells: 309 single iPSCs and 1634 single cells for differentiation timepoints.

### Data Analysis
- Software: [[DIA-NN]], [[Seurat]], [[CellRank]], [[ClusterProfiler]], [[CellRanger]], [[Scanpy]].
- Downstream: [[GSEA]] (Gene Set Enrichment Analysis), linear regression, [[UMAP]] embedding, trajectory inference via [[Palantir]].

## Results

### Main Findings
1. iPSCs show unexpected protein-level heterogeneity regarding pluripotency markers like Oct4, Lin28A, and Podocalyxin (Podxl), which correlates with their cell cycle stage and metabolic state.
2. Differentiation into motor neurons involves significant proteome remodeling, with downregulation of pluripotency factors and an increase in MN-specific markers such as Nfh and ChAT.
3. Protein-RNA discordance is highly dynamic; proteins involved in translation and splicing are typically upregulated even when mRNA remains stable, while other pathways exhibit protein repression, particularly during the transition from neurosphere progenitors to mature MNs.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Overview of [[MS-SCP]] pipeline, iPSC sub-clustering, and metabolic/cell-cycle fluctuations. |
| Fig 2 | Proteomic landscape of motor neuron differentiation and organelle abundance changes. |
| Fig 3 | Identification of MN and glial clusters; comparison between [[MS-SCP]] and [[snRNA-seq]]. |
| Fig 4 | Analysis of dynamic RNA-protein discordance and lineage-specific regulation. |

## Discussion

### Strengths
- Provides high-coverage single-cell proteomic data which reveals biological insights missed by RNA-seq.
- Successfully validates clusters using both proteomic and transcriptomic data.
- Directly addresses the limitations of bulk proteomics in heterogeneous cell populations.

### Limitations
- Low-abundance canonical markers (e.g., ChAT) remained challenging to detect, likely due to instrument sensitivity limits.
- The study compares protein and RNA from different cells (paired approach, not same-cell).

### Future Work
- Further investigation into post-transcriptional regulatory mechanisms that drive the observed RNA-protein discordance.
- Application of these methods to patient-derived cells to identify proteomic signatures of neurodegenerative diseases.

## Personal Notes



## Related Papers

- [[SCoPE2]] (Multiplexed single-cell proteomics)
- [[Wu et al., 2026]] (Single-cell proteomic landscape of the developing human brain)
- [[Guise et al., 2024]] (TDP-43-stratified single-cell proteomics of postmortem human spinal motor neurons)