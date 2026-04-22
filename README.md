# 🎒 Knapsack Problem Solver (Genetic Algorithm)

A Python implementation of a Genetic Algorithm designed to solve the optimization challenge of the Knapsack Problem.

## 🚀 Overview
The goal is to select a subset of items with maximum total value such that their total weight does not exceed a predefined limit (**40 units**). The algorithm evolves a population of solutions through biological-inspired processes.

## Versatile
**you can change any aspect of predefined limit, items, their value and their weights**

## What is Knapsack Problem
The Knapsack Problem is a classic optimization puzzle in computer science and mathematics. Imagine you have a backpack (knapsack) with a fixed weight capacity, and you have a set of items, each with a specific weight and value. The goal is to determine which items to include so that the total weight is less than or equal to the limit, and the total value is as large as possible.

## 🧬 Genetic Operators
- **Fitness Function**: Calculates total value; returns `0` if the weight limit is exceeded.
- **Selection**: Uses weighted random choices (Roulette Wheel Selection) based on fitness.
- **Crossover**: Single-point crossover to combine "DNA" from two parent genomes.
- **Mutation**: Randomly flips bits in a genome based on a user-defined probability to maintain genetic diversity.
- **Elitism**: Preserves the top 2 best-performing individuals for the next generation to prevent regression.



## 🖥️ Usage
1. Run the script:
   ```bash
   python knapsack_ga.py
