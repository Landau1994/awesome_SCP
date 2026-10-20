---
title: Single-sample GSEA
aliases:
- ssGSEA
- single sample GSEA
tags:
- methods
category: method
url: https://doi.org/10.1038/nature08460
date_created: '2026-10-20'
---

# Single-sample GSEA

## Overview

Single-sample gene set enrichment analysis (ssGSEA) assigns a score to a gene set within each sample from the ranks of its measured features. The scores summarize relative enrichment of the set and can be compared or modeled downstream.

ssGSEA is mathematically distinct from phenotype-comparison [[GSEA]]. A score is not by itself a pathway-activity measurement or a significance test. In proteomics, identifier mapping, set coverage, normalization and missing values need particular attention.

## Sources

- Barbie et al. (2009), *Systematic RNA interference reveals that oncogenic KRAS-driven cancers require TBK1*. [10.1038/nature08460](https://doi.org/10.1038/nature08460).
- [GSEA-MSigDB documentation on ssGSEA versus standard GSEA](https://docs.gsea-msigdb.org/GSEA/GSEA_and_RNA-Seq/).

## Related Methods

- [[GSEA]]
- [[GSVA]]
- [[Protein Set Enrichment Analysis (PSEA)]]
