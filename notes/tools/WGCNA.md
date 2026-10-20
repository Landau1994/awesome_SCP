---
title: WGCNA
aliases:
  - WGCNA
tags:
  - tools
  - software
category: tool
url: https://cran.r-project.org/package=WGCNA
date_created: 2026-03-25
---

# WGCNA

**Weighted Gene Co-expression Network Analysis framework for module detection and trait association.**

## Overview

WGCNA identifies co-expression modules and links them to phenotypes, and is used in both transcriptomic and proteomic network analyses.

## Key Features

- **Module Discovery**: Detects co-expressed feature groups; correlation alone does not establish common regulation.
- **Trait Association**: Relates modules to phenotypes and covariates.
- **Network Perspective**: Highlights systems-level organization.
- **Environment**: Follow the official release requirements; operating-system support depends on the package and its dependencies.

## Usage

```r
# Example code
library(WGCNA)
```

## Input/Output

**Input:**

- Normalized expression/intensity matrices
- Sample metadata

**Output:**

- Module assignments
- Eigengene-trait association results

## Key Publications

> [!cite] Primary Reference
> Langfelder et al. (2008). WGCNA: an R package for weighted correlation network analysis. *BMC Bioinformatics*.
> DOI: [10.1186/1471-2105-9-559](https://doi.org/10.1186/1471-2105-9-559)

## Links

- Source availability: See the official source below; no separate public repository was confirmed.
- Documentation/source: https://cran.r-project.org/package=WGCNA

## Related Tools

- [[GSEA]]
- [[Scanpy]]
- [[Linear Mixed Models]]

## Source Check

- Source checked on 2026-10-20: [WGCNA documentation or source](https://cran.r-project.org/package=WGCNA).
