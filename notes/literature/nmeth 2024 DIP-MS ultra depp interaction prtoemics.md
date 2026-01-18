---
title: "DIP-MS: ultra-deep interaction proteomics for the deconvolution of protein complexes"
authors:
  - Fabian Frommelt
  - Andrea Fossati
  - Federico Uliana
  - Fabian Wendt
  - Peng Xue
  - Moritz Heusel
  - Bernd Wollscheid
  - Ruedi Aebersold
  - Rodolfo Ciuffa
  - Matthias Gstaiger
aliases:
   - DIP-MS paper
   - Frommelt et al. 2024
tags:
  - literature
  - paper
  - proteomics
  - mass-spectrometry
  - protein-complexes
category: literature
date_created: 2024-05-22
Journal: Nature Methods
Year: 2024
---

# DIP-MS: ultra-deep interaction proteomics for the deconvolution of protein complexes

## Citation

> [!cite] Reference
> **Title**: DIP-MS: ultra-deep interaction proteomics for the deconvolution of protein complexes
> **Authors**: Fabian Frommelt, Andrea Fossati, Federico Uliana, Fabian Wendt, Peng Xue, Moritz Heusel, Bernd Wollscheid, Ruedi Aebersold, Rodolfo Ciuffa & Matthias Gstaiger
> **Year**: 2024
> **Journal**: Nature Methods
> **DOI**: 10.1038/s41592-024-02211-y

## Abstract

Most proteins are organized in macromolecular assemblies, which represent key functional units regulating and catalyzing most cellular processes. Affinity purification combined with mass spectrometry (AP–MS) is the standard for identifying interacting proteins but cannot resolve complex isoforms concurrently present in a sample from a single experiment. Here the authors introduce **deep interactome profiling by mass spectrometry (DIP-MS)**, which combines AP with blue-native-PAGE (BNP) separation, data-independent acquisition (DIA) mass spectrometry, and deep-learning-based signal processing (**PPIprophet**). This method resolves complex isoforms sharing the same bait protein in a single experiment. Applied to the human prefoldin family, DIP-MS resolved distinct prefoldin holo- and subcomplex variants, complex–complex interactions, and a novel prefoldin homolog (PFDh) containing the subunit PDRG1.

## Key Points

- **Novel Method (DIP-MS)**: Integrates affinity purification (enrichment) with native gel fractionation (resolution) and deep-learning-based deconvolution to identify multiple distinct protein complexes from a single bait protein.
- **PPIprophet Framework**: A deep neural network (DNN) trained on >1.5 million binary interactions that predicts protein-protein interactions (PPIs) and deconvolves complex profiles with high precision (ROC of 0.995).
- **Superior Performance**: DIP-MS provides broader dynamic range, higher resolution, and denser interaction networks compared to traditional SEC–MS or reciprocal AP–MS workflows.
- **Biological Discovery**: Identified a new prefoldin complex isoform (**PFDh**) where PDRG1 replaces PFDN4, and mapped the extensive client landscape of the **PAQosome** chaperone complex.

## Methods

### Sample Preparation
- **Method used**: Affinity Purification (AP) followed by Blue-Native-PAGE (BNP) fractionation.
- **Cell type**: HEK293 (Human Embryonic Kidney) cells.
- **Scale**: Purified bait protein complexes (~1–3 µg) are separated on a BNP gel, cut into ~70 slices (1 mm each), and processed in a miniaturized 96-well filter plate format.
- **Measurement**: High-throughput DIA–MS (up to 60 samples per day).

### Data Analysis
- **Software**: 
    - **PPIprophet**: Deep-learning tool for PPI prediction and complex deconvolution.
    - **CCprofiler**: For initial peptide correlation filtering.
    - **Spectronaut**: For DIA data searching and quantification.
- **Downstream**: MCL clustering for data-driven discovery; AlphaFold2/ColabFold for structural modeling of identified complexes.

## Results

### Main Findings
1. **Enhanced Resolution**: DIP-MS successfully resolved overlapping complexes (e.g., PFD, PFDL, and PAQosome) that share the same bait protein (PFDN2) but have different molecular weights.
2. **Detection of Low-Abundance Entities**: The bait enrichment step allowed for a 4.4-log dynamic range, significantly better than SEC–MS (3.8-log), enabling the detection of sub-stoichiometric components and rare complex-client interactions.
3. **Identification of PFDh**: Discovery of a previously unknown prefoldin homolog (PFDh) where PDRG1 functions as a core subunit instead of PFDN4. Structural modeling confirmed the feasibility of this "jellyfish" architecture.
4. **PAQosome Client Mapping**: Identified 92 proteins across 19 complexes as PAQosome clients, including RNA polymerases, snRNA assemblies, and the APC/C complex.

### Figures

| Figure | Description |
|--------|-------------|
| **Fig 1** | Overview of the DIP-MS workflow: AP → BNP → Gel Slicing → DIA-MS → PPIprophet analysis. |
| **Fig 2** | Benchmarking results showing DIP-MS recovers more interactors and has higher peak resolution than SEC–MS or AP–MS. |
| **Fig 3** | Deconvolution of PFD and PFDL assemblies and determination of subunit stoichiometry using PFDN2 and UXT baits. |
| **Fig 4** | Discovery and structural modeling of the PDRG1-containing prefoldin homolog (PFDh). |
| **Fig 5** | Mapping of PFD and CCT/TRiC-PFD clients and shuttling substrates (e.g., tubulins, actins). |
| **Fig 6** | Comprehensive map of the PAQosome chaperone network and its diverse client complexes. |

## Discussion

### Strengths
- **Single-Bait Resolution**: Can identify multiple complex instances from one experiment, reducing the need for dozens of reciprocal AP–MS runs.
- **Efficiency**: Miniaturized protocol requires 10x less material than traditional chromatography-based separation and significantly increases throughput.
- **Knowledge-Free Discovery**: The deep-learning framework allows for the discovery of new complexes without relying solely on existing databases.

### Limitations
- **Signal Dilution**: Extensive fractionation can dilute low-abundant proteins, potentially compromising the profile quality for very rare interactors.
- **Complex Stability**: Some large or transient supercomplexes might be sensitive to the native-PAGE separation conditions, leading to partial disassembly.

### Future Work
- Application of DIP-MS under cellular perturbations to study the dynamic remodeling of the interactome.
- Further functional characterization of the newly discovered PFDh complex.

## Personal Notes

- The integration of "enrichment" (AP) and "separation" (BNP) addresses the primary weakness of each method (AP-MS's lack of complex resolution and SEC-MS's sensitivity limits).
- PPIprophet's use of a DNN for coelution analysis represents a significant step forward from simple correlation-based metrics.

## Related Papers

- Heusel, M. et al. (2019). Complex-centric proteome profiling by SEC-SWATH-MS. *Mol. Syst. Biol.*
- Cloutier, P. et al. (2020). ASDURF is a novel prefoldin-like subunit of the PAQosome. *J. Proteome Res.*
- Skinnider, M. A. & Foster, L. J. (2021). Meta-analysis defines principles for the design and analysis of co-fractionation mass spectrometry experiments. *Nat. Methods.*