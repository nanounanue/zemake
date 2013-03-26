import pygame
from Fountain.Engine import Engine
from Components.Camera2D import Camera2D
from Components.Representation2D import Representation2D
from Components.Position2D import Position2D
from Components.Square import Square

class Camera2DEngine(Engine):
  """A system for rendering 2-dimensional scenes via a camera viewport."""
  def __init__(self, screen):
    self._screen = screen
    super(Camera2DEngine, self).__init__(Position2D, Camera2D)
    
  def update(self):
    for entity in reversed(sorted(self._entities.values(), key=lambda e: e.getComponent(Camera2D).depth)):
      epc = entity.getComponent(Position2D)
      ecc = entity.getComponent(Camera2D)
      halfw = ecc.outputRegion.w / 2.0
      halfh = ecc.outputRegion.h / 2.0
          
      viewport = pygame.Surface((ecc.outputRegion.w, ecc.outputRegion.h))
      renderables = [e for e in self.world.entities.values() 
                     if Representation2D in e.componentTypes
                       and e.getComponent(Representation2D).isVisible
                       and Square in e.componentTypes
                       and Position2D in e.componentTypes]
      
      for r in reversed(sorted(renderables, 
          key=lambda x: x.getComponent(Representation2D).depth)):
        rrc = r.getComponent(Representation2D)
        rsc = r.getComponent(Square)
        rpc = r.getComponent(Position2D)
        camrect = pygame.Rect(ecc.outputRegion)
        camrect.center = epc.x, epc.y
        if (camrect.colliderect(
         pygame.Rect(rsc.left(rpc.x), rsc.top(rpc.y), rsc.size, rsc.size))):
          viewport.blit(rrc.image, (rsc.left(rpc.x)+halfw-epc.x, 
                                  rsc.top(rpc.y)+halfh-epc.y))
      frame = pygame.Surface((ecc.outputRegion.w+2, ecc.outputRegion.h+2))
      frame.fill((255,0,0))
      self._screen.blit(frame, (ecc.outputRegion.x-1, ecc.outputRegion.y-1))
      self._screen.blit(viewport, (ecc.outputRegion.x, ecc.outputRegion.y))
          
    
