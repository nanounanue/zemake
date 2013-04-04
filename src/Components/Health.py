from Fountain.Component import Component

class Health(Component):
  def __init__(self, max, initial=None):
    self._max = max
    if initial is None:
      initial = max
    self._health = min(max, initial)
    
  @property
  def max(self):
    return self._max
  @max.setter
  def max(self, value):
    self._max = value
    
  @property
  def health(self):
    return self._health
  @health.setter
  def health(self, value):
    self._health = value
    
  def add(self, value):
    self._health = max(min(self._max, self._health + value), 0)
    
  def remove(self, value):
    self.add(-value)
    
    
if __name__ == '__main__':
  import unittest
  
  class TestShape2D(unittest.TestCase):
    def setUp(self):
      pass
      
    def testInit(self):
      h = Health(100, 50)
      self.assertEquals(h.max, 100)
      self.assertEquals(h.health, 50)
    def testAdd(self):
      h = Health(100, 50)
      h.add(25)
      self.assertEquals(h.health, 75)
    def testAddOver(self):
      h = Health(100, 50)
      h.add(70)
      self.assertEquals(h.health, 100)
    def testAddUnder(self):
      h = Health(100, 50)
      h.add(-70)
      self.assertEquals(h.health, 0)
    def testRemove(self):
      h = Health(100)
      h.remove(70)
      self.assertEquals(h.health, 30)
    def testRemoveUnder(self):
      h = Health(100, 69)
      h.remove(70)
      self.assertEquals(h.health, 0)
      
  unittest.main()
  