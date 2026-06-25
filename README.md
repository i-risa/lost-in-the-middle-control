# lost-in-the-middle-control
Control dataset to test the hypotheses from the paper "Lost in the Middle: How Language Models Use Long Contexts" by Liu et al., TACL 2023

## Control Dataset: Isolating Positional Bias in RAG Architectures

This repository contains a controlled synthetic dataset designed to isolate and evaluate the "Lost in the Middle" phenomenon in Large Language Models (LLMs). 

## Motivation
Standard evaluation benchmarks for multi-document question answering often suffer from semantic confounding variables. Distractor documents are usually retrieved via similarity search, meaning they share lexical overlap with the answer. This dataset eliminates those confounds by using structurally identical "person profiles", isolating spatial position as the sole independent variable.

## Repo Structure
* `generate_dataset.py`: Generation script
* `data/n5_positions.jsonl`: 250 test cases (5 documents, 50 examples per position)
* `data/n10_positions.jsonl`: 500 test cases (10 documents, 50 examples per position)
* `data/n20_positions.jsonl`: 1000 test cases (20 documents, 50 examples per position)

## Dataset Format
Each JSONL row contains a fully formatted prompt, the expected exact-match answer (a 4-digit birth year), the total number of documents, and the target position index.

## Usage
To regenerate the datasets, simply run:
`python generate_dataset.py`
