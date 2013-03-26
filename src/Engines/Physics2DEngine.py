from Fountain.Engine import Engine
from Components.Position2D import Position2D
from Components.Velocity2D import Velocity2D
from Components.Square import Square

class Physics2DEngine(Engine):
  """A system for processing 2-dimensional physics calculations."""
  def __init__(self):
    super(Physics2DEngine, self).__init__(Position2D, Velocity2D, Square)

  def update(self):
    for entity in [e for e in self._entities.values() if _isMoving(e)]:
      epc = entity.getComponent(Position2D)
      evc = entity.getComponent(Velocity2D)
      esc = entity.getComponent(Square)
          
      walls = [e for e in set(self.world.entities.values())-(set([(entity)]))
               if Square in e.componentTypes
               and e.getComponent(Square).isSolid
               and _near(e.getComponent(Position2D), epc)]

      epc.x += evc.dx
      for wall in walls:
        wpc = wall.getComponent(Position2D)
        wsc = wall.getComponent(Square)
        if _collide(epc,esc,wpc,wsc):
          if evc.dx > 0: epc.x = wsc.left(wpc.x)-esc.half
          elif evc.dx < 0: epc.x = wsc.right(wpc.x)+esc.half
        
      epc.y += evc.dy
      for wall in walls:
        wpc = wall.getComponent(Position2D)
        wsc = wall.getComponent(Square)
        if _collide(epc,esc,wpc,wsc):
          if evc.dy > 0: epc.y = wsc.top(wpc.y)-esc.half
          elif evc.dy < 0: epc.y = wsc.bottom(wpc.y)+esc.half
    
def _collide(ap, az, bp, bz):
  return not (az.right(ap.x) <= bz.left(bp.x)
              or az.left(ap.x) >= bz.right(bp.x)
              or az.top(ap.y) >= bz.bottom(bp.y)
              or az.bottom(ap.y) <= bz.top(bp.y))

def _isMoving(e):
  vc = e.getComponent(Velocity2D)
  return vc.dx != 0 or vc.dy != 0
  
def _near(p1,p2):
  #return True
  return abs(p1.x-p2.x<50) and abs(p1.y-p2.y<50)
