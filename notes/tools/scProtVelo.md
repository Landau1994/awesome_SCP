---
title: scProtVelo
aliases:
  - scProtVelo
tags:
  - tools
  - software
category: tool
url: https://github.com/theislab/scProtVelo
date_created: 2026-03-25
---

# scProtVelo

**A modeling framework for single-cell protein velocity and translation dynamics.**

## Overview

scProtVelo models protein abundance changes along differentiation trajectories by incorporating production and turnover dynamics.

## Key Features

- **Protein Velocity Modeling**: Infers directionality in cell-state transitions.
- **Temporal Dynamics**: Goes beyond static protein snapshots.
- **Multi-Omics Input**: Uses paired mRNA and protein measurements to model protein dynamics.
- **Environment**: Follow the official release requirements; operating-system support depends on the package and its dependencies.

## Input/Output

**Input:**

- Paired single-cell mRNA and MS protein measurements with compatible feature/cell identifiers
- For independent datasets, pairing/integration must be established first

**Output:**

- Model-derived protein-velocity estimates and trajectory visualizations

## Key Publications

> [!cite] Related Study Context
> See Science 2025 blood differentiation literature note.

## Links

- GitHub: https://github.com/theislab/scProtVelo
- Documentation/source: https://github.com/theislab/scProtVelo

## Related Tools

- [[cellrank]]
- [[Scanpy]]
- [[RNA Velocity]]

## Source Check

- Source checked on 2026-10-20: [scProtVelo documentation or source](https://github.com/theislab/scProtVelo).
