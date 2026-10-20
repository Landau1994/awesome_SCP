---
title: PASEF
aliases:
  - PASEF
tags:
  - methods
category: method
url: https://pubmed.ncbi.nlm.nih.gov/30385480/
date_created: 2026-03-25
---

# PASEF

**Parallel Accumulation-Serial Fragmentation, an ion mobility-enhanced MS acquisition strategy.**

## Overview

PASEF improves sequencing speed and sensitivity by combining trapped ion mobility separation with efficient MS/MS fragmentation scheduling.

## Key Features

- **Ion Mobility Integration**: Adds an orthogonal separation dimension.
- **Higher Efficiency**: Increases MS/MS duty cycle.
- **Sensitivity Gain**: Beneficial for low-input proteomics.

## Workflow

```text
Ion accumulation → Mobility separation → Serial MS/MS fragmentation → Computational analysis
```

## Performance

The original work demonstrated gains in sequencing efficiency with mobility-synchronized precursor scheduling. Protein depth and completeness depend on sample, chromatography, accumulation settings and analysis; they are not fixed properties of the PASEF name.

## Advantages

- Better selectivity in complex mixtures
- Enhanced speed-sensitivity balance
- Compatible with advanced DIA variants

## Limitations

- Requires compatible instrument platforms
- Method setup can be non-trivial
- Analysis software must handle mobility dimension

## Key Publications

> [!cite] Primary Reference
> Meier F, Brunner AD, Koch S, et al. (2018). Online Parallel Accumulation–Serial Fragmentation (PASEF) with a Novel Trapped Ion Mobility Mass Spectrometer. *Molecular & Cellular Proteomics* 17, 2534–2545.
> [Primary publication record](https://pubmed.ncbi.nlm.nih.gov/30385480/)

## Related Methods

- [[diaPASEF]]
- [[diagonal-PASEF]]
- [[DIA]]

## Sources

- [Reference for PASEF](https://pubmed.ncbi.nlm.nih.gov/30385480/)
