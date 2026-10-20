---
title: Trap-and-elute
aliases:
  - Trap-and-elute
tags:
  - methods
category: method
url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13118651/
date_created: 2026-03-25
---

# Trap-and-elute

**A chromatography workflow using a trap column for loading/cleanup before analytical separation.**

## Overview

Trap-and-elute improves sample cleanup and concentration by first capturing peptides on a trap column and then eluting them to the analytical column for LC-MS.

## Key Features

- **On-line Cleanup**: Removes salts and contaminants before separation.
- **Low-Input Handling**: May support peptide loading; recovery must be evaluated for the chosen trap and sample.
- **Loading Design**: Separates trap loading from analytical-column elution.

## Workflow

```
Sample loading on trap column → Wash/desalt → Elute to analytical column → MS acquisition
```

## Performance

Trapping can support loading and desalting, particularly when injection volumes would otherwise impair separation. Recovery, carryover and depth depend on trap chemistry and loading/elution conditions; improvement over direct injection is not universal.

## Advantages

- Better desalting and concentration
- Compatible with short-gradient high-throughput LC-MS
- Useful in SCP-level sample amounts

## Limitations

- Additional plumbing/method tuning needed
- Potential carryover if not optimized
- Performance depends on trap chemistry

## Key Publications

[Trap-column optimization study](https://pmc.ncbi.nlm.nih.gov/articles/PMC13118651/), an experimental assessment of loading and low-input performance.

## Related Methods

- [[nanoLC-MS]]
- [[DIA]]
- [[Label-free single-cell proteomics]]

## Sources

- [Reference for Trap-and-elute](https://pmc.ncbi.nlm.nih.gov/articles/PMC13118651/)
