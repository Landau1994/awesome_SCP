---
title: scProtVelo
aliases:
  - scProtVelo
tags:
  - tools
  - software
category: tool
url: 
date_created: 2026-03-25
---

# scProtVelo

**A modeling framework for single-cell protein velocity and translation dynamics.**

## Overview

scProtVelo models protein abundance changes along differentiation trajectories by incorporating production and turnover dynamics.

## Key Features

- **Protein Velocity Modeling**: Infers directionality in cell-state transitions.
- **Temporal Dynamics**: Goes beyond static protein snapshots.
- **Multi-Omics Context**: Can be interpreted alongside transcriptomic trajectories.
- **Cross-Platform**: Windows, Linux, macOS

## Installation

```bash
# Installation commands
# Refer to scProtVelo project release
```

## Usage

```r
# Example code
# Usually run in Python-based analysis workflows
```

## Input/Output

**Input:**
- Single-cell protein matrix
- Cell graph / pseudotime information

**Output:**
- Velocity vectors and transition tendencies
- Dynamic regulation interpretation outputs

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| smoothing | user-defined | Neighborhood smoothing for velocity estimation |
| time_scale | user-defined | Dynamic scaling of transition rates |

## Key Publications

> [!cite] Primary Reference
> See Science 2025 blood differentiation literature note.

## Links

- GitHub:
- Documentation:

## Related Tools

- [[cellrank]]
- [[Scanpy]]
- [[RNA Velocity]]
