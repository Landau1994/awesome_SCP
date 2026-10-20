---
title: Spatial Transcriptomics
aliases:
  - ST
  - spatially resolved transcriptomics
tags:
  - methods
  - spatial
  - transcriptomics
category: method
url: https://doi.org/10.1126/science.aaf2403
date_created: 2026-03-17
---

# Spatial Transcriptomics

**A family of technologies that measure gene expression while preserving spatial information within tissue sections, enabling the study of transcriptomic heterogeneity in the context of tissue architecture.**

## Overview

Spatial transcriptomics encompasses a broad range of methods (Visium, MERFISH, seqFISH, Slide-seq, HDST, etc.) that profile gene expression in situ. Unlike dissociation-based scRNA-seq, these methods retain the physical location of each measurement, revealing how gene expression varies across tissue microenvironments. The original Spatial Transcriptomics method was developed by Ståhl et al. (2016) using arrayed oligo-dT capture probes on glass slides.

## Key Features

- **Spatial Resolution**: Gene expression mapped to tissue coordinates (spot-based or subcellular)
- **Tissue Context**: Preserves microenvironment, cell-cell interactions, and tissue architecture
- **Diverse Platforms**: Sequencing-based (Visium, Slide-seq) and imaging-based (MERFISH, seqFISH+)

## Workflow

```
Tissue sectioning → Slide mounting → Permeabilization/Hybridization →
Capture/Imaging → Library prep or direct readout →
Sequencing/Imaging → Spatial data analysis
```

## Performance

- **Genes**: Broad transcriptome sampling or targeted panels, depending on the specific sequencing or imaging technology.
- **Resolution**: Platform- and analysis-dependent; capture spot size, optical localization precision and effective cell-level resolution are distinct quantities.
- **Throughput**: Depends on platform, tissue area, assay design and multiplexing.

## Advantages

- Preserves spatial relationships and tissue architecture
- Reveals spatial associations that can motivate hypotheses about cell communication and microenvironment effects.
- Complementary to dissociation-based single-cell methods

## Limitations

- Trade-off between spatial resolution and gene coverage
- Spatial pixels may contain multiple cells; whether segmentation or deconvolution is needed depends on resolution and tissue morphology.
- Requires tissue sectioning and specialized platforms

## Key Publications

> [!cite] Primary Reference
> Ståhl PL, Salmén F, Vickovic S, et al. (2016) *Science* 353(6294), 78–82
> DOI: [10.1126/science.aaf2403](https://doi.org/10.1126/science.aaf2403)

## Related Methods

- [[Spatial CITE-seq]] — Adds protein quantification to spatial transcriptomics
- [[CITE-seq]] — Dissociation-based protein + RNA (non-spatial)
- [[SCoPE2]] — Mass-spectrometry-based single-cell proteomics
