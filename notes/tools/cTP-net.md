---
title: cTP-net
aliases:
  - cTPnet
  - single-cell Transcriptome to Protein prediction
tags:
  - tools
  - software
  - deep-learning
  - multi-omics
  - single-cell
category: tool
url: https://github.com/zhouzilu/cTPnet
date_created: 2026-03-17
---

# cTP-net

**Single-cell Transcriptome to Protein prediction — a deep learning model that predicts surface protein abundance from single-cell RNA-seq data, trained on CITE-seq datasets.**

## Overview

cTP-net (Zhou Z et al., 2020) uses a neural network to learn the mapping from gene expression profiles to surface protein levels. Trained on paired [[CITE-seq]] data, it enables imputation of protein measurements on unimodal scRNA-seq datasets. It was one of the earliest deep learning approaches for this task.

## Key Features

- **Protein Prediction**: Imputes surface protein levels from scRNA-seq input
- **Transfer Learning**: Trained on CITE-seq reference, applied to RNA-only data
- **Gene Selection**: Identifies informative genes for each protein prediction

## Installation

Use the [official cTPnet repository](https://github.com/zhouzilu/cTPnet), which provides an R interface and version-specific Seurat notebooks. The project also links its Python implementation; use those instructions rather than an inferred package name.

## Usage

Follow the official notebook for the relevant Seurat version. Input is scRNA-seq data prepared as specified by the model; output is imputed relative surface-protein abundance. Predictions depend on the reference cell types and protein panel and are not directly measured MS protein abundances.

## Key Publications

> [!cite] Primary Reference
> Zhou Z, Ye C, Wang J, Zhang NR (2020). Surface protein imputation from single cell transcriptomes by deep neural networks. *Nature Communications* 11, 651.
> DOI: [10.1038/s41467-020-14391-0](https://doi.org/10.1038/s41467-020-14391-0)

## Links

- GitHub: https://github.com/zhouzilu/cTPnet

## Related Tools

- [[sciPENN]] — Alternative method with uncertainty quantification
- [[totalVI]] — Probabilistic approach to multi-omics integration
- [[BABEL]] — Bidirectional translation between modalities

## Source Check

- Source checked on 2026-10-20: [cTP-net documentation or source](https://github.com/zhouzilu/cTPnet).
- [Original cTP-net paper](https://doi.org/10.1038/s41467-020-14391-0).
