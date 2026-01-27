---
title: Fertilization triggers early proteomic symmetry breaking in mammalian embryos
authors:
  - Lisa K. Iwamoto-Stohl
  - Aleksandra A. Petelski
  - Baiyi Quan
  - Maciej Meglicki
  - Audrey Fu
  - Shoma Nakagawa
  - Breanna McMahon
  - Ting-Yu Wang
  - Saad Khan
  - Harrison Specht
  - Gray Huffman
  - Jason Derks
  - Sergi Junyent
  - Bailey A.T. Weatherbee
  - Antonia Weberling
  - Carlos W. Gantner
  - Rachel S. Mandelbaum
  - Richard J. Paulson
  - Lisa Lam
  - Tsui-Fen Chou
  - Nikolai Slavov
  - Magdalena Zernicka-Goetz
aliases:
   - Fertilization triggers early proteomic symmetry breaking in mammalian embryos
   - Iwamoto-Stohl et al. 2025
   - Cell 2025 proteomic asymmetry paper
tags:
  - literature
  - paper
  - embryology
  - single-cell-proteomics
  - development
category: literature
date_created: 2025-01-01
Journal: Cell
Year: 2025
---

# Fertilization triggers early proteomic symmetry breaking in mammalian embryos

## Citation

> [!cite] Reference
> **Title**： Fertilization triggers early proteomic symmetry breaking in mammalian embryos
> **Authors**: Lisa K. Iwamoto-Stohl, Aleksandra A. Petelski, Baiyi Quan, et al.
> **Year**: 2025
> **Journal**: Cell
> **DOI**: 10.1016/j.cell.2025.11.006

## Abstract

This study challenges the long-held view that mammalian blastomeres are developmentally equivalent until the 8-to-16-cell stage. Using multiplexed and label-free single-cell proteomics, the authors identify over 300 asymmetrically abundant proteins in mouse 2-cell embryos, classifying blastomeres into two distinct proteomic states: "alpha" and "beta." These asymmetries are detectable in the zygote, intensify by the 4-cell stage, and are triggered by fertilization, correlating with the sperm entry site. Functional analysis reveals that beta blastomeres possess greater developmental potential, contributing more significantly to the epiblast. This proteomic pre-patterning is conserved in human embryos, suggesting a fundamental mechanism of early symmetry breaking and lineage bias in mammalian development.

## Key Points

- Proteomic asymmetry arises at the zygote stage and divides 2-cell blastomeres into distinct **alpha** and **beta** clusters.
- This asymmetry is triggered by fertilization and aligns with the sperm entry site; parthenotes (unfertilized activated eggs) do not show this asymmetry.
- **Beta blastomeres** (enriched in protein degradation/transport factors) have higher developmental potential and contribute more to the epiblast than alpha blastomeres.
- Similar proteomic clustering and protein enrichment patterns are conserved in human 2-cell embryos.

## Methods

### Sample Preparation
- **Method used**: [[SCoPE2]] (Single Cell ProtEomics by Mass Spectrometry), [[pSCoPE]] (prioritized SCoPE), and Label-free [[DIA]] (Data-Independent Acquisition).
- **Cell type**: Single blastomeres from mouse embryos (zygote halves, 2-cell, 4-cell), parthenogenetic mouse embryos, and human 2-cell embryos.
- **Number of cells**: 
    - Mouse: 36 2-cell embryos (72 blastomeres), 31 4-cell embryos, 14 zygote halves.
    - Human: 13 pairs of 2-cell blastomeres.
    - Controls: 200 [[mouse embryonic stem cells (ESCs)]] used as carrier.

### Data Analysis
- **Software**: [[MaxQuant]], [[Proteome Discoverer]] (with [[Chimerys]]), [[Spectronaut]], [[DIA-NN]], [[R]], [[Python]].
- **Downstream**: [[k-means clustering]], [[Principal Component Analysis (PCA)]], [[Protein Set Enrichment Analysis (PSEA)]], [[Hierarchical Clustering]], [[Gene Ontology (GO)]] analysis.

## Results

### Main Findings
1.  **Proteomic Biclustering**: Single-cell proteomics revealed two reproducible clusters (alpha and beta) in sister blastomeres of 2-cell mouse embryos, defined by ~349 differentially abundant proteins involved in transport and degradation.
2.  **Origin of Asymmetry**: Asymmetry is detected in mechanically bisected zygotes and correlates with the sperm entry site (fertilization cone). Parthenogenetic embryos lacked this consistent asymmetry, indicating fertilization is the trigger.
3.  **Developmental Potential**: Beta blastomeres (containing the sperm entry site) yielded blastocysts with significantly higher epiblast cell counts compared to alpha blastomeres. Knockdown of beta-enriched proteins (e.g., [[Gps1]], [[Nedd8]]) altered lineage composition.
4.  **Human Conservation**: Human 2-cell blastomeres also segregated into two distinct proteomic clusters with consistent enrichment of protein degradation and transport pathways, showing evolutionary conservation.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Identification of Alpha and Beta proteomic states in mouse 2-cell and 4-cell embryos using [[SCoPE2]]. |
| Fig 2 | Proteomic asymmetry is inherited from the zygote (bisected zygote analysis) and intensifies during development. |
| Fig 3 | Functional validation: Knockdown of beta-enriched proteins ([[Nedd8]], [[Gps1]]) and alpha-enriched protein ([[PSMC4]]) alters lineage fate (TE vs. Epiblast). |
| Fig 4 | Beta blastomeres exhibit higher developmental potential (more epiblast cells) compared to alpha blastomeres when cultured separately. |
| Fig 5 | Fertilization triggers asymmetry: Sperm entry point (SEP) correlates with beta identity; parthenotes lack asymmetry. |
| Fig 6 | Conservation in humans: Human 2-cell embryos show similar proteomic clustering and pathway enrichment (using [[DIA]] and [[SCoPE2]]). |
| Fig 7 | Cross-species comparison confirming conservation of Alpha/Beta clusters and specific protein markers between mouse and human. |

## Discussion

### Strengths
- **Technological Advancement**: Application of [[SCoPE2]] and label-free [[DIA]] to single mammalian blastomeres allows for depth not possible with previous bulk methods.
- **Causal Link**: Establishes a direct link between the sperm entry site, proteomic heterogeneity, and developmental potential.
- **Functional Validation**: Goes beyond observation by using dsRNA knockdown to prove the functional relevance of identified proteins (Nedd8, Gps1).
- **Cross-Species Relevance**: Demonstrates conservation in valuable human embryo samples.

### Limitations
- **Validation Difficulty**: Immunofluorescence (IF) could not reliably validate the subtle quantitative differences detected by MS, highlighting the sensitivity gap between MS and antibody-based methods.
- **Sample Size**: Limited number of human embryos due to scarcity and ethical constraints.
- **Mechanism Specifics**: While sperm entry is the trigger, the precise molecular mechanism of how the sperm entry site orchestrates the asymmetric distribution of maternal proteins remains to be fully elucidated.

### Future Work
- Investigating mechanisms regulating the maintenance versus dissolution of totipotency based on these proteomic profiles.
- Studying how beta-enriched proteins (specifically those in protein degradation) impact Zygotic Genome Activation ([[ZGA]]).
- Further exploration of the "cytoplasmic lattice" proteins enriched in beta cells.

## Personal Notes



## Related Papers

- [[Petelski et al., 2021]] - Multiplexed single-cell proteomics using SCoPE2.
- [[Huffman et al., 2023]] - Prioritized mass spectrometry (pSCoPE).
- [[Casser et al., 2017]] - Totipotency segregation in 2-cell mouse embryos.
- [[Piotrowska & Zernicka-Goetz, 2001]] - Role for sperm in spatial patterning of the early mouse embryo.