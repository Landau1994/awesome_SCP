---
title: Single Cell Proteomics in the Developing Human Brain
authors:
  - Tianzhi Wu
  - Lihua Jiang
  - Tanzila Mukhtar
  - Li Wang
  - Ruiqi Jian
  - Cheng Wang
  - Tiffany Trinh
  - Arnold R. Kriegstein
  - Michael Snyder
  - Jingjing Li
aliases:
   - <article>
   - <paper>
   - <literature>
tags:
  - literature
  - paper
  - proteomics
  - neuroscience
  - single-cell
category: literature
date_created: 2024-05-23
Journal: bioRxiv (Preprint)
Year: 2025
---

# Single Cell Proteomics in the Developing Human Brain

## Citation

> [!cite] Reference
> **Title**：Single Cell Proteomics in the Developing Human Brain
> **Authors**: Tianzhi Wu, Lihua Jiang, Tanzila Mukhtar, Li Wang, Ruiqi Jian, Cheng Wang, Tiffany Trinh, Arnold R. Kriegstein, Michael Snyder, and Jingjing Li
> **Year**: 2025
> **Journal**: bioRxiv
> **DOI**: 10.1101/2025.06.23.660079

## Abstract

This study presents the first quantitative, single-cell resolution proteomic map of the developing human brain. Using a rigorously optimized label-free mass spectrometry workflow, the researchers quantified ~800 proteins per cell across 2,310 individual cells from prenatal human brain samples (GW 13, 15, and 19). The study reveals widespread discordance between mRNA and protein levels, particularly in genes associated with neurodevelopmental disorders (NDDs). Proteins exhibited significantly higher cell-type specificity than their mRNA counterparts. By reconstructing developmental trajectories, the authors identified a critical "vulnerability window" for autism spectrum disorder (ASD) during the transition from intermediate progenitor cells to excitatory neurons, characterized by a specific protein co-expression module.

## Key Points

- **Deep Proteomic Coverage:** Achieved quantification of ~800 proteins per individual cell in small (5–10 μm) primary human fetal neurons, a significant technical advance over previous studies focused on larger cell lines or oocytes.
- **mRNA-Protein Discordance:** Demonstrated that transcript levels are often poor proxies for protein abundance in the brain, identifying specific "outlier" gene groups where protein levels are either much higher (Group A) or much lower (Group B) than mRNA predicts.
- **Cell-Type Specificity:** Proteomic data reveals much sharper cellular identity and lineage-restricted expression (measured by Tau scores) than transcriptomic data, which often shows more "promiscuous" or broad expression.
- **ASD Vulnerability Window:** Identified a protein module (Module 4) active during the IPC-to-neuron transition that is highly enriched for ASD-associated genes and deleterious mutations, pinpointing a specific molecular bottleneck in disease pathogenesis.

## Methods

### Sample Preparation
- **Method used:** Microdissection of Germinal Zone (GZ) and Cortical Plate (CP), tissue dissociation, followed by FACS sorting.
- **Cell type:** Primary prenatal human brain cells (excitatory neurons, radial glia, interneurons, etc.) and erythroid cells.
- **Number of cells:** 2,310 individual cells (independent MS runs).

### Data Analysis
- **Software:** DIA-NN (for quantification from MS2 fragment-ion intensities), Seurat (clustering), Scanpy (trajectory analysis).
- **Downstream:** Weighted Gene Co-expression Network Analysis (WGCNA), Tau score calculation for specificity, and dN/dS ratio for evolutionary conservation.

## Results

### Main Findings
1. **Resolution of Brain Cell Types:** Successfully identified all major brain cell populations (RG, oRG, IPC-EN, EN, CGE-IN, OPC, Microglia, Vascular) using proteomic signatures and established markers (e.g., HOPX, EOMES, TBR1).
2. **Identification of Regulatory Outliers:** Found Group B genes (high RNA, low protein) are enriched for neurodevelopmental processes and display high loss-of-function intolerance (pLI), suggesting tight post-transcriptional regulation of dosage-sensitive proteins.
3. **Lineage-Specific Discovery:** Reconstructed the RG-to-EN trajectory at the protein level, identifying 6 distinct modules. Module 4 and 5 showed high evolutionary conservation and strong links to NDD and ASD risk.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Label-free single-cell proteome workflow, protein yields (~800/cell), and comparison with previous studies. |
| Fig 2 | Proteomic atlas showing UMAP clusters of erythroid and brain-associated cells with specific protein marker validation. |
| Fig 3 | Comparative analysis between scProteome and scRNA-seq, highlighting discrepancies in markers like MKI67, TBR1, and SCGN. |
| Fig 4 | Immunostaining and RNAscope validation of mRNA-protein discordance for genes like CHD3, ZBTB18, and MAPT. |
| Fig 5 | Statistical analysis of discordance, identification of Group A/B outliers, and Tau score-based cell-type specificity. |
| Fig 6 | Lineage reconstruction and WGCNA protein modules; enrichment of ASD risk genes and deleterious mutations in Module 4. |

## Discussion

### Strengths
- First application of single-cell proteomics to complex primary human brain tissue.
- Overcomes the "input barrier" for small primary cells (100 pg total protein).
- Integration of proteomic data with large-scale genetic datasets (SFARI, de novo mutations) provides clinical relevance.

### Limitations
- Though a significant advance, the throughput (one cell per MS run) is lower than droplet-based scRNA-seq.
- Sensitivity is still limited compared to bulk proteomics (~800 proteins vs. >5,000 in bulk).

### Future Work
- Improving scalability and sensitivity to capture lower-abundance proteins (e.g., transcription factors).
- Applying this workflow to other complex tissues and disease models (e.g., brain organoids or NDD patient samples).

## Personal Notes

- The finding that protein abundance is more cell-type specific than mRNA is a critical takeaway for developmental biology.
- The "primed-but-silent" state for TBR1 (high mRNA in IPCs but protein only in mature ENs) is a perfect example of why transcriptomics alone can be misleading regarding functional states.

## Related Papers

- **Gry et al. (2009):** Correlations between RNA and protein expression profiles.
- **Wang et al. (2025):** Molecular and cellular dynamics of the developing human neocortex (Nature).
- **Demichev et al. (2020):** DIA-NN software for high-throughput proteomics.