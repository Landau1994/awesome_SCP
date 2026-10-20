---
title: Transfer Learning
aliases:
  - transfer learning
tags:
  - concept
  - machine-learning
  - deep-learning
category: concept
date_created: 2026-03-17
url: https://www.tensorflow.org/tutorials/images/transfer_learning
---

# Transfer Learning

**A machine learning strategy where a model trained on one task/dataset is adapted to a different but related task, leveraging pre-learned representations to improve performance and reduce data requirements.**

## Overview

Transfer learning reuses knowledge from a source task or dataset for a related target task. Pre-training followed by fine-tuning is a common implementation, but not the only one. Domain adaptation concerns a change in the data distribution and overlaps with transfer learning; the terms are not interchangeable.

## Key Paradigms

| Strategy | Description | Example |
|----------|-------------|---------|
| **Pre-training + Fine-tuning** | Train on large data, fine-tune on target | scTranslator: bulk → single-cell |
| **Domain Adaptation** | Adapt model to new distribution | Cross-tissue or cross-species transfer |
| **Few-shot Learning** | Fine-tune with very few examples | Target-task adaptation with a small labeled sample |
| **[[Zero-shot Learning]]** | Apply without any target training data | scTranslator: pan-cancer prediction |

## Application in SCP

scTranslator employs a two-stage transfer learning strategy:
1. **Bulk pre-training**: Learn RNA-to-protein relationships from paired bulk data.
2. **Single-cell adaptation**: Adapt and evaluate using the study’s single-cell datasets. The counts and training/evaluation split should be read from the original study rather than inferred from the total resource size.

This hierarchical transfer (bulk → single-cell) is analogous to learning the "language" of gene-protein relationships at the population level first, then refining for cell-level nuances.

## Related Concepts

- [[Zero-shot Learning]] — Prediction without any target-domain training
- [[Transformer]] — Architecture commonly used with transfer learning
- [[Central Dogma]] — Biological basis for the RNA-to-protein translation task

## Sources

- [TensorFlow: transfer learning and fine-tuning](https://www.tensorflow.org/tutorials/images/transfer_learning)
- [scTranslator official repository](https://github.com/TencentAILabHealthcare/sctranslator)
