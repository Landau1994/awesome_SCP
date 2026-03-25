---
title: RNA Velocity
aliases:
  - RNA Velocity
tags:
  - methods
category: method
url: 
date_created: 2026-03-25
---

# RNA Velocity

**A method to infer future cellular states from spliced and unspliced RNA dynamics.**

## Overview

RNA Velocity estimates directional trajectories in single-cell data and serves as a conceptual basis for protein-velocity approaches.

## Key Features

- **Directionality Inference**: Predicts near-future cell transitions.
- **Dynamic Interpretation**: Adds temporal context to static embeddings.
- **Trajectory Analysis Utility**: Complements pseudotime approaches.

## Workflow

```text
Quantify spliced/unspliced RNA → Fit kinetic model → Compute velocity vectors → Project on embedding
```

## Performance

- **Proteins per cell**: Not directly applicable
- **Throughput**: High (computational)
- **Data completeness**: Depends on RNA quantification quality

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
