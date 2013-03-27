import TileEngine as te
import pygame
import math
import time
from Fountain.World import World
from Fountain.World import EngineType
from Engines.Physics2DEngine import Physics2DEngine
from Engines.Camera2DEngine import Camera2DEngine
from Components.Position2D import Position2D
from Components.Velocity2D import Velocity2D
from Components.Shape2D import Shape2D
from Components.Representation2D import Representation2D
from Components.Camera2D import Camera2D
from Components.AIKeyboard import AIKeyboard
from MazeMaker import makemaze

SQUARESIZE=16
HALFSQUARESIZE=SQUARESIZE/2
SCREENW=640
SCREENH=480

def makePC(world):
  pcblock = pygame.image.load("../resources/images/link.bmp")
  #pcblock = pygame.Surface((SQUARESIZE,SQUARESIZE))
  #pcblock.fill((0,0,255))
  pcblock.set_colorkey((255,0,255))
  #pcblock = pygame.transform.scale(pcblock, (HALFSQUARESIZE,HALFSQUARESIZE))
  pc = world.createEntity()
  pc.addComponent(Position2D(120, 80))
  pc.addComponent(Velocity2D())
  pc.addComponent(Shape2D(pygame.Rect(0,HALFSQUARESIZE,SQUARESIZE,HALFSQUARESIZE)))
  pc.addComponent(Representation2D(pcblock, 0))
  pc.addComponent(Camera2D(pygame.Rect(0,0,SCREENW,SCREENH),1,2))
  pc.addToWorld()
  return pc
  
def makeAI(world):
  aiblock = pygame.image.load("../resources/images/link.bmp")
  #pcblock = pygame.Surface((SQUARESIZE,SQUARESIZE))
  #pcblock.fill((0,0,255))
  aiblock.set_colorkey((255,0,255))
  #aiblock = pygame.transform.scale(aiblock, (HALFSQUARESIZE,HALFSQUARESIZE))
  ai = world.createEntity()
  ai.addComponent(Position2D(80, 80))
  ai.addComponent(Velocity2D())
  ai.addComponent(Shape2D(pygame.Rect(0,HALFSQUARESIZE,SQUARESIZE,HALFSQUARESIZE)))
  ai.addComponent(Representation2D(aiblock, 0))
  ai.addComponent(Camera2D(pygame.Rect(520,20,100,100),0))
  ai.addComponent(AIKeyboard())
  ai.addToWorld()
  return ai

def main():
  quit = False

  pygame.init()
  size = width, height = SCREENW, SCREENH
  screen = pygame.display.set_mode(size)

  world = World()
  world.addEngine(Physics2DEngine(), EngineType.UPDATE)
  world.addEngine(Camera2DEngine(screen), EngineType.RENDER)
  
  pc = makePC(world)
  pcpc = pc.getComponent(Position2D)
  pcvc = pc.getComponent(Velocity2D)
  pcsc = pc.getComponent(Shape2D)
  ai = makeAI(world)
  
  tiles = te.buildMap("../resources/maps/first.map",SQUARESIZE)
  w=20
  h=20
  #tiles = makemaze(w,h,SQUARESIZE)
  #walls = te.getWalls(tiles)

  wallblock = pygame.image.load("../resources/images/wall.bmp")
  floorblock = pygame.Surface((SQUARESIZE,SQUARESIZE))
  floorblock.fill((255,227,171))

  for tile in tiles:
    e = world.createEntity()
    e.addComponent(Position2D(tile.x, tile.y))
    if tile.type == 'wall':
      e.addComponent(Shape2D(pygame.Rect(0,0,tile.size,tile.size)))
      e.addComponent(Representation2D(wallblock,1))
      e.addToWorld()
    elif tile.type == 'floor':
      e.addComponent(Shape2D(pygame.Rect(0,0,tile.size,tile.size), isSolid=False))
      e.addComponent(Representation2D(floorblock,1))
      e.addToWorld()
    #else:
    #  e.addComponent(Square(tile.size, isSolid=False))
    #  e.addComponent(Representation2D(blankblock,1))
    
  #mep = te.blitMap(tiles,w*2+1,h*2+1)
  speed = 4
  t = time.time()
  nexttick = t + (1.0/30)

  while not quit:
    t = time.time()
    if t >= nexttick:
      nexttick = t + (1.0/30)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          quit = True
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            pc.getComponent(Velocity2D).dy = -speed
          if event.key == pygame.K_DOWN:
            pc.getComponent(Velocity2D).dy = speed
          if event.key == pygame.K_LEFT:
            pc.getComponent(Velocity2D).dx = -speed
          if event.key == pygame.K_RIGHT:
            pc.getComponent(Velocity2D).dx = speed
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_UP:
            pc.getComponent(Velocity2D).dy = 0 
          if event.key == pygame.K_DOWN:
            pc.getComponent(Velocity2D).dy = 0
          if event.key == pygame.K_LEFT:
            pc.getComponent(Velocity2D).dx = 0 
          if event.key == pygame.K_RIGHT:
            pc.getComponent(Velocity2D).dx = 0
      buttons = ai.getComponent(AIKeyboard).getButtons()
      for event in buttons:
        if event == None:
          pass
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            ai.getComponent(Velocity2D).dy = -speed
          if event.key == pygame.K_DOWN:
            ai.getComponent(Velocity2D).dy = speed
          if event.key == pygame.K_LEFT:
            ai.getComponent(Velocity2D).dx = -speed
          if event.key == pygame.K_RIGHT:
            ai.getComponent(Velocity2D).dx = speed
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_UP:
            ai.getComponent(Velocity2D).dy = 0 
          if event.key == pygame.K_DOWN:
            ai.getComponent(Velocity2D).dy = 0
          if event.key == pygame.K_LEFT:
            ai.getComponent(Velocity2D).dx = 0 
          if event.key == pygame.K_RIGHT:
            ai.getComponent(Velocity2D).dx = 0

      t0 = time.time()
      world.update()
      t1 = time.time()
      screen.fill((0,0,0))
      world.render()
      pygame.display.flip()
      t2 = time.time()
      fullt=t2-t
      updatet=t1-t0
      rendert=t2-t1
      if fullt != 0:
        print("# of Entities: " + str(len(world.entities)))
        print("# of Walls: " + str(len([e for e in world.entities.values() if Shape2D in e.componentTypes and e.getComponent(Shape2D).isSolid])))
        print("Time: " + str(fullt) + "("+str(fullt*3000)+"%)")
        print("Update: " + str(updatet/fullt*100) + '%')
        print("Render: " + str(rendert/fullt*100) + '%')
        print("Other: " + str((t2-t-updatet-rendert)/fullt*100) + '%\n')
      
if __name__ == '__main__':
  main()
