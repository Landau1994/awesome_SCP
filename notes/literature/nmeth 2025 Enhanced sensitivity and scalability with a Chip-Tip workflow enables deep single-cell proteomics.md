---
title: nmeth 2025 Enhanced sensitivity and scalability with a Chip-Tip workflow enables deep single-cell proteomics
aliases:
  - <% tp.file.cursor(1) %>
  - <article>
  - <paper>
  - <literature>
tags:
  - methods
  - literature
  - paper
category: literature
url: <% tp.file.cursor(3) %>
date_created: 2026-01-18
Journal: Nature Methods
Year: "2025"
---
# Enhanced sensitivity and scalability with a Chip-Tip workflow enables deep single-cell proteomics

## Citation

> [!cite] Reference
> **Authors**: Zilu Ye, Pierre Sabatier, Leander van der Hoeven, Maico Y. Lechner, Teeradon Phlairaharn, Ulises H. Guzman, Zhen Liu, Haoran Huang, Min Huang, Xiangjun Li, David Hartlmayr, Fabiana Izaguirre, Anjali Seth, Hiren J. Joshi, Sergey Rodin, Karl-Henrik Grinnemo, Ole B. Hørning, Dorte B. Bekker-Jensen, Nicolai Bache & Jesper V. Olsen
> **Year**: 2025
> **Journal**: Nature Methods
> **DOI**: https://doi.org/10.1038/s41592-024-02558-2

## Abstract

Single-cell proteomics (SCP) promises to revolutionize biomedicine by providing an unparalleled view of the proteome in individual cells. Here, we present a high-sensitivity SCP workflow named Chip-Tip, identifying >5,000 proteins in individual HeLa cells. It also facilitated direct detection of post-translational modifications in single cells, making the need for specific post-translational modification-enrichment unnecessary. Our study demonstrates the feasibility of processing up to 120 label-free SCP samples per day. An optimized tissue dissociation buffer enabled effective single-cell disaggregation of drug-treated cancer cell spheroids, refining overall SCP analysis. Analyzing nondirected human-induced pluripotent stem cell differentiation, we consistently quantified stem cell markers OCT4 and SOX2 in human-induced pluripotent stem cells and lineage markers such as GATA4 (endoderm), HAND1 (mesoderm) and MAP2 (ectoderm) in different embryoid body cells. Our workflow sets a benchmark in SCP for sensitivity and throughput, with broad applications in basic biology and biomedicine for identification of cell type-specific markers and therapeutic targets.

## Key Points

- Development of **Chip-Tip**, a nearly lossless label-free SCP workflow integrating [[cellenONE]] isolation, [[proteoCHIP EVO]], and [[Evotips]].
- Achieved identification of **>5,000 proteins** and **>40,000 peptides** in single HeLa cells using the [[Orbitrap Astral]] mass spectrometer.
- Demonstrated **direct detection of PTMs** (phosphorylation and glycosylation) in single cells without enrichment.
- Validated workflow on biological models: drug response in cancer spheroids and lineage markers in human iPSC differentiation.

## Methods

### Sample Preparation
- Method used: [[Chip-Tip]] ([[Label-free single-cell proteomics]] [[nDIA]])
- Cell type: HeLa, HCT116 (spheroids), hiPSCs (human induced pluripotent stem cells), Embryoid Bodies (EBs), HEK293T
- Number of cells: Single cells, 10, 20, 40 cells (up to 96 cells processed in parallel)

### Data Analysis
- Software: [[Spectronaut]] (v18), [[DIA-NN]] (v1.9)
- Downstream: [[ClusterProfiler]], [[Enrichplot]], [[Pathview]], [[Imp4p]]

## Results

### Main Findings
1. **Unprecedented Sensitivity**: Using the [[Orbitrap Astral]] and optimized [[nDIA]] settings (4Th6ms), the workflow identified a median of 5,204 proteins in single HeLa cells with high peptide coverage (median 41,700 peptides).
2. **Carrier Proteome Effects**: Benchmarking between [[Spectronaut]] and [[DIA-NN]] showed that including carrier proteomes (e.g., 20-cell samples) increases identification numbers (~4,000 to ~5,000 proteins) but requires careful FDR control, which was validated using an entrapment database strategy.
3. **Deep PTM Profiling**: The method allowed for the quantification of 168 protein kinases and the direct identification of phosphosites (median 120 pSer per cell) and glycans (via oxonium ions) without specific enrichment.
4. **Biological Application**: 
   - **Spheroids**: 5-FU treatment caused metabolic shifts (ribosome/purine synthesis) in HCT116 spheroids.
   - **Stem Cells**: Successfully tracked low-abundance transcription factors (OCT4, SOX2) and lineage markers (GATA4, HAND1, MAP2) during hiPSC differentiation.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Schematic of the **Chip-Tip** workflow; Protein/peptide IDs in single HeLa cells (>5k proteins); Sequence coverage and subcellular localization. |
| Fig 2 | Evaluation of the **carrier proteome effect** comparing [[Spectronaut]] and [[DIA-NN]]; Impact of search strategies on low-abundance protein detection. |
| Fig 3 | Throughput optimization (40, 80, 120 SPD) using [[Evosep One]] Whisper methods; Performance enhancement with **FAIMS** interface. |
| Fig 4 | **PTM profiling** in single cells: Kinome tree, phosphosite identification (pSer/pThr/pTyr), and glycan oxonium ion screening. |
| Fig 5 | Analysis of **5-FU impact** on colorectal cancer spheroids: Morphology changes, metabolic pathway diagrams, and GO term enrichment. |
| Fig 6 | Single-cell analysis of **hiPSC differentiation** into Embryoid Bodies (EBs): PCA plots, marker expression (OCT4, SOX2), and hierarchical clustering. |

## Discussion

### Strengths
- **Sensitivity**: Surpasses previous state-of-the-art (typically 1,500-2,500 proteins) by identifying >5,000 proteins per cell.
- **Workflow Efficiency**: The [[proteoCHIP EVO]] and direct transfer to [[Evotips]] minimize sample loss and manual handling.
- **PTM Capability**: Proves that deep coverage allows for "enrichment-free" PTM analysis in single cells.
- **Robustness**: Validated across different cell types and commercial instruments (Orbitrap Astral, Fusion Lumos, timsTOF Ultra).

### Limitations
- **Throughput Bottleneck**: Currently capped at 120 samples per day (SPD) due to MS run times, though faster than many deep-coverage methods.
- **PTM Localization**: Precise identification of modified peptides is still limited by current database search algorithms.
- **Dynamic Range**: While high, the dynamic range is not fully quantitative across all orders of magnitude.

### Future Work
- Integration of [[nDIA]] with multiplexed approaches (e.g., [[TMT]] or [[plexDIA]]) to exponentially increase throughput.
- Integrating single-cell genomic and proteomic measurements (multi-omics).
- Investigation of non-MS techniques (e.g., nanopore sequencing) for protein identification.

## Personal Notes

## Related Papers

- [[SCoPE2]]
- [[plexDIA]]
- [[nPOP]]