---
title: Percolator
aliases:
  - Percolator
tags:
  - tools
  - software
category: tool
url: 
date_created: 2026-03-25
---

# Percolator

**A semi-supervised machine learning tool for improving peptide-spectrum match confidence.**

## Overview

Percolator re-scores search engine outputs to improve identification sensitivity while controlling false discovery rates.

## Key Features

- **PSM Rescoring**: Improves discrimination of true/false matches.
- **FDR Control**: Supports robust confidence estimation.
- **Search-Engine Agnostic**: Integrates with multiple upstream tools.
- **Cross-Platform**: Windows, Linux, macOS

## Installation

```bash
# Installation commands
# See official Percolator releases
```

## Usage

```r
# Example code
# Usually called in proteomics pipelines
```

## Input/Output

**Input:**
- Search engine PSM outputs
- Decoy/target annotations

**Output:**
- Re-scored PSM/peptide/protein confidence tables
- q-values and posterior scores

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| fdr_threshold | 0.01 | Acceptance threshold |
| feature_set | user-defined | Scoring feature configuration |

## Key Publications

> [!cite] Primary Reference
> Kall et al. (2007) *Nature Methods*

## Links

- GitHub:
- Documentation:

## Related Tools

- [[MSFragger]]
- [[MaxQuant]]
- [[Open-pFind]]
