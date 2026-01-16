# MaxQuant

**Quantitative Proteomics Software**

## Overview

MaxQuant is a comprehensive software platform for mass spectrometry-based proteomics developed by the Cox lab. It's widely used for TMT-based single-cell proteomics including SCoPE2.

## Key Features

- **Andromeda Search Engine**: Peptide identification
- **TMT/iTRAQ Support**: Isobaric label quantification
- **LFQ**: Label-free quantification
- **Match Between Runs**: Transfers IDs across samples
- **Protein Groups**: Handles protein inference

## SCoPE2 Analysis Settings

Key parameters for single-cell TMT data:
- Reporter ion quantification: TMTpro 16-plex
- MS/MS tolerance: 20 ppm
- Minimum peptide length: 7
- FDR: 1% at PSM and protein level

## Workflow

```
Raw Files → Andromeda Search →
Reporter Ion Extraction → Protein Quantification →
evidence.txt / proteinGroups.txt
```

## Output Files

| File | Description |
|------|-------------|
| evidence.txt | PSM-level data |
| peptides.txt | Peptide summaries |
| proteinGroups.txt | Protein-level data |
| msms.txt | MS/MS spectra info |

## Limitations for SCP

- Windows only
- Can be slow for large datasets
- Memory intensive
- Less optimal for DIA data

## Installation

Download from: https://www.maxquant.org/

## Key Publications

- Cox & Mann (2008) Nature Biotechnology

## Related Tools

- [[DIA-NN]] - For DIA data
- [[FragPipe]] - Faster alternative
- [[scp Package]] - Downstream analysis in R

## Tags

#tools #software #TMT #DDA #quantification
