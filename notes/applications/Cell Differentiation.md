---
title: Cell Differentiation
aliases:
  - Cellular Differentiation
  - Developmental Proteomics
tags:
  - applications
  - differentiation
  - development
  - trajectories
category: application
url: https://doi.org/10.1186/s13059-021-02267-5
---

# Cell Differentiation

**Studying Cellular Hierarchies with SCP**

## Overview

Single-cell proteomics enables direct measurement of protein abundance changes during cell differentiation, capturing post-transcriptional regulation invisible to transcriptomics.

## Key Studies

### Monocyte-Macrophage Differentiation
- **Method**: [[SCoPE2]]
- **Cells**: 1,490 single cells
- **Proteins**: 3,042 across the 1,490-cell quantified matrix; not 3,042 measured in every cell
- **Finding**: Protein-RNA discordance during differentiation

### Stem Cell Differentiation
- Hematopoietic stem cells
- Embryonic stem cells
- iPSC differentiation

## Advantages Over scRNA-seq

| Aspect | SCP | scRNA-seq |
|--------|-----|-----------|
| Protein abundance | Measured for detected proteins | RNA-based inference |
| PTMs | Possible | No |
| Functional state | Inferred from measured proteins unless function is directly assayed | Inferred from RNA |
| Throughput | Lower | Higher |

## Analysis Approaches

### Trajectory Analysis
```
Cells → Dimensionality Reduction →
Pseudotime Ordering → Protein Dynamics
```

### Tools
- Monocle (adapted for protein)
- Palantir
- PAGA
- Diffusion maps

## Protein-RNA Discordance

> [!important] Key Finding
> Many proteins don't correlate with their mRNA due to:
> - Post-transcriptional regulation
> - Protein stability differences
> - Translation rate variation

## Applications

1. **Development biology**: Lineage decisions
2. **Regenerative medicine**: iPSC quality
3. **Immunology**: Immune cell states
4. **Aging**: Cellular senescence

## Key Publications

> [!cite] Primary References
> - Specht et al. (2021) *Genome Biology*
>   DOI: [10.1186/s13059-021-02267-5](https://doi.org/10.1186/s13059-021-02267-5)
> - Schoof et al. (2021) *Nature Communications*
>   DOI: [10.1038/s41467-021-23667-y](https://doi.org/10.1038/s41467-021-23667-y)

## Related Topics

- [[Cancer Applications]] - Tumor hierarchies
- [[SCoPE2]] - Primary method used
- [[scp Package]] - Analysis workflow

## Interpretation Limits

Pseudotime orders observed cell states; it is not direct lineage tracing or a measured time axis. RNA-derived trajectory tools require validation for the coverage, missingness and normalization of protein data. Routine abundance measurements do not automatically measure PTM occupancy or protein activity.

## Sources

- [Specht et al. (2021), SCoPE2](https://doi.org/10.1186/s13059-021-02267-5)
- [Schoof et al. (2021), cellular hierarchies](https://doi.org/10.1038/s41467-021-23667-y)
