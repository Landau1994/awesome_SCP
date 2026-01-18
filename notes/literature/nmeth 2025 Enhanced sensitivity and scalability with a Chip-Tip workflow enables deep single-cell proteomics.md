---
title: Enhanced sensitivity and scalability with a Chip-Tip workflow enables deep single-cell proteomics
authors:
  - Zilu Ye
  - Pierre Sabatier
  - Leander van der Hoeven
  - Maico Y. Lechner
  - Teeradon Phlairaharn
  - Ulises H. Guzman
  - Zhen Liu
  - Haoran Huang
  - Min Huang
  - Xiangjun Li
  - David Hartlmayr
  - Fabiana Izaguirre
  - Anjali Seth
  - Hiren J. Joshi
  - Sergey Rodin
  - Karl-Henrik Grinnemo
  - Ole B. Hørning
  - Dorte B. Bekker-Jensen
  - Nicolai Bache
  - Jesper V. Olsen
aliases:
   - <article>
   - <paper>
   - <literature>
tags:
  - literature
  - paper
  - proteomics
  - single-cell
  - PTMs
category: literature
date_created: 2025-05-22
Journal: Nature Methods
Year: 2025
---

# Enhanced sensitivity and scalability with a Chip-Tip workflow enables deep single-cell proteomics

## Citation

> [!cite] Reference
> **Title**：Enhanced sensitivity and scalability with a Chip-Tip workflow enables deep single-cell proteomics
> **Authors**: Zilu Ye, Pierre Sabatier, Leander van der Hoeven, Maico Y. Lechner, Teeradon Phlairaharn, Ulises H. Guzman, Zhen Liu, Haoran Huang, Min Huang, Xiangjun Li, David Hartlmayr, Fabiana Izaguirre, Anjali Seth, Hiren J. Joshi, Sergey Rodin, Karl-Henrik Grinnemo, Ole B. Hørning, Dorte B. Bekker-Jensen, Nicolai Bache & Jesper V. Olsen
> **Year**: 2025
> **Journal**: Nature Methods
> **DOI**: 10.1038/s41592-024-02558-2

## Abstract

Single-cell proteomics (SCP) aims to provide a granular view of the proteome in individual cells, but faces challenges in sensitivity and throughput. The authors present "Chip-Tip," a high-sensitivity SCP workflow that identifies >5,000 proteins in individual HeLa cells. The method utilizes the cellenONE platform for cell isolation, a proteoCHIP EVO 96 for nanoliter-scale sample preparation, and direct transfer to Evotip trap columns for analysis on an Orbitrap Astral mass spectrometer using narrow-window data-independent acquisition (nDIA). This workflow enables the direct detection of post-translational modifications (PTMs), such as phosphorylation and glycosylation, without enrichment. The study demonstrates the feasibility of processing up to 120 label-free SCP samples per day and applies the workflow to analyze drug-treated cancer cell spheroids and human-induced pluripotent stem cell (hiPSC) differentiation.

## Key Points

- **Deep Proteome Coverage**: Achieves identification of over 5,000 proteins and 40,000 peptides from a single HeLa cell, setting a new benchmark for label-free SCP.
- **PTM Detection without Enrichment**: Exceptional depth allows for the direct identification of phosphorylation (median 120 p-Ser, 28 p-Thr, 13 p-Tyr) and glycosylation patterns in single cells without specialized enrichment steps.
- **High Throughput and Scalability**: Demonstrates successful workflows for 40, 80, and 120 samples per day (SPD) while maintaining high sensitivity (>4,500 proteins at 120 SPD).
- **Application to Complex Systems**: Successfully used to profile heterogeneous cell populations in cancer spheroids (using a novel dissociation buffer) and hiPSC differentiation into multiple germ layers.

## Methods

### Sample Preparation
- **Method used**: Chip-Tip (one-pot preparation in nanoliter volumes).
- **Cell isolation**: cellenONE X1 platform for single-cell dispensing.
- **Chip**: proteoCHIP EVO 96 (polypropylene or Teflon) using a hexadecane oil layer to prevent evaporation.
- **Lysis/Digestion**: 0.2% DDM, 100 mM TEAB, Trypsin, and Lys-C.
- **Cleanup**: Direct transfer from chip to Evotip disposal trap columns via centrifugation.
- **Cell types**: HeLa, HCT116 (spheroids), hiPSCs (hi12), and HEK293T.
- **Number of cells**: Single cells, 10, 20, and 40 cell batches.

### Data Analysis
- **MS Instrument**: Orbitrap Astral mass spectrometer coupled with Evosep One LC.
- **Acquisition**: narrow-window DIA (nDIA) with various window settings (e.g., 4Th6ms).
- **Software**: Spectronaut (v.18/19) using directDIA+; DIA-NN (v.1.9) with match-between-run (MBR).
- **Downstream**: GO enrichment (Clusterprofiler), PTM site localization (Spectronaut), and FDR benchmarking via entrapment database strategies.

## Results

### Main Findings
1. **Optimization of nDIA**: Determined that 4-Th DIA windows and 6-ms injection times (4Th6ms) provided the highest proteome coverage for single cells.
2. **Carrier Proteome Effect**: Systematic evaluation showed that using a carrier proteome (e.g., 20-cell samples) significantly increases protein IDs in single-cell files by enabling the identification of lower-abundance proteins.
3. **PTM Profiling**: Quantified 168 protein kinases and identified hundreds of phosphorylation sites and multiple glycosylation pathways (e.g., O-GlcNAc, NeuAc) directly from single cells.
4. **Biological Insights**: Consistently quantified low-abundance stem cell markers (OCT4, SOX2) and lineage-specific markers (GATA4, HAND1, MAP2) in hiPSC-derived embryoid bodies.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Schematic of Chip-Tip workflow and benchmark protein/peptide IDs across different nDIA settings and cell counts. |
| Fig 2 | Evaluation of carrier proteome effects and search strategies (Spectronaut vs. DIA-NN) on protein identification and quantification. |
| Fig 3 | Performance of high-throughput methods (80 and 120 SPD) and the effect of FAIMS interface on sensitivity. |
| Fig 4 | Kinome tree representation and direct PTM profiling (phosphorylation and glycosylation) in single cells. |
| Fig 5 | Impact of 5-FU drug treatment on cancer spheroids, showing metabolic pathway alterations and GO term enrichment. |
| Fig 6 | Single-cell analysis of hiPSC differentiation into embryoid bodies, highlighting lineage-specific marker quantification. |

## Discussion

### Strengths
- **Lossless Workflow**: Integration of nanoliter-scale preparation with direct-to-tip transfer minimizes peptide loss.
- **High Sensitivity**: Utilization of the Orbitrap Astral allows for unprecedented depth in label-free SCP.
- **Robustness**: Validated across multiple cell types and biological contexts (spheroids, differentiation).
- **Accessibility**: Demonstrated performance on various commercial MS platforms (Orbitrap Astral, Fusion Lumos, timsTOF Ultra).

### Limitations
- **MS Throughput**: Currently capped at 120 SPD, which remains a bottleneck compared to single-cell RNA-seq.
- **PTM Quantification**: While identification is possible, the entire dynamic range of modified peptides is not yet fully quantitative.
- **Adsorption**: Surface adsorption and buffer evaporation still require meticulous control despite the oil-layer innovation.

### Future Work
- **Multiplexing**: Integration of nDIA with multiplexed approaches (e.g., TMT, plexDIA) to exponentially increase throughput.
- **Multi-omics**: Combining Chip-Tip SCP with single-cell genomic and transcriptomic measurements for a holistic view of cellular states.
- **Hardware Optimization**: Further refinement of chip materials and processing volumes to enhance sensitivity.

## Personal Notes

- The ability to detect PTMs without enrichment is a significant breakthrough for SCP, as enrichment is usually impossible at the single-cell level due to material loss.
- The "one-pot" nature of the proteoCHIP EVO 96 combined with Evosep's "Whisper" methods provides a very streamlined path from cell to data.

## Related Papers

- Li, Z.-Y. et al. (2018) Nanoliter-scale oil-air-droplet chip-based single cell proteomic analysis. *Anal. Chem.*
- Brunner, A. D. et al. (2022) Ultra-high sensitivity mass spectrometry quantifies single-cell proteome changes upon perturbation. *Mol. Syst. Biol.*
- Guzman, U. H. et al. (2024) Ultra-fast label-free quantification and comprehensive proteome coverage with narrow-window data-independent acquisition. *Nat. Biotechnol.*