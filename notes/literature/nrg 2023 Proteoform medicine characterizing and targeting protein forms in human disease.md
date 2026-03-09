---
title:Proteoform medicine: characterizing and targeting protein forms in human disease
authors:
  - Jennifer A. Korchak
  - S. Stephen Yi
  - Neil L. Kelleher
  - Nidhi Sahni
  - Gloria M. Sheynkman
aliases:
   - <article>
   - <paper>
   - <literature>
tags:
  - literature
  - paper
  - proteoforms
  - precision-medicine
  - proteomics
  - network-biology
category: literature
date_created: 2023-10-24
Journal: Nature Reviews Genetics
Year: 2025
---

# Proteoform medicine: characterizing and targeting protein forms in human disease

## Citation

> [!cite] Reference
> **Title**: Proteoform medicine: characterizing and targeting protein forms in human disease
> **Authors**: Jennifer A. Korchak, S. Stephen Yi, Neil L. Kelleher, Nidhi Sahni & Gloria M. Sheynkman
> **Year**: 2025
> **Journal**: Nature Reviews Genetics
> **DOI**: 10.1038/s41576-025-00915-1

## Abstract

Proteoforms are the diverse molecular protein species produced from a single gene through genetic variation, alternative splicing and post-translational modifications. They are the crucial link between genotype and phenotype. There are estimated to be more than one million distinct protein variants produced from ~20,000 protein-coding genes in a given cell, making these proteoforms a vast and largely uncharacterized dimension in biomedical research. This Review focuses on the role of proteoforms in human genetic diseases. We highlight cutting-edge technologies for the identification and characterization of proteoforms, including long-read transcriptomics and emerging methods for direct protein sequencing, and we present a network biology framework to explain how proteoforms can perturb the molecular interactions and cellular pathways underlying disease phenotypes. We believe that precision medicine will require precision proteomics. An increasing knowledge of proteoform biology from molecular, systems and clinical perspectives will guide future research, ultimately contributing to a more precise understanding of the molecular basis of disease and refined therapeutic interventions.

## Key Points

- Proteoforms represent the vast diversity of protein species (>1 million in human cells) arising from genetic, transcriptomic, translational, and post-translational variations.
- The authors propose a unified "map–perturb–predict" framework to systematically discover, functionally characterize, and computationally model proteoforms.
- Proteoforms act as distinct functional nodes within molecular networks; their specific variations can rewire network topology by causing loss, gain, or alteration of molecular interactions.
- Proteoform-resolved precision medicine enables novel therapeutic interventions, categorized into node correction (targeting the proteoform itself), edge correction (targeting its interactions), and neighborhood correction (targeting surrounding network pathways).

## Methods

### Sample Preparation
- Method used: N/A (Review Article). Discusses various techniques including [[Top-down proteomics]], [[Bottom-up proteomics]], [[Long-read RNA sequencing]], and emerging [[Single-molecule protein sequencing]].
- Cell type: N/A (Discusses applications across human cell lines, healthy tissues, biofluids, and cancers).
- Number of cells: N/A (Discusses bulk to [[Single-cell proteomics]]).

### Data Analysis
- Software: N/A (Review Article). Highlights computational tools such as [[ProSightPD]], [[MetaMorpheus-TC]], [[AlphaFold 3]], and variant effect predictors like [[PolyPhen]] and [[VEP]].
- Downstream: [[Network biology]], [[Interactome mapping]], [[Proteogenomics]].

## Results

### Main Findings
1. **Sources of Proteoform Diversity:** Combinatorial complexity arises from the interplay of genetic mutations, alternative RNA processing (splicing, promoter use), translational recoding, and PTMs. This interplay is not merely additive but represents a fine-tuned regulatory logic dictating protein function and homeostasis.
2. **The Map-Perturb-Predict Framework:** 
   - *Map:* Involves high-resolution bioanalytical measurements (e.g., TDP, BUP, long-read sequencing) to build comprehensive proteoform atlases.
   - *Perturb:* Utilizes targeted experimental manipulations (CRISPR editing, base/prime editing, PROTACs) and comparative functional assays.
   - *Predict:* Employs deep-learning models (e.g., AlphaFold 3) and network tools to infer intrinsic biophysical properties and system-level functional outputs.
3. **Network Rewiring by Proteoforms:** Proteoform-specific alterations frequently drive disease by fundamentally rewiring interaction networks rather than simply causing loss-of-function misfolding. Changes include loss of interaction (e.g., CREB5 variants), gain of interaction (e.g., BRAF V600E binding KEAP1), or change of interaction/localization (e.g., FOXP1 and RBFOX1 isoforms).
4. **Therapeutic Targeting:** Introduces a scalable intervention framework:
   - *Node correction:* Gene/protein therapies, antisense oligonucleotides, or selective degradation (PROTACs).
   - *Edge correction:* Inhibiting pathogenic interactions or stabilizing disrupted physiological ones (e.g., bemarituzumab).
   - *Neighborhood correction:* Modulating primary/secondary interactors or using pharmacological bypassing (e.g., drug repurposing) to restore system balance.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Overview of proteoform diversity, molecular ontogeny, and functional examples of reference and alternative proteoforms across regulatory layers (KRAS, DMD, FOXP1, CDKN2A, IκBα). |
| Fig 2 | Combinatorial complexity of protein variation, showing how genetic, transcriptomic, translational, and post-translational changes interact to shape function (e.g., in Histone tails, MAPT, KRAS, CFTR). |
| Fig 3 | The map–perturb–predict conceptual framework for proteoform medicine, outlining systematic mapping, experimental manipulation, and computational prediction strategies. |
| Fig 4 | Proteoform-resolved networks reveal functional rewiring beyond gene-level models, illustrating loss, gain, and change of interactions driving unique disease phenotypes. |
| Fig 5 | Proteoform-resolved therapeutic strategies across molecular and network scales, categorizing interventions into node correction, edge correction, and neighborhood correction. |

## Discussion

### Strengths
- Provides a highly structured, comprehensive conceptual framework (map-perturb-predict) to transition biology from a gene-centric to a proteoform-centric perspective.
- Effectively bridges the gap between analytical proteomics technologies (like top-down MS) and clinical/therapeutic applications via network biology principles.

### Limitations
- Acknowledges that current mapping technologies (especially top-down proteomics) are limited by throughput, sensitivity, and mass range (struggling with proteins >30-45 kDa).
- Predictive models (like AlphaFold) and current interaction databases are heavily biased toward canonical "reference" proteins, limiting generalizability to alternative proteoforms.

### Future Work
- Development of technologies capable of high-throughput, intact proteoform sequencing and quantification at the single-cell level.
- Shifting experimental validations to human-relevant models (organoids, xenografts) rather than simple models that may not conserve proteoform diversity.
- Creating standardized, ancestry-aware, and clinically actionable annotation systems (similar to ClinGen) to support decision-making and biomarker application in diverse populations.

## Personal Notes



## Related Papers

- Smith, L. M. et al. (2021). The human proteoform project: defining the human proteome. *Science Advances*, 7, eabk0734.
- Aebersold, R. et al. (2018). How many human proteoforms are there? *Nature Chemical Biology*, 14, 206–214.
- Sahni, N. et al. (2015). Widespread macromolecular interaction perturbations in human genetic disorders. *Cell*, 161, 647–660.