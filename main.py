# Atcoder Beginner Contest 351 - D

from union_find import UnionFind

h, w = map(int, input().split())
b = [input() for _ in range(h)]

magnet_neighbor = [[False] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if b[i][j] == "#":
            if i > 0 and not b[i - 1][j] == "#":
                magnet_neighbor[i - 1][j] = True
            if i < h - 1 and not b[i + 1][j] == "#":
                magnet_neighbor[i + 1][j] = True
            if j > 0 and not b[i][j - 1] == "#":
                magnet_neighbor[i][j - 1] = True
            if j < w - 1 and not b[i][j + 1] == "#":
                magnet_neighbor[i][j + 1] = True

uf: UnionFind[tuple[int, int]] = UnionFind([])

for i in range(h):
    for j in range(w):
        if b[i][j] == "#" or magnet_neighbor[i][j]:
            continue

        uf.add((i, j))

        if i > 0 and not b[i - 1][j] == "#" and not magnet_neighbor[i - 1][j]:
            uf.unite((i, j), (i - 1, j))

        if j > 0 and not b[i][j - 1] == "#" and not magnet_neighbor[i][j - 1]:
            uf.unite((i, j), (i, j - 1))


counts = {p: uf.get_size(p) for p in uf.roots}
for i, j in [(i, j) for i in range(h) for j in range(w) if magnet_neighbor[i][j]]:
    s = set()
    if i > 0 and not b[i - 1][j] == "#" and not magnet_neighbor[i - 1][j]:
        s.add(uf.find_root((i - 1, j)))
    if j > 0 and not b[i][j - 1] == "#" and not magnet_neighbor[i][j - 1]:
        s.add(uf.find_root((i, j - 1)))
    if i < h - 1 and not b[i + 1][j] == "#" and not magnet_neighbor[i + 1][j]:
        s.add(uf.find_root((i + 1, j)))
    if j < w - 1 and not b[i][j + 1] == "#" and not magnet_neighbor[i][j + 1]:
        s.add(uf.find_root((i, j + 1)))

    for root in s:
        counts[root] += 1

print(max(counts.values()) if counts else 1)
