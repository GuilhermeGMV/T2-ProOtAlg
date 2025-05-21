import argparse
import copy

def is_possible(board, l, c, n, s):
    for i in range(n):
        if board[i][c] == s or board[l][i] == s:
            return False

    for i in range(-n, n):
        if 0 <= l + i < n and 0 <= c + i < n and board[l + i][c + i] == s:
            return False

    for i in range(-n, n):
        if 0 <= l + i < n and 0 <= c - i < n and board[l + i][c - i] == s:
            return False

    return True

def mosteiro(board, n, ns, l=0, c=0, plain=0, m=float('inf'), best_board=None):
    if l == n:
        if plain < m:
            return plain, copy.deepcopy(board)
        else:
            return m, best_board

    if plain >= m:
        return m, best_board

    for s in range(ns, -1, -1):
        if s == 0:
            v = 1
        else:
            v = 0

        if is_possible(board, l, c, n, s) or s == 0:
            board[l][c] = s

            if c + 1 < n:
                m, best_board = mosteiro(board, n, ns, l, c + 1, plain + v, m, best_board)
            else:
                m, best_board = mosteiro(board, n, ns, l + 1, 0, plain + v, m, best_board)

            board[l][c] = None

    return m, best_board

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, help="Board Size(n)")
parser.add_argument("ns", type=int, help="Number of tile patterns(ns)")
args = parser.parse_args()

board = [[None for _ in range(args.n)] for _ in range(args.n)]

min_plain, best_board = mosteiro(board, args.n, args.ns)

print(f"\nMinimum number of plain tiles: {min_plain}")
print("Best board found:")
for line in best_board:
    print(" ".join(str(x) for x in line))
