import pygame
from Fountain.Engine import Engine
from Components.Camera2D import Camera2D
from Components.Representation2D import Representation2D
from Components.Position2D import Position2D
from Components.Shape2D import Shape2D

class Camera2DEngine(Engine):
  """A system for rendering 2-dimensional scenes via a camera viewport."""
  def __init__(self, screen):
    self._screen = screen
    super(Camera2DEngine, self).__init__(Position2D, Camera2D)
    
  def update(self):
    for entity in reversed(sorted(self._entities.values(), key=lambda e: e.getComponent(Camera2D).depth)):
      epc = entity.getComponent(Position2D)
      ecc = entity.getComponent(Camera2D)
      halfw = ecc.outputRegion.w / 2
      halfh = ecc.outputRegion.h / 2
          
      viewport = pygame.Surface((ecc.outputRegion.w, ecc.outputRegion.h))
      renderables = [e for e in self.world.entities.values() 
                     if Representation2D in e.componentTypes
                       and e.getComponent(Representation2D).isVisible
                       and Shape2D in e.componentTypes
                       and Position2D in e.componentTypes]
      camrect = pygame.Rect(ecc.outputRegion)
      camrect.w = camrect.w/ecc.zoom
      camrect.h = camrect.h/ecc.zoom
      camrect.center = epc.x, epc.y
      
      for r in reversed(sorted(renderables, 
          key=lambda x: x.getComponent(Representation2D).depth)):
        rrc = r.getComponent(Representation2D)
        rsc = r.getComponent(Shape2D)
        rpc = r.getComponent(Position2D)
        if (camrect.colliderect(
         pygame.Rect(rsc.left(rpc.x), rsc.top(rpc.y), rsc.w, rsc.h))):
          viewport.blit(pygame.transform.scale(rrc.image, (rsc.w*ecc.zoom, rsc.h*ecc.zoom)), 
                        ((rsc.left(rpc.x)-epc.x)*ecc.zoom+halfw, (rsc.top(rpc.y)-epc.y)*ecc.zoom+halfh))
      frame = pygame.Surface((camrect.w+2, camrect.h+2))
      frame.fill((255,0,0))
      self._screen.blit(frame, (ecc.outputRegion.x-1, ecc.outputRegion.y-1))
      self._screen.blit(viewport, (ecc.outputRegion.x, ecc.outputRegion.y))
          
    
