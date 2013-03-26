from Fountain.Component import Component

class Position2D(Component):
  """2-dimensional position component for an entity."""
  def __init__(self, x=0, y=0):
    self._x = x
    self._y = y
    
  @property
  def x(self):
    return self._x
  @x.setter
  def x(self, value):
    self._x = value
    
  @property
  def y(self):
    return self._y
  @y.setter
  def y(self, value):
    self._y = value
