---
title: Single-Cell Spatial Proteomics Uncovers Molecular Interconnectivity among Hallmarks of Aging
authors:
  - Seungmin Yoo
  - Christopher Young
  - Liying Li
  - Lingraj Vannur
  - Junming Zhuang
  - Fan Zheng
  - Meiying Wu
  - Julie K. Andersen
  - Chuankai Zhou
aliases:
   - Single-Cell Spatial Proteomics Uncovers Molecular Interconnectivity among Hallmarks of Aging
   - Yoo et al., 2026
tags:
  - literature
  - paper
  - aging
  - spatial-proteomics
  - yeast
category: literature
date_created: 2026-02-28
Journal: bioRxiv
Year: 2026
---

# Single-Cell Spatial Proteomics Uncovers Molecular Interconnectivity among Hallmarks of Aging

## Citation

> [!cite] Reference
> **Title**：Single-Cell Spatial Proteomics Uncovers Molecular Interconnectivity among Hallmarks of Aging
> **Authors**: Seungmin Yoo, Christopher Young, Liying Li, Lingraj Vannur, Junming Zhuang, Fan Zheng, Meiying Wu, Julie K. Andersen, and Chuankai Zhou
> **Year**: 2026
> **Journal**: bioRxiv
> **DOI**: https://doi.org/10.64898/2026.02.26.708335

## Abstract

Aging is accompanied by conserved hallmarks including genomic instability, epigenetic alterations, loss of proteostasis, and mitochondrial dysfunction, but how these processes emerge and become mechanistically linked remains unclear. Here we leverage a proteome-wide, single-cell, subcellular atlas of protein expression, localization, and aggregation across yeast replicative aging to map hallmark-linked remodeling in its spatial context. We identify hundreds of previously unappreciated molecular changes that underlie major hallmarks of aging and show that hallmark phenotypes frequently manifest as compartment-specific erosion of spatial confinement, relocalization, and aggregation. 91.6% human orthologs of these hallmark-linked yeast proteins also change during human aging. Integrating these spatial phenotypes reveals many molecular connections linking different hallmarks. Temporal analysis suggests that disorganization of nucleolar ribosome biogenesis, proteostasis decline, and mitochondrial dysfunction precede other hallmarks. Together, our findings substantially deepen the molecular underpinnings of aging hallmarks and provide a framework for linking them into a hierarchical sequence of cellular failures.

## Key Points

- **Spatial Proteome Erosion**: Aging is characterized by a progressive loss of spatial organization, including the loss of compartmental confinement, protein relocalization, and widespread aggregation, which disrupts spatially organized cellular reactions.
- **Interconnected Hallmarks**: The study maps molecular "conduits" connecting distinct aging hallmarks. For instance, proteostasis defects and impaired mitochondrial import lead to the loss of shared DNA repair enzymes (e.g., Ogg1) from mitochondria, directly linking proteostasis collapse to mitochondrial genomic instability.
- **Temporal Hierarchy**: Hallmark trajectories reveal two distinct groups. **Group 1** (Nucleolar disruption, proteostasis decline, and mitochondrial dysfunction) progresses rapidly and early. **Group 2** (Epigenetic alterations, genomic instability, etc.) emerges more gradually, suggesting early Group 1 failures may drive downstream Group 2 hallmarks.
- **Nucleolar Vulnerability**: The nucleolus and ribosome biogenesis machinery are identified as early, critical failure points. Key biogenesis factors escape the nucleolus and aggregate, potentially acting as a primary driver of downstream proteostasis collapse.

## Methods

### Sample Preparation
- **Method used**: [[High-content confocal microscopy]] of a seamless mNeonGreen (mNG) tagging library.
- **Cell type**: [[Saccharomyces cerevisiae]] (strain BY4741); Replicative aging mother cells enriched via biotinylation and magnetic sorting.
- **Number of cells**: The localization classifier was applied to 79.4 million cells across ~5,661 strains; specific analyses focused on age-stratified cohorts.

### Data Analysis
- **Software**: [[Deep Learning]] pipeline (Dual-stream architecture: [[DeepLoc]] 2D CNN + 3D ResNet-50), [[Fiji]]/[[ImageJ]] for processing, [[Python]] (scikit-learn) for embedding.
- **Downstream**: [[t-SNE]] for localization maps, [[GeneMANIA]] for interaction networks, Ensemble-model quantification of localization scores.

## Results

### Main Findings
1.  **Genomic & Epigenetic Instability**: Aged cells show increased DNA repair factors (Rad52, Rad1) and nuclear shape abnormalities. A critical finding is the compartment-specific loss of Base Excision Repair (BER) enzymes from mitochondria while they remain abundant in the nucleus, linking import defects to mtDNA instability.
2.  **Mitochondrial & Metabolic Collapse**: Mitochondrial dysfunction is stepwise, starting with Fe-S cluster biogenesis failure, followed by membrane organization defects, and ending with bioenergetic collapse. Nutrient transporters (glucose, amino acid, phosphate) are downregulated or mislocalized, decoupling sensing from availability.
3.  **Ribosome Biogenesis Failure**: Ribosome biogenesis factors lose nucleolar confinement and aggregate early in aging. This "spatial failure mode" uncouples maturation steps, likely generating aberrant ribosomes that exacerbate proteotoxic stress.
4.  **Conservation**: 91.6% of the yeast proteins identified as hallmark-linked have human orthologs that show age-associated abundance changes in human proteomics datasets, particularly in ribosome biogenesis and mitochondrial pathways.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Molecular changes underlying genomic instability and epigenetic alterations: Increase in DNA damage markers (Rfa1, Rad52), nuclear shape defects, loss of mitochondrial BER enzymes (Apn1), and remodeling of histone modifiers (Dot1, Rpd3L). |
| Fig 2 | Disabled autophagy and loss of proteostasis: Defects in the Cvt pathway (Ape1 puncta), accumulation of P-bodies, mislocalization of proteasome 19S subunits, and aggregation of Ubp10 linking proteostasis to silencing. |
| Fig 3 | Organelle proteostasis and rejuvenation: Mitochondrial and peroxisomal protein aggregation, formation of mitochondria-derived compartments, and restoration of organelle health in daughter cells via asymmetric division. |
| Fig 4 | Deregulated nutrient sensing: Loss of plasma membrane transporters for amino acids, glucose, and phosphate; mislocalization of nutrient sensors (Gtr1/2, Opi1). |
| Fig 5 | Dysfunctional mitochondria: Collapse of Fe-S cluster biogenesis, protein aggregation, cytosolic mislocalization of mitochondrial enzymes, and a stepwise trajectory of mitochondrial failure. |
| Fig 6 | Nucleolus and ribosome biogenesis defects: Widespread loss of nucleolar confinement for SSU/LSU assembly factors, aggregation of processing enzymes, and decoupling of transcription from processing. |
| Fig 7 | Summary of interconnections and temporal relationships: A proteome-scale map of links between hallmarks. Temporal analysis separates hallmarks into early-onset (Group 1: Nucleolus, Proteostasis, Mito) and gradual (Group 2) categories. |

## Discussion

### Strengths
- **Spatial Resolution**: Moves beyond bulk proteomics to identify compartment-specific failures (e.g., specific loss of mitochondrial enzymes despite high total cellular abundance).
- **Scale**: Comprehensive coverage of >94% of the yeast proteome at single-cell resolution across the replicative lifespan.
- **Temporal Insight**: Allows for the construction of time-resolved trajectories to infer the sequence of aging events.

### Limitations
- **Model System**: While ortholog analysis suggests conservation, the study is performed in yeast, requiring validation of specific spatial mechanisms in mammalian systems.
- **Observational Nature**: The high-throughput nature identifies correlations and trajectories; while mechanistic links are inferred from function, causal perturbations for all identified links are not feasible in a single study.

### Future Work
- Investigating if interventions that stabilize "Group 1" hallmarks (e.g., nucleolar integrity) delay the onset of "Group 2" hallmarks.
- Validating the compartment-specific "erosion" of proteins (like BER enzymes) in mammalian aging models.
- Exploring the causal role of aberrant ribosomes produced by the disorganized nucleolus in driving age-related proteotoxicity.

## Personal Notes

## Related Papers

- [[Yoo et al., 2026a]] (Companion study establishing the single-cell atlas)
- [[López-Otín et al., 2013]] / [[López-Otín et al., 2023]] (Hallmarks of Aging frameworks)
- [[Janssens et al., 2015]] (Protein biogenesis machinery as a driver of aging)
- [[Denoth Lippuner et al., 2014]] (Yeast as a model for aging)