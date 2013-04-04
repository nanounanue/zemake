from Fountain.Engine import Engine
from Components.Position2D import Position2D
from Components.Velocity2D import Velocity2D
from Components.Shape2D import Shape2D
from Components.Hazard import Hazard
from Components.Player import Player
from Components.Health import Health

class Physics2DEngine(Engine):
  """A system for processing 2-dimensional physics calculations."""
  def __init__(self):
    super(Physics2DEngine, self).__init__(Position2D, Velocity2D, Shape2D)

  def update(self):
    for entity in [e for e in self._entities.values()]:
      epc = entity.getComponent(Position2D)
      evc = entity.getComponent(Velocity2D)
      esc = entity.getComponent(Shape2D)
      olddx = evc.dx
      olddy = evc.dy
      
      if Player in entity.componentTypes and Health in entity.componentTypes:
        ehc = entity.getComponent(Health)
        hazards = [e for e in self.world.entities.values()
                   if Hazard in e.componentTypes
                   and Shape2D in e.componentTypes
                   and Position2D in e.componentTypes]
        for hazard in hazards:
          hpc = hazard.getComponent(Position2D)
          hsc = hazard.getComponent(Shape2D)
          if esc.collides(epc.x, epc.y, hsc, hpc.x, hpc.y):
            ehc.remove(8)
            if evc.dx == 0 and evc.dy == 0:
              evc.dx = 16
            elif evc.dx != 0:
              evc.dx = -16*(evc.dx/abs(evc.dx))
            else:
              evc.dy = -16*(evc.dy/abs(evc.dy))
          
      walls = [e for e in set(self.world.entities.values())-(set([(entity)]))
               if Shape2D in e.componentTypes
               and e.getComponent(Shape2D).isSolid
               and Velocity2D not in e.componentTypes
               and _near(e.getComponent(Position2D), epc, evc.dx, evc.dy)]

      epc.x += evc.dx
      for wall in walls:
        wpc = wall.getComponent(Position2D)
        wsc = wall.getComponent(Shape2D)
        if esc.collides(epc.x, epc.y, wsc, wpc.x, wpc.y):
          if evc.dx > 0: epc.x = wsc.left(wpc.x)-esc.w
          elif evc.dx < 0: epc.x = wsc.right(wpc.x)
        
      epc.y += evc.dy
      for wall in walls:
        wpc = wall.getComponent(Position2D)
        wsc = wall.getComponent(Shape2D)
        if esc.collides(epc.x, epc.y, wsc, wpc.x, wpc.y):
          if evc.dy > 0: epc.y = wsc.top(wpc.y)-esc.h
          elif evc.dy < 0: epc.y = wsc.bottom(wpc.y)-esc.halfh
      if evc.dx >= 16: evc.dx = olddx
      if evc.dy >= 16: evc.dy = olddy

def _isMoving(e):
  vc = e.getComponent(Velocity2D)
  return vc.dx != 0 or vc.dy != 0
  
def _near(p1,p2,dx,dy):
  #return True
  return abs(p1.x-p2.x<20) and abs(p1.y-p2.y<20)
