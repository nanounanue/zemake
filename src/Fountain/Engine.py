from Messages import Messages

class Engine(object):
  def __init__(self, *componentTypes, **kwargs):
    self._world = None
    self._componentTypes = set(componentTypes)
    self._entities = {}
    self._isActive = kwargs.pop('isActive', True)
    
  def notify(self, message, entity):
    if message == Messages.ADD:
      if self._isInteresting(entity): self._entities[entity.uid] = entity
    if message == Messages.UPDATE:
      if self._isInteresting(entity): self._entities[entity.uid] = entity
    if message == Messages.DELETE:
      if entity.uid in self._entities.keys: self._entities.pop(entity.uid)
    
  def update(self):
    raise NotImplementedError("override me!")
  
  @property
  def isActive(self):
    return self._isActive
  @isActive.setter
  def isActive(self, value):
    self._isActive = value
    
  def toggle(self):
    self._isActive = not self._isActive
    
  @property
  def world(self):
    return self._world
    
  @world.setter
  def world(self, value):
    if self._world == None:
      self._world = value
    
  def _isInteresting(self, entity):
    for t in self._componentTypes:
      if not _hasType(entity, t): return False
    return True
        
def _hasType(entity, t):
  for c in entity.components:
    if isinstance(c, t): return True
  return False
