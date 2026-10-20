---
title: "Mass-spectrometry-based proteomics: from single cells to clinical applications"
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
doi: "10.1038/s41586-025-08584-0"
url: "https://doi.org/10.1038/s41586-025-08584-0"
publication_status: "published"
published_online: "2025-02-26"
published_print: "2025-02-27"
---


# Mass-spectrometry-based proteomics: from single cells to clinical applications

> [!info] Verification scope — 2026-10-20
> Bibliographic metadata and the public abstract were checked. This does not verify every experimental detail, figure, parameter or performance claim in the full note.
> Detailed review-specific performance and clinical comparisons remain unverified; the comparison below is a qualified overview, not a benchmark.
> See the [per-note audit record](../../audit/literature-audit.json) for evidence and unresolved items.

## Citation

> [!cite] Reference
> **Title**：Mass-spectrometry-based proteomics: from single cells to clinical applications
> **Authors**: Tiannan Guo, Judith A. Steen & Matthias Mann
> **Year**: 2025
> **Journal**: Nature
> **DOI**: [10.1038/s41586-025-08584-0](https://doi.org/10.1038/s41586-025-08584-0)
## Abstract

Mass-spectrometry (MS)-based proteomics has evolved into a robust tool for comprehensive biological analysis. This review highlights recent technological advances in sensitivity, throughput, and robustness that now enable [[single-cell proteomics|Single-cell proteomics]] and [[Spatial proteomics]]. The authors discuss novel sample preparation, advanced instrumentation (such as [[timsTOF]] and [[Astral]] analyzers), and data acquisition strategies like [[Data-independent acquisition]] (DIA). The review explores applications in [[Protein-protein interactions]], [[Post-translational modifications]] (PTMs), and [[Structural proteomics]]. A significant focus is placed on the integration of [[Artificial Intelligence]] to accelerate data analysis and the transition of proteomics from basic research to clinical practice, particularly in biomarker discovery and diagnostics using body fluids.

## Key Takeaways

- **Technological Revolution**: Advances in instrumentation (e.g., [[Orbitrap Astral]], [[timsTOF]]) and data acquisition ([[DIA]]) have dramatically increased sensitivity and throughput, enabling the analysis of thousands of proteins from minute samples.
- **New Dimensions**: The field has expanded from bulk analysis to [[single-cell proteomics|Single-cell proteomics]] (revealing cellular heterogeneity) and [[Spatial proteomics]] (preserving tissue context via methods like [[Deep Visual Proteomics]]).
- **AI Integration**: [[Deep Learning]] supports tasks such as peptide-property prediction, identification and structural analysis (e.g., [[AlphaFold]]). These applications do not make [[Large Language Models]] a required component of every proteomics workflow.
- **Clinical Transition**: Plasma proteomics is being investigated for diagnostic applications. Any advantage over a standard clinical test requires an indication-specific cohort and comparator; regulatory approval, standardization and assay validation remain important.

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
- **Single-cell Proteomics**: Protein content varies by cell type and size. Nanolitre preparation, [[SCoPE2]] (isobaric labeling with carrier), and sensitive label-free workflows address low starting amounts; a fixed protein mass is not a universal sensitivity threshold.
- **Spatial Proteomics**: Techniques like [[Deep Visual Proteomics]] (DVP) combine high-resolution imaging with AI-driven laser capture microdissection and MS to map proteomes to specific tissue phenotypes.
- **Structural & Interaction Proteomics**: Utilization of [[Cross-linking mass spectrometry]] (XL-MS), [[Hydrogen-deuterium exchange]] (HDX-MS), and [[Limited proteolysis]] to study protein structures and complexes in native environments.
- **Chemoproteomics**: Methods like [[Activity-based protein profiling]] (ABPP) and [[Thermal protein profiling]] (TPP) for drug target discovery.

### Theme 3: Clinical Proteomics
- **Body Fluids**: Plasma coverage and throughput depend on preparation, enrichment, instrument and analysis settings. An exact protein count requires the corresponding experiment and definition of coverage.
- **Biomarkers**: Moving from broad discovery profiling to focused, independently validated assays.
- **Challenges**: Clinical translation requires a defined intended use, analytical and clinical validation, reproducibility and feasible costs/turnaround time. Absolute quantification and spike-in standards are assay-dependent choices.

### Comparison of Approaches

Single-cell MS remains subject to ion-sampling and background noise; see the experimental quantification assessment in [Schoof et al. (2021)](https://doi.org/10.1038/s41467-021-23667-y).

| Approach/Theory | Key Features | Strengths | Weaknesses |
|-----------------|--------------|-----------|------------|
| **[[Data-dependent acquisition]] (DDA)** | Selects most abundant ions for fragmentation. | Intuitive data interpretation; standard for spectral libraries. | Stochastic sampling leads to missing values; bias toward high-abundance proteins. |
| **[[Data-independent acquisition]] (DIA)** | Fragments co-isolated ions across programmed mass windows. | Systematic sampling; retrospective analysis of acquired signals is possible. | Complex spectra require appropriate scoring and interference control; library-free workflows also exist. |
| **[[single-cell proteomics\|Single-cell proteomics]]** | Analyzes proteins in individual cells. | Measures protein abundance directly; complements transcript-level measurements. | Ion sampling noise, incomplete coverage and limited starting material; throughput depends on workflow. |
| **Affinity-based methods** (e.g., Olink) | Uses antibodies/aptamers for detection. | Sensitive measurement of selected targets from limited material; clinical validation is assay-specific. | Epitope masking issues; cross-reactivity; limited to available binders. |
| **MS-based Proteomics** | Infers peptide identities from mass spectra; targeted and discovery modes are available. | Broad coverage without selecting an antibody panel; suitable workflows can characterize PTMs and some isoforms. | Coverage depends on abundance, preparation and acquisition; peptide-to-protein inference and PTM localization require care. |

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