---
title: <% tp.file.title %>
aliases:
  - <% tp.file.cursor(1) %>
tags:
  - literature
  - paper
category: literature
date_created: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

## Citation

> [!cite] Reference
> **Authors**: <% tp.file.cursor(3) %>
> **Year**: <% tp.file.cursor(4) %>
> **Journal**: <% tp.file.cursor(5) %>
> **DOI**: [10.xxxx/xxxxx](https://doi.org/<% tp.file.cursor(6) %>)

## Abstract

<% tp.file.cursor(7) %>

## Key Points

-
-
-

## Methods

### Sample Preparation
- Method used: [[SCoPE2]] / [[plexDIA]] / [[nPOP]]
- Cell type:
- Number of cells:

### Data Analysis
- Software: [[MaxQuant]] / [[DIA-NN]]
- Downstream: [[scp Package]]

## Results

### Main Findings
1.
2.
3.

### Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | |
| Fig 2 | |

## Discussion

### Strengths
-

### Limitations
-

### Future Work
-

## Personal Notes

<% tp.file.cursor(8) %>

## Related Papers

-

## Related Topics

- [[Cancer Applications]]
- [[Cell Differentiation]]
