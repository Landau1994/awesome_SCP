---
title: Proteomics reveals spatial and molecular heterogeneities in advanced atherosclerotic carotid artery plaques
authors:
  - Ankit Sinha
  - Nadja Sachs
  - Elena Kratz
  - Jessica Pauli
  - Sophia Steigerwald
  - Vincent Albrecht
  - Thierry M. Nordmann
  - Enes Ugur
  - Edwin H. Rodriguez
  - Marie-Luise Engl
  - Patricia Skowronek
  - Denys Oliinyk
  - Andreas Metousis
  - Moritz von Scheidt
  - Michael Wierer
  - Hanna Winter
  - Heribert Schunkert
  - Daniela Branzan
  - Lars Maegdefessel
  - Matthias Mann
aliases:
  - 
tags:
  - literature
  - paper
  - proteomics
  - atherosclerosis
category: literature
date_created: 2024-05-23
Journal: Nature Cardiovascular Research
Year: 2026
---

# Proteomics reveals spatial and molecular heterogeneities in advanced atherosclerotic carotid artery plaques

## Citation

> [!cite] Reference
> **Title**：Proteomics reveals spatial and molecular heterogeneities in advanced atherosclerotic carotid artery plaques
> **Authors**: Ankit Sinha et al.
> **Year**: 2026
> **Journal**: Nature Cardiovascular Research
> **DOI**: 10.1038/s44161-026-00827-1

## Abstract

Atherosclerotic plaque rupture is a primary cause of cerebrovascular events, but the molecular factors defining vulnerability-related plaque morphology—specifically fibrous-cap thickness—remain poorly understood. This study utilizes histomorphology-guided [[spatial proteomics]] on 112 carotid endarterectomy specimens to delineate molecular programs associated with plaque cap phenotypes across discrete subregions (media, necrotic core, and fibrous cap). The results reveal that differences between thin-cap (TnC) and thick-cap (TkC) plaques are primarily localized to the necrotic core and fibrous cap, showing significant enrichment for processes related to inflammation, lipid handling, extracellular matrix remodeling, and calcification. PCSK9 was identified as a key protein associated with TnC plaques. An in vitro model of necrotic core-like stress confirmed that oxidative and inflammatory environments increase PCSK9 secretion in primary vascular smooth muscle cells (VSMCs). These findings provide a spatial framework for biomarker discovery in advanced atherosclerosis.

## Key Points

- Spatial proteomics mapping of carotid plaques identifies distinct molecular programs in subregions (necrotic core, fibrous cap, and media).
- The necrotic core is the most molecularly distinct subregion and shows significant proteomic variation linked to plaque cap thickness.
- PCSK9 is a robust marker for thin-cap plaques, with in vitro validation showing its expression is induced in VSMCs under oxidative/inflammatory stress.
- A multi-subregion protein panel (using tissue data) effectively discriminates TnC plaques, though serum-based biomarker performance remains modest.

## Methods

### Sample Preparation
- Method used: [[Laser microdissection]] of FFPE plaque sections, followed by [[LC-MS/MS]].
- Cell type: Primary human vascular smooth muscle cells (VSMCs).
- Number of cells: 15,000 cells per well for in vitro culture.

### Data Analysis
- Software: [[DIA-NN]], [[WGCNA]], [[XGBoost]], [[g:Profiler]], [[Cytoscape]].
- Downstream: [[Differential expression analysis]] via LIMMA, consensus clustering, module enrichment analysis.

## Results

### Main Findings
1. Plaque subregions exhibit highly distinct molecular landscapes; the necrotic core shows the largest proteomic differences related to thin-cap (TnC) plaque status.
2. TnC plaques are characterized by increased immune response, lipid metabolism, and ECM degradation, while TkC plaques show enrichment for cellular respiration and VSMC contractile programs.
3. PCSK9 is strongly linked to the TnC phenotype and is predominantly enriched in the necrotic core; stress-induced VSMC models confirm its role in response to the pro-atherogenic environment.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Clinical metadata and spatial proteomics workflow overview. |
| Fig 2 | Protein detection characteristics and necrotic core subtypes identified by consensus clustering. |
| Fig 3 | GO enrichment analysis and module score profiles for necrotic core subclusters. |
| Fig 4 | Subregion-specific proteomic programs and inferred cell-type enrichment. |
| Fig 5 | Comparative analysis of TnC vs TkC plaque proteomes and functional pathway enrichment. |
| Fig 6 | Mechanistic analysis of PCSK9 secretion in primary VSMCs under oxidative/inflammatory stress. |
| Fig 7 | Development and validation of a multi-subregion protein panel to discriminate plaque phenotypes. |
| Fig 8 | Serum proteome profiling and derivation of a serum-based biomarker panel. |

## Discussion

### Strengths
- Unprecedented spatial resolution of the plaque proteome via [[laser microdissection]].
- Integration of human tissue findings with functional in vitro perturbation models.
- Hierarchical machine learning approach for protein panel selection.

### Limitations
- The cross-sectional design prevents predicting future clinical events or longitudinal progression.
- Serum biomarker discrimination was significantly weaker than tissue-based panels, likely due to dilution effects.
- The study focuses on advanced disease; molecular patterns in early lesions are not captured.

### Future Work
- Mechanistic studies on the causal relationship between PCSK9 signaling and plaque remodeling.
- Further refinement of serum-based markers to potentially improve diagnostic performance.

## Personal Notes



## Related Papers

- Newby, A. C. & Zaltsman, A. B. Fibrous cap formation or destruction. Cardiovasc. Res. 41, 345–360 (1999).
- Saba, L. et al. Carotid artery atherosclerosis: mechanisms of instability and clinical implications. Eur. Heart J. 46, 904–921 (2025).
- Redgrave, J. N. et al. Histological assessment of 526 symptomatic carotid plaques... Circulation 113, 2320–2328 (2006).