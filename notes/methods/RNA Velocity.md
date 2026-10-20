---
title: RNA Velocity
aliases:
  - RNA Velocity
tags:
  - methods
category: method
url: https://www.nature.com/articles/s41586-018-0414-6
date_created: 2026-03-25
---

# RNA Velocity

**A method to infer future cellular states from spliced and unspliced RNA dynamics.**

## Overview

RNA Velocity estimates local RNA expression-change rates from spliced and unspliced RNA. Projected directions can inform trajectory hypotheses and motivate protein-velocity approaches, but do not directly measure time or establish lineage.

## Key Features

- **Directionality Inference**: Estimates local expression-change direction under a kinetic model; this is not a deterministic prediction of cell transitions.
- **Dynamic Interpretation**: Adds temporal context to static embeddings.
- **Trajectory Analysis Utility**: Complements pseudotime approaches.

## Workflow

```text
Quantify spliced/unspliced RNA → Fit kinetic model → Compute velocity vectors → Project on embedding
```

## Performance

Velocity vectors are model-based estimates from spliced/unspliced RNA measurements. Reliability depends on kinetic assumptions, gene selection and preprocessing; an embedding arrow is not a directly observed cell fate.

## Advantages

- Provides dynamic interpretation of lineage progression
- Useful for developmental and differentiation studies
- Integrates with common single-cell analysis pipelines

## Limitations

- Model assumptions may not hold in all systems
- Sensitive to preprocessing and parameter choices
- Requires careful biological interpretation

## Key Publications

> [!cite] Primary Reference
> La Manno et al. (2018) *Nature*

## Related Methods

- [[scProtVelo]]
- [[cellrank]]
- [[Scanpy]]

## Sources

- [Reference for RNA Velocity](https://www.nature.com/articles/s41586-018-0414-6)
