---
title: FACS
aliases:
  - FACS
tags:
  - methods
category: method
url: 
date_created: 2026-03-25
---

# FACS

**Fluorescence-Activated Cell Sorting for isolating specific cell populations.**

## Overview

FACS is used to sort single cells or defined populations based on fluorescence markers before downstream single-cell proteomics workflows.

## Key Features

- **Marker-Based Isolation**: Selects cells using fluorescence signatures.
- **Single-Cell Compatible**: Enables controlled input for SCP pipelines.
- **High Specificity**: Supports purification of rare populations.

## Workflow

```text
Cell staining → Flow cytometry gating → Sorting into vessels/plates → Downstream preparation
```

## Performance

- **Proteins per cell**: Not directly applicable
- **Throughput**: High
- **Data completeness**: Depends on downstream MS workflow

## Advantages

- Precise selection of target populations
- Compatible with multiplexed marker strategies
- Widely established instrumentation/protocols

## Limitations

- Requires viable single-cell suspension quality
- Gating strategy can introduce bias
- Sorting stress may affect fragile cell states

## Key Publications

> [!cite] Primary Reference
> Widely used across SCP and multi-omics studies.

## Related Methods

- [[single-cell proteomics]]
- [[CITE-seq]]
- [[Laser Microdissection]]
