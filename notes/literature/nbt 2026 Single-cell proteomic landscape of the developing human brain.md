---
title: Single-cell proteomic landscape of the developing human brain
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
   - Single-cell proteomic landscape of the developing human brain
   - Wu et al. 2026
tags:
  - literature
  - paper
  - single-cell-proteomics
  - neuroscience
  - developmental-biology
  - ASD
category: literature
date_created: 2025-06-25
Journal: Nature Biotechnology
Year: 2026
---

# Single-cell proteomic landscape of the developing human brain

## Citation

> [!cite] Reference
> **Title**：Single-cell proteomic landscape of the developing human brain
> **Authors**: Tianzhi Wu, Lihua Jiang, Tanzila Mukhtar, Li Wang, Ruiqi Jian, Cheng Wang, Tiffany Trinh, Arnold R. Kriegstein, Michael Snyder & Jingjing Li
> **Year**: 2026
> **Journal**: Nature Biotechnology
> **DOI**: https://doi.org/10.1038/s41587-025-02980-7

## Abstract

Profiling protein abundance and dynamics at single-cell resolution in complex human tissues is challenging. Given the discordance between transcript and protein abundance observed in studies of the human cerebral cortex, the authors developed an optimized workflow that combines label-free single-cell mass spectrometry with precise sample preparation to resolve quantitative proteomes of individual cells from the developing human brain. The method achieves deep proteomic coverage (~800 proteins per cell) even in small immature prenatal human neurons (diameter ~7–10 μm, ~50 pg protein), capturing major brain cell types. The study documents extensive transcriptome–proteome discordance across cell types, particularly in genes associated with neurodevelopmental disorders. Proteins exhibit markedly higher cell-type specificity than their mRNA counterparts. By reconstructing developmental trajectories, the authors identify dynamic, stage-specific protein co-expression modules and pinpoint the intermediate progenitor-to-neuron transition as a genetically vulnerable phase associated with autism.

## Key Points

- Development of an optimized [[label-free single-cell mass spectrometry]] workflow capable of quantifying ~800 proteins per cell in small primary human neurons (~7–10 μm).
- Identification of significant mRNA-protein discordance, where proteins associated with neurodevelopmental disorders (NDDs) and autism spectrum disorder (ASD) show high cell-type specificity despite broad mRNA expression.
- Discovery of a specific protein co-expression module (Module 4) that is enriched for ASD de novo mutations and is active during the transition from intermediate progenitors (IPCs) to excitatory neurons (ENs).

## Methods

### Sample Preparation
- Method used: [[Papain]] dissociation, [[FACS]] sorting into 384-well plates, miniaturized [[Trypsin]] digestion, and [[EvoTip]] desalting.
- Cell type: Primary prenatal human brain cells (GW13, GW15, GW19), including radial glia, excitatory neurons, interneurons, and microglia.
- Number of cells: 2,310 cells (after QC) for proteomics; ~31,000 paired cells for scRNA-seq.

### Data Analysis
- Software: [[DIA-NN]] (for MS data processing), [[Seurat]] (clustering and dimensionality reduction), [[Scanpy]], [[Harmony]] (batch correction), [[QuPath]] (image analysis).
- Downstream: [[WGCNA]] (Weighted Gene Co-expression Network Analysis), [[Gene Ontology]] enrichment, Pseudotime trajectory inference, [[ORBIT]] (custom method for proteome-transcriptome comparison).

## Results

### Main Findings
1. **Deep Proteomic Coverage in Small Cells:** The workflow successfully quantified proteomes from small primary neurons (~50 pg protein), distinguishing major cell types (RG, oRG, IPC-EN, EN, IN, OPC, Microglia, Vascular) without carrier channels.
2. **mRNA-Protein Discordance:** A distinct group of genes (Group B) was identified with high mRNA but low protein abundance. These genes are enriched for neuronal differentiation functions and ASD risk factors, suggesting post-transcriptional repression until specific developmental checkpoints.
3. **ASD-Associated Protein Module:** Trajectory analysis revealed "Module 4," a protein network tightly coordinated during the IPC-to-EN transition. This module is significantly enriched for genes harboring de novo deleterious mutations in ASD patients, highlighting a critical developmental window of vulnerability.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Label-free single-cell proteome profiling workflow and protein yield comparison against other studies. |
| Fig 2 | Proteomics-based cell map (UMAP) of the prenatal human neocortex identifying major cell types and erythroid clusters. |
| Fig 3 | Comparison of paired single-cell proteomes and single-cell transcriptomes from the same tissue samples. |
| Fig 4 | Experimental validation (IHC and RNAscope) of RNA-protein discordance for markers like TBR1, SCGN, ZBTB18, and CHD3. |
| Fig 5 | Global analysis of mRNA-protein discordance, defining Group A (Low RNA/High Protein) and Group B (High RNA/Low Protein) genes and their association with ASD. |
| Fig 6 | Protein dynamics across neurodevelopment (WGCNA), identifying Module 4 as an ASD-linked module during the RG-to-EN trajectory. |

## Discussion

### Strengths
- **Label-free Quantification:** Avoids ratio compression and carrier artifacts common in isobaric labeling methods (e.g., TMT), providing more accurate absolute quantification.
- **Primary Tissue Application:** successfully applied to small, biologically heterogeneous primary human cells rather than large cultured cell lines (like HeLa).
- **Multi-modal Validation:** Findings were robustly validated using paired scRNA-seq, bulk proteomics, and spatial imaging (IHC/RNAscope).

### Limitations
- **Dissociation Artifacts:** Enzymatic dissociation leads to the loss of distal cellular processes (axons/dendrites) and associated proteins (e.g., synaptic components).
- **Solubility Bias:** The workflow favors soluble proteins, potentially under-representing membrane-bound or insoluble nuclear scaffold proteins.
- **Throughput:** The label-free approach (one cell per run) has lower throughput compared to multiplexed strategies.

### Future Work
- Implementation of [[plexDIA]] to balance quantitative fidelity with increased throughput.
- Application of the workflow to later developmental stages and different brain regions.

## Personal Notes



## Related Papers

- [[Wang et al. 2025]] (Molecular and cellular dynamics of the developing human neocortex - Reference scRNA-seq atlas)
- [[Demichev et al. 2020]] (DIA-NN: neural networks and interference correction enable deep proteome coverage in high throughput)
- [[Brunner et al. 2022]] (Ultra-high sensitivity mass spectrometry quantifies single-cell proteome changes upon perturbation)