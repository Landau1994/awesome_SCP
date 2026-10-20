---
title: msImpute
aliases: ["MsImpute"]
tags:
  - tools
  - software
  - Bioconductor
category: tool
url: https://bioconductor.org/packages/msImpute/
date_created: 2026-10-20
---

# msImpute

## Overview

msImpute is an R/Bioconductor package for estimating missing peptide intensities in label-free quantitative proteomics. It includes diagnostics for missing-at-random (MAR) and missing-not-at-random (MNAR) patterns, low-rank approximation methods, and methods intended for MNAR data.

## Input and Use

Use a peptide-by-sample intensity matrix prepared as required by the chosen method, with missing values represented explicitly. The reference manual describes normalization/log transformation and filtering requirements; output is a completed matrix plus diagnostic information. Install with `BiocManager::install("msImpute")` in a compatible R/Bioconductor release.

## Limitations

Imputation assumptions must match the experiment. Compare distributions and downstream results before/after imputation; imputed values are estimates and do not increase experimentally observed coverage.

## Sources

- [Bioconductor package and documentation](https://bioconductor.org/packages/msImpute/) — definition, methods and installation checked 2026-10-20.
- [Original MsImpute paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10368900/).

## Related Tools

- [[MissForest]]
- [[scp Package]]
- [[limma]]
