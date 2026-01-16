# plexDIA

**Multiplexed Data-Independent Acquisition**

## Overview

plexDIA combines multiplexed sample labeling with data-independent acquisition (DIA) to dramatically increase throughput while maintaining high data completeness.

## Key Features

- **Non-isobaric Labels**: Uses mass tags that create mass shifts (mTRAQ, dimethyl, PSMtags)
- **DIA Acquisition**: All peptides fragmented systematically
- **High Completeness**: ~98% data completeness within a plexDIA set
- **Fast Analysis**: ~5 min active chromatography per cell

## Multiplexing Options

| Label | Plex | Notes |
|-------|------|-------|
| mTRAQ | 3-plex | Most common |
| Dimethyl | 2-3 plex | Cost-effective |
| PSMtags | Up to 9-plex | Newest option |

## Workflow

```
Single Cells → nPOP Preparation → Label with mTRAQ/dimethyl →
Pool 3 samples → DIA-MS → DIA-NN Analysis
```

## Performance

- **Proteins per cell**: ~1,000-3,000
- **Throughput**: 3x multiplier over label-free
- **Missing data**: <2% within plex sets

## Software

- **DIA-NN**: Primary analysis software with plexDIA module
- Supports spectral library and library-free search

## Advantages

- Higher throughput than SCoPE2
- Better data completeness than DDA
- MS1-level quantification (less ratio compression)

## Key Publications

- Derks et al. (2022) Nature Biotechnology

## Related Methods

- [[SCoPE2]] - TMT-based alternative
- [[nPOP]] - Compatible sample prep
- [[DIA-NN]] - Analysis software

## Tags

#methods #DIA #multiplexing #MS1
