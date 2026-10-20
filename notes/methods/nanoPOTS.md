---
title: nanoPOTS
aliases:
  - Nanodroplet Processing in One pot for Trace Samples
  - Nested nanoPOTS
  - N2
tags:
  - methods
  - sample-prep
  - microfluidics
  - chip
category: method
url: https://www.nature.com/articles/s41467-018-03367-w
---

# nanoPOTS

**Nanodroplet Processing in One pot for Trace Samples**

## Overview

nanoPOTS is a chip-based microfluidic platform for processing ultra-low input samples including single cells. Developed at Pacific Northwest National Laboratory (PNNL).

## Key Features

- **Nanowell Chips**: Microfabricated arrays for sample processing
- **Nanoliter Reactions**: Minimizes surface losses
- **Integrated Workflow**: Lysis, digestion, and optional labeling on-chip

## Chip Versions

### Standard nanoPOTS
- Individual nanowells
- Chip capacity depends on layout; the 2021 comparison used a 44-well conventional nanoPOTS chip.

### Nested nanoPOTS (N2)
- 243 cells per chip
- Tenfold increase in sample-processing throughput reported for the 2021 N2 design; this is not a tenfold increase in MS acquisition speed.
- Hierarchical nanowell design

## Workflow

```
Single Cells → Dispense to Nanowells →
Lysis Buffer → Trypsin Digestion →
Direct injection or Collection → LC-MS/MS
```

## Performance

- **Sensitivity**: Picogram-level protein input
- **Original 2018 benchmark**: approximately 1,500–3,000 proteins from approximately 10–140 mammalian cells; these are small-population, not single-cell, results.
- **Recovery**: nanoliter processing reduces surface losses; recovery depends on the protocol and is not a universal >80% value.

## Advantages

- Excellent sensitivity
- Reduced sample loss vs tubes
- Reproducible processing
- Suitable for rare cells

## Limitations

- Specialized chip fabrication
- Lower throughput than [[nPOP]]
- Higher per-sample cost

## Key Publications

> [!cite] Primary References
> - Zhu et al. (2018) *Nature Communications* - Original nanoPOTS
>   DOI: [10.1038/s41467-018-03367-w](https://doi.org/10.1038/s41467-018-03367-w)
> - Woo et al. (2021). High-throughput and high-efficiency sample preparation for single-cell proteomics using a nested nanowell chip. *Nature Communications* 12, 6246.
>   DOI: [10.1038/s41467-021-26514-2](https://doi.org/10.1038/s41467-021-26514-2)

## Related Methods

- [[nPOP]] - Slide-based alternative
- [[mPOP]] - Simpler tube-based method

## Sources

- [Reference for nanoPOTS](https://www.nature.com/articles/s41467-018-03367-w)
