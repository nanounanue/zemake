import xml.etree.ElementTree as et
import pygame

def buildMap(filename, tileWidth):
  tree = et.parse(filename)
  root = tree.getroot()
  
  width = int(root.get('width'))
  height = int(root.get('height'))
  
  rettiles = []
  
  rows = root.findall('row')
  for j in range(len(rows)):
    tiles = rows[j].findall('tile')
    row = []
    for i in range(len(tiles)):
      row.append(Tile(tiles[i].get('type', 'blank'), i*tileWidth, j*tileWidth))
    rettiles.append(row)
  
  return [tile for row in rettiles for tile in row]
  
class Tile:
  def __init__(self, t, x, y, size, url=None):
    self._type = t
    self._size = size
    self._halfsize = size / 2.0
    self._url = url
    self._x = x
    self._y = y

    self._top = y
    self._bottom = y + self._size
    self._left = x
    self._right = x + self._size
    self._center = (x+self._halfsize,y+self._halfsize)
    
  @property
  def type(self):
    return self._type

  @property
  def size(self):
    return self._size
    
  @property
  def halfsize(self):
    return self._halfsize
    
  @property
  def url(self):
    return self._url
    
  @property
  def x(self):
    return self._x
    
  @property
  def y(self):
    return self._y

  @property
  def top(self): 
    return self._top

  @property
  def bottom(self): 
    return self._bottom

  @property
  def left(self): 
    return self._left

  @property
  def right(self): 
    return self._right

  @property
  def center(self):
    return self._center

  def __repr__(self):
    return 'Tile<'+self._type +','+ str(self._x) +','+ str(self._y)+'>'
