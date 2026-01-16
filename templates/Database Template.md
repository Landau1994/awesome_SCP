---
title: <% tp.file.title %>
aliases:
  - <% tp.file.cursor(1) %>
tags:
  - database
  - resource
category: database
url: <% tp.file.cursor(3) %>
date_created: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

**<% tp.file.cursor(4) %>**

## Overview

<% tp.file.cursor(5) %>

## Statistics

- **Datasets**:
- **Cells**:
- **Proteins**:
- **Species**:
- **Technologies**:

## Data Content

### Technologies Covered
- [[SCoPE2]]
- [[plexDIA]]
- Label-free DIA

### Data Types
- Expression matrices
- Metadata
- Quality metrics

## Features

- **Search**: Query by protein, cell type, tissue
- **Visualization**: Interactive plots
- **Download**: Bulk data export
- **API Access**: Programmatic queries

## Access

**Website**: <% tp.file.cursor(6) %>

## Use Cases

1. Benchmark datasets for method development
2. Reference data for cell type annotation
3. Meta-analysis across studies
4. Training data for ML models

## Key Publications

> [!cite] Primary Reference
> Author et al. (Year) *Journal*
> DOI: [10.xxxx/xxxxx](https://doi.org/10.xxxx/xxxxx)

## Related Resources

- [[SPDB]]
- [[SingPro]]
- scpdata (Bioconductor)
