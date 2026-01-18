---
title: Mass spectrometry based proteomics:from single cells to clinical applications
authors: Tiannan Guo, Judith A. Steen, Matthias Mann 
aliases:
  - MS-based proteomics review 2025
  - Nature Proteomics Review
tags:
  - literature
  - review
  - proteomics
  - mass_spectrometry
  - single-cell
  - spatial_biology
  - clinical_translation
  - AI
category: literature
date_created: 2025-02-27
Journal: Nature
Year: 2025
---


# Mass-spectrometry-based proteomics: from single cells to clinical applications

## Citation

> [!cite] Reference
> **Title**：Mass-spectrometry-based proteomics: from single cells to clinical applications
> **Authors**: Tiannan Guo, Judith A. Steen & Matthias Mann
> **Year**: 2025
> **Journal**: Nature
> **DOI**: https://doi.org/10.1038/s41586-025-08584-0

## Abstract

Mass-spectrometry (MS)-based proteomics has evolved into a robust tool for comprehensive biological analysis. This review highlights recent technological advances in sensitivity, throughput, and robustness that now enable [[Single-cell proteomics]] and [[Spatial proteomics]]. The authors discuss novel sample preparation, advanced instrumentation (such as [[timsTOF]] and [[Astral]] analyzers), and data acquisition strategies like [[Data-independent acquisition]] (DIA). The review explores applications in [[Protein-protein interactions]], [[Post-translational modifications]] (PTMs), and [[Structural proteomics]]. A significant focus is placed on the integration of [[Artificial Intelligence]] to accelerate data analysis and the transition of proteomics from basic research to clinical practice, particularly in biomarker discovery and diagnostics using body fluids.

## Key Takeaways

- **Technological Revolution**: Advances in instrumentation (e.g., [[Orbitrap Astral]], [[timsTOF]]) and data acquisition ([[DIA]]) have dramatically increased sensitivity and throughput, enabling the analysis of thousands of proteins from minute samples.
- **New Dimensions**: The field has expanded from bulk analysis to [[Single-cell proteomics]] (revealing cellular heterogeneity) and [[Spatial proteomics]] (preserving tissue context via methods like [[Deep Visual Proteomics]]).
- **AI Integration**: [[Deep Learning]] and [[Large Language Models]] (LLMs) are now integral to the workflow, enhancing peptide identification, PTM prediction, structural analysis (e.g., [[AlphaFold]]), and data interpretation.
- **Clinical Transition**: While plasma proteomics shows promise for diagnostics (outperforming some standard clinical tests), challenges remain in regulatory approval, standardization, and the development of robust, cost-effective assays for clinical deployment.

## Scope & Methodology

### Search Strategy
- **Timeframe covered**: Focuses on developments since the authors' last review (approx. 2016) up to early 2025.
- **Databases used**: N/A (Narrative Review).
- **Keywords**: Mass spectrometry, Proteomics, Single-cell, Spatial profiling, Clinical applications, Artificial Intelligence.

### Inclusion Criteria
- **Focus area**: [[MS-based proteomics]] technologies and applications.
- **Types of studies included**: Technological developments (instrumentation, software), biological applications (PTMs, structure, interactions), and clinical studies (biomarkers, diagnostics).

## State of the Art (Main Themes)

### Theme 1: Technological Workflow Advances
- **Sample Preparation**: Shift towards automation (robotics), digestion on beads to remove detergents, and handling of [[FFPE tissues]].
- **Chromatography**: Use of micro-pillar array columns ([[uPAC]]) and preformed gradients (e.g., [[Evosep One]]) to improve robustness and throughput.
- **Instrumentation**: Revival of TOF analyzers. Key instruments include [[timsTOF]] (using [[PASEF]] for ion mobility separation) and [[Orbitrap Astral]] (combining Orbitrap with a multi-reflection TOF for high speed and sensitivity).
- **Acquisition**: Move from [[Data-dependent acquisition]] (DDA) to [[Data-independent acquisition]] (DIA) as the method of choice for comprehensive coverage and reproducibility.

### Theme 2: Emerging Applications
- **Single-cell Proteomics**: Overcoming sensitivity limits (50-500 pg protein/cell) using nanolitre droplets, [[SCoPE2]] (isobaric labeling with carrier), and ultra-sensitive label-free methods.
- **Spatial Proteomics**: Techniques like [[Deep Visual Proteomics]] (DVP) combine high-resolution imaging with AI-driven laser capture microdissection and MS to map proteomes to specific tissue phenotypes.
- **Structural & Interaction Proteomics**: Utilization of [[Cross-linking mass spectrometry]] (XL-MS), [[Hydrogen-deuterium exchange]] (HDX-MS), and [[Limited proteolysis]] to study protein structures and complexes in native environments.
- **Chemoproteomics**: Methods like [[Activity-based protein profiling]] (ABPP) and [[Thermal protein profiling]] (TPP) for drug target discovery.

### Theme 3: Clinical Proteomics
- **Body Fluids**: Plasma proteomics can now measure ~1,000 proteins in high throughput. Strategies to handle the dynamic range include deep learning deconvolution and enrichment of protein coronas or extracellular vesicles.
- **Biomarkers**: Transitioning from discovery (unbiased, thousands of proteins) to targeted validation (quantifiable panels).
- **Challenges**: Requires absolute quantification (spike-in standards), regulatory compliance (IVD/CLIA), and reduction of costs/turnaround time.

### Comparison of Approaches

| Approach/Theory | Key Features | Strengths | Weaknesses |
|-----------------|--------------|-----------|------------|
| **[[Data-dependent acquisition]] (DDA)** | Selects most abundant ions for fragmentation. | Intuitive data interpretation; standard for spectral libraries. | Stochastic sampling leads to missing values; bias toward high-abundance proteins. |
| **[[Data-independent acquisition]] (DIA)** | Fragments all ions in sequential mass windows. | Comprehensive coverage; reproducible; retrospective analysis possible. | Complex spectra require advanced deconvolution algorithms/libraries. |
| **[[Single-cell proteomics]]** | Analyzes proteins in individual cells. | Functional readout of cell state; no Poisson noise (unlike RNA). | Lower throughput than transcriptomics; cannot amplify proteins (sensitivity limits). |
| **Affinity-based methods** (e.g., Olink) | Uses antibodies/aptamers for detection. | High sensitivity; low sample volume; established in clinics. | Epitope masking issues; cross-reactivity; limited to available binders. |
| **MS-based Proteomics** | Direct sequencing of peptides. | Unbiased; detects PTMs and isoforms; high specificity. | Higher equipment cost; lower sensitivity than PCR/affinity methods; complex workflow. |

## Critical Analysis

### Current Consensus
- The proteome is a more direct effector of phenotype than the transcriptome, and correlation between the two is often low (especially in dynamic states or secreted proteins).
- [[DIA]] coupled with ion mobility (e.g., [[diaPASEF]]) is becoming the gold standard for quantitative proteomics.
- AI is indispensable for processing the complex data generated by modern instruments.

### Controversies / Debates
- **Depth vs. Throughput**: Balancing the need for deep proteome coverage (thousands of proteins) against the throughput required for clinical cohorts (thousands of samples).
- **Clinical Utility**: The debate between targeted MS assays vs. affinity-based panels for routine clinical diagnostics. MS offers specificity but faces regulatory and adoption hurdles compared to immunoassays.

### Gaps in Knowledge
- **The "Dark Proteome"**: Small unannotated open reading frames (sORFs), alternative splice variants, and complex combinatorial PTMs remain difficult to capture systematically.
- **Absolute Quantification**: Lack of standardized, proteome-wide heavy isotope resources for absolute quantification across different labs and platforms.
- **Standardization**: Need for community-driven standards in data formats and protocols to enable large-scale "foundation models" similar to those in genomics/NLP.

## Future Directions

- **Foundation Models**: Training "large proteomics models" (similar to LLMs) on vast spectral datasets to predict peptide behavior, biological function, and response to perturbations.
- **Multi-omics Integration**: Building knowledge graphs that integrate genomics, transcriptomics, proteomics, and metabolomics to solve systems biology problems.
- **Perturbation Proteomics**: Large-scale screening of cellular responses to drugs or genetic edits to map functional networks.
- **Clinical AI**: Using "reasoning models" to interpret patient proteomic data for personalized medicine while maintaining privacy.

## Personal Notes



## Related Papers

- **The Human Proteome Project**: Adhikari, S. et al. *A high-stringency blueprint of the human proteome.* Nat. Commun. (2020).
- **Deep Visual Proteomics**: Mund, A. et al. *Deep visual proteomics defines single-cell identity and heterogeneity.* Nat. Biotechnol. (2022).
- **The Astral Analyzer**: Stewart, H. I. et al. *Parallelized acquisition of Orbitrap and Astral analyzers...* Anal. Chem. (2023).
- **DIA-NN Software**: Demichev, V. et al. *DIA-NN: neural networks and interference correction...* Nat. Methods (2020).
- **AlphaFold-Multimer**: Evans, R. et al. *Protein complex prediction with AlphaFold-Multimer.* bioRxiv (2022).