---
title: cTP-net
aliases:
  - cTPnet
  - Cellular To Protein network
tags:
  - tools
  - software
  - deep-learning
  - multi-omics
  - single-cell
category: tool
url: https://doi.org/10.1038/s41592-020-0876-x
date_created: 2026-03-17
---

# cTP-net

**Cellular To Protein network — a deep learning model that predicts surface protein abundance from single-cell RNA-seq data, trained on CITE-seq datasets.**

## Overview

cTP-net (Zhou Z et al., 2020) uses a neural network to learn the mapping from gene expression profiles to surface protein levels. Trained on paired [[CITE-seq]] data, it enables imputation of protein measurements on unimodal scRNA-seq datasets. It was one of the earliest deep learning approaches for this task.

## Key Features

- **Protein Prediction**: Imputes surface protein levels from scRNA-seq input
- **Transfer Learning**: Trained on CITE-seq reference, applied to RNA-only data
- **Gene Selection**: Identifies informative genes for each protein prediction

## Installation

```bash
pip install ctpnet
```

## Usage

```python
import ctpnet
model = ctpnet.load_model('cTPnet_model')
predicted_proteins = model.predict(rna_data)
```

## Key Publications

> [!cite] Primary Reference
> Zhou Z, Ye C, Wang J, Zhang NR (2020) *Nature Methods* 17, 1053–1055
> DOI: [10.1038/s41592-020-0876-x](https://doi.org/10.1038/s41592-020-0876-x)

## Links

- GitHub: https://github.com/zhouzilu/cTPnet

## Related Tools

- [[sciPENN]] — Successor with uncertainty quantification
- [[totalVI]] — Probabilistic approach to multi-omics integration
- [[BABEL]] — Bidirectional translation between modalities
