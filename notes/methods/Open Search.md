---
title: Open Search
aliases:
  - Open Search
tags:
  - methods
category: method
url: 
date_created: 2026-03-25
---

# Open Search

**A search strategy using wide precursor mass tolerances to discover unexpected modifications.**

## Overview

Open Search allows peptide identification without predefining all possible modifications, making it suitable for modification discovery and exploratory proteomics.

## Key Features

- **Wide Mass Tolerance**: Captures unknown mass shifts.
- **Modification Discovery**: Finds unanticipated PTMs/artifacts.
- **Hypothesis Generation**: Useful in exploratory datasets.

## Workflow

```
MS/MS data → Open search engine → Mass shift clustering → Annotation/validation
```

## Performance

- **Proteins per cell**: Dataset-dependent
- **Throughput**: Moderate to high (engine-dependent)
- **Data completeness**: Good for discovery workflows

## Advantages

- Detects unexpected modifications
- Reduces bias from predefined modification lists
- Expands interpretation space

## Limitations

- Increased search space and complexity
- Requires careful false-positive control
- Annotation of mass shifts can be ambiguous

## Key Publications

> [!cite] Primary Reference
> See OpenSpec and related literature notes.

## Related Methods

- [[Spectral Deconvolution]]
- [[Hybrid Spectral Library]]
- [[DIA]]
