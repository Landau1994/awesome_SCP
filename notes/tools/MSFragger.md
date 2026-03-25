---
title: MSFragger
aliases:
  - MSFragger
tags:
  - tools
  - software
category: tool
url: 
date_created: 2026-03-25
---

# MSFragger

**A fast database search engine for peptide identification in high-throughput proteomics.**

## Overview

MSFragger is frequently used within FragPipe workflows and supports efficient peptide-spectrum matching across multiple search strategies.

## Key Features

- **High-Speed Search**: Optimized for large-scale MS datasets.
- **Flexible Search Modes**: Supports open and restricted searches.
- **Workflow Integration**: Commonly paired with FragPipe pipelines.
- **Cross-Platform**: Windows, Linux, macOS

## Installation

```bash
# Installation commands
# Available via FragPipe ecosystem
```

## Usage

```r
# Example code
# Usually configured through FragPipe
```

## Input/Output

**Input:**
- Raw/mzML MS files
- Protein FASTA

**Output:**
- PSM and peptide identification tables
- Search reports for downstream quantification

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| precursor_tol | user-defined | Precursor mass tolerance |
| fragment_tol | user-defined | Fragment mass tolerance |

## Key Publications

> [!cite] Primary Reference
> Kong et al. (2017) *Nature Methods*

## Links

- GitHub:
- Documentation:

## Related Tools

- [[FragPipe]]
- [[pFind3]]
- [[Open Search]]
