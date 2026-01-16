# pSCoPE

**Prioritized SCoPE (Targeted Proteomics)**

## Overview

pSCoPE is a targeted acquisition method that prioritizes specific peptides for quantification, enabling deeper coverage of selected proteins in single cells.

## Key Features

- **Targeted Selection**: Prioritizes pre-selected peptides
- **Inclusion Lists**: Uses mass/RT windows
- **Higher Sensitivity**: More scans per target
- **Complement to SCoPE2**: Same sample prep

## Workflow

```
SCoPE2 Sample Prep → TMT Labeling →
Targeted Acquisition (inclusion list) →
MaxQuant Analysis
```

## Use Cases

1. **Pathway-focused**: Target specific signaling pathways
2. **Validation**: Confirm discovery results
3. **Low-abundance**: Increase sensitivity for specific proteins

## Comparison with SCoPE2

| Aspect | SCoPE2 | pSCoPE |
|--------|--------|--------|
| Approach | Discovery | Targeted |
| Proteins | ~3000 | Selected subset |
| Depth | Broad | Deep (targeted) |
| Use case | Exploration | Validation |

## Related Methods

- [[SCoPE2]] - Parent method
- [[plexDIA]] - Alternative approach

## Tags

#methods #targeted #TMT #validation
