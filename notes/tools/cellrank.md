---
title: cellrank
aliases: ["CellRank"]
tags:
  - tools
  - software
category: tool
url: https://cellrank.readthedocs.io/en/stable/
date_created: 2026-03-25
---

# cellrank

**A toolkit for probabilistic fate mapping and trajectory inference in single-cell data.**

## Overview

cellrank estimates cell-state transition probabilities and terminal fates using graph-based and velocity-informed models.

## Key Features

- **Fate Probability Estimation**: Quantifies lineage commitment likelihoods.
- **Trajectory Integration**: Works with pseudotime and velocity information.
- **Single-Cell Focus**: Supports developmental and differentiation analyses.
- **Environment**: Follow the official release requirements; operating-system support depends on the package and its dependencies.

## Input/Output

**Input:**

- Single-cell embedding/graph
- Optional velocity or transition priors

**Output:**

- Fate probabilities
- Absorption/lineage statistics

## Key Publications

> [!cite] Primary Reference
> Lange et al. (2022). CellRank for directed single-cell fate mapping. *Nature Methods*.
> DOI: [10.1038/s41592-021-01346-6](https://doi.org/10.1038/s41592-021-01346-6)

## Links

- Source availability: See the official source below; no separate public repository was confirmed.
- Documentation/source: https://cellrank.readthedocs.io/en/stable/

## Related Tools

- [[Scanpy]]
- [[RNA Velocity]]
- [[scProtVelo]]

## Source Check

- Source checked on 2026-10-20: [cellrank documentation or source](https://cellrank.readthedocs.io/en/stable/).
