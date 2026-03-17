---
title: BABEL
aliases:
  - BABEL
tags:
  - tools
  - software
  - deep-learning
  - multi-omics
  - single-cell
  - translation
category: tool
url: https://doi.org/10.1073/pnas.2023070118
date_created: 2026-03-17
---

# BABEL

**A deep learning model for bidirectional translation between single-cell multi-omics modalities, capable of predicting chromatin accessibility from RNA and vice versa, as well as protein levels from transcriptomes.**

## Overview

BABEL (Wu KE et al., 2021) trains paired autoencoders on multi-modal single-cell data (e.g., paired RNA + ATAC from 10x Multiome, or RNA + Protein from [[CITE-seq]]) to learn a shared latent space. Once trained, it can translate from one modality to another bidirectionally, enabling prediction of missing modalities in unimodal datasets.

## Key Features

- **Bidirectional Translation**: Predicts ATAC from RNA and RNA from ATAC; also supports RNA ↔ Protein
- **Paired Autoencoder Architecture**: Two modality-specific encoders/decoders with a shared latent space
- **Cross-Dataset Generalization**: Trained on one tissue/condition, applied to others

## Installation

```bash
pip install babel-sc
```

## Key Publications

> [!cite] Primary Reference
> Wu KE, Katzen J, Bhatt RS, et al. (2021) *PNAS* 118(15), e2023070118
> DOI: [10.1073/pnas.2023070118](https://doi.org/10.1073/pnas.2023070118)

## Links

- GitHub: https://github.com/wukevin/babel

## Related Tools

- [[totalVI]] — Probabilistic joint model for CITE-seq data
- [[sciPENN]] — Unidirectional protein imputation from RNA
- [[cTP-net]] — Earlier protein prediction model
