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
url: https://scp.slavovlab.net/nPOP
---

# nPOP

**Nano-ProteOmic sample Preparation**

## Overview

nPOP is a massively parallel sample preparation method that enables processing thousands of single cells in nanoliter-volume droplets on glass slides.

## Key Features

- **Nanoliter Volumes**: 8-20 nL reaction volumes per cell
- **Parallel Processing**: >3,000 cells simultaneously
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

- **Proteins identified**: 3,000-3,700 per human cell
- **Processing capacity**: >3,000 cells per batch
- **Reproducibility**: High CV consistency

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
> DOI: [10.1038/s41596-024-01000-z](https://doi.org/10.1038/s41596-024-01000-z)

## Related Methods

- [[nanoPOTS]] - Chip-based alternative
- [[mPOP]] - Tube-based lysis method
- [[plexDIA]] - Often used together
- [[SCoPE2]] - Alternative labeling approach
