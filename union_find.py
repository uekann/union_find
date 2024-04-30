from typing import Generic, Hashable, Iterable, Optional, Protocol, TypeVar

_T = TypeVar("_T")


class UnionFind(Generic[_T]):
    def __init__(self, l: Iterable[_T]) -> None:
        l_ = set(l)
        self._all_members = l_
        self._parent: dict[_T, Optional[_T]] = {t: None for t in l_}
        self._chils_num: dict[_T, int] = {t: 1 for t in l_}

    def find_root(self, p: _T) -> _T:
        l = []
        while not self._parent[p] is None:
            l.append(p)
            p = self._parent[p]  # type:ignore

        if l:
            l.pop()
            for t in l:
                self._parent[t] = p

        return p

    @property
    def roots(self) -> set[_T]:
        return set(self._chils_num.keys())

    def unite(self, p: _T, q: _T) -> None:
        root_p = self.find_root(p)
        root_q = self.find_root(q)
        if root_p == root_q:
            return
        if self._chils_num[root_p] > self._chils_num[root_q]:
            parent = root_p
            child = root_q
        else:
            parent = root_q
            child = root_p

        self._parent[child] = parent
        self._chils_num[parent] += self._chils_num[child]
        del self._chils_num[child]

    def add(self, p: _T) -> None:
        if p in self._all_members:
            return
        self._parent[p] = None
        self._all_members.add(p)
        self._chils_num[p] = 1

    def is_in_same(self, p: _T, q: _T) -> bool:
        return self.find_root(p) == self.find_root(q)

    def get_size(self, p: _T) -> int:
        return self._chils_num[self.find_root(p)]

    def __iter__(self):
        d = {r: set() for r in self._roots}
        for p in self._all_members:
            d[self.find_root(p)].add(p)

        return list(d.values()).__iter__()

    def __str__(self) -> str:
        return str(list(self))

    def __repr__(self) -> str:
        return f"UnionFind({self._all_members})"
