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
url: https://github.com/jlakkis/sciPENN
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

The [official repository](https://github.com/jlakkis/sciPENN) provides `sciPENN_API` tutorials for training, prediction and imputation. Follow the tutorial matching the task and supply the required AnnData/reference inputs. The previously shown abbreviated constructor and `impute()` call were not validated as a runnable workflow.

## Key Publications

> [!cite] Primary Reference
> Lakkis J, Schroeder A, Su K, et al. (2022). A multi-use deep learning method for CITE-seq and single-cell RNA-seq data integration with cell surface protein prediction and imputation. *Nature Machine Intelligence* 4, 940–952.
> DOI: [10.1038/s42256-022-00545-w](https://doi.org/10.1038/s42256-022-00545-w)

## Links

- GitHub: https://github.com/jlakkis/sciPENN

## Related Tools

- [[totalVI]] — Probabilistic multi-omics integration
- [[cTP-net]] — Earlier protein imputation method
- [[Seurat]] — General single-cell toolkit with WNN integration

## Source Check

- Source checked on 2026-10-20: [sciPENN documentation or source](https://github.com/jlakkis/sciPENN).
- [Original sciPENN paper](https://www.nature.com/articles/s42256-022-00545-w).
