# pythonによるUnion-Find木の実装

競プロ勉強用
mypy推奨
rootを探索した時に通ったnodeを全てroot直下に付け替えるといった申し訳程度の高速化がされています。

## コンストラクタ

インスタンスの生成は以下の通り。要素全体の集合が既にある場合はそれを渡すことも可能。

```python
# 集合の要素を後から追加する場合
uf = UnionFind()

# 集合の要素が既にわかっている場合
l = [1, 2, 3, 4, 5, 6]
uf = UnionFind(l)
```

## 結合

```python
l = [1, 2, 3, 4, 5, 6]
uf = UnionFind(l)
uf.unite(3, 4)  # [{1}, {2}, {3, 4}, {5}, {6}]
uf.unite(5, 6)  # [{1}, {2}, {3, 4}, {5, 6}]
```

## 値の追加

全体に新しい要素を追加する。

```python
l = [1, 2, 3, 4, 5, 6]
uf = UnionFind(l)
uf.add(7)  # [{1}, {2}, {3}, {4}, {5}, {6}, {7}]
```

## 同じ集合に属するかの判定

```python
l = [1, 2, 3, 4, 5, 6]
uf = UnionFind(l)
uf.is_in_same(3, 4)  # False
uf.unite(3, 4)
uf.is_in_same(3, 4)  # True
```

## 属する集合のサイズを取得

```python
l = [1, 2, 3, 4, 5, 6]
uf = UnionFind(l)
uf.get_size(3)  # 1
uf.unite(3, 4)
uf.get_size(3)  # 2
```

## ある要素のrootの取得

```python
l = [1, 2, 3, 4, 5, 6]
uf = UnionFind(l)
uf.find_root(3)  # 3
uf.unite(3, 4)
uf.find_root(3)  # 3 or 4
```

## root一覧の取得

```python
l = [1, 2, 3, 4, 5, 6]
uf = UnionFind(l)
print(uf.roots)  # {1, 2, 3, 4, 5, 6}
uf.unite(3, 4)
print(uf.roots)  # {1, 2, 3, 5, 6} or {1, 2, 4, 5, 6}
```

## ループ

`for s in uf`の様にループを回した場合、`s`には集合が一つずつ渡される。

```python
l = [1, 2, 3, 4, 5, 6]
uf = UnionFind(l)
uf.unite(3, 4)
uf.add(7)
uf.unite(1, 5)

for s in uf:
    print(s)

# {2}
# {3, 4}
# {1, 5}
# {6}
# {7}

```

## 表示

```python
l = [1, 2, 3, 4, 5, 6]
uf = UnionFind(l)
uf.unite(3, 4)
uf.add(7)
uf.unite(1, 5)

print(uf)  # [{2}, {3, 4}, {1, 5}, {6}, {7}]
```