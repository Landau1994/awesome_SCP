---
title: scvi-tools
aliases:
  - scvi-tools
  - scVI
tags:
  - tools
  - software
category: tool
url: 
date_created: 2026-03-25
---

# scvi-tools

**A probabilistic deep learning toolkit for single-cell omics integration and modeling.**

## Overview

scvi-tools provides variational models for single-cell data integration, batch correction, and probabilistic inference across modalities.

## Key Features

- **Probabilistic Modeling**: Uncertainty-aware inference.
- **Multi-Omics Integration**: Supports RNA/protein and related modalities.
- **Model Ecosystem**: Includes widely used models such as totalVI.
- **Cross-Platform**: Windows, Linux, macOS

## Installation

```bash
# Installation commands
# pip install scvi-tools
```

## Usage

```r
# Example code
# Used through Python APIs
```

## Input/Output

**Input:**
- Single-cell matrices and metadata
- Model configuration and covariates

**Output:**
- Latent embeddings
- Corrected representations and uncertainty estimates

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| latent_dim | user-defined | Latent space dimensionality |
| max_epochs | user-defined | Training duration |

## Key Publications

> [!cite] Primary Reference
> Gayoso et al. (2022) *Nature Biotechnology*

## Links

- GitHub:
- Documentation:

## Related Tools

- [[totalVI]]
- [[Scanpy]]
- [[PyTorch]]
