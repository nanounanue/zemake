import pygame
from Fountain.Component import Component

class Camera2D(Component):
  def __init__(self, outputRegion, depth=0, zoom=1, isActive=True, border=None):
    if not isinstance(outputRegion, pygame.Rect):
      raise TypeError("Camera2D outputRegion only supports pygame.Rect")
    self._outputRegion = outputRegion
    if depth > 50: 
      depth = 50
    elif depth < 0:
      depth = 0
    self._depth = depth
    self._zoom = zoom
    self._isActive = isActive
    if border is None:
      border = (0,0,0)
    self._border = border
   
  @property
  def zoom(self):
    return self._zoom
  @zoom.setter
  def zoom(self, value):
    self._zoom = value
    
  @property
  def border(self):
    return self._border
  @border.setter
  def border(self, value):
    self._border = value

  @property
  def outputRegion(self):
    return self._outputRegion
  @outputRegion.setter
  def outputRegion(self, value):
    self._outputRegion = value

  @property
  def depth(self):
    return self._depth
  @depth.setter
  def depth(self, value):
    self._depth = value

  @property
  def isActive(self):
    return self._isActive
  @isActive.setter
  def isActive(self, value):
    self._isActive = value

  def toggle(self):
    self._isActive = not self._isActive
