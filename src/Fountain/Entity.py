class Entity(object):
  def __init__(self, world, uid):
    self._world = world
    self._uid = uid
    self._components = {}
    
  def addToWorld(self):
    self._world.addEntity(self)
    
  def addComponent(self, component):
    self._components[type(component)] = component
    return component
    
  def removeComponent(self, componentType):
    return self._components.pop(componentType)
  
  def clearComponents(self):
    self._components.clear()
  
  @property
  def world(self):
    return self._world
    
  @property
  def uid(self):
    return self._uid
    
  @property
  def components(self):
    return self._components.values()
    
  @property
  def componentTypes(self):
    return self._components.keys()

  def getComponent(self, componentType):
    return self._components[componentType]
    
if __name__ == '__main__':
  #UNIT TESTS
  import uuid
  e = Entity(uuid.uuid1())
  print(e.uid)
  
  class foo: pass
  class bar: pass
  class baz: pass
  
  e.addComponent(foo())
  print(e._components)
  e.addComponent(bar())
  print(e._components)
  e.removeComponent(foo)
  print(e._components)
  e.removeComponent(bar)
  print(e._components)
  e.addComponent(baz())
  print(e._components)
  e.addComponent(foo())
  print(e._components)
  e.clearComponents()
  print(e._components)
