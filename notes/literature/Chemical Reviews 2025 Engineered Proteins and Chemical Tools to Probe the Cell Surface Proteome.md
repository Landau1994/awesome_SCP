---
title: Engineered Proteins and Chemical Tools to Probe the Cell Surface Proteome
authors:
  - Kevin K. Leung
  - Kaitlin Schaefer
  - Zhi Lin
  - Zi Yao
  - James A. Wells
aliases:
  - Surfaceomics Review 2025
tags:
  - literature
  - paper
  - proteomics
  - surfaceome
  - immunopeptidomics
category: literature
date_created: 2025-05-14
Journal: Chemical Reviews
Year: 2025
---

# Engineered Proteins and Chemical Tools to Probe the Cell Surface Proteome

## Citation

> [!cite] Reference
> **Title**：Engineered Proteins and Chemical Tools to Probe the Cell Surface Proteome
> **Authors**: Kevin K. Leung, Kaitlin Schaefer, Zhi Lin, Zi Yao, and James A. Wells
> **Year**: 2025
> **Journal**: Chemical Reviews
> **DOI**: 10.1021/acs.chemrev.4c00554

## Abstract

The cell surface proteome, or surfaceome, acts as the primary hub for cellular communication with the external environment. Despite its functional importance in disease, it remains a "difficult-to-drug" compartment, with approved drugs targeting fewer than 50 surface proteins. In the past decade, advancements in proteomics have enabled researchers to study the surfaceome's complexity through specialized labeling, enrichment, and analytical strategies. This review provides an overview of surfaceomics methods for measuring protein expression and identifying novel targets. It highlights breakthroughs in proximity labeling proteomics (PLP)—including enzymatic and photoaffinity-based techniques—for mapping protein-protein interactions and membrane complexes in situ. Furthermore, the review covers the role of extracellular post-translational modifications (PTMs), specifically glycosylation and proteolytic remodeling, and discusses the emerging field of the immunopeptidome (MHC-I peptide presentation) and its therapeutic potential for neo-epitope discovery.

## Key Points

- The surfaceome occupies a volume roughly 100-fold smaller than the cytosol, and while protein density is similar, absolute protein amounts are significantly lower, necessitating robust enrichment.
- Membrane proteins operate in a two-dimensional environment, limiting their degrees of freedom compared to cytosolic proteins, which allows for faster association rates and enables rapid cellular signaling.
- Proximity labeling proteomics (PLP) methods, such as [[APEX2]], [[TurboID]], and photocatalytic platforms like [[μMap]], allow for in situ "snapshot" mapping of protein neighborhoods without the need for membrane solubilization.
- Unlike intracellular PTMs which are often reversible, extracellular PTMs (glycosylation, proteolysis) are predominantly irreversible and serve as critical regulators of cellular state and pathology.
- Advances in [[Mass Spectrometry]] ([[DIA]], [[DIA-PASEF]]) and bioinformatics ([[NetMHCpan]], [[AlphaFold]]) have revolutionized the study of the immunopeptidome, enabling the discovery of disease-associated neo-antigens.

## Methods

### Sample Preparation
- Method used: [[Membrane Fractionation]], [[Chemical Labeling]] ([[sulfo-NHS-biotin]]), [[Proximity Labeling]] ([[APEX]], [[BioID]], [[TurboID]], [[miniSOG]], [[PUP-IT]], [[EMARS]], [[μMap]]), [[Glycoprotein Enrichment]] ([[CSC]], [[lectin pull-down]]), [[Mild-Acid Elution]], [[Immunoprecipitation]] ([[anti-MHC antibodies]]).
- Cell type: Mammalian cell lines, primary tissues, immune cells.
- Number of cells: Varies by method; ranges from 0.5 × 10^6 to 10^9 cells for immunopeptidomics.

### Data Analysis
- Software: [[NetMHCpan]], [[AlphaFold]], [[GSEA]], [[PSEA-quant]], [[PEAKS]], [[MHCquant]], [[SpectMHC]].
- Downstream: [[Mass Spectrometry]] ([[DDA]], [[DIA]], [[DIA-PASEF]], [[MRM]], [[PRM]]), [[NGS]], [[transcriptomics]].

## Results

### Main Findings
1. The surfaceome exhibits unique physical properties, including 100-fold smaller volume than the cytosol and restricted degrees of freedom for membrane proteins, facilitating high-speed lateral signaling.
2. PLP techniques have overcome the challenges of traditional affinity-based solubilization, allowing for high-resolution mapping of transient membrane protein complexes.
3. Extracellular proteolysis is a global modification that regulates signaling via shedding and neo-N-termini generation; cell surface N-terminomics using engineered subtiligases can successfully map these events.
4. Immunopeptidomics reveals that the peptide repertoire is more dynamic than previously thought, involving non-canonical sources, and is highly responsive to pathological transformations and therapeutic perturbations.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Schematic of cell surfaceome enrichment techniques. |
| Fig 2 | Annotation and analysis of the surfaceome. |
| Fig 3 | Efficacy of antibody modalities based on receptor copy number. |
| Fig 4 | Overview of proximity labeling proteomics (PLP) methods and reactive intermediates. |
| Fig 5 | Protein glycosylation: major PTM on the cell surface. |
| Fig 6 | Cell surface proteolysis as an irreversible molecular switch. |
| Fig 7 | Basics of MHC-I peptide presentation and processing. |
| Fig 8 | Profiling the immunopeptidome via mass spectrometry workflows. |
| Fig 9 | Platforms for mapping disease-induced immunopeptidome. |

## Discussion

### Strengths
- Provides a deep, mechanistic understanding of the differences between the surfaceome and cytosol.
- Excellent synthesis of chemical biology tools (e.g., photocatalysts) and clinical applications (e.g., ADCs, CAR-T, TCEs).
- Strong focus on actionable target discovery in oncology.

### Limitations
- Many high-resolution PLP studies are still confined to 2D cell cultures, which do not fully recapitulate the heterogeneity of human tissue.
- Low abundance of the surfaceome (compared to the cytosolic proteome) makes single-cell surfaceomics technically demanding.
- Current validation workflows for interactomics data can be laborious and difficult to perform in high throughput.

### Future Work
- Development of robust, tissue-based surfaceomics methods that do not rely solely on paraffin-embedded incompatible antibodies.
- Integration of spatial proteomics and single-cell technologies to analyze patient-derived samples.
- Expansion of integrated bioinformatics platforms containing curated, experimentally validated PLP interaction data.

## Personal Notes

-