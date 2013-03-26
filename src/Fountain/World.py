import uuid
from Messages import Messages
from Fountain.Utils import enum

from Entity import Entity

EngineType = enum('UPDATE', 'RENDER')

class World(object):
  def __init__(self):
    self._entities = {}
    self._engines = {}
    
  @property
  def entities(self):
    return self._entities
  @property
  def updateEngines(self):
    return set(self._engines[EngineType.UPDATE])
  @property
  def renderEngines(self):
    return set(self._engines[EngineType.RENDER])
  @property
  def engines(self):
    return [e for v in self._engines.values() for e in v]
    
  def createEntity(self):
    uid = uuid.uuid1()
    entity = Entity(self, uid)
    return entity
    
  def addEntity(self, entity):
    self._entities[entity.uid] = entity
    self._notifyEngines(Messages.ADD, entity)
    return entity
    
  def updateEntity(self, entity):
    if not entity.uid in self._entities.keys:
      self._entities[entity.uid] = entity
    else:
      self._notifyEngines(Messages.UPDATE, entity)
      return entity

  def addEngine(self, engine, engineType=EngineType.UPDATE):
    if engineType not in self._engines.keys():
      self._engines[engineType] = []
    self._engines[engineType].append(engine)
    engine.world = self
    # TODO: Update engine with every current world entity
    return engine
    
  def _notifyEngines(self, message, entity):
    for engine in self.engines:
      engine.notify(message, entity)
      
  def update(self):
    for engine in self._engines[EngineType.UPDATE]:
      engine.update()

  def render(self):
    for engine in self._engines[EngineType.RENDER]:
      engine.update()
    
if __name__ == '__main__':
  #UNIT TESTS
  w = World()
  #INTEGRATION TESTS
  e = w.createEntity()
  print(e.uid)
