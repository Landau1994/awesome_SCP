---
title: LFQ Benchmark Dataset - Generation Beta Assessing Modern Proteomics Instruments and Acquisition Workflows with High-Throughput LC Gradients
authors:
  - Bart Van Puyvelde
  - Robbe Devreese
  - Cristina Chiva
  - Eduard Sabidó
  - Sibylle Pfammatter
  - Christian Panse
  - Jeewan Babu Rijal
  - Charline Keller
  - Ihor Batruch
  - Patrick Pribil
  - Jean-Baptiste Vincendet
  - Frédéric Fontaine
  - Lars Lefever
  - Pedro Magalhães
  - Dieter Deforce
  - Paolo Nanni
  - Bart Ghesquière
  - Yasset Perez-Riverol
  - Lennart Martens
  - Christine Carapito
  - Robbin Bouwmeester
  - Maarten Dhaenens
aliases:
   - Generation Beta LFQ Benchmark
   - PXD070049
   - PXD071205
tags:
  - literature
  - paper
  - proteomics
  - benchmarking
  - LC-MS
  - DIA
  - single-cell
category: literature
date_created: 2026-02-09
Journal: bioRxiv
Year: 2026
---

# LFQ Benchmark Dataset - Generation Beta: Assessing Modern Proteomics Instruments and Acquisition Workflows with High-Throughput LC Gradients

## Citation

> [!cite] Reference
> **Title**：LFQ Benchmark Dataset - Generation Beta: Assessing Modern Proteomics Instruments and Acquisition Workflows with High-Throughput LC Gradients
> **Authors**: Bart Van Puyvelde, Robbe Devreese, et al.
> **Year**: 2026
> **Journal**: bioRxiv
> **DOI**: 10.64898/2026.01.29.702266

## Abstract

Recent advances in liquid chromatography–mass spectrometry ([[LC-MS]]) have accelerated the adoption of high-throughput workflows that deliver deep proteome coverage using minimal sample amounts. This trend is largely driven by clinical and [[single-cell proteomics]], where sensitivity and reproducibility are essential. Here, we extend our previous benchmark dataset (PXD028735) using next-generation LC-MS platforms optimized for rapid proteome analysis. We generated an extensive [[DDA]]/[[DIA]] dataset using a human-yeast-E. coli hybrid proteome. The proteome sample was distributed across multiple laboratories together with standardized analytical protocols specifying two short LC gradients (5 and 15 min) and low sample input amounts. This dataset includes data acquired on four different platforms, and features new scanning quadrupole-based implementations, extending coverage across different instruments and acquisition strategies. Our comprehensive evaluation highlights how technological advances and reduced LC gradients may affect proteome depth, quantitative precision, and cross-instrument consistency. The release of this benchmark dataset via [[ProteomeXchange]] (PXD070049 and PXD071205), allows for the acceleration of cross-platform algorithm development, enhance data mining strategies, and supports standardization of short-gradient, high-throughput LC-MS-based proteomics.

## Key Points

- Creation of a second-generation LFQ benchmark dataset (Generation Beta) designed for high-throughput and low-input proteomics (updating PXD028735).
- Evaluation of four state-of-the-art MS platforms: [[SCIEX ZenoTOF 7600+]], [[SCIEX ZenoTOF 8600]], [[Thermo Scientific Orbitrap Astral]], and [[Bruker timsTOF Ultra 2]].
- Implementation of standardized short gradients (5 and 15 minutes) and low sample loads ([[50 ng]] standard and [[250 pg]] single-cell equivalent).
- Assessment of novel scanning quadrupole acquisition methods including [[ZT Scan DIA]] and [[diagonal-PASEF]].
- Integration with [[ProteoBench]] to facilitate community-driven software benchmarking and transparent performance evaluation.

## Methods

### Sample Preparation
- Method used: Hybrid proteome mixtures created from commercially available digests.
- Cell type: Human [[K562]], Yeast, and [[Escherichia coli]].
- Number of cells: N/A (Protein digests used). Input loads were [[50 ng]] (standard) and [[250 pg]] (single-cell equivalent).
- **Mixture Ratios (Human/Yeast/E. coli w/w%):**
    - Sample A: 65% / 30% / 5%
    - Sample B: 65% / 15% / 20%
    - Sample C: 65% / 3% / 32%

### Data Analysis
- Software: [[Skyline]] (QC), [[Mascot Daemon]] (QC search), [[DIA-NN]], [[Spectronaut]], [[AlphaDIA]], [[FragPipe]], [[PEAKS]].
- Downstream: [[ProteoBench]], [[Panorama Web]], [[AutoQC Loader]].

## Results

### Main Findings
1. **Instrument Performance:** The study successfully generated a multi-platform dataset covering [[ZenoTOF]], [[Orbitrap Astral]], and [[timsTOF Ultra 2]] systems. It demonstrates that modern instruments can handle short gradients (5-15 min) and low inputs (down to 250 pg) while maintaining robust data quality.
2. **Advanced Acquisition Modes:** Scanning quadrupole methods like [[diagonal-PASEF]] (Bruker) and [[ZT Scan DIA]] (SCIEX) showed clear improvements in quantification accuracy for low-input/short-gradient experiments compared to standard acquisition modes, effectively adding an extra separation dimension.
3. **Refined Conditions:** On the [[Orbitrap Astral]], moving from a standardized "best practice" method to a "refined" method (optimized gradients, trap-and-elute, or specific direct injection settings) resulted in substantial performance gains, highlighting the importance of method tuning for specific hardware.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Schematic overview of acquisition strategies and instrumentation. Shows the three hybrid proteome mixtures (A, B, C), the two LC gradients (5 and 15 min), and the four LC-MS platforms used (SCIEX ZenoTOF 7600+/8600, Thermo Orbitrap Astral, Bruker timsTOF Ultra 2). |
| Supp Figs | (Text Reference) Supplementary figures provide detailed metrics on TIC, precursor area, retention time, mass accuracy, and specific software comparisons (e.g., AlphaDIA vs DIA-NN). |

## Discussion

### Strengths
- **Community Resource:** Provides a massive, publicly available dataset (via [[ProteomeXchange]] and [[ProteoBench]]) for software developers to test algorithms on relevant, modern data.
- **Realistic Benchmarking:** Unlike manufacturer specs, this uses "lab's best practice" to reflect real-world performance in core facilities.
- **Future-Proofing:** Includes emerging methods like [[diagonal-PASEF]] and [[ZT Scan DIA]], and addresses the "single-cell" trend with 250 pg inputs.

### Limitations
- **No Direct "Winner":** The study intentionally avoids declaring a "best" instrument, as setups varied (LC columns, flow rates) and were not strictly harmonized for head-to-head competition.
- **Flow Rate Variability:** Different labs used different flow rates (nanoflow vs. microflow), introducing variables that make direct instrument comparison difficult without considering the LC setup.

### Future Work
- **Software Evaluation:** The dataset is intended to be used within [[ProteoBench]] to continuously evaluate and improve proteomics software (e.g., [[DIA-NN]], [[Spectronaut]], [[AlphaDIA]]).
- **Standardization:** Supports the move towards standardizing short-gradient, high-throughput workflows in clinical and single-cell proteomics.

## Personal Notes

## Related Papers

- [[Navarro et al., 2016]] - A multicenter study benchmarks software tools for label-free proteome quantification (Original LFQ Benchmark).
- [[Van Puyvelde et al., 2022]] - A comprehensive LFQ benchmark dataset on modern day acquisition strategies in proteomics (Generation Alpha/Previous version).
- [[Guzman et al., 2024]] - Ultra-fast label-free quantification and comprehensive proteome coverage with narrow-window data-independent acquisition.