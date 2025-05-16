import argparse

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

def mosteiro(tab, n, ns, l=0, c=0, lisas=0, m=float('inf')):
    if l == n:
        return min(lisas, m)

    v = 0

    if lisas >= m:
        return m

    for s in range(ns, -1, -1):

        if s == 0:
            v = 1

        if is_possible(tab, l, c, n, s) or s == 0: # testa se pode colocar ou se é uma peça lisa é certo que pode
            tab[l][c] = s

            if c+1 < n:
                m = mosteiro(tab, n, ns, l, c + 1, lisas + v, m)
            else:
                m = mosteiro(tab, n, ns, l + 1, 0, lisas + v, m)

            tab[l][c] = None

    return m

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, help="Tamanho do Tabuleiro(n)")
parser.add_argument("ns", type=int, help="Número de estampas disponíveis(ns)")
args = parser.parse_args()

tab = [[None for _ in range(args.n)] for _ in range(args.n)]


print(mosteiro(tab, args.n, args.ns))