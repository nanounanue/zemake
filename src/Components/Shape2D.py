from Fountain.Component import Component

class Shape2D(Component):
  def __init__(self, *aabbs, **kwargs):
    self._aabbs = aabbs
    self._isSolid = kwargs.pop('isSolid', True)
    w = 0
    h = 0
    for aabb in aabbs:
      if aabb.w + aabb.x > w:
        w = aabb.w+aabb.x
      if aabb.h + aabb.y > h:
        h = aabb.h + aabb.y
    self._w = w
    self._h = h
    self._halfw = w / 2
    self._halfh = h / 2
    
  ## THESE WILL PROBABLY BE REMOVED ##
  def left(self, x):
    return x
  def right(self, x):
    return self._w + x
  def top(self, y):
    return y
  def bottom(self, y):
    return self._h + y
  @property
  def halfw(self):
    return self._halfw
  @property
  def halfh(self):
    return self._halfh
  ####
    
  @property
  def w(self):
    return self._w
  @property
  def h(self):
    return self._h

  @property
  def isSolid(self):
    return self._isSolid

  @isSolid.setter
  def isSolid(self, value):
    self._isSolid = value
    
  def collides(self, selfx, selfy, other, otherx, othery):
    for selfaabb in self._aabbs:
      for otheraabb in other._aabbs:
        if not (selfx + selfaabb.x >= otherx + otheraabb.x + otheraabb.w
            or selfx + selfaabb.x + selfaabb.w <= otherx + otheraabb.x
            or selfy + selfaabb.y >= othery + otheraabb.y + otheraabb.h
            or selfy + selfaabb.y + selfaabb.h <= othery + otheraabb.y):
          return True
    return False
    
if __name__ == '__main__':
  import random
  import unittest
  
  from pygame import Rect
  
  class TestShape2D(unittest.TestCase):
    def setUp(self):
      pass
      
    def testWidth(self):
      s1 = Shape2D(Rect(0,0,4,2), Rect(0,2,2,2))
      s2 = Shape2D(Rect(0,0,4,2), Rect(2,2,2,2))
      s3 = Shape2D(Rect(0,2,4,2))
      self.assertEquals(s1.w, 4)
      self.assertEquals(s1.h, 4)
      self.assertEquals(s2.w, 4)
      self.assertEquals(s2.h, 4)
      self.assertEquals(s3.w, 4)
      self.assertEquals(s3.h, 4)
      
      
    def testCollisions(self):
      s1 = Shape2D(Rect(0,0,4,2), Rect(0,2,2,2))
      s2 = Shape2D(Rect(0,0,4,2), Rect(2,2,2,2))
      s1x, s1y, s2x, s2y = 0,0,3,3
      #s1 and s2 shouldn't collide . . .
      self.assertFalse(s1.collides(s1x,s1y,s2,s2x,s2y), "The two shapes should not collide.")
  
      s1x, s1y, s2x, s2y = 0,0,2,2
      #still shouldn't collide . . .
      self.assertFalse(s1.collides(s1x,s1y,s2,s2x,s2y), "The two shapes should not collide.")
  
      s1x, s1y, s2x, s2y = 0,0,1,1
      #now they should . . .
      self.assertTrue(s1.collides(s1x,s1y,s2,s2x,s2y), "The two shapes should collide.")
  
      s1x, s1y, s2x, s2y = 0,0,0,0
      #and they should again . . .
      self.assertTrue(s1.collides(s1x,s1y,s2,s2x,s2y), "The two shapes should collide.")
  
      s1 = Shape2D(Rect(0,0,4,2), Rect(0,2,2,2))
      s2 = Shape2D(Rect(2,2,2,2))
      s1x, s1y, s2x, s2y = 0,0,0,0
      #Once again, shouldn't collide . . .
      self.assertFalse(s1.collides(s1x,s1y,s2,s2x,s2y), "The two shapes should not collide.")
      
  unittest.main()
  
