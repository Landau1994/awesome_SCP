---
title: Transfer Learning
aliases:
  - transfer learning
  - domain adaptation
tags:
  - concept
  - machine-learning
  - deep-learning
category: concept
date_created: 2026-03-17
---

# Transfer Learning

**A machine learning strategy where a model trained on one task/dataset is adapted to a different but related task, leveraging pre-learned representations to improve performance and reduce data requirements.**

## Overview

Transfer learning addresses the problem of limited labeled data by first pre-training a model on a large, data-rich source domain and then fine-tuning it on a smaller target domain. This approach has been transformative in NLP ([[Transformer]]-based models like BERT, GPT) and is increasingly adopted in computational biology for single-cell analysis.

## Key Paradigms

| Strategy | Description | Example |
|----------|-------------|---------|
| **Pre-training + Fine-tuning** | Train on large data, fine-tune on target | scTranslator: bulk → single-cell |
| **Domain Adaptation** | Adapt model to new distribution | Cross-tissue or cross-species transfer |
| **Few-shot Learning** | Fine-tune with very few examples | scTranslator: 20 cells fine-tuning |
| **[[Zero-shot Learning]]** | Apply without any target training data | scTranslator: pan-cancer prediction |

## Application in SCP

scTranslator employs a two-stage transfer learning strategy:
1. **Bulk Pre-training**: Learns general RNA-to-protein relationships from ~18,000 bulk samples
2. **Single-cell Fine-tuning**: Adapts to cellular heterogeneity using ~2.4M single cells

This hierarchical transfer (bulk → single-cell) is analogous to learning the "language" of gene-protein relationships at the population level first, then refining for cell-level nuances.

## Related Concepts

- [[Zero-shot Learning]] — Prediction without any target-domain training
- [[Transformer]] — Architecture commonly used with transfer learning
- [[Central Dogma]] — Biological basis for the RNA-to-protein translation task
