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
url: https://github.com/wukevin/babel
date_created: 2026-03-17
---

# BABEL

**A deep learning model for bidirectional translation between single-cell multi-omics modalities, capable of predicting chromatin accessibility from RNA and vice versa, as well as protein levels from transcriptomes.**

## Overview

BABEL (Wu et al., 2021) learns a shared latent representation from paired RNA and chromatin-accessibility measurements. It supports RNA-to-ATAC and ATAC-to-RNA prediction; the paper also demonstrates an extension for predicting surface proteins from RNA. These results do not establish arbitrary bidirectional translation between every pair of modalities.

## Key Features

- **Bidirectional Translation**: Predicts ATAC from RNA and RNA from ATAC; RNA-to-protein prediction is an extension
- **Paired Autoencoder Architecture**: Two modality-specific encoders/decoders with a shared latent space
- **Cross-Dataset Generalization**: Trained on one tissue/condition, applied to others

## Installation

Use the [repository environment and installation instructions](https://github.com/wukevin/babel). The previous `pip install babel-sc` command was not supported by the project instructions.

## Key Publications

> [!cite] Primary Reference
> Wu KE, Yost KE, Chang HY, Zou J (2021) *PNAS* 118(15), e2023070118
> DOI: [10.1073/pnas.2023070118](https://doi.org/10.1073/pnas.2023070118)

## Links

- GitHub: https://github.com/wukevin/babel

## Related Tools

- [[totalVI]] — Probabilistic joint model for CITE-seq data
- [[sciPENN]] — Unidirectional protein imputation from RNA
- [[cTP-net]] — Earlier protein prediction model

## Source Check

- Source checked on 2026-10-20: [BABEL documentation or source](https://github.com/wukevin/babel).
