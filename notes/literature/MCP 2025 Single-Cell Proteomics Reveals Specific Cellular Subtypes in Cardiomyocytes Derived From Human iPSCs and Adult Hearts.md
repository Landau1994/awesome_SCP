
# Single-Cell Proteomics Reveals Specific Cellular Subtypes in Cardiomyocytes Derived From Human iPSCs and Adult Hearts

## Citation

> [!cite] Reference
> **Title**：Single-Cell Proteomics Reveals Specific Cellular Subtypes in Cardiomyocytes Derived From Human iPSCs and Adult Hearts
> **Authors**: Lizhuo Ai, Aleksandra Binek, Vladimir Zhemkov, Jae Hyung Cho, Ali Haghani, Simion Kreimer, Edo Israely, Madelyn Arzt, Blandine Chazarin, Niveda Sundararaman, Jesse G. Meyer, Arun Sharma, Eduardo Marbán, Clive N. Svendsen, and Jennifer E. Van Eyk
> **Year**: 2025
> **Journal**: Mol Cell Proteomics
> **DOI**: [10.1016/j.mcpro.2025.100910](https://doi.org/10.1016/j.mcpro.2025.100910)

## Abstract

The authors report a large-scale single-cell proteomics (SCP) characterization of the differentiation trajectory of cardiomyocytes derived from human induced pluripotent stem cells (iPSCs) and cross-compare them to adult cardiomyocytes (aCMs) isolated from human heart tissue. Using a label-free "one pot" approach with parallelized nanoflow liquid chromatography, they analyzed over 1,300 single cells across differentiation stages and ~280 adult cardiomyocytes. The study reveals distinct cell subpopulations, including iCMs characterized by glycolytic metabolism versus aCMs enriched in fatty acid metabolism proteins. Notably, the study uncovers rare hybrid cells in both iCM and aCM populations that co-express canonical cardiac markers and neuronal-enriched proteins, suggesting a potential novel cell type or state flexibility.

## Key Points

- Establishment of a label-free [[single-cell proteomics]] trajectory for human iPSC-derived cardiomyocytes (iCMs) covering 5 time points (Day 0 to Day 21).
- Direct proteomic comparison reveals that iCMs rely on glycolysis and lack the mitochondrial/fatty acid oxidation machinery prevalent in adult cardiomyocytes (aCMs).
- Identification of rare "hybrid" cells in both iCMs and aCMs that co-express cardiac structural proteins (e.g., [[MYH6]]) and neuronal markers (e.g., [[ENO2]], [[NPTN]]).
- Detection of heterogeneity within iPSC colonies (Lin28a gradients) and differentiated iCMs (metabolic vs. structural subtypes).

## Methods

### Sample Preparation
- **Method used**: "One pot" label-free single-cell sample preparation; parallelized [[nanoflow dual-trap single-column liquid chromatography]] (nanoDTSC).
- **Cell type**: Human [[iPSCs]], iPSC-derived cardiomyocytes ([[iCMs]]) at Days 0, 2, 4, 10, and 21; [[adult cardiomyocytes]] (aCMs) isolated from left ventricle and other regions of donor hearts.
- **Number of cells**: Total 1,326 single cells for iPSC/iCM trajectory; ~279 viable aCMs from 3 human donors.

### Data Analysis
- **Software**: [[DIA-NN]] (versions 1.8.1 and 1.8.2) for spectral library generation and search.
- **Downstream**: [[SCANPY]] (Python) for clustering and visualization, [[UMAP]] for dimensionality reduction, [[Leiden clustering]], [[Monocle 3]] for trajectory analysis, and [[ClueGO]] for pathway enrichment.

## Results

### Main Findings
1. **Differentiation Trajectory**: The proteomic analysis successfully tracked the transition from pluripotency (Day 0) to mesoderm (Day 2) and contracting cardiomyocytes (Day 21). iPSCs showed heterogeneity, with outer colony cells expressing higher [[Lin28a]].
2. **iCM Heterogeneity**: Day 21 iCMs clustered into distinct groups. Clusters 0 and 2 were true iCMs, distinguished by metabolic profiles (glycolysis enrichment in Cluster 0). Cluster 1 expressed smooth muscle markers ([[CALD1]], [[MYH11]]).
3. **Comparison with Adult CMs**: aCMs were significantly larger and possessed a proteome enriched in mitochondrial and fatty acid metabolism proteins compared to the glycolytic iCMs. However, both shared core contractile machinery.
4. **Rare Hybrid Cells**: A small subset of cells in both the engineered (iCM) and native (aCM) populations expressed hybrid proteomes containing both cardiac (Troponin T, Myosin-6) and neuronal (Enolase 2, Neuroplastin) proteins.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | **Single-cell proteome trajectory of differentiating cardiomyocytes.** Displays the workflow, UMAPs of differentiation time points (Day 0–21), and identification of distinct clusters within iPSCs (Lin28a heterogeneity) and Day 21 iCMs (separating smooth muscle-like cells from cardiomyocytes). |
| Fig 2 | **Single-cell proteomics of aCMs.** Shows isolation of adult CMs, size comparison (aCMs > iCMs), and proteomic comparison. Radar plots highlight aCM enrichment in mitochondrial/fatty acid pathways vs. iCM enrichment in glycolysis. Also details the detection of heterogeneity within aCMs from different donors. |

## Discussion

### Strengths
- **Label-free Approach**: Allows for flexible processing without the limitations of carrier proteomes or labeling channels.
- **Direct Human Comparison**: Uniquely benchmarks iPSC-derived cells against freshly isolated human adult cardiomyocytes, providing a rigorous standard for maturation.
- **High Sensitivity**: Capable of detecting >700 proteins per cell, allowing for the resolution of rare cell states (e.g., the hybrid neuronal-cardiac cells).

### Limitations
- **Proteome Coverage**: While high for single cells, coverage is still lower than bulk proteomics, potentially missing low-abundance regulatory proteins.
- **Donor Variability**: aCMs were obtained from only three donors, one of which yielded low cell numbers due to heart condition, limiting the generalizability of inter-individual heterogeneity findings.
- **Maturation Gap**: Confirms that standard 2D differentiation yields immature, glycolytic iCMs compared to adult tissue.

### Future Work
- Investigation into the functional role and origin of the rare cardiac-neuronal hybrid cells.
- Application of the method to disease models and drug toxicology screening.
- Improving differentiation protocols to drive metabolic maturation (switch to fatty acid oxidation) in iCMs.

## Personal Notes

## Related Papers

- [[SCoPE2]]: Specht et al. (2021) - Cited as a related single-cell proteomics method.
- [[DIA-NN]]: Demichev et al. (2020) - The software used for data analysis.