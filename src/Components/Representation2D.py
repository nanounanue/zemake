from Fountain.Component import Component

class Representation2D(Component):
  def __init__(self, image, depth, isVisible=True):
    self._image = image
    self._depth = depth
    self._isVisible = isVisible

  @property
  def image(self):
    return self._image
  @image.setter
  def image(self, value):
    self._image = value

  @property
  def isVisible(self):
    return self._isVisible
  @isVisible.setter
  def isVisible(self, value):
    self._isVisible = value

  @property
  def depth(self):
    return self._depth
  @depth.setter
  def depth(self, value):
    self._depth = value
