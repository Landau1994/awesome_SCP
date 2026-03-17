---
title: totalVI
aliases:
  - Total Variational Inference
  - TOTALVI
tags:
  - tools
  - software
  - deep-learning
  - multi-omics
  - single-cell
  - variational-inference
category: tool
url: https://doi.org/10.1038/s41592-020-01050-x
date_created: 2026-03-17
---

# totalVI

**Total Variational Inference — a deep generative model for joint analysis of CITE-seq RNA and protein data, enabling dimensionality reduction, batch correction, differential expression, and protein imputation within a unified probabilistic framework.**

## Overview

totalVI (Gayoso et al., 2021) is part of the [[scvi-tools]] ecosystem. It models the joint distribution of RNA and surface protein counts from [[CITE-seq]] data using a variational autoencoder (VAE). By learning a shared latent space, totalVI can perform batch correction across datasets, impute missing proteins, and conduct differential expression analysis at both RNA and protein levels.

## Key Features

- **Joint Probabilistic Model**: Simultaneously models RNA (negative binomial) and protein (negative binomial mixture) distributions
- **Batch Correction**: Removes batch effects across multiple CITE-seq experiments
- **Protein Imputation**: Denoises protein measurements and imputes missing values
- **Differential Expression**: Bayesian differential expression testing for both modalities

## Installation

```bash
pip install scvi-tools
```

## Usage

```python
import scvi
scvi.model.TOTALVI.setup_anndata(adata, protein_expression_obsm_key="protein")
model = scvi.model.TOTALVI(adata)
model.train()
latent = model.get_latent_representation()
denoised_proteins = model.get_normalized_expression(n_samples=25, include_protein_background=False)
```

## Key Publications

> [!cite] Primary Reference
> Gayoso A, Steier Z, Lopez R, et al. (2021) *Nature Methods* 18, 272–282
> DOI: [10.1038/s41592-020-01050-x](https://doi.org/10.1038/s41592-020-01050-x)

## Links

- GitHub: https://github.com/scverse/scvi-tools
- Documentation: https://docs.scvi-tools.org/

## Related Tools

- [[sciPENN]] — Neural network-based protein imputation with uncertainty
- [[cTP-net]] — Earlier protein prediction approach
- [[Seurat]] — WNN-based multi-omics integration
- [[BABEL]] — Bidirectional modality translation
