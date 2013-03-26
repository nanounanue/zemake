from Fountain.Component import Component

class Shape2D(Component):
  def __init__(self, isSolid=True):
    self._isSolid = isSolid

  @property
  def isSolid(self):
    return self._isSolid

  @isSolid.setter
  def isSolid(self, value):
    self._isSolid = value
