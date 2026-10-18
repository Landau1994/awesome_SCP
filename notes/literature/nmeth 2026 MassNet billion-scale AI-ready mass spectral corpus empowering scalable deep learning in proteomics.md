---
title: MassNet:billion-scale AI-ready mass spectral corpus empowering scalable deep learning in proteomics
authors:
  - Jun A
  - Xiang Zhang
  - Xiaofan Zhang
  - Jiaqi Wei
  - Te Zhang
  - Yamin Deng
  - Pu Liu
  - Zongxiang Nie
  - Yiwen Yu
  - Yi Chen
  - Nanqing Dong
  - Zhiqiang Gao
  - Siqi Sun
  - Tiannan Guo
aliases:
  - MassNet
tags:
  - literature
  - paper
  - proteomics
  - deep-learning
category: literature
date_created: 2025-05-14
Journal: Nature Methods
Year: 2026
---

# MassNet: billion-scale AI-ready mass spectral corpus empowering scalable deep learning in proteomics

## Citation

> [!cite] Reference
> **Title**: MassNet: billion-scale AI-ready mass spectral corpus empowering scalable deep learning in proteomics
> **Authors**: Jun A, Xiang Zhang, Xiaofan Zhang, Jiaqi Wei, Te Zhang, Yamin Deng, Pu Liu, Zongxiang Nie, Yiwen Yu, Yi Chen, Nanqing Dong, Zhiqiang Gao, Siqi Sun, Tiannan Guo
> **Year**: 2026
> **Journal**: Nature Methods
> **DOI**: https://doi.org/10.1038/s41592-026-03247-y

## Abstract

The paper introduces MassNet, an artificial intelligence (AI)-ready data corpus for mass spectrometry (MS)-based proteomics. Inspired by large-scale data corpora in NLP and computer vision, MassNet contains 1.5 billion tandem MS spectra from high-quality data-dependent acquisition (DDA) MS data across 35 species. The authors also present the Mass Spectrometry DDA Tensor (MSDT), a standardized, compact, and AI-ready data format. Based on this corpus, they developed XuanjiNovo, a non-autoregressive transformer model for de novo peptide sequencing that utilizes a novel curriculum learning strategy. XuanjiNovo demonstrates significant performance improvements over existing state-of-the-art models on human Astral data and supports additional tasks like retention time (RT) prediction and PSM rescoring.

## Key Points

- MassNet provides a large-scale (1.5 billion spectra, ~30 TB) AI-ready resource for proteomics, standardizing data from PRIDE and iProX.
- Development of the [[MSDT]] format, which uses [[Apache Parquet]] to enable efficient data storage, faster I/O, and easier downstream deep learning integration.
- Introduction of [[XuanjiNovo]], a non-autoregressive transformer model for de novo sequencing, achieving 38.35–143.57% improvements in peptide recall over state-of-the-art methods.
- The use of a curriculum learning strategy significantly improves the training stability of non-autoregressive models on complex, heterogeneous proteomics datasets.

## Methods

### Sample Preparation
- Method used: [[Data-dependent acquisition]] (DDA) MS data.
- Cell type: Diverse (animals, plants, microorganisms across 35 species).
- Number of cells: N/A (Project-level integration).

### Data Analysis
- Software: [[FragPipe]], [[Sage]], [[XuanjiNovo]], [[DeepLC]], [[DDA-BERT]].
- Downstream: [[De novo peptide sequencing]], [[Retention time prediction]], [[PSM rescoring]].

## Results

### Main Findings
1. MassNet integrates 27,643 LC–MS/MS runs into a standardized resource, providing 548 million target PSMs.
2. The [[MSDT]] format reduces storage overhead by approximately 82% compared to source files while providing faster read/write speeds for deep learning pipelines.
3. XuanjiNovo, trained on 100 million PSMs, consistently outperforms established models (e.g., [[π-PrimeNovo]], [[InstaNovo+]]) in peptide recall across 15 species and various MS platforms, including high-resolution Orbitrap Astral data.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Overview of MassNet, showing the data-processing workflow, species composition, and representative downstream applications. |
| Fig 2 | Programmatic construction of MassNet and performance evaluation of the [[MSDT]] format, comparing compression ratios and read times across various serialization formats. |

## Discussion

### Strengths
- Unprecedented scale and diversity of the MS-based proteomics dataset.
- Standardized, AI-ready data representation ([[MSDT]]) facilitates cross-platform and cross-study usability.
- Curriculum learning approach effectively addresses training instability in non-autoregressive models.

### Limitations
- The current MassNet dataset focus on common post-translational modifications (PTMs) like methionine oxidation and N-terminal acetylation, omitting more complex PTMs (e.g., phosphorylation, glycosylation).
- The filtering strategy for "confidently identified" spectra may exclude valuable, unidentified spectra that could provide additional signal.

### Future Work
- Expanding MassNet to include a wider variety of PTM-rich spectra and specialized workflows (e.g., phosphoproteomics, glycoproteomics).
- Integrating more search engines to reduce algorithm-specific bias.
- Incorporating data from other acquisition modes, such as data-independent acquisition (DIA).

## Personal Notes

