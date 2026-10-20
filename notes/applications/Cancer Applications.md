---
title: Cancer Applications
aliases:
  - SCP in Cancer Research
  - Tumor Proteomics
tags:
  - applications
  - cancer
  - heterogeneity
  - clinical
category: application
url: https://doi.org/10.1038/s41467-021-23667-y
---

# Cancer Applications

**Single-Cell Proteomics in Cancer Research**

## Overview

Single-cell proteomics provides unprecedented resolution for understanding tumor heterogeneity, drug resistance mechanisms, and immune microenvironment dynamics.

## Key Applications

### Tumor Heterogeneity
- Identify rare cell populations
- Map clonal evolution
- Detect drug-resistant subclones

### Drug Response
- Single-cell pharmacoproteomics
- Resistance mechanism discovery
- Biomarker identification

### Immune Microenvironment
- T cell exhaustion states
- Macrophage polarization
- Immune checkpoint expression

## Cancer Types Studied

| Context | Evidence type and finding | Reference |
|---------|---------------------------|-----------|
| Triple-negative breast cancer | Review of applications and challenges, not a new experimental cohort | Nalla et al. (2025), [DOI](https://doi.org/10.1002/prca.202400101) |
| Leukemia / hematopoietic hierarchies | Single-cell protein measurements of differentiation hierarchies | Schoof et al. (2021), [DOI](https://doi.org/10.1038/s41467-021-23667-y) |
| Glioblastoma-associated neutrophils | Distinct proteomic states in the studied human tumors | Sadiku et al., online 2025 / volume 2026, [DOI](https://doi.org/10.1038/s41467-025-67367-3) |

## Advantages Over Bulk

1. **Cell-level heterogeneity**: Resolve protein-abundance distributions that bulk averaging can obscure.
2. **Rare populations**: Detection depends on sampling, cell recovery and classification accuracy; there is no universal <1% detection guarantee.
3. **Trajectories**: Pseudotime is inferred from cross-sectional data and is not direct longitudinal tracking.
4. **Protein-level evidence**: Measure abundance; activity, modification or causality require appropriate additional measurements.

## Integration Opportunities

- **Multi-omics**: SCP + scRNA-seq
- **Spatial**: Location-aware proteomics
- **Temporal**: Time-course studies

## Challenges

- Limited throughput for clinical samples
- Sample preparation depends on the method; fresh tissue is not universal, and some spatial workflows use fixed/FFPE material
- Complex data interpretation
- Statistical power considerations

## Key Publications

> [!cite] Key References
> - Nalla et al. (2025) *Proteomics Clin Appl* - TNBC review
> - Schoof et al. (2021) *Nature Communications* - Cellular hierarchies
>   DOI: [10.1038/s41467-021-23667-y](https://doi.org/10.1038/s41467-021-23667-y)
> -  Sadiku, P., Brenes, A.J., Mayer, R.L. _et al._ Single cell proteomic analysis defines discrete neutrophil functional states in human glioblastoma. _Nat Commun_ (online 2025; volume 2026). [https://doi.org/10.1038/s41467-025-67367-3](https://doi.org/10.1038/s41467-025-67367-3)





## Future Directions

- Clinical biomarker discovery
- Patient stratification
- Drug combination optimization
- Minimal residual disease detection

## Related Topics

- [[Cell Differentiation]] - Developmental hierarchies
- [[SCoPE2]] - Primary method used
- [[plexDIA]] - High-throughput alternative

## Sources

- [Schoof et al. (2021), cellular hierarchies](https://doi.org/10.1038/s41467-021-23667-y)
- [Sadiku et al., online 2025 / volume 2026](https://doi.org/10.1038/s41467-025-67367-3)
- [Nalla et al. (2025), TNBC review](https://doi.org/10.1002/prca.202400101)
- [Deep Visual Proteomics, including fixed tissue](https://doi.org/10.1038/s41587-022-01302-5)
