from DisjointSets import DisjointSets
import random
from TileEngine import Tile

def _newp(i,tw):
  hw=tw/2.0
  return i*tw+hw

def makemaze(w,h,tw):
  random.seed()
  size = w*h
  ds = DisjointSets(size)
  walls = ([(a,a+1) for a in [x for x in range(size) if (x+1)%w != 0]]
          + [(a,a+w) for a in [x for x in range(size-w)]])
  while not _done(ds):
    a,b = walls[random.randint(0, len(walls)-1)]
    x,y = ds.find(a), ds.find(b)
    if not x == y:
      ds.union(x,y)
      walls.remove((a,b))

  tiles = ([Tile('wall',_newp(i,tw),_newp(j,tw),tw) for i in range(2*w+1) for j in range(2*h+1)
           if (i == 0 or j == 0 or i == w*2 or j == h*2 or (i%2==0 and j%2==0))
           and not (j == 2*h-1 and i == 2*w)]
           + [Tile('floor',_newp(i,tw),_newp(j,tw),tw) 
              for i in range(1,2*w+1) for j in range(1,2*h+1)
              if (i%2==1 and j%2==1)
              or (j == 2*h-1 and i == 2*w)]
           + [Tile('wall' if i%2==0 and
                            list(set([(a,a+1) for a in range(i/2-1,size,w)])
                             & set([(b,b+1) for b in 
                                range(j/2*w,(j/2+1)*w-1)]))[0] in walls
                          or i%2==1 and
                            list(set([(a,a+w) for a in range(i/2,size,w)])
                            & set([(b,b+w) for b in 
                               range((j/2-1)*w,j/2*w)]))[0] in walls
                          else 'floor'
                   ,_newp(i,tw),_newp(j,tw),tw) 
              for i in range(1,2*w) for j in range(1,2*h)
              if i%2 != j%2])

  return tiles

def _done(ds):
  root = ds.find(0)
  for i in range(ds.size):
    if ds.find(i) != root:
      return False
  return True
  

if __name__ == '__main__':
  print(makemaze(10,5))
