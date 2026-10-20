# Awesome Single-Cell Proteomics [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of resources, tools, databases, and publications for single-cell proteomics (SCP) research.

Single-cell proteomics (SCP) enables the quantification of proteins at single-cell resolution, revealing cellular heterogeneity that bulk measurements obscure. Recent advances in mass spectrometry sensitivity, sample preparation miniaturization, and computational methods have made it possible to quantify thousands of proteins from individual cells.

## Contents

- [Sample Preparation Methods](#sample-preparation-methods)
- [Data Acquisition Strategies](#data-acquisition-strategies)
- [Mass Spectrometry Platforms](#mass-spectrometry-platforms)
- [Software & Tools](#software--tools)
  - [Data Processing](#data-processing)
  - [Quality Control](#quality-control)
  - [Data Analysis](#data-analysis)
- [Databases & Datasets](#databases--datasets)
- [Reviews & Tutorials](#reviews--tutorials)
- [Key Publications](#key-publications)
- [Contributing](#contributing)

---

## Sample Preparation Methods

### Isobaric Labeling-Based

- **[SCoPE2](https://doi.org/10.1186/s13059-021-02267-5)** - Isobaric-label single-cell proteomics using a carrier channel; the published study measured 1,490 cells. Throughput and depth depend on the workflow.
- **[pSCoPE](https://doi.org/10.1038/s41592-023-01830-1)** - Prioritized SCoPE combines prioritized acquisition with broader proteome measurements; see the [method note](notes/methods/pSCoPE.md).

### Label-Free & Multiplexed DIA

- **[plexDIA](https://doi.org/10.1038/s41587-022-01389-w)** - Multiplexed DIA using non-isobaric labels. The original human-cell study reported approximately 1,000 proteins per cell and 98% completeness within a multiplexed set; later chemistries and workflows have different performance.
- **[nDIA](notes/methods/nDIA.md)** - Narrow-window DIA. The 4-Th/6-ms setting belongs to the later Chip-Tip single-cell benchmark; it is not the definition or a universal default of nDIA.
- **[diaPASEF](https://doi.org/10.1038/s41592-020-00998-0)** - Combines trapped ion mobility, parallel accumulation–serial fragmentation and DIA.
- **[SC-pSILAC](https://doi.org/10.1016/j.cell.2025.03.002)** - Single-cell pulsed SILAC for joint analysis of protein abundance and turnover dynamics.

### Miniaturized Sample Preparation

- **[Chip-Tip](https://doi.org/10.1038/s41592-024-02558-2)** - Integrated proteoCHIP-to-Evotip workflow. Its Orbitrap Astral/40-samples-per-day HeLa benchmark reported a median of 5,204 protein identifications per cell; see the [conditions](notes/methods/Chip-Tip.md).
- **[nPOP](https://doi.org/10.1038/s41596-024-01033-8)** - Parallel nanoliter-droplet preparation on slides. The reported 3,000–3,700 proteins per human cell refer to a specific combined plexDIA workflow, not preparation alone.
- **[nanoPOTS](https://doi.org/10.1038/s41467-018-03367-w)** - Nanodroplet Processing in One pot for Trace Samples; the original study characterized low-cell-number samples. Later implementations extended the platform to individual cells.
- **[Nested NanoPOTS (N2)](https://doi.org/10.1038/s41467-021-26514-2)** - Nested-well implementation with 243 nanowells per chip; capacity and analytical throughput are different quantities.
- **[mPOP](https://doi.org/10.1101/399774)** - Minimal ProteOmic sample Preparation; see the [method note](notes/methods/mPOP.md) for scope and original source.

### Automated Platforms

- **[CellenONE](https://www.scienion.com/products/single-cell-dispensers/)** - Image-guided single-cell isolation and dispensing used in workflows such as Chip-Tip and nPOP.
- **[cellenONE + Evosep](https://www.evosep.com/)** - Integrated workflow combining cell dispensing with robust LC separation.

---

## Data Acquisition Strategies

| Strategy | Main distinction | Interpretation |
|----------|------------------|----------------|
| **DDA** | Selects precursors for fragmentation | Label-free and labeled workflows are possible |
| **DIA** | Acquires predefined precursor windows | Performance depends on window design and analysis |
| **nDIA** | Narrower DIA isolation windows | Needs suitable acquisition speed and ion sampling |
| **plexDIA** | Non-isobaric sample multiplexing with DIA | Distinguish within-set completeness from across-run coverage |
| **pSCoPE** | Prioritized acquisition within a broader workflow | Not restricted to a small targeted panel |
| **diaPASEF** | DIA with trapped ion mobility and PASEF | Instrument- and workflow-dependent |

Depth and throughput should be compared under matched cell types, chromatography, instruments and error-control settings. This table does not assign a universal performance ranking.

---

## Mass Spectrometry Platforms

### Optimized for Single-Cell

- **[Bruker timsTOF SCP](https://www.bruker.com/en/products-and-solutions/mass-spectrometry/timstof.html)** - timsTOF instrument designed for low-input and single-cell applications.
- **[Bruker timsTOF Ultra 2](https://www.bruker.com/en/products-and-solutions/mass-spectrometry/timstof.html)** - timsTOF model for sensitive proteomics; use model-specific documentation for specifications.
- **[Thermo Orbitrap Astral](https://doi.org/10.1038/s41587-023-02099-7)** - Hybrid mass spectrometer combining an Orbitrap and Astral analyzer; used in deep SCP workflows.
- **Thermo Exploris Series** - Orbitrap platforms used in proteomics; [platform overview](notes/tools/Orbitrap.md).

### LC Systems

- **[Evosep One](https://www.evosep.com/evosep-one/)** - LC platform with standardized methods, including Whisper workflows.
- **[IonOpticks Aurora Series](https://ionopticks.com/)** - High-performance columns optimized for low-flow proteomics.

---

## Software & Tools

### Data Processing

| Tool | Platform | Description | Link |
|------|----------|-------------|------|
| **MaxQuant** | Windows GUI; Linux CLI support | Quantitative proteomics with LFQ and TMT support; check release requirements | [Link](https://www.maxquant.org/) |
| **DIA-NN** | Windows / Linux | DIA analysis with multiplex-aware workflows | [Link](https://github.com/vdemichev/DiaNN) |
| **Spectronaut** | Windows | Leading vendor software for DIA analysis (directDIA+) | [Link](https://biognosys.com/software/spectronaut/) |
| **Proteome Discoverer** | Windows | Workflow-based MS data analysis | [Link](https://www.thermofisher.com/us/en/home/industrial/mass-spectrometry/liquid-chromatography-mass-spectrometry-lc-ms/lc-ms-software/multi-omics-data-analysis/proteome-discoverer-software.html) |
| **FragPipe** | Release-dependent | Integrated analysis workflows using MSFragger and other tools | [Link](https://fragpipe.nesvilab.org/) |
| **AlphaPeptDeep** | Python | Modular deep learning framework for peptide property prediction | [GitHub](https://github.com/MannLabs/alphapeptdeep) |

### Quality Control

| Tool | Description | Link |
|------|-------------|------|
| **DO-MS** | Interactive QC and optimization for LC-MS/MS | [do-ms.slavovlab.net](https://do-ms.slavovlab.net/) |
| **QuantQC** | QC reports for nPOP experiments | [GitHub](https://github.com/SlavovLab/QuantQC) |
| **RawDiag** | Diagnostic plots for raw MS data | [GitHub](https://github.com/fgcz/rawDiag) |

### Data Analysis

#### R Packages

| Package | Description | Link |
|---------|-------------|------|
| **scp** | Bioconductor package for MS-based SCP analysis | [Bioconductor](https://bioconductor.org/packages/scp/) |
| **scpdata** | Curated SCP datasets in scp format | [Bioconductor](https://bioconductor.org/packages/scpdata/) |
| **QFeatures** | Quantitative proteomics data management | [Bioconductor](https://bioconductor.org/packages/QFeatures/) |
| **SCPline** | Interactive Shiny framework for SCP preprocessing | [Oxford Academic](https://academic.oup.com/bib/article/26/3/bbaf256/8156470) |

#### Python Packages

| Package | Description | Link |
|---------|-------------|------|
| **SCPDA** | Python framework for DIA-based SCP analysis and benchmarking | [GitHub](https://github.com/WangJianwei1991/SCPDA) |
| **SCeptre** | Processing workflow for isobaric SCP; use the project installation instructions | [GitHub](https://github.com/bfurtwa/SCeptre) |
| **scProtVelo** | Modeling translation dynamics and cell velocity | [Science](https://www.science.org/doi/10.1126/science.adr8785) |
| **pyteomics** | MS data parsing and analysis | [GitHub](https://github.com/levitsky/pyteomics) |
| **alphapept** | Modular framework for peptide identification and quantification | [GitHub](https://github.com/MannLabs/alphapept) |

---

## Databases & Datasets

### Comprehensive Databases

- **[SPDB](https://scproteomicsdb.com/)** - Homepage snapshot on 2026-10-20: 143 datasets, 398,038,707 cells and 8,304 proteins across four species. Totals combine MS and antibody-based technologies; they are not MS-only cell counts or proteins per cell.
- **[SingPro](https://singpro.idrblab.net/)** - Single-cell and multimodal protein-data knowledge base. See the [database note](notes/databases/SingPro.md) for the distinction between the 2024 article and current 2.0 release.
- **[Slavov Lab Data Repository](https://scp.slavovlab.net/data)** - Curated datasets organized by publication with linked protocols.

### Benchmark Datasets

- **[scpdata (Bioconductor)](https://bioconductor.org/packages/scpdata/)** - Published SCP and low-input datasets in standardized structures; dataset totals vary by package release.
- **[SCoPE2 Macrophage Dataset](https://doi.org/10.1186/s13059-021-02267-5)** - 3,042 proteins across a matrix of 1,490 monocytes/macrophages, not 3,042 measurements in every cell.

---

## Reviews & Tutorials

### Review Articles

- [Recent methodological advances towards single-cell proteomics (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10749393/) - Review by Kim, Kamarulzaman and Taniguchi.
- [Single-Cell Proteomics Using Mass Spectrometry (2025 preprint)](https://arxiv.org/abs/2502.11982) - Momenzadeh and Meyer; arXiv version 2, revised 2025-03-29.
- [Trends in Mass Spectrometry-Based Single-Cell Proteomics (2025)](https://pubs.acs.org/doi/10.1021/acs.analchem.5c00661) - Current trends and future directions.
- [Data acquisition approaches for single cell proteomics (online 2024; volume 2025)](https://doi.org/10.1002/pmic.202400022) - Review of acquisition approaches by Ghosh, Shannon and Searle.

### Tutorials & Workshops

- [scp Bioconductor Workshop](https://github.com/lgatto/2024_scpworkshop_EUBIC) - Hands-on tutorial for SCP data analysis.
- [Slavov Lab Protocols](https://scp.slavovlab.net/protocols) - Detailed experimental protocols for SCoPE2 and plexDIA.
- [scp Package Vignette](https://uclouvain-cbio.github.io/scp/articles/scp.html) - Step-by-step data processing guide.
- [Single cell proteomics Rescoring and comparison to single cell transcriptomics](https://www.mls.ls.tum.de/en/compms/teaching/sose-2026/advanced-practical-course-bioinformatics-2025-i/)-Advanced Practical Course Bioinformatics - 2026 - Advancing single-cell proteomics by foundational tools
- [Comprehensive Overview of Bottom-Up Proteomics using Mass Spectrometry](https://jessegmeyerlab.github.io/proteomics-tutorial/)-Comprehensive Overview of Bottom-Up Proteomics using Mass Spectrometry

### Guidelines

- [Performing, benchmarking, and reporting single-cell proteomics experiments](https://www.nature.com/articles/s41592-023-01785-3) - Community guidelines (Nat Methods 2023).

---

## Key Publications

### Foundational Methods & Workflows

| Year | Title                                                                            | Method    | Journal     |
| ---- | -------------------------------------------------------------------------------- | --------- | ----------- |
| 2018 | SCoPE-MS: mass spectrometry of single mammalian cells                            | SCoPE-MS  | Genome Biol |
| 2021 | Single-cell proteomic and transcriptomic analysis of macrophage heterogeneity... | SCoPE2    | Genome Biol |
| 2022 online / 2023 volume | Increasing the throughput of sensitive proteomics by plexDIA                     | plexDIA   | Nat Biotech |
| 2025 | **Global analysis of protein turnover dynamics in single cells**                 | SC-pSILAC | Cell        |
| 2025 | **Enhanced sensitivity and scalability with a Chip-Tip workflow...**             | Chip-Tip  | Nat Methods |

### Computational Methods

| Year | Title                                                                              | Focus                | Journal  |
| ---- | ---------------------------------------------------------------------------------- | -------------------- | -------- |
| 2022 | AlphaPeptDeep: a modular deep learning framework...                                | Peptide Prediction   | Nat Comm |
| 2024 | [Standardized Workflow for Mass-Spectrometry-Based Single-Cell Proteomics Data Processing and Analysis Using the scp Package](https://doi.org/10.1007/978-1-0716-3934-4_14) | scp workflow | Methods Mol Biol (book chapter) |
| 2025 | **Benchmarking informatics workflows for data-independent acquisition SCP**        | SCPDA / Benchmarking | Nat Comm |
| 2025 | **Mapping early human blood cell differentiation using single-cell proteomics...** | scProtVelo           | Science  |

### Applications

| Year | Title | Application | Journal |
|------|-------|-------------|---------|
| 2021 | Quantitative single-cell proteomics as a tool to characterize cellular hierarchies | Differentiation | Nat Comm |
| 2025 online / 2026 volume | **Single cell proteomic analysis defines discrete neutrophil functional states...** | Glioblastoma/Neutrophils | Nat Comm |

---

## Emerging Technologies

- **Single-molecule protein sequencing** - Nanopore-based approaches for PTM identification
- **Spatial proteomics** - Combining SCP with spatial information
- **Protein Turnover Analysis** - Measuring synthesis and degradation rates (e.g., SC-pSILAC)
- **Multi-omics integration** - Linking SCP with scRNA-seq (CITE-seq, etc.)
- **AI/ML applications** - Deep learning for peptide-property prediction (AlphaPeptDeep), identification workflows and data imputation

---

## Obsidian Vault Resources

This repository doubles as an [Obsidian](https://obsidian.md/) knowledge base with interconnected notes, visual canvases, and dynamic views.

### Structure

```
awesome_SCP/
├── canvas/                      # Visual knowledge maps
│   ├── SCP Overview.canvas      # High-level field overview
│   ├── Methods Workflow.canvas  # Sample-to-data pipeline
│   └── Tools and Software.canvas
├── notes/
│   ├── methods/                 # SCoPE2, plexDIA, Chip-Tip, SC-pSILAC, nDIA
│   ├── tools/                   # MaxQuant, DIA-NN, SCPDA, AlphaPeptDeep
│   ├── databases/               # SPDB, SingPro
│   ├── applications/            # Cancer, differentiation
│   ├── literature/              # Detailed paper notes
│   └── research_group/          # Leading scientists & research groups
├── templates/                   # Templater templates
└── Project Overview.base        # Dynamic Bases view
```

### Templater Templates

Use with the [Templater](https://github.com/SilentVoid13/Templater) plugin:

| Template | Purpose |
|----------|---------|
| Method Template | New experimental methods |
| Tool Template | Software & analysis tools |
| Database Template | Data resources |
| Application Template | Research applications |
| Literature Note | Paper annotations with citation |
| Quick Note | Simple notes |

### Features

- **Wikilinks**: `[[note]]` for cross-referencing
- **Callouts**: `> [!cite]` for publications with DOIs
- **YAML Frontmatter**: Structured metadata (title, tags, category, url)
- **Canvas**: Visual flowcharts and concept maps
- **Bases**: Dynamic queries and views

---

## Audit Status

Core facts and links were reviewed as of **2026-10-20**. See the [Chinese audit report](audit/knowledge-base-audit.md) for per-note coverage, corrections and unresolved items. A checked source or working URL does not mean every statement or experimental detail has been independently verified.

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) before submitting a pull request.

### How to Contribute

1. Fork the repository
2. Create a new branch (`git checkout -b add-new-resource`)
3. Add your resource with a brief description
4. Commit your changes (`git commit -am 'Add new resource'`)
5. Push to the branch (`git push origin add-new-resource`)
6. Create a Pull Request

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This work is licensed under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

---

## Acknowledgments

This list is inspired by the [awesome](https://github.com/sindresorhus/awesome) movement and the pioneering work of the single-cell proteomics community, particularly the [Slavov Laboratory](https://scp.slavovlab.net/).
