---
title: nDIA
aliases:
  - narrow-window DIA
  - 4Th6ms nDIA
tags:
  - methods
category: method
url: https://www.nature.com/articles/s41587-023-02099-7
date_created: 2026-01-18
---

# nDIA

**Narrow-window Data-Independent Acquisition**

## Overview

nDIA denotes narrow-window data-independent acquisition. In the 2024 Orbitrap Astral study, high-resolution MS1 scans were combined with approximately 200-Hz MS/MS acquisition and 2-Th isolation windows, principally for rapid bulk-proteome profiling. The later [[Chip-Tip]] single-cell workflow optimized a different setting: 4-Th windows with a 6-ms maximum injection time. Window width and injection time are experimental settings, not a universal definition of nDIA.

## Key Features

- **Narrow isolation windows** reduce the number of coisolated precursors and spectral interference.
- **Instrument speed and sensitivity** determine the feasible window width, ion accumulation time and cycle time.
- **Input-specific optimization** is required: the 2024 bulk study and 2025 single-cell study used different settings.

## Workflow

```text
Low-loss preparation → LC separation → Narrow-window DIA with input-appropriate settings → DIA analysis and error control
```

## Performance

- **2024 bulk study**: approximately 10,000 human protein groups in a 30-minute analysis; this is not a single-cell result.
- **2025 Chip-Tip benchmark**: 4-Th windows and 6-ms maximum injection time produced a median of 5,204 protein identifications per HeLa cell in the evaluated 40-samples-per-day setup.
- **PTMs**: direct detection without enrichment was demonstrated in that single-cell workflow. Coverage, identification transfer and quantitative reliability depend on the search and validation settings; the result is not a universal PTM detection guarantee.

## Advantages

- Reduced coisolation can improve selectivity.
- Fast MS/MS acquisition enables short gradients and dense precursor sampling.
- Sensitivity gains depend on the complete sample-preparation, LC, instrument and analysis workflow.

## Limitations

- **Hardware Dependency**: Narrow windows require acquisition speed and sensitivity appropriate to the intended experiment. The two studies discussed here used Orbitrap Astral; nDIA as a general acquisition concept is not exclusive to that model.
- **Data Complexity**: Generates dense data requiring advanced deconvolution algorithms (e.g., Spectronaut DirectDIA+ or DIA-NN).

## Key Publications

> [!cite] Bulk nDIA
> Guzman UH, Martinez-Val A, Ye Z, et al. (2024). Ultra-fast label-free quantification and comprehensive proteome coverage with narrow-window data-independent acquisition. *Nature Biotechnology* 42, 1855–1866.
> [10.1038/s41587-023-02099-7](https://doi.org/10.1038/s41587-023-02099-7)

> [!cite] Single-cell optimization
> Ye Z, Sabatier P, et al. (2025). Enhanced sensitivity and scalability with a Chip-Tip workflow enables deep single-cell proteomics. *Nature Methods* 22, 499–509.
> [10.1038/s41592-024-02558-2](https://doi.org/10.1038/s41592-024-02558-2)

## Related Methods

- [[SCoPE2]]
- [[plexDIA]]
- [[nPOP]]
- [[Chip-Tip]]

## Sources

- [Reference for nDIA](https://www.nature.com/articles/s41587-023-02099-7)
