from Fountain.Component import Component

class Velocity2D(Component):
  """2-dimensional velocity component for an entity."""
  def __init__(self, dx=0, dy=0):
    self._dx = dx
    self._dy = dy
    
  @property
  def dx(self):
    return self._dx
  @dx.setter
  def dx(self, value):
    self._dx = value
    
  @property
  def dy(self):
    return self._dy
  @dy.setter
  def dy(self, value):
    self._dy = value