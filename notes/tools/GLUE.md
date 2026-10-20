---
title: GLUE
aliases:
  - GLUE
tags:
  - tools
  - software
category: tool
url: https://github.com/gao-lab/GLUE
date_created: 2026-03-25
---

# GLUE

**A framework for graph-linked integration of unpaired single-cell multi-omics data.**

## Overview

GLUE is used to align modalities into a shared latent space, using a guidance graph to connect features across assays. The core demonstrated setting includes unpaired RNA and chromatin-accessibility data; use with MS proteomics requires an appropriate feature graph and dataset-specific validation.

## Key Features

- **Cross-Modality Alignment**: Integrates different omics views.
- **Graph-Based Prior Use**: Incorporates regulatory/feature relationships.
- **Label Transfer Support**: Helps map cell states across datasets.
- **Environment**: Follow the official release requirements; operating-system support depends on the package and its dependencies.

## Input/Output

**Input:**

- Multi-omics matrices
- Feature linkage graph/prior knowledge

**Output:**

- Joint latent embedding
- Cross-modal integration and transfer results

## Key Publications

> [!cite] Primary Reference
> Cao et al. (2022). Multi-omics single-cell data integration and regulatory inference with graph-linked embedding. *Nature Biotechnology*.
> DOI: [10.1038/s41587-022-01284-4](https://doi.org/10.1038/s41587-022-01284-4)

## Links

- GitHub: https://github.com/gao-lab/GLUE
- Documentation/source: https://github.com/gao-lab/GLUE

## Related Tools

- [[Scanpy]]
- [[scvi-tools]]
- [[scProtVelo]]

## Source Check

- Source checked on 2026-10-20: [GLUE documentation or source](https://github.com/gao-lab/GLUE).
