---
title: Top-down proteomics
authors:
  - David S. Roberts
  - Joseph A. Loo
  - Yury O. Tsybin
  - Xiaowen Liu
  - Si Wu
  - Julia Chamot-Rooke
  - Jeffrey N. Agar
  - Ljiljana Paša-Tolić
  - Lloyd M. Smith
  - Ying Ge
aliases:
   - Top-down proteomics Primer
tags:
  - literature
  - paper
  - proteomics
  - mass-spectrometry
category: literature
date_created: 2024-05-22
Journal: Nature Reviews Methods Primers
Year: 2024
---

# Top-down proteomics

## Citation

> [!cite] Reference
> **Title**: Top-down proteomics
> **Authors**: David S. Roberts, Joseph A. Loo, Yury O. Tsybin, Xiaowen Liu, Si Wu, Julia Chamot-Rooke, Jeffrey N. Agar, Ljiljana Paša-Tolić, Lloyd M. Smith & Ying Ge
> **Year**: 2024
> **Journal**: Nature Reviews Methods Primers
> **DOI**: https://doi.org/10.1038/s43586-024-00318-2

## Abstract

Proteoforms, which arise from post-translational modifications, genetic polymorphisms and RNA splice variants, play a pivotal role as drivers in biology. Understanding proteoforms is essential to unravel the intricacies of biological systems and bridge the gap between genotypes and phenotypes. By analysing whole proteins without digestion, top-down proteomics (TDP) provides a holistic view of the proteome and can decipher protein function, uncover disease mechanisms and advance precision medicine. This Primer explores TDP, including the underlying principles, recent advances and an outlook on the future. The experimental section discusses instrumentation, sample preparation, intact protein separation, tandem mass spectrometry techniques and data collection. The results section looks at how to decipher raw data, visualize intact protein spectra and unravel data analysis. Additionally, proteoform identification, characterization and quantification are summarized, alongside approaches for statistical analysis. Various applications are described, including the human proteoform project and biomedical, biopharmaceutical and clinical sciences.

## Key Points

- **Holistic Analysis**: Unlike bottom-up proteomics (BUP), TDP analyzes intact proteins, preserving the connectivity between different post-translational modifications (PTMs) and sequence variations on a single molecule.
- **Proteoform Resolution**: TDP is the only technology capable of unambiguously identifying and quantifying "proteoforms"—the specific molecular forms of a protein product from a single gene.
- **Technological Pillars**: The field relies on three main areas: front-end sample preparation/separation, high-resolution tandem mass spectrometry (MS/MS), and specialized informatics for deconvolution and database searching.
- **Biomedical Impact**: Crucial for studying complex diseases (cancer, cardiovascular, neurodegenerative) where specific proteoform ratios (e.g., cardiac troponin I phosphorylation) serve as biomarkers.

## Methods

### Sample Preparation
- **Method used**: Solubilization using MS-compatible surfactants (e.g., the photocleavable surfactant "Azo") or traditional reagents followed by rigorous cleanup (ultracentrifugation, SEC spin columns).
- **Fractionation**: Intact proteins are separated using Reversed-Phase LC (RPLC), Size Exclusion Chromatography (SEC), Hydrophobic Interaction Chromatography (HIC), Ion-Exchange (IEX), or Capillary Electrophoresis (CE).
- **Controls**: Standardized mixtures (e.g., ubiquitin, myoglobin, carbonic anhydrase) are used for performance benchmarking.

### Data Analysis
- **Software**: Deconvolution tools (e.g., MASH Explorer, ProSight, TopFD, FLASHDeconv) to convert isotopic envelopes into monoisotopic masses.
- **Database Searching**: Identification via Proteoform Spectrum Matches (PrSMs) using tools like TopPIC, MSPathFinder, and Informed-Proteomics.
- **Quantification**: Label-free (intensity-based), metabolic labeling (SILAC/NeuCode), or chemical labeling (TMT).

## Results

### Main Findings
1. **Human Proteoform Project**: TDP has enabled the identification of ~30,000 unique proteoforms across 21 cell types, far exceeding the number of human genes (~20,000).
2. **Clinical Utility**: TDP accurately identifies hemoglobin variants in blood for diabetes and blood disorder diagnosis and can distinguish endogenous M-proteins from therapeutic monoclonal antibodies (mAbs).
3. **Biopharmaceutical Application**: TDP is superior for determining Drug-to-Antibody Ratios (DAR) and site-specific drug localization in Antibody-Drug Conjugates (ADCs).

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Illustrates the "Revised Central Dogma" and compares the TDP approach (intact proteins) with BUP (peptide digests). |
| Fig 2 | Outlines the three pillars of TDP: Sample preparation/separation, MS1/MS2 analysis, and Data processing. |
| Fig 3 | Details surfactant-aided sample preparation and various chromatography/electrophoresis fractionation strategies. |
| Fig 4 | Summarizes tandem MS techniques including fragmentation methods (CID, IRMPD, ECD/ETD, UVPD) and ion nomenclature. |
| Fig 5 | Shows the relationship between protein size and MS signal-to-noise (S/N) and the complexity of isotopic distributions. |
| Fig 6 | Overview of quantification methods: Label-free, metabolic, and chemical labeling. |
| Fig 7 | Showcases applications in neurodegenerative disease, cancer (KRAS4b), cardiovascular disease (cTnI), and ADCs. |

## Discussion

### Strengths
- Provides a "complete" view of the protein molecule.
- High accuracy in PTM localization and combinatorial PTM mapping.
- Essential for biopharmaceutical characterization (mAbs, ADCs).

### Limitations
- **Sensitivity**: Requires higher sample amounts (micrograms) compared to BUP (nanograms).
- **Large Proteins**: S/N decreases exponentially as protein mass increases; identification of proteins >30 kDa remains challenging.
- **Data Complexity**: High-resolution spectra require sophisticated, often non-automated, deconvolution and manual validation.

### Future Work
- **Single-cell TDP**: Developing nano-POTS and ultra-sensitive CE-MS to analyze proteoforms in individual cells.
- **Spatial Proteomics**: Integrating TDP with mass spectrometry imaging.
- **Human Proteoform Atlas**: Completing a definitive set of reference proteoforms for the entire human proteome.

## Personal Notes
- This paper is a comprehensive "Primer" and serves as an excellent entry point for researchers new to the top-down field. 
- The distinction between "monoisotopic mass" and "average mass" for large proteins (Fig 5) is a critical technical takeaway.

## Related Papers
- Smith, L. M. & Kelleher, N. L. "Proteoforms as the next proteomics currency." *Science* (2018).
- Tran, J. C. et al. "Mapping intact protein isoforms in discovery mode using top-down proteomics." *Nature* (2011).