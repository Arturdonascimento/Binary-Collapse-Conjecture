# Binary Collapse Conjecture – Δ(n) Dataset

This repository provides empirical data and tools for exploring the Binary Collapse Conjecture (BCC), a symbolic process defined by:

**Δ(n) = |n - rev_k(n)|**

Where `rev_k(n)` is the reverse of the binary representation of `n`.

## Files

- `DeltaResults_n_1to10000.csv`: Collapse behavior for all integers from 1 to 10,000.
- `DeltaProcess.py`: Python script to compute the Δ(n) process and cycles.

## How It Works

The Δ(n) process iteratively applies:

1. Compute `rev_k(n)` (reverse binary form of `n`);
2. Take the absolute difference: `|n - rev_k(n)|`;
3. Repeat until reaching 0 or entering a cycle.

## Author

- Artur do Nascimento (Conjecture author)
- Lyriam (Symbolic Assistant – development and formal analysis)

This dataset supports the article:  
**"Binary Collapse: The Most Recent Conjecture in Modern Mathematics"**

## License

Distributed under the Creative Commons Attribution 4.0 License (CC BY 4.0).
