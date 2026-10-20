---
title: Chip-Tip
aliases:
  - Chip-Tip
tags:
  - methods
category: method
url: https://www.nature.com/articles/s41592-024-02558-2
date_created: 2026-01-18
---

# Chip-Tip

**An integrated chip-to-Evotip sample-preparation workflow for sensitive single-cell proteomics.**

## Overview

Chip-Tip is the specific workflow described by Ye, Sabatier and colleagues in 2025. It combines cellenONE single-cell isolation, nanoliter preparation in proteoCHIP EVO 96, direct centrifugation-mediated transfer to Evotips, and sensitive LC–MS analysis. The principal deep-coverage benchmark used Evosep One with an Orbitrap Astral.

## Key Features

- **Low-Loss Processing**: Minimizes sample loss in ultralow-input handling.
- **Depth Improvement**: Increases detectable proteins per cell in optimized setups.
- **Scalable Operation**: Supports larger single-cell cohorts with automation-friendly steps.

## Workflow

```text
Single-cell capture -> Chip-Tip-assisted prep/cleanup -> LC-MS acquisition -> DIA/quantitative analysis
```

## Performance

- **Depth**: in the paper's HeLa benchmark, the 4-Th/6-ms nDIA method yielded a median of 5,204 protein identifications per cell.
- **Acquisition setting**: that comparison used the 40-samples-per-day Whisper workflow. The paper also evaluated 80 and 120 samples per day with different chromatographic settings; these settings should not be conflated with the deepest-coverage result.
- **Transferability**: cell size, preparation, gradient, instrument and analysis settings affect both identification depth and quantitative accuracy.

## Advantages

- Better sample recovery in tiny-volume workflows.
- Compatible with high-throughput short-gradient strategies.
- Practical route to deeper label-free SCP.

## Limitations

- Requires careful protocol tuning and hardware compatibility.
- Gains depend on end-to-end pipeline quality.
- Can increase workflow complexity versus simple prep methods.

## Key Publications

> [!cite] Primary Reference
> Ye Z, Sabatier P, van der Hoeven L, et al. (2025). Enhanced sensitivity and scalability with a Chip-Tip workflow enables deep single-cell proteomics. *Nature Methods* 22, 499–509.
> [10.1038/s41592-024-02558-2](https://doi.org/10.1038/s41592-024-02558-2)

## Related Methods

- [[SCoPE2]]
- [[plexDIA]]
- [[nPOP]]

## Sources

- [Reference for Chip-Tip](https://www.nature.com/articles/s41592-024-02558-2)
