# 🧩 Monastery of Eternal Doubts

## 📌 Project Description

This project was developed for the Algorithm Optimization course in the Software Engineering program at [PUCRS](https://portal.pucrs.br/).

Inspired by a medieval tale, the challenge is to arrange tiles in a monastery hall while minimizing the number of **plain tiles** and avoiding any repeated patterns in the **same row, column, or diagonal**.

The solution uses **backtracking** to test all possible configurations and return the optimal one based on the given constraints.

### Rules:

1. The number of **plain tiles** (tiles with no pattern) must be **as small as possible**.
2. No pattern may repeat **in the same row, column, or diagonal**.

The user must input:
- The size of the board (a square matrix `n × n`)
- The number of available tile patterns (`ns`)

## 🧠 Implemented Algorithms

Two versions are available:

- `mosteiro.py`: Basic recursive backtracking implementation.
- `mosteiro2.py`: Optimized version that returns both the **minimum number of plain tiles** and the **best board configuration**.

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/GuilhermeGMV/T2-ProOtAlg
cd T2-ProOtAlg
```

Run one of the scripts using Python 3.7+:

```bash
python mosteiro.py 4 3
```

or

```bash
python mosteiro2.py 4 3
```

Where `4` is the board size (`n`) and `3` is the number of tile patterns (`ns`).

### Example Output (`mosteiro2.py`):

```bash
Minimum number of plain tiles: 6
Best board found:
1 2 0 3
0 3 1 2
2 0 3 1
3 1 2 0
```

> `0` represents a **plain tile**, while other numbers represent different patterns.

## 🛠️ Technologies

- Python 3.7+
- Backtracking algorithm
- `copy.deepcopy` to track the best solution

## 📄 Notes

This project simulates a **constraint optimization problem**, applying **exhaustive search** and **pruning techniques**. It was proposed as a practical assignment for the course.
