from Shape2D import Shape2D
#from Fountain.Utils import enum

class Square(Shape2D):
  def __init__(self, size, isSolid=True):
    self._size = size
    self._half = size / 2.0
    super(Square, self).__init__(isSolid)
#    self._anchor = anchor

  @property
  def size(self):
    return self._size
    
  @property
  def half(self):
    return self._half
    
#  @property
#  def anchor(self):
#    return self._anchor

  def left(self, x):
    return x - self._half
    
  def right(self, x):
    return x + self._half
    
  def top(self, y):
    return y - self._half
    
  def bottom(self, y):
    return y + self._half

  def topleft(self, x, y):
    return (x - self._half, y - self._half)
    
#SquareAnchors = enum('TOPLEFT', 'TOP', 'TOPRIGHT', 
#                     'LEFT', 'CENTER', 'RIGHT',
#                     'BOTTOMLEFT', 'BOTTOM', 'BOTTOMRIGHT')
