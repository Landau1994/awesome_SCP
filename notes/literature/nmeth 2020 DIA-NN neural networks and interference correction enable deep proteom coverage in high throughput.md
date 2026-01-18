---
title: DIA-NN: neural networks and interference correction enable deep proteome coverage in high throughput
authors:
  - Vadim Demichev
  - Christoph B. Messner
  - Spyros I. Vernardis
  - Kathryn S. Lilley
  - Markus Ralser
aliases:
   - DIA-NN
   - neural networks proteomics
   - interference correction DIA
tags:
  - literature
  - paper
  - proteomics
  - deep-learning
  - DIA-MS
category: literature
date_created: 2024-05-22
Journal: Nature Methods
Year: 2020
---

# DIA-NN: neural networks and interference correction enable deep proteome coverage in high throughput

## Citation

> [!cite] Reference
> **Title**：DIA-NN: neural networks and interference correction enable deep proteome coverage in high throughput
> **Authors**: Vadim Demichev, Christoph B. Messner, Spyros I. Vernardis, Kathryn S. Lilley, Markus Ralser
> **Year**: 2020
> **Journal**: Nature Methods
> **DOI**: 10.1038/s41592-019-0638-x

## Abstract

The computational processing of data-independent acquisition (DIA) mass spectrometry datasets is challenging due to inherent complexity and signal interference. DIA-NN is an integrated software suite that exploits deep neural networks (DNNs) and new quantification and signal correction strategies to improve the identification and quantification performance in conventional DIA proteomic applications. It is particularly beneficial for high-throughput applications, as it enables deep and confident proteome coverage when used with fast chromatographic methods. DIA-NN is easy to use, supports library-free searches through *in silico* spectral library generation, and does not require retention time standards.

## Key Points

- **Deep Learning Integration**: Uses an ensemble of deep neural networks (DNNs) to distinguish real signals from noise and calculate accurate q-values.
- **Interference Correction**: Implements a novel algorithm to detect and subtract interferences from tandem-MS spectra, significantly improving quantification accuracy.
- **High Throughput Optimization**: Specifically designed to handle short chromatographic gradients, enabling deep proteome coverage in a fraction of the time required by traditional methods.
- **Library-Free Mode**: Capable of generating *in silico* spectral libraries from protein sequence databases, eliminating the need for experimental spectral libraries.
- **Robustness**: Demonstrated robust performance across large-scale datasets (e.g., 364 yeast acquisitions processed in ~3 hours).

## Methods

### Sample Preparation
- **Method used**: Tryptic digestion, protein denaturation in 8M urea, reduction with DTT, alkylation with iodoacetamide.
- **Cell types**: HeLa whole-proteome tryptic digest, K562 human cell line, *Saccharomyces cerevisiae* (yeast), *Escherichia coli*, and human plasma.
- **Number of cells/Amount**: Varies by experiment; e.g., 2 µg protein injection for mass spectrometry.

### Data Analysis
- **Software**: DIA-NN (version 1.6.0), compared against OpenSWATH, Skyline, and Spectronaut.
- **Ensemble DNN**: 12 feed-forward, fully connected DNNs with five tanh-activated hidden layers and a softmax output layer.
- **Downstream**: LFQbench R package for quantification precision benchmarking; PyProphet for FDR processing of competitor tools.

## Results

### Main Findings
1. **Superior Identification**: DIA-NN consistently identifies more precursors and proteins than existing tools, particularly at strict FDR thresholds and when using fast (0.5h) gradients.
2. **Improved Quantification**: Outperformed Spectronaut in quantification precision (median CVs for human peptides: 5.6% for DIA-NN vs 7.0% for Spectronaut).
3. **High Efficiency**: Enables high-throughput workflows by maintaining deep proteome coverage even with very short LC gradients, identifying >35,000 precursors in a 19-minute microflow gradient.
4. **Validation via Long Gradients**: Precursors identified by DIA-NN on short gradients were highly validated by identifications from longer, less complex gradients.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Schematic of the DIA-NN workflow and identification performance comparison (FDR vs. Human precursors) across different gradient lengths (0.5h to 4h). |
| Fig 2 | LFQbench benchmarking results showing peptide and protein ratio distributions for human, yeast, and *E. coli* mixtures compared to Spectronaut. |

## Discussion

### Strengths
- **Ease of Use**: Fully automated pipeline with both GUI and command-line interfaces.
- **No iRT Needed**: Uses endogenous peptides for retention time alignment, removing the need for spiked-in standards.
- **Speed**: Highly optimized C implementation (Cranium library) allows for rapid processing of large cohorts.
- **Versatility**: Works effectively with both spectral libraries and *in silico* generated databases.

### Limitations
- **Data Complexity**: While it corrects for interference, extremely high multiplexing in very short gradients still poses a fundamental limit to MS signal resolution.
- **Dependency on Fragment Number**: Like many tools, it performs best when at least a few fragment ions are consistently detected.

### Future Work
- Application to even larger clinical cohorts and extremely fast chromatographic setups (e.g., <10 min gradients).
- Integration with emerging fragmentation techniques or ion mobility mass spectrometry.

## Personal Notes

- DIA-NN has become a gold standard in the field since this publication, particularly for "library-free" DIA analysis.
- The use of ensemble DNNs for scoring is a significant shift from the linear discriminant analysis (mProphet) used by previous generation tools.

## Related Papers

- Bruderer, R. et al. *Mol. Cell. Proteomics* **16**, 2296–2309 (2017). (Optimization of experimental parameters for DIA).
- Navarro, P. et al. *Nat. Biotechnol.* **34**, 1130–1136 (2016). (LFQbench benchmarking paper).
- Reiter, L. et al. *Nat. Methods* **8**, 430–435 (2011). (Original mProphet algorithm).