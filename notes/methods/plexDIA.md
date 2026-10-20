---
title: plexDIA
aliases:
  - Multiplexed DIA
  - plexed DIA
tags:
  - methods
  - DIA
  - multiplexing
  - MS1
category: method
url: https://www.nature.com/articles/s41587-022-01389-w
---

# plexDIA

**Multiplexed data-independent acquisition using non-isobaric mass tags.**

## Overview

plexDIA combines mass-offset labeling with [[DIA]] so peptides from multiple samples can be analyzed together. Its analysis extracts sample-specific precursor and fragment evidence; it is not solely an MS1 quantification method.

## Key Features

- **Non-isobaric labeling**: channels remain distinguishable by mass offsets.
- **Multiplexed DIA**: selected isolation windows sample the configured precursor range.
- **Within-plex comparison**: co-analysis can improve completeness between the samples in a multiplex; this does not guarantee completeness across all runs.

## Multiplexing Options

| Label | Reported design | Scope |
|---|---|---|
| mTRAQ | 3-plex | Original Derks et al. plexDIA study |
| Dimethyl | 3 channels | Related multiplex-DIA study with a reference channel; a distinct labeling design |
| PSMtags | 9-plex | Later extension described by the developers; not a result of the original 2022 study |

## Workflow

```text
Single-cell preparation (for example nPOP) → Label separate samples → Pool labeled channels → DIA-MS → Multiplex-aware analysis
```

## Performance

In the original study, individual human cells yielded approximately 1,000 proteins per cell, with approximately 98% completeness **within a plexDIA set** and approximately 5 minutes of active chromatography per cell after multiplexing. These figures describe that experiment, not all cell types or later implementations. Active chromatography per cell is not the same as total instrument run time.

Later [[nPOP]] implementations report deeper coverage under different conditions. Multiplexing increases samples measured per acquisition, but achieved throughput and accuracy depend on labeling, acquisition, chromatography and analysis. There is no universal throughput ranking against [[SCoPE2]].

## Software

- [[DIA-NN]] supports multiplex-aware analysis.
- Search-library choices and channel-specific error control should be reported for each implementation.

## Advantages and Limitations

Co-analyzing labeled samples can improve throughput and matched measurements. Non-isobaric labels distinguish channels at the precursor/fragment level, but interference, incomplete labeling and detection limits still affect accuracy. Comparisons to reporter-ion methods require matched experimental conditions.

## Key Publications

- Derks et al. *Increasing the throughput of sensitive proteomics by plexDIA*. Online 2022; *Nature Biotechnology* 41, 50–59 (2023). [DOI: 10.1038/s41587-022-01389-w](https://www.nature.com/articles/s41587-022-01389-w).
- *Robust dimethyl-based multiplex-DIA doubles single-cell proteome depth via a reference channel* (2023). [DOI: 10.15252/msb.202211503](https://pmc.ncbi.nlm.nih.gov/articles/PMC10495816/).
- [PSMtags developer page](https://www.parallelsq.org/psmtags), including the later nine-channel extension.

## Related Methods

- [[SCoPE2]]
- [[nPOP]]
- [[DIA-NN]]
