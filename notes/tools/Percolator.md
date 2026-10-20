---
title: Percolator
aliases:
  - Percolator
tags:
  - tools
  - software
category: tool
url: https://github.com/percolator/percolator
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
- **Environment**: Follow the official release requirements; operating-system support depends on the package and its dependencies.

## Input/Output

**Input:**

- Search engine PSM outputs
- Decoy/target annotations

**Output:**

- Re-scored PSM/peptide/protein confidence tables
- q-values and posterior scores

## Key Publications

> [!cite] Primary Reference
> Käll et al. (2007). Semi-supervised learning for peptide identification from shotgun proteomics datasets. *Nature Methods*.
> DOI: [10.1038/nmeth1113](https://doi.org/10.1038/nmeth1113)

## Links

- GitHub: https://github.com/percolator/percolator
- Documentation/source: https://github.com/percolator/percolator

## Related Tools

- [[MSFragger]]
- [[MaxQuant]]
- [[Open-pFind]]

## Source Check

- Source checked on 2026-10-20: [Percolator documentation or source](https://github.com/percolator/percolator).
