---
title: sciPENN
aliases:
  - sciPENN
tags:
  - tools
  - software
  - deep-learning
  - multi-omics
  - single-cell
category: tool
url: https://doi.org/10.1038/s41592-022-01728-4
date_created: 2026-03-17
---

# sciPENN

**Single-cell Imputation and Embedding Neural Network — a deep learning tool for multi-modal single-cell data integration, protein imputation, and uncertainty quantification.**

## Overview

sciPENN (Lakkis et al., 2022) is a neural network-based method for integrating [[CITE-seq]] protein and RNA data. It can impute missing protein measurements in query datasets that only have transcriptomic data, using a reference CITE-seq dataset. It also provides uncertainty estimates for predictions and produces a joint embedding for downstream analysis (clustering, visualization).

## Key Features

- **Protein Imputation**: Predicts surface protein levels from scRNA-seq using a trained CITE-seq reference
- **Uncertainty Quantification**: Provides prediction confidence for each imputed protein
- **Joint Embedding**: Learns a shared latent space for RNA and protein data integration
- **Transfer Learning**: Trained on one CITE-seq dataset, applied to RNA-only datasets

## Installation

```bash
pip install sciPENN
```

## Usage

```python
from sciPENN.API import sciPENN_API
sciPENN = sciPENN_API(gene_trainsets, protein_trainsets, gene_test)
sciPENN.train(n_epochs=10000, ES_max=12, decay_max=6)
imputed_proteins = sciPENN.impute()
```

## Key Publications

> [!cite] Primary Reference
> Lakkis J, Wang D, Zhang Y, et al. (2022) *Nature Methods* 19, 1534–1541
> DOI: [10.1038/s41592-022-01728-4](https://doi.org/10.1038/s41592-022-01728-4)

## Links

- GitHub: https://github.com/jlakkis/sciPENN

## Related Tools

- [[totalVI]] — Probabilistic multi-omics integration
- [[cTP-net]] — Earlier protein imputation method
- [[Seurat]] — General single-cell toolkit with WNN integration
