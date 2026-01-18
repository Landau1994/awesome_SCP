---
title: nDIA
aliases:
  - narrow-window DIA
  - 4Th6ms nDIA
tags:
  - methods
category: method
url: 
date_created: 2026-01-18
---

# nDIA

**Narrow-window Data-Independent Acquisition**

## Overview

nDIA is a label-free mass spectrometry acquisition strategy optimized for the **Orbitrap Astral** instrument. By utilizing the high sequencing speed and sensitivity of the Astral analyzer, this method employs significantly narrower isolation windows compared to traditional DIA. This reduction in window size minimizes spectral complexity and interference (chimericity), which is critical for analyzing low-input samples such as single cells.

## Key Features

- **Narrow Isolation Window**: Utilizes a **4 Th** window to isolate precursors, improving specificity and reducing co-elution interference.
- **Short Injection Time**: Optimized at **6 ms** to allow for rapid cycling and high scan rates necessary to cover the mass range with narrow windows.
- **Hardware Optimization**: Specifically designed to leverage the >100 Hz scan speed and high sensitivity of the Orbitrap Astral.

## Workflow

```
Single Cell Lysis (Chip-Tip) → Tryptic Digestion → Orbitrap Astral (nDIA 4Th6ms) → Analysis (Spectronaut/DIA-NN)
```

## Performance

- **Proteins per cell**: >5,000 (identified in single HeLa cells).
- **Peptides per cell**: >40,000.
- **PTM Detection**: Capable of detecting phosphopeptides and glycopeptides without specific enrichment.

## Advantages

- **Deep Coverage**: Achieves proteome depth previously difficult to attain in single cells (approx. 50% of the bulk proteome).
- **Sensitivity**: High ion transmission efficiency suitable for nanogram-level inputs.
- **Versatility**: Can identify post-translational modifications (PTMs) directly from single-cell data.

## Limitations

- **Hardware Dependency**: Requires the high speed and sensitivity of the Orbitrap Astral mass spectrometer.
- **Data Complexity**: Generates dense data requiring advanced deconvolution algorithms (e.g., Spectronaut DirectDIA+ or DIA-NN).

## Key Publications

> [!cite] Primary Reference
> 1.  [[nbt 2024 Ultra-fast label-free quantification and comprehensive proteome covergae]],Mass spectrometry (MS)-based proteomics aims to characterize comprehensive proteomes in a fast and reproducible manner. The authors present a **narrow-window data-independent acquisition (nDIA)** strategy. Using a quadrupole Orbitrap mass spectrometer paired with the asymmetric track lossless (**Astral**) analyzer, they achieve >200-Hz MS/MS scanning speeds with 2-Th isolation windows. This approach dissolves the traditional differences between data-dependent (DDA) and data-independent (DIA) methods. The strategy allows for profiling >100 yeast proteomes or 48 human proteomes per day, reaching depths of ~10,000 human protein groups in 30 minutes.
> 2. Hartlmayr et al. (2025) *Nature Methods* [[nmeth 2025 Enhanced sensitivity and scalability with a Chip-Tip workflow enables deep single-cell proteomics]]

## Related Methods

- [[SCoPE2]]
- [[plexDIA]]
- [[nPOP]]
- [[Chip-Tip]]
