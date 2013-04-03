from Representation2D import Representation2D

class Sprite(Representation2D):
  def __init__(self, depth, **kwargs):
    isVisible = kwargs.pop('isVisible', True)
    self._spritemap = kwargs
    self._spritekey = kwargs.keys()[0]
    self._frame = 0
    self._i = 0
    super(Sprite, self).__init__(kwargs.values()[0][0], depth, isVisible)

  @property
  def spritekey(self):
    return self.spritekey
  @spritekey.setter
  def spritekey(self, value):
    self.spritekey = value

  def step(self):
    if self._frame < self._spritemap[self._spritekey][i][1]:
      self._frame += 1
    else:
      self._i = (self._i + 1) % len(self._spritemap[self._spritekey])
      self._frame = 0
      self._image = self._spritemap[self._spritekey][i][0]
    
