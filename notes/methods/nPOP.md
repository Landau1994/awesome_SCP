---
title: nPOP
aliases:
  - Nano-ProteOmic sample Preparation
  - nanoPOP
tags:
  - methods
  - sample-prep
  - automation
  - nanoliter
category: method
url: https://www.nature.com/articles/s41596-024-01033-8
---

# nPOP

**Nano-ProteOmic sample Preparation**

## Overview

nPOP is a massively parallel sample preparation method that enables processing thousands of single cells in nanoliter-volume droplets on glass slides.

## Key Features

- **Nanoliter Volumes**: reaction volume changes across dispensing, lysis, digestion and labeling steps; follow the protocol's step-specific volumes.
- **Parallel Processing**: Thousands of cells can be prepared in parallel in the reported workflow.
- **Flexible Design**: Compatible with multiple MS methods
- **Automation**: Implemented on CellenONE platform

## Workflow

```
1. Deposit DMSO droplets on fluorocarbon-coated slide
2. Dispense single cells into droplets
3. Add lysis/digestion reagents
4. Optional: Add TMT/mTRAQ labels
5. Collect with larger droplet into 384-well plate
6. Transfer to LC-MS
```

## Equipment Required

- **CellenONE**: Cell dispensing and droplet handling
- **Fluorocarbon-coated slides**: Reaction surface
- **Bravo liquid handler**: Sample collection (optional)

## Performance

- **Proteins identified**: The protocol reports about 3,000–3,700 proteins per human cell in a specific plexDIA implementation. Depth depends on the combined preparation, labeling, acquisition and analysis workflow; this is not an intrinsic property of nPOP.
- **Processing capacity**: Thousands of cells per preparation workflow; practical capacity depends on slide layout and dispensing/collection design.
- **Reproducibility**: assess quantitative precision and preparation quality using the protocol's controls and QuantQC workflow.

## Advantages

- Minimal sample loss
- No specialized consumables beyond slides
- Flexible experimental designs
- Scalable to very high throughput

## Limitations

- Requires CellenONE instrument
- Humidity control critical
- Learning curve for droplet handling

## Key Publications

> [!cite] Primary Reference
> Leduc et al. (2024) *Nature Protocols*
> DOI: [10.1038/s41596-024-01033-8](https://doi.org/10.1038/s41596-024-01033-8)

## Related Methods

- [[nanoPOTS]] - Chip-based alternative
- [[mPOP]] - Tube-based lysis method
- [[plexDIA]] - Often used together
- [[SCoPE2]] - Alternative labeling approach

## Sources

- [Reference for nPOP](https://www.nature.com/articles/s41596-024-01033-8)
