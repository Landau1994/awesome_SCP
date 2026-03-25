---
title: GLUE
aliases:
  - GLUE
tags:
  - tools
  - software
category: tool
url: 
date_created: 2026-03-25
---

# GLUE

**A framework for graph-linked integration of unpaired single-cell multi-omics data.**

## Overview

GLUE is used to align modalities into a shared latent space, supporting integration of transcriptomic and proteomic single-cell datasets.

## Key Features

- **Cross-Modality Alignment**: Integrates different omics views.
- **Graph-Based Prior Use**: Incorporates regulatory/feature relationships.
- **Label Transfer Support**: Helps map cell states across datasets.
- **Cross-Platform**: Windows, Linux, macOS

## Installation

```bash
# Installation commands
# See official GLUE package instructions
```

## Usage

```r
# Example code
# Commonly used in Python
```

## Input/Output

**Input:**
- Multi-omics matrices
- Feature linkage graph/prior knowledge

**Output:**
- Joint latent embedding
- Cross-modal integration and transfer results

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| latent_dim | user-defined | Shared embedding dimensionality |
| graph_weight | user-defined | Strength of prior graph constraints |

## Key Publications

> [!cite] Primary Reference
> Cao and Gao (2022) *Nature Biotechnology*

## Links

- GitHub:
- Documentation:

## Related Tools

- [[Scanpy]]
- [[scvi-tools]]
- [[scProtVelo]]
