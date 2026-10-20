---
title: GSEA
aliases:
  - GSEA
tags:
  - methods
category: method
url: https://doi.org/10.1073/pnas.0506580102
date_created: 2026-03-25
---

# GSEA

**Gene Set Enrichment Analysis for pathway-level interpretation of ranked molecular signatures.**

## Overview

GSEA evaluates whether predefined gene/protein sets are enriched at the top or bottom of ranked differential profiles.

## Key Features

- **Pathway-Level Analysis**: Moves beyond single-feature significance.
- **Rank-Based Statistic**: Uses continuous effect information.
- **Biological Interpretation**: Supports mechanistic hypothesis generation.

## Workflow

```text
Generate ranked feature list → Evaluate enrichment score per gene set → Permutation testing → FDR correction
```

## Performance

Results depend on the ranking metric, gene identifiers, gene-set definition and permutation scheme. GSEA tests enrichment in the measured data; it does not increase molecular detection completeness.

## Advantages

- Robust to modest per-feature effects
- Biologically interpretable outputs
- Standard in omics downstream analysis

## Limitations

- Gene-set quality influences conclusions
- Can miss novel pathways not in databases
- Requires careful multiple-testing interpretation

## Key Publications

> [!cite] Primary Reference
> Subramanian et al. (2005) *PNAS*

## Related Methods

- [[WGCNA]]
- [[Linear Mixed Models]]
- [[Pathview]]

## Sources

- [Reference for GSEA](https://doi.org/10.1073/pnas.0506580102)
