class DisjointSets(object):
  def __init__(self, n):
    self._size = n
    self._s = [-1 for x in range(n)]

  @property
  def size(self):
    return self._size

  def union(self, a, b):
    if self._s[b] < self._s[a]:
      self._s[a] = b
    else:
      if self._s[a] == self._s[b]:
        self._s[a] -= 1
      self._s[b] = a

  def find(self, a):
    if self._s[a] < 0:
      return a
    else:
      self._s[a] = self.find(self._s[a])
      return self._s[a]

