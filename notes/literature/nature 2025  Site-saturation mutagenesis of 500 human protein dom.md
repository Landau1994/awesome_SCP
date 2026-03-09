---
title: " Site-saturation mutagenesis of 500 human protein dom"
authors:
  - Antoni Beltran
  - Xiang'er Jiang
  - Yue Shen
  - Ben Lehner
aliases:
  - <article>
  - <paper>
  - <literature>
tags:
  - literature
  - paper
category: literature
date_created: 2026-03-09
Journal: Nature
Year: 2025
---

# Site-saturation mutagenesis of 500 human protein domains

## Citation

> [!cite] Reference
> **Title**: Site-saturation mutagenesis of 500 human protein domains
> **Authors**: Antoni Beltran, Xiang'er Jiang, Yue Shen & Ben Lehner
> **Year**: 2025
> **Journal**: Nature
> **DOI**: 10.1038/s41586-024-08370-4

## Abstract

Missense variants that change the amino acid sequences of proteins cause one-third of human genetic diseases. Tens of millions of missense variants exist in the current human population, and the vast majority of these have unknown functional consequences. Here we present a large-scale experimental analysis of human missense variants across many different proteins. Using DNA synthesis and cellular selection experiments we quantify the effect of more than 500,000 variants on the abundance of more than 500 human protein domains. This dataset reveals that 60% of pathogenic missense variants reduce protein stability. The contribution of stability to protein fitness varies across proteins and diseases and is particularly important in recessive disorders. We combine stability measurements with protein language models to annotate functional sites across proteins. Mutational effects on stability are largely conserved in homologous domains, enabling accurate stability prediction across entire protein families using energy models. Our data demonstrate the feasibility of assaying human protein variants at scale and provides a large consistent reference dataset for clinical variant interpretation and training and benchmarking of computational methods.

## Key Points

- Quantified the effects of over 563,000 missense variants on the abundance of 522 diverse human protein domains using high-throughput cellular selection experiments.
- Demonstrated that approximately 60% of known pathogenic missense variants cause a detectable reduction in protein stability, with stability changes being particularly critical in recessive disorders.
- Combined stability measurements with evolutionary fitness scores (via protein language models) to successfully map over 5,000 functional sites, including poorly annotated "second-shell" residues.
- Showed that mutational effects are largely conserved across homologous domains, allowing the training of additive thermodynamic energy models to predict variant effects proteome-wide across entire protein families.

## Methods

### Sample Preparation
- Method used: [[mMPS]] (microchip-based massive in parallel synthesis), [[aPCA]] (abundance protein fragment complementation assay), [[Site-Saturation Mutagenesis]]
- Cell type: [[Saccharomyces cerevisiae]] (BY4741 cells)
- Number of cells: Bulk yeast culture transformations with library coverage of ~170x.

### Data Analysis
- Software: [[DiMSum]] (sequencing data processing), [[MoCHI]] (thermodynamic modeling), [[Foldseek]] (structural similarity), [[ESM1v]] (protein language models)
- Downstream: Differential growth rate estimation, functional site identification via residual analysis, energy modeling (Boltzmann partition function), clinical variant classification (ROC/AUC analysis).

## Results

### Main Findings
1. Created "Human Domainome 1", a highly reproducible (r = 0.85) dataset mapping the sequence-to-stability landscapes of 522 structurally diverse human protein domains.
2. Stability is a major driver of pathogenicity: 61% of pathogenic variants showed detectable destabilization, though this contribution varies by disease mechanism (higher in loss-of-function and recessive diseases, lower in dominant or gain-of-function disorders).
3. Thermodynamic models built on the mutational data demonstrated that mutational effects are largely additive and conserved among homologous domains. This permitted the creation of energy models capable of accurately predicting stability changes for over 4 million unseen variants across entire domain families.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Mutating the human domainome. Explains the experimental strategy (aPCA assay), replicate correlations, and structural diversity of the domains assayed. |
| Fig 2 | Deep mutational scans of protein homologues. Heatmaps showing the sequence-to-stability mutational landscapes for representative examples of the most abundant protein families. |
| Fig 3 | The contribution of protein stability to evolutionary fitness. Compares aPCA fitness with ESM1v evolutionary fitness predictions to identify evolutionary functional sites and binding interfaces. |
| Fig 4 | The contribution of protein destabilization to genetic disease. Shows the relationship between mutational effects on stability and clinical pathogenicity across different modes of inheritance and mechanisms. |
| Fig 5 | The genetic architecture of stability across protein families. Displays the thermodynamic modeling results, demonstrating that mutational effects are highly conserved across homologues. |

## Discussion

### Strengths
- Unprecedented scale for experimental protein variant analysis, expanding the number of high-quality stability measurements for human variants by approximately fivefold.
- Robust cross-validation of results using established in vitro measurements (e.g., ∆∆G values) and multiple computational predictors (like ThermoMPNN).
- Direct translation of experimental datasets into generalizable thermodynamic models that can predict variant effects on unseen homologues proteome-wide.

### Limitations
- The assay studied isolated protein domains removed from their native, full-length sequence context, potentially missing context-dependent mutational effects.
- Some tested domains did not yield sufficient signal in the aPCA assay, indicating low intrinsic stability/solubility or complex folding behaviors incompatible with two-state folding models.

### Future Work
- Expanding the platform to assess full-length proteins and multidomain interactions.
- Reusing the variant libraries to quantify additional molecular traits such as protein-protein/protein-nucleic acid interactions, localization, and allostery.
- Expanding coverage to include extracellular and transmembrane proteins, as well as complex genetic variations like insertions and deletions.

## Personal Notes



## Related Papers

- Tsuboyama, K. et al. (2023). Mega-scale experimental analysis of protein folding stability in biology and design. *Nature*.
- Frazer, J. et al. (2021). Disease variant prediction with deep generative models of evolutionary data. *Nature*.
- Levy, E. D., Kowarzyk, J. & Michnick, S. W. (2014). High-resolution mapping of protein concentration reveals principles of proteome architecture and adaptation. *Cell Reports*.