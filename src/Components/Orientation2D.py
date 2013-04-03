from Fountain.Component import Component
from Fountain.Utils import enum

Direction = enum('UP', 'DOWN', 'LEFT', 'RIGHT')

class Orientation2D(Component):
  def __init__(self, direction=Direction.DOWN):
    self._orientation = direction
    
  @property
  def direction(self):
    return self._orientation
    
  @direction.setter
  def direction(self, value):
    self._orientation = value
    
  