---
title: Spatial CITE-seq
aliases:
  - Spatial-CITE-seq
tags:
  - methods
  - multi-omics
  - single-cell
  - spatial
category: method
url: https://doi.org/10.1038/s41592-023-01809-2
date_created: 2026-03-17
---

# Spatial CITE-seq

**A spatially resolved multi-omics method that combines antibody-based protein quantification with spatially resolved transcriptomics, enabling simultaneous mapping of surface proteins and gene expression within tissue context.**

## Overview

Spatial CITE-seq extends the [[CITE-seq]] framework to tissue sections, enabling the joint measurement of surface protein abundance and transcriptomic profiles while preserving spatial information. By integrating DNA-barcoded antibodies with spatial transcriptomics platforms, it allows researchers to map protein and RNA co-expression patterns within the tissue microenvironment.

## Key Features

- **Spatial Resolution**: Protein and RNA measurements retain tissue spatial context
- **Multi-Modal**: Simultaneous surface protein and transcriptome profiling
- **Tissue Context**: Preserves microenvironment information lost in dissociation-based methods

## Workflow

```
Tissue sectioning → Antibody staining (DNA-barcoded) →
Spatial capture (slide-based) → Library prep (RNA + ADT) →
Sequencing → Spatial deconvolution & integration
```

## Performance

- **Proteins**: Panel of surface proteins (DNA-barcoded antibody panel)
- **Throughput**: Tissue section-level, spot-based resolution
- **Data completeness**: Dual readout per spatial spot

## Advantages

- Preserves tissue architecture and spatial relationships
- Enables study of protein-RNA co-regulation in situ
- Combinable with histological imaging

## Limitations

- Spatial resolution limited by capture spot size (not truly single-cell in all platforms)
- Antibody panel size restricted
- Requires specialized spatial transcriptomics instrumentation

## Key Publications

> [!cite] Primary Reference
> Liu Y, DiStasio M, Su G, et al. (2023) *Nature Methods* 20, 1078–1082
> DOI: [10.1038/s41592-023-01809-2](https://doi.org/10.1038/s41592-023-01809-2)

## Related Methods

- [[CITE-seq]] — Dissociation-based multi-omics; no spatial information
- [[Spatial Transcriptomics]] — RNA-only spatial profiling
- [[NEAT-seq]] — Nuclear protein + ATAC + RNA (non-spatial)
