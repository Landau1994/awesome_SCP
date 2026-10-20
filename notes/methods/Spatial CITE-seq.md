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
url: https://www.nature.com/articles/s41587-023-01676-0
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
Deterministic spatial barcoding with microfluidic channels → Library prep (RNA + ADT) →
Sequencing → Spatial deconvolution & integration
```

## Performance

- **Proteins**: Panel of surface proteins (DNA-barcoded antibody panel)
- **Spatial sampling**: Tissue sections are mapped to barcoded pixels; the study demonstrated 25-µm pixels with a 189-antibody mouse panel.
- **Readout design**: Protein and RNA measurements per spatial pixel; pixel composition and detection completeness require QC.

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
> Liu Y, DiStasio M, Su G, et al. (2023) *Nature Biotechnology* 41, 1405–1409
> DOI: [10.1038/s41587-023-01676-0](https://doi.org/10.1038/s41587-023-01676-0)

## Related Methods

- [[CITE-seq]] — Dissociation-based multi-omics; no spatial information
- [[Spatial Transcriptomics]] — RNA-only spatial profiling
- [[NEAT-seq]] — Nuclear protein + ATAC + RNA (non-spatial)

## Sources

- [Reference for Spatial CITE-seq](https://www.nature.com/articles/s41587-023-01676-0)
