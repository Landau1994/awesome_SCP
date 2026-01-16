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

- **[SCoPE2](https://scp.slavovlab.net/protocols)** - Single Cell ProtEomics by Mass Spectrometry. Uses TMT/TMTpro isobaric labeling with carrier cells for enhanced peptide identification. Cost-effective and scalable to thousands of cells.
- **[pSCoPE](https://scp.slavovlab.net/)** - Prioritized SCoPE using targeted MS acquisition for increased proteome coverage.

### Label-Free & Multiplexed DIA

- **[plexDIA](https://scp.slavovlab.net/plexDIA)** - Multiplexed data-independent acquisition using non-isobaric mass tags (mTRAQ, dimethyl, PSMtags). Achieves ~1,000 proteins per cell with 98% data completeness.
- **[diaPASEF](https://www.bruker.com/)** - Combines parallel accumulation–serial fragmentation with DIA for enhanced sensitivity.

### Miniaturized Sample Preparation

- **[nPOP](https://scp.slavovlab.net/)** - Nano-ProteOmic sample Preparation. Enables parallel preparation of thousands of cells in nanoliter droplets on glass slides. Quantifies 3,000-3,700 proteins per human cell.
- **[nanoPOTS](https://www.pnnl.gov/)** - Nanodroplet Processing in One pot for Trace Samples. Chip-based platform using nanoliter reaction volumes.
- **[Nested NanoPOTS (N2)](https://www.pnnl.gov/)** - Enhanced version accommodating 243 cells per chip with 10-fold improvement in throughput.
- **[mPOP](https://scp.slavovlab.net/)** - Minimal ProteOmic sample Preparation for cell lysis and processing.

### Automated Platforms

- **[CellenONE](https://www.scienion.com/)** - Single-cell isolation and dispensing platform widely used for SCP workflows.
- **[cellenONE + Evosep](https://www.evosep.com/)** - Integrated workflow combining cell dispensing with robust LC separation.

---

## Data Acquisition Strategies

| Strategy | Description | Throughput | Proteome Depth |
|----------|-------------|------------|----------------|
| **DDA** | Data-Dependent Acquisition | Moderate | High |
| **DIA** | Data-Independent Acquisition | High | Very High |
| **plexDIA** | Multiplexed DIA | Very High | High |
| **pSCoPE** | Targeted/Prioritized | Moderate | Focused |
| **diaPASEF** | Ion mobility-enhanced DIA | High | Very High |

---

## Mass Spectrometry Platforms

### Optimized for Single-Cell

- **[Bruker timsTOF SCP](https://www.bruker.com/)** - Purpose-built for single-cell proteomics with trapped ion mobility.
- **[Bruker timsTOF Ultra 2](https://www.bruker.com/)** - Next-generation platform with enhanced sensitivity.
- **[Thermo Orbitrap Astral](https://www.thermofisher.com/)** - High-resolution mass analyzer with exceptional sensitivity.
- **[Thermo Exploris Series](https://www.thermofisher.com/)** - Versatile Orbitrap platforms for SCP applications.

### LC Systems

- **[Evosep One](https://www.evosep.com/)** - Robust LC platform with standardized gradients (e.g., 5-min Whisper methods).
- **[IonOpticks Aurora Series](https://ionopticks.com/)** - High-performance columns optimized for low-flow proteomics.

---

## Software & Tools

### Data Processing

| Tool | Platform | Description | Link |
|------|----------|-------------|------|
| **MaxQuant** | Windows | Quantitative proteomics with LFQ and TMT support | [Link](https://www.maxquant.org/) |
| **DIA-NN** | Cross-platform | Deep learning-based DIA analysis, supports plexDIA | [Link](https://github.com/vdemichev/DiaNN) |
| **Proteome Discoverer** | Windows | Comprehensive MS data analysis | [Link](https://www.thermofisher.com/) |
| **FragPipe** | Cross-platform | Fast peptide/protein identification | [Link](https://fragpipe.nesvilab.org/) |
| **SCeptre** | Python | Pipeline for isobaric carrier-based SCP | [GitHub](https://github.com/schoof-lab/SCeptre) |

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
| **SCP (Single Cell Pipeline)** | Seurat-compatible analysis pipeline | [GitHub](https://zhanghao-njmu.github.io/SCP/) |

#### Python Packages

| Package | Description | Link |
|---------|-------------|------|
| **SCeptre** | Processing pipeline for isobaric carrier SCP | [GitHub](https://github.com/schoof-lab/SCeptre) |
| **pyteomics** | MS data parsing and analysis | [GitHub](https://github.com/levitsky/pyteomics) |
| **alphapept** | DIA-NN integration for Python workflows | [GitHub](https://github.com/MannLabs/alphapept) |

---

## Databases & Datasets

### Comprehensive Databases

- **[SPDB](https://scproteomicsdb.com/)** - Single-cell Proteomic DataBase. 143 datasets, >300 million cells, 8000+ proteins across 4 species. Unified format with visualization tools.
- **[SingPro](https://academic.oup.com/nar/article/52/D1/D552/7306671)** - Database for MS-based and flow cytometry-based SCP data with detailed experimental metadata.
- **[Slavov Lab Data Repository](https://scp.slavovlab.net/data)** - Curated datasets organized by publication with linked protocols.

### Benchmark Datasets

- **[scpdata (Bioconductor)](https://bioconductor.org/packages/scpdata/)** - 21 MS-based SCP datasets from 13 publications in standardized format.
- **[SCoPE2 Macrophage Dataset](https://scp.slavovlab.net/)** - 3,042 proteins quantified in 1,490 single monocytes/macrophages.

---

## Reviews & Tutorials

### Review Articles

- [Recent methodological advances towards single-cell proteomics (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10749393/) - Comprehensive overview of technological developments.
- [Single-Cell Proteomics using Mass Spectrometry (2025)](https://arxiv.org/pdf/2502.11982) - State-of-the-art methods and applications.
- [Trends in Mass Spectrometry-Based Single-Cell Proteomics (2025)](https://pubs.acs.org/doi/10.1021/acs.analchem.5c00661) - Current trends and future directions.
- [Data acquisition approaches for single cell proteomics (2025)](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/pmic.202400022) - Comparison of DDA, DIA, and hybrid approaches.

### Tutorials & Workshops

- [scp Bioconductor Workshop](https://github.com/lgatto/2024_scpworkshop_EUBIC) - Hands-on tutorial for SCP data analysis.
- [Slavov Lab Protocols](https://scp.slavovlab.net/protocols) - Detailed experimental protocols for SCoPE2 and plexDIA.
- [scp Package Vignette](https://uclouvain-cbio.github.io/scp/articles/scp.html) - Step-by-step data processing guide.

### Guidelines

- [Performing, benchmarking, and reporting single-cell proteomics experiments](https://www.nature.com/articles/s41592-023-01785-3) - Community guidelines (Nat Methods 2023).

---

## Key Publications

### Foundational Methods

| Year | Title | Method | DOI |
|------|-------|--------|-----|
| 2018 | SCoPE-MS: mass spectrometry of single mammalian cells | SCoPE-MS | [10.1186/s13059-018-1547-5](https://doi.org/10.1186/s13059-018-1547-5) |
| 2021 | Single-cell proteomic and transcriptomic analysis of macrophage heterogeneity using SCoPE2 | SCoPE2 | [10.1186/s13059-021-02267-5](https://doi.org/10.1186/s13059-021-02267-5) |
| 2022 | Increasing the throughput of sensitive proteomics by plexDIA | plexDIA | [10.1038/s41587-022-01389-w](https://doi.org/10.1038/s41587-022-01389-w) |
| 2023 | Massively parallel sample preparation for multiplexed single-cell proteomics using nPOP | nPOP | [10.1038/s41596-024-01033-8](https://doi.org/10.1038/s41596-024-01033-8) |

### Computational Methods

| Year | Title | Focus | DOI |
|------|-------|-------|-----|
| 2021 | Replication of SCoPE2 analysis with scp | scp R package | [Bioconductor](https://uclouvain-cbio.github.io/SCP.replication/) |
| 2024 | Standardized Workflow for Mass-Spectrometry-Based SCP Data Processing | scp workflow | [PubMed](https://pubmed.ncbi.nlm.nih.gov/38907155/) |
| 2024 | Benchmark of Data Integration in Single-Cell Proteomics | Integration | [10.1021/acs.analchem.4c04933](https://doi.org/10.1021/acs.analchem.4c04933) |

### Applications

| Year | Title | Application | DOI |
|------|-------|-------------|-----|
| 2021 | Quantitative single-cell proteomics as a tool to characterize cellular hierarchies | Cell differentiation | [10.1038/s41467-021-23667-y](https://doi.org/10.1038/s41467-021-23667-y) |
| 2025 | Advancements in SCP for Triple Negative Breast Cancer | Cancer | [10.1002/prca.202400101](https://doi.org/10.1002/prca.202400101) |

---

## Emerging Technologies

- **Single-molecule protein sequencing** - Nanopore-based approaches for PTM identification
- **Spatial proteomics** - Combining SCP with spatial information
- **Multi-omics integration** - Linking SCP with scRNA-seq (CITE-seq, etc.)
- **AI/ML applications** - Deep learning for peptide identification and data imputation
- **Quantum computing** - Potential for overcoming computational bottlenecks

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
│   ├── methods/                 # SCoPE2, plexDIA, nPOP, etc.
│   ├── tools/                   # MaxQuant, DIA-NN, scp, etc.
│   ├── databases/               # SPDB, SingPro
│   └── applications/            # Cancer, differentiation
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
