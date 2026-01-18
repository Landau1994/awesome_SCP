---
title: Ultra-high sensitivity mass spectrometry quantifies single-cell proteome changes upon perturbation
authors:
  - Andreas-David Brunner
  - Marvin Thielert
  - Catherine Vasilopoulou
  - Constantin Ammar
  - Fabian Coscia
  - Andreas Mund
  - Ole B Hoerning
  - Nicolai Bache
  - Amalia Apalategui
  - Markus Lubeck
  - Sabrina Richter
  - David S Fischer
  - Oliver Raether
  - Melvin A Park
  - Florian Meier
  - Fabian J. Theis
  - Matthias Mann
aliases:
  - Ultra-high sensitivity mass spectrometry quantifies single-cell proteome changes upon perturbation
  - T-SCP paper
tags:
  - literature
  - paper
  - proteomics
  - single-cell
  - mass-spectrometry
category: literature
date_created: 2024-05-22
Journal: Molecular Systems Biology
Year: 2022
---

# Ultra-high sensitivity mass spectrometry quantifies single-cell proteome changes upon perturbation

## Citation

> [!cite] Reference
> **Title**：Ultra-high sensitivity mass spectrometry quantifies single-cell proteome changes upon perturbation
> **Authors**: Andreas-David Brunner, Marvin Thielert, Catherine Vasilopoulou, Constantin Ammar, Fabian Coscia, Andreas Mund, Ole B Hoerning, Nicolai Bache, Amalia Apalategui, Markus Lubeck, Sabrina Richter, David S Fischer, Oliver Raether, Melvin A Park, Florian Meier, Fabian J Theis, Matthias Mann
> **Year**: 2022
> **Journal**: Molecular Systems Biology
> **DOI**: 10.15252/msb.202110798

## Abstract

Single-cell technologies are currently dominated by imaging and sequencing, but proteins are the primary functional drivers of cells. This paper describes the development of a robust workflow (T-SCP: true single-cell-derived proteomics) combining miniaturized sample preparation, very low flow-rate chromatography, and a novel trapped ion mobility mass spectrometer (timsTOF SCP). The technology achieves a 10-fold improvement in sensitivity, allowing the quantification of proteomes in single FACS-isolated cells. By studying HeLa cells arrested at different cell cycle stages, the authors identified key regulators and predicted cell phases. A comparison of over 430 single-cell proteomes with transcriptomic data revealed a "stable-core" proteome despite perturbations, contrasted against a more stochastic transcriptome.

## Key Points

- **Technology Development**: Creation of the "T-SCP" workflow which utilizes a modified timsTOF mass spectrometer with enhanced ion transmission and a brighter ion source.
- **Sensitivity Increase**: Achieved a >10-fold increase in sensitivity, enabling the identification of ~1,000 to 2,000 proteins from a single HeLa cell.
- **Biological Insight**: Demonstrated that the proteome is significantly more stable and less prone to "shot noise" or stochasticity compared to the transcriptome at the single-cell level.
- **Cell Cycle Profiling**: Successfully classified single cells into G1, G1/S, G2, and G2/M phases based on their proteomic profiles.

## Methods

### Sample Preparation
- **Method used**: Miniaturized sample preparation in 384-well plates; cells were FACS-sorted into 1 μl lysis buffer. Proteins were digested with Trypsin/LysC. Peptides were concentrated in 20 nl nanopackages using EvoTip devices.
- **Chromatography**: Standardized nanoflow LC at 100 nl/min to maximize electrospray ionization efficiency.
- **Cell type**: HeLa cells (drug-perturbed with thymidine and nocodazole, and untreated).
- **Number of cells**: Primarily 1 cell per run (T-SCP), with benchmarks at 0, 2, and 6 cells. Analysis covered >430 single-cell proteomes.

### Data Analysis
- **Software**: MaxQuant (1.6.7.0) for DDA data; DIA-NN (1.8) for DIA data; Perseus (1.6.7.0) for downstream statistics.
- **Downstream**: SCANPY for cell cycle state prediction; Principal Component Analysis (PCA) for population grouping; Coefficient of Variation (CV) analysis for proteome vs. transcriptome comparison.

## Results

### Main Findings
1. **Hardware Optimization**: The modified mass spectrometer (timsTOF SCP) featured a brighter ion source and optimized ion optics, resulting in a 4.7-fold increase in ion transmission and a 3-fold increase in charge capacity.
2. **Proteome Coverage**: Using diaPASEF, the workflow quantified over 2,000 proteins per single cell and identified a total of over 2,500 proteins across the cell cycle population.
3. **Core Proteome Stability**: Identified a "core proteome" of ~200 proteins with very low variability (CV < 0.17) across hundreds of cells, whereas transcriptomic data for the same genes showed high stochastic variation.
4. **Functional Dynamics**: T-SCP correctly reflected the proliferation state (G2 cells being ~1.8-fold larger in protein mass than G1 cells) and identified known and novel cell cycle regulators (e.g., CDKN2A, STMN1).

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Principle of TIMS-qTOF and benchmarks showing linear response and sensitivity down to 0.8 ng HeLa digest. |
| Fig 2 | Comparison of standard vs. modified MS; protein counts from 1 to 6 cells; precursor isotope pattern at single-cell level. |
| Fig 3 | Miniaturized sample preparation workflow and signal increase from 100 nl/min nanoflow vs. 1 μl/min microflow. |
| Fig 4 | Analysis of drug-arrested cell cycle states; PCA and ROC curves for cell phase prediction; volcano plot of regulated proteins. |
| Fig 5 | Comparison of single-cell proteomics with scRNA-seq (Drop-seq and SMART-seq2), highlighting the stable core proteome. |

## Discussion

### Strengths
- **Unbiased Analysis**: Unlike antibody-based methods, MS-based proteomics provides an unbiased view of the detectable proteome.
- **Robustness**: Uses commercially available technologies (EvoSep, Bruker timsTOF), making it more accessible for community adoption.
- **High Sensitivity**: Overcomes the previous limitations of MS in single-cell analysis without requiring chemical multiplexing/booster channels.

### Limitations
- **Coverage**: While high for single cells, coverage is still significantly lower than bulk proteomics (~10,000+ proteins).
- **Throughput**: Currently at 40 single-cell measurements per day per instrument, which is lower than droplet-based sequencing methods.

### Future Work
- Application to post-translational modifications (PTMs), metabolites, and drugs at the single-cell level.
- Integration with clinical samples, such as FFPE pathology specimens and small cell counts from tissue material.

## Personal Notes

- The definition of a "core proteome" is a significant conceptual contribution, suggesting that protein levels are much more tightly regulated than mRNA levels in individual cells.
- The use of 100 nl/min flow rate is a critical technical detail for achieving the necessary ionization efficiency for single cells.

## Related Papers

- Budnik et al. (2018) SCoPE-MS: First major single-cell proteomics paper using TMT/booster channels.
- Schoof et al. (2021) and Tsai et al. (2020): Further developments in multiplexed single-cell proteomics.
- Meier et al. (2020): Introduction of diaPASEF, which is a key acquisition mode used here.