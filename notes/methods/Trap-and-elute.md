---
title: Trap-and-elute
aliases:
  - Trap-and-elute
tags:
  - methods
category: method
url: 
date_created: 2026-03-25
---

# Trap-and-elute

**A chromatography workflow using a trap column for loading/cleanup before analytical separation.**

## Overview

Trap-and-elute improves sample cleanup and concentration by first capturing peptides on a trap column and then eluting them to the analytical column for LC-MS.

## Key Features

- **On-line Cleanup**: Removes salts and contaminants before separation.
- **Sensitivity Support**: Improves low-input peptide handling.
- **Workflow Robustness**: Stabilizes injection and loading behavior.

## Workflow

```
Sample loading on trap column → Wash/desalt → Elute to analytical column → MS acquisition
```

## Performance

- **Proteins per cell**: Improved for low-input workflows
- **Throughput**: High with optimized gradients
- **Data completeness**: Better retention/reproducibility in many setups

## Advantages

- Better desalting and concentration
- Compatible with short-gradient high-throughput LC-MS
- Useful in SCP-level sample amounts

## Limitations

- Additional plumbing/method tuning needed
- Potential carryover if not optimized
- Performance depends on trap chemistry

## Key Publications

> [!cite] Primary Reference
> See trap-column optimization studies in literature notes.

## Related Methods

- [[nanoLC-MS]]
- [[DIA]]
- [[Label-free single-cell proteomics]]
