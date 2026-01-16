# SCoPE2

**Single Cell ProtEomics by Mass Spectrometry (Version 2)**

## Overview

SCoPE2 is a breakthrough method for quantifying proteins in single cells using mass spectrometry. It represents a major advancement over the original SCoPE-MS method.

## Key Features

- **TMT/TMTpro Labeling**: Uses isobaric mass tags for multiplexing
- **Carrier Channel**: Includes carrier cells (~200 cells) to boost peptide identification
- **Reference Channel**: Contains reference cells for normalization
- **Throughput**: ~100-200 cells per day per instrument

## Workflow

```
Single Cells → FACS/CellenONE Isolation → mPOP Lysis →
Trypsin Digestion → TMT Labeling → Pooling → LC-MS/MS
```

## Advantages

- Cost-effective (~$1-2 per cell)
- Scalable to thousands of cells
- Compatible with standard lab equipment
- Well-documented protocols

## Limitations

- Carrier channel can cause ratio compression
- Requires careful optimization of carrier ratio
- MS2-based quantification

## Key Publications

- Specht et al. (2021) Genome Biology - SCoPE2 method paper
- Slavov Lab Protocols: https://scp.slavovlab.net/protocols

## Related Methods

- [[pSCoPE]] - Prioritized targeting version
- [[plexDIA]] - Label-free DIA alternative
- [[nPOP]] - Sample preparation method

## Tags

#methods #TMT #isobaric #MS2
