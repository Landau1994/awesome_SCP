---
title: Laser Microdissection
aliases:
  - Laser Microdissection
tags:
  - methods
category: method
url: 
date_created: 2026-03-25
---

# Laser Microdissection

**A method for isolating specific microscopic regions or cells from tissue sections.**

## Overview

Laser Microdissection enables targeted sampling from complex tissues, often used in spatial proteomics workflows.

## Key Features

- **Region-Specific Isolation**: Captures selected cells/structures.
- **Spatial Precision**: Preserves tissue-context-driven sampling logic.
- **MS Compatibility**: Suitable for downstream proteomics preparation.

## Workflow

```text
Tissue staining/imaging → ROI definition → Laser capture/dissection → Sample collection for LC-MS
```

## Performance

- **Proteins per cell**: Depends on captured material and workflow sensitivity
- **Throughput**: Moderate
- **Data completeness**: Improved by careful ROI selection

## Advantages

- Targets biologically meaningful microenvironments
- Reduces background from irrelevant tissue regions
- Integrates with image-guided pipelines

## Limitations

- Throughput lower than dissociation-based approaches
- Requires specialized instrumentation
- Sample handling losses can affect low-input depth

## Key Publications

> [!cite] Primary Reference
> See DVP/scDVP and spatial liver proteomics studies.

## Related Methods

- [[Deep Visual Proteomics]]
- [[scDVP]]
- [[Spatial proteomics]]
