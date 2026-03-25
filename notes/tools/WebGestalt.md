---
title: WebGestalt
aliases:
  - WebGestalt
tags:
  - tools
  - software
category: tool
url: https://www.webgestalt.org/
date_created: 2026-01-18
---

# WebGestalt

**A web-based toolkit for gene/protein set enrichment and functional interpretation.**

## Overview

WebGestalt supports over-representation and network-based enrichment analyses across multiple organism and annotation databases.

## Key Features

- **Web Interface**: Accessible enrichment analysis without heavy local setup.
- **Broad Annotation Support**: Multiple pathway and ontology resources.
- **Flexible Input Modes**: Ranked lists and unranked gene/protein sets.
- **Visualization Utilities**: Interpretable summaries for downstream reporting.

## Installation

```bash
# Web service; no local installation required
```

## Usage

```r
# Example code
library(WebGestalt)
```

## Input/Output

**Input:**
- Raw files (.raw, .d, .mzML)
- Gene/protein identifiers or ranked feature lists

**Output:**
- Protein/peptide matrices
- Quality metrics

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| organism | user-defined | Target species database |
| enrichment_method | ORA/GSEA variants | Statistical analysis mode |

## Key Publications

> [!cite] Primary Reference
> Liao et al. WebGestalt platform publications.

## Links

- Documentation: https://www.webgestalt.org/

## Related Tools

- [[MaxQuant]]
- [[DIA-NN]]
- [[scp Package]]
