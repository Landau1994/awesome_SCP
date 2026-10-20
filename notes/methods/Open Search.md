---
title: Open Search
aliases:
  - Open Search
tags:
  - methods
category: method
url: https://www.nature.com/articles/nmeth.4256
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

Runtime and identification yield depend on the search engine, database and allowed mass-shift range. An open search is a modification-discovery strategy, not a guarantee of more complete protein quantification.

## Advantages

- Detects unexpected modifications
- Reduces bias from predefined modification lists
- Expands interpretation space

## Limitations

- Increased search space and complexity
- Requires careful false-positive control
- Annotation of mass shifts can be ambiguous

## Key Publications

Kong et al. (2017). [MSFragger: ultrafast and comprehensive peptide identification in mass spectrometry–based proteomics](https://www.nature.com/articles/nmeth.4256).

## Related Methods

- [[Spectral Deconvolution]]
- [[Hybrid Spectral Library]]
- [[DIA]]

## Sources

- [Reference for Open Search](https://www.nature.com/articles/nmeth.4256)
