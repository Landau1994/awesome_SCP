---
title: WGCNA
aliases:
  - WGCNA
tags:
  - tools
  - software
category: tool
url: 
date_created: 2026-03-25
---

# WGCNA

**Weighted Gene Co-expression Network Analysis framework for module detection and trait association.**

## Overview

WGCNA identifies co-expression modules and links them to phenotypes, and is used in both transcriptomic and proteomic network analyses.

## Key Features

- **Module Discovery**: Detects co-regulated feature groups.
- **Trait Association**: Relates modules to phenotypes and covariates.
- **Network Perspective**: Highlights systems-level organization.
- **Cross-Platform**: Windows, Linux, macOS

## Installation

```bash
# Installation commands
# install.packages("WGCNA")
```

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

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| power | user-defined | Soft-thresholding power |
| min_module_size | user-defined | Minimum module size |

## Key Publications

> [!cite] Primary Reference
> Langfelder and Horvath (2008) *BMC Bioinformatics*

## Links

- GitHub:
- Documentation:

## Related Tools

- [[GSEA]]
- [[Scanpy]]
- [[Linear Mixed Models]]
