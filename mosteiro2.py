import argparse
import copy

def is_possible(tab, l, c, n, s):
    for i in range(n):
        if tab[i][c] == s or tab[l][i] == s:
            return False

    for i in range(-n, n):
        if 0 <= l + i < n and 0 <= c + i < n and tab[l + i][c + i] == s:
            return False

    for i in range(-n, n):
        if 0 <= l + i < n and 0 <= c - i < n and tab[l + i][c - i] == s:
            return False

    return True

def mosteiro(tab, n, ns, l=0, c=0, lisas=0, m=float('inf'), melhor_tabuleiro=None):
    if l == n:
        if lisas < m:
            return lisas, copy.deepcopy(tab)
        else:
            return m, melhor_tabuleiro

    if lisas >= m:
        return m, melhor_tabuleiro

    for s in range(ns, -1, -1):
        if s == 0:
            v = 1
        else:
            v = 0

        if is_possible(tab, l, c, n, s) or s == 0:
            tab[l][c] = s

            if c + 1 < n:
                m, melhor_tabuleiro = mosteiro(tab, n, ns, l, c + 1, lisas + v, m, melhor_tabuleiro)
            else:
                m, melhor_tabuleiro = mosteiro(tab, n, ns, l + 1, 0, lisas + v, m, melhor_tabuleiro)

            tab[l][c] = None

    return m, melhor_tabuleiro

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, help="Tamanho do Tabuleiro(n)")
parser.add_argument("ns", type=int, help="Número de estampas disponíveis(ns)")
args = parser.parse_args()

tab = [[None for _ in range(args.n)] for _ in range(args.n)]

min_lisas, melhor_tab = mosteiro(tab, args.n, args.ns)

print(f"\nMenor número de peças lisas: {min_lisas}")
print("Melhor tabuleiro encontrado:")
for linha in melhor_tab:
    print(" ".join(str(x) for x in linha))
