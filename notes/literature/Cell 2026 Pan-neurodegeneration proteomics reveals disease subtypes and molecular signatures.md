---
title: Pan-neurodegeneration proteomics reveals disease subtypes and molecular signatures
authors:
- Him K. Shrestha
- Huan Sun
- Jay M. Yarbro
- Dong Geun Lee    
- Danting Liu
- Erming Wang
- Xusheng Wang
- Bin Zhang
- Junmin Peng
aliases: 
- PanNDA    
- Pan-neurodegeneration atlas 
tags:
- literature
- paper
- proteomics
- neurodegeneration
- AD
- LBD
category: literature
date_created: 2026-03-25
Journal: Cell
    
Year: 2026
    

---

# Pan-neurodegeneration proteomics reveals disease subtypes and molecular signatures

## Citation

> [!cite] Reference Title: Pan-neurodegeneration proteomics reveals disease subtypes and molecular signatures Authors: Him K. Shrestha, Huan Sun, Jay M. Yarbro, Dong Geun Lee, Danting Liu, Erming Wang, ..., Xusheng Wang, Bin Zhang, Junmin Peng Year: 2026 Journal: Cell DOI: [https://doi.org/10.1016/j.cell.2026.02.026](https://doi.org/10.1016/j.cell.2026.02.026)

## Abstract

The authors present the **Pan-neurodegeneration atlas (PanNDA)**, a deep multilayer proteomic analysis of **2,279 human brain samples** across six major neurodegenerative diseases (NDs): Alzheimer's (AD), Lewy body dementia (LBD), FTLD-TDP, PSP/FTLD-tau, vascular dementia (VAD), and Parkinson's disease (PD). By integrating whole proteome, detergent-insoluble proteome, and PTM (phosphorylation and ubiquitination) data, they identified distinct molecular subtypes for each disease (e.g., three in AD, four in LBD). Inter-disease comparisons revealed shared alterations, such as the upregulation of **GPNMB** and downregulation of **NPTX2**, alongside disease-specific hubs and drivers.

## Key Points

- **Deep Proteomic Coverage**: Identified an average of 14,767 proteins per disease group using an optimized TMT-LC/LC-MS/MS platform.
    
- **Molecular Subtyping**: Unsupervised clustering revealed distinct subtypes driven by different biological pathways:
    
    - **AD**: Synaptic signaling (ST1), cytoskeletal regulation (ST2), and BBB transport (ST3).
        
    - **LBD**: Mitochondrial function (ST1), lipid metabolism (ST2), transport (ST3), and inflammation (ST4).
        
- **Shared vs. Specific Signatures**: While most alterations are disease-specific, GPNMB (lysosomal activation) and NPTX2 (synaptic regulation) emerged as universal markers of neurodegeneration.
    
- **Network Drivers**: Identified global hub proteins (GHPs) like **MDK** in AD and **CD44** in FTLD-TDP as potential disease drivers.
    

## Methods

### Sample Preparation

- **Method used**: Multiplexed Tandem Mass Tag (TMT) labeling combined with 2D liquid chromatography and tandem mass spectrometry (LC/LC-MS/MS).
    
- **Sample types**: Postmortem human brain tissue (whole lysate and detergent-insoluble fractions) and CSF.
    
- **Data layers**: Whole proteome, detergent-insoluble proteome, phosphoproteome, and ubiquitinome.
    

### Data Analysis

- **Software**: **JUMP** software suite for search and quantification, **JUMP-ptm** for unenriched PTMs, and **MEGENA** for co-expression network analysis.
    
- **Downstream**: Consensus clustering for subtyping, key driver analysis (KDA) for hub identification, and Slingshot for pseudo-time trajectory analysis.
    

## Results

### Main Findings

1. **Multilayer Integration**: The detergent-insoluble proteome identified aggregates beyond A$\beta$ and tau, such as spliceosome components (U1-70K) in AD.
    
2. **Subtype Robustness**: AD subtypes identified in brain tissue were validated in independent cohorts and detectable in CSF with high classification accuracy ($AUC \approx 0.89$).
    
3. **Cross-Disease Taxonomy**: Pseudo-time analysis mapped NDs into three distinct lineages, highlighting molecular progression from control/MCI states to advanced disease.
    

### Figures

|**Figure**|**Description**|
|---|---|
|**Fig 1**|Experimental workflow and sample distribution (n=2,279) across 6 NDs.|
|**Fig 2**|AD molecular characterization; reveals 3 subtypes (Synaptic, Cytoskeletal, BBB).|
|**Fig 3**|LBD characterization; identifies 4 subtypes and SNCA-related PTM dysregulation.|
|**Fig 4**|FTLD-TDP proteomics; prioritizes CD44 and GPNMB as key associated proteins.|
|**Fig 5**|Inter-disease comparison of DAPs; highlights shared (GPNMB, NPTX2) and specific proteins.|
|**Fig 6**|MEGENA network modules and Global Hub Proteins (GHPs) like MDK.|

## Discussion

### Strengths

- **Unprecedented Scale**: Largest pan-ND proteomic study to date, providing a comprehensive "atlas" for the community.
    
- **Technical Depth**: Integration of insoluble fractions and PTMs captures proteinopathy dynamics missed by transcriptomics.
    

### Limitations

- **Cohort Diversity**: Samples predominantly from individuals of Caucasian background.
    
- **Bulk Proteomics**: Analysis of bulk tissue may obscure cell-type-specific signatures compared to single-cell methods.
    
- **Small Cohorts for Some NDs**: PSP and PD findings lack independent validation due to smaller sample sizes.
    

### Future Work

- Exploring identified brain subtypes as biomarkers in longitudinal biofluid studies.
    
- Hypothesis-driven investigation into the causative roles of hub proteins like MDK and GPNMB.
    

## Personal Notes

The PanNDA resource is accessible via an interactive website: [https://penglab.shinyapps.io/pannda](https://www.google.com/search?q=https://penglab.shinyapps.io/pannda).

## Related Papers

- Bai et al. (2020) - _Neuron_ (AD proteomic networks).
    
- Johnson et al. (2022) - Nat. Neurosci. (AD multilayer analysis).
    

---

Would you like me to extract more details on the specific proteins associated with the **AD ST3 (BBB transport)** subtype?