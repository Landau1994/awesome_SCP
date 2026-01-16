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
---

# Cell Differentiation

**Studying Cellular Hierarchies with SCP**

## Overview

Single-cell proteomics enables direct measurement of protein abundance changes during cell differentiation, capturing post-transcriptional regulation invisible to transcriptomics.

## Key Studies

### Monocyte-Macrophage Differentiation
- **Method**: [[SCoPE2]]
- **Cells**: 1,490 single cells
- **Proteins**: 3,042 quantified
- **Finding**: Protein-RNA discordance during differentiation

### Stem Cell Differentiation
- Hematopoietic stem cells
- Embryonic stem cells
- iPSC differentiation

## Advantages Over scRNA-seq

| Aspect | SCP | scRNA-seq |
|--------|-----|-----------|
| Protein regulation | Direct | Indirect |
| PTMs | Possible | No |
| Functional state | Yes | Inferred |
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
> - Brunner et al. (2022) *Nature*
>   DOI: [10.1038/s41586-022-05426-1](https://doi.org/10.1038/s41586-022-05426-1)

## Related Topics

- [[Cancer Applications]] - Tumor hierarchies
- [[SCoPE2]] - Primary method used
- [[scp Package]] - Analysis workflow
