---
title: One-Tip enables comprehensive proteome coverage in minimal cells and single zygotes
authors:
  - Zilu Ye
  - Pierre Sabatier
  - Javier Martin-Gonzalez
  - Akihiro Eguchi
  - Maico Lechner
  - Ole Østergaard
  - Jingsheng Xie
  - Yuan Guo
  - Lesley Schultz
  - Rafaela Truffer
  - Dorte B. Bekker-Jensen
  - Nicolai Bache
  - Jesper V. Olsen
aliases:
   - One-Tip
   - Single-cell proteomics
   - nDIA
tags:
  - literature
  - paper
  - proteomics
  - mass-spectrometry
  - single-cell
category: literature
date_created: 2024-05-22
Journal: Nature Communications
Year: 2024
---

# One-Tip enables comprehensive proteome coverage in minimal cells and single zygotes

## Citation

> [!cite] Reference
> **Title**：One-Tip enables comprehensive proteome coverage in minimal cells and single zygotes
> **Authors**: Zilu Ye, Pierre Sabatier, Javier Martin-Gonzalez, Akihiro Eguchi, Maico Lechner, Ole Østergaard, Jingsheng Xie, Yuan Guo, Lesley Schultz, Rafaela Truffer, Dorte B. Bekker-Jensen, Nicolai Bache & Jesper V. Olsen
> **Year**: 2024
> **Journal**: Nature Communications
> **DOI**: https://doi.org/10.1038/s41467-024-46777-9

## Abstract

Mass spectrometry (MS)-based proteomics workflows typically involve complex, multi-step processes, presenting challenges with sample losses, reproducibility, and requiring substantial time and financial investments. Here, the authors introduce **One-Tip**, a methodology that integrates efficient, one-pot sample preparation within an Evotip with precise, narrow-window data-independent acquisition (nDIA) analysis. One-Tip simplifies sample processing to just two pipetting steps, enabling the identification of >9000 proteins from ~1000 HeLa cells and ~6000 proteins in single cells from early mouse embryos. The study also demonstrates its utility in single-cell proteomics using the Uno Single Cell Dispenser and in analyzing extracellular vesicles (EVs) from blood plasma.

## Key Points

- **Streamlined Workflow**: Reduces sample preparation to a two-step pipetting process performed directly in an Evotip, minimizing sample loss and contamination.
- **High Sensitivity**: Achieves deep proteome coverage at the single-cell level (>3000 proteins per single HeLa cell) and minimal cell counts (~9000 proteins from 1000 cells).
- **Broad Versatility**: Successfully applied to HeLa cells, single mouse oocytes/zygotes/embryos, and plasma-derived extracellular vesicles (EVs).
- **Technological Integration**: Combines one-pot preparation with the Orbitrap Astral mass spectrometer and narrow-window DIA (nDIA) for superior analytical performance.

## Methods

### Sample Preparation
- **Method used**: One-Tip (one-pot lysis and digestion inside an Evotip). Uses MS-compatible surfactant n-Dodecyl-β-D-Maltoside (DDM) for lysis.
- **Cell type**: HeLa cells, mouse oocytes, zygotes, 2-cell and 4-cell embryos, and blood plasma extracellular vesicles (EVs).
- **Number of cells**: Titrations ranging from single cells up to 3000 cells.

### Data Analysis
- **Software**: Spectronaut v18 (spectral library-free approach, directDIA+).
- **Downstream**: MaxLFQ for protein quantitation; Gene Ontology (GO) enrichment analysis; Principal Component Analysis (PCA).
- **Instrumentation**: Evosep One LC system coupled to an Orbitrap Astral mass spectrometer using Whisper LC methods.

## Results

### Main Findings
1. **Efficiency and Depth**: One-Tip identified >9000 proteins from 1000 HeLa cells in a 30-minute LC-MS/MS run, comparable to the more complex PAC (Protein Aggregation Capture) protocol.
2. **Single-Cell Embryomics**: Successfully profiled mouse pre-implantation development, identifying ~5000-6000 proteins per single cell/oocyte, revealing biological transitions from zygote to 4-cell stage.
3. **EV Analysis**: Demonstrated high sensitivity by identifying >3000 proteins from only 16 ng of extracellular vesicles, matching state-of-the-art results with significantly less material.
4. **Automation Potential**: Validated the use of the Uno Single Cell Dispenser for automated, carrier-free single-cell proteomics.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Workflow depiction and HeLa titration results showing protein/peptide identification counts. |
| Fig 2 | Comparison between One-Tip and PAC methods regarding reproducibility, coverage, and missed cleavages. |
| Fig 3 | Analysis of mouse pre-implantation embryos, showing protein overlap and intensity changes across stages. |
| Fig 4 | Biological insights from embryo data, including GO enrichment and PCA of developmental stages. |
| Fig 5 | Integration with Uno Single Cell Dispenser for single-cell HeLa analysis. |
| Fig 6 | Workflow and results for Extracellular Vesicle (EV) analysis from blood plasma. |

## Discussion

### Strengths
- **Simplicity**: Drastically reduces the "expertise barrier" for high-sensitivity proteomics.
- **Low Sample Loss**: By performing all steps in a single tip, it circumvents losses associated with tube transfers and sonication.
- **Throughput**: Compatible with manual multi-channel pipetting or robotic automation, allowing for thousands of samples to be processed daily.

### Limitations
- **Missed Cleavages**: Shows a slightly higher rate of missed cleavages (up to 30% in some conditions) compared to bulk PAC methods.
- **Single-Cell Recovery**: Using the Uno Dispenser, consistent signal was detected in ~80% of samples, suggesting some cells may not reach the tip bottom or lyse perfectly.

### Future Work
- Improving the recovery rate and identification depth for single-cell sorting technologies.
- Expanding the method to other rare clinical samples and tissue micro-dissections.

## Personal Notes
- The integration of the sample prep *into* the chromatography tip (Evotip) is a clever way to eliminate transfer losses.
- The use of the Orbitrap Astral is key to the high protein counts reported.

## Related Papers
- Kulak et al. (2014) *Nature Methods* - in-StageTip protocol.
- Batth et al. (2019) *Mol. Cell. Proteomics* - PAC protocol.
- Guzman et al. (2024) *Nat. Biotechnol.* - nDIA method development.