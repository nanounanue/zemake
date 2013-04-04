import TileEngine as te
import pygame
import math
import time
import random
from Fountain.World import World
from Fountain.World import EngineType
from Engines.Physics2DEngine import Physics2DEngine
from Engines.Camera2DEngine import Camera2DEngine
from Engines.InputEngine import InputEngine
from Components.Position2D import Position2D
from Components.Velocity2D import Velocity2D
from Components.Shape2D import Shape2D
from Components.Representation2D import Representation2D
from Components.Camera2D import Camera2D
from Components.AIKeyboard import AIKeyboard
from Components.Player import Player
from Components.Hazard import Hazard
from Components.Weapon import Weapon
from Components.Health import Health

SQUARESIZE=16
HALFSQUARESIZE=SQUARESIZE/2
SCREENW=512
SCREENH=480

def makePC(world):
  pcblock = pygame.image.load("../resources/images/link.bmp")
  #pcblock = pygame.Surface((SQUARESIZE,SQUARESIZE))
  #pcblock.fill((0,0,255))
  pcblock.set_colorkey((255,0,255))
  #pcblock = pygame.transform.scale(pcblock, (HALFSQUARESIZE,HALFSQUARESIZE))
  pc = world.createEntity()
  pcpos = Position2D(120,80)
  pc.addComponent(Position2D(120, 80))
  pc.addComponent(Velocity2D())
  pc.addComponent(Shape2D(pygame.Rect(0,HALFSQUARESIZE,SQUARESIZE,HALFSQUARESIZE)))
  pc.addComponent(Representation2D(pcblock, 0))
  pc.addComponent(Player())
  pc.addComponent(Health(16*3))
  #pc.addComponent(Camera2D(pygame.Rect(HALFSQUARESIZE,SQUARESIZE*2*4,SCREENW-SQUARESIZE,SQUARESIZE*2*11),1,2))
  pc.addToWorld()
  
  cam = world.createEntity()
  cam.addComponent(Camera2D(pygame.Rect(0,SQUARESIZE*2*4,SCREENW,SQUARESIZE*2*11),depth=0,zoom=2))
  cam.addComponent(Position2D(128, 88))
  cam.addToWorld()
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
  #ai.addComponent(Camera2D(pygame.Rect(HALFSQUARESIZE,0,SCREENW-SQUARESIZE,SQUARESIZE*2*4),0,0.5))
  ai.addComponent(AIKeyboard())
  ai.addComponent(Hazard())
  ai.addToWorld()
  return ai

def main():
  quit = False
  random.seed()

  pygame.init()
  size = width, height = SCREENW, SCREENH
  screen = pygame.display.set_mode(size)

  world = World()
  inputEngine = InputEngine()
  physEngine = Physics2DEngine()
  camEngine = Camera2DEngine(screen)
  world.addEngine(inputEngine, EngineType.MANUAL)
  world.addEngine(physEngine, EngineType.UPDATE)
  world.addEngine(camEngine, EngineType.RENDER)
  
  pc = makePC(world)
  pcpc = pc.getComponent(Position2D)
  pcvc = pc.getComponent(Velocity2D)
  pcsc = pc.getComponent(Shape2D)
  pchc = pc.getComponent(Health)
  ai = makeAI(world)
  
  tiles = te.buildMap("../resources/maps/first.map",SQUARESIZE)
  w=20
  h=20

  wallblock = pygame.image.load("../resources/images/wall.bmp")
  walltopblock = pygame.image.load("../resources/images/walltop.bmp")
  topleftcornerblock = pygame.image.load("../resources/images/topleftcorner.bmp")
  toprightcornerblock = pygame.image.load("../resources/images/toprightcorner.bmp")
  bottomrightcornerblock = pygame.image.load("../resources/images/bottomrightcorner.bmp")
  bottomleftcornerblock = pygame.image.load("../resources/images/bottomleftcorner.bmp")
  floorblock = pygame.Surface((SQUARESIZE,SQUARESIZE))
  floorblock.fill((255,227,171))

  for tile in [t for t in tiles if t.type != 'blank']:
    e = world.createEntity()
    e.addComponent(Position2D(tile.x, tile.y))
    e.addComponent(Shape2D(pygame.Rect(0,0,tile.size,tile.size), isSolid = False))
    if tile.type == 'wall':
      e.addComponent(Representation2D(wallblock,1))
      e.getComponent(Shape2D).isSolid = True
    if tile.type == 'wall-top':
      e.addComponent(Representation2D(walltopblock,1))
      e.getComponent(Shape2D).isSolid = True
    elif tile.type == 'floor':
      e.addComponent(Representation2D(floorblock,1))
    elif tile.type == 'top-left-corner':
      e.addComponent(Representation2D(topleftcornerblock,1))
      e2 = world.createEntity()
      e2.addComponent(Position2D(tile.x,tile.y+tile.size/2))
      e2.addComponent(Shape2D(pygame.Rect(0,0,tile.size/2,tile.size/2)))
      e2.addToWorld()
      e3 = world.createEntity()
      e3.addComponent(Position2D(tile.x, tile.y))
      e3.addComponent(Shape2D(pygame.Rect(0,0,tile.size,tile.size/2)))
      e3.addToWorld()
    elif tile.type == 'top-right-corner':
      e.addComponent(Representation2D(toprightcornerblock,1))
      e2 = world.createEntity()
      e2.addComponent(Position2D(tile.x+tile.size/2,tile.y+tile.size/2))
      e2.addComponent(Shape2D(pygame.Rect(0,0,tile.size/2,tile.size/2)))
      e2.addToWorld()
      e3 = world.createEntity()
      e3.addComponent(Position2D(tile.x, tile.y))
      e3.addComponent(Shape2D(pygame.Rect(0,0,tile.size,tile.size/2)))
      e3.addToWorld()
    elif tile.type == 'bottom-right-corner':
      e.addComponent(Representation2D(bottomrightcornerblock,1))
      e2 = world.createEntity()
      e2.addComponent(Position2D(tile.x+tile.size/2,tile.y))
      e2.addComponent(Shape2D(pygame.Rect(0,0,tile.size/2,tile.size/2)))
      e2.addToWorld()
      e3 = world.createEntity()
      e3.addComponent(Position2D(tile.x,tile.y+tile.size/2))
      e3.addComponent(Shape2D(pygame.Rect(0,0,tile.size,tile.size/2)))
      e3.addToWorld()
    elif tile.type == 'bottom-left-corner':
      e.addComponent(Representation2D(bottomleftcornerblock,1))
      e2 = world.createEntity()
      e2.addComponent(Position2D(tile.x,tile.y))
      e2.addComponent(Shape2D(pygame.Rect(0,0,tile.size/2,tile.size/2)))
      e2.addToWorld()
      e3 = world.createEntity()
      e3.addComponent(Position2D(tile.x,tile.y+tile.size/2))
      e3.addComponent(Shape2D(pygame.Rect(0,0,tile.size,tile.size/2)))
      e3.addToWorld()
    e.addToWorld()
    
  #mep = te.blitMap(tiles,w*2+1,h*2+1)
  aispeed = random.randint(2,6)
  t = time.time()
  nexttick = t + (1.0/30)
  ct = 90
  hbg = pygame.Surface((32*3,32))
  hbg.fill((255,255,255))
  hbgrect = (5,5)
  hfg = pygame.Surface((32*3-2,30))  
  hfg.fill((255,0,0))
  hfgrect = (6,6)    
  while not quit:
    t = time.time()
    if t >= nexttick:
      if ct == 0: 
        #physEngine.toggle()
        ct = 90
      ct -= 1
      nexttick = t + (1.0/30)
      buttons = ai.getComponent(AIKeyboard).getButtons()
      for event in buttons:
        if event == None:
          pass
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            ai.getComponent(Velocity2D).dy = -aispeed
          if event.key == pygame.K_DOWN:
            ai.getComponent(Velocity2D).dy = aispeed
          if event.key == pygame.K_LEFT:
            ai.getComponent(Velocity2D).dx = -aispeed
          if event.key == pygame.K_RIGHT:
            ai.getComponent(Velocity2D).dx = aispeed
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_UP:
            ai.getComponent(Velocity2D).dy = 0 
          if event.key == pygame.K_DOWN:
            ai.getComponent(Velocity2D).dy = 0
          if event.key == pygame.K_LEFT:
            ai.getComponent(Velocity2D).dx = 0 
          if event.key == pygame.K_RIGHT:
            ai.getComponent(Velocity2D).dx = 0
      if inputEngine.update() == pygame.event.Event(pygame.QUIT):
        quit = True
      t0 = time.time()
      world.update()
      t1 = time.time()
      screen.fill((0,0,0))
      world.render()
      screen.blit(hbg, hbgrect)
      hfg = pygame.transform.scale(hfg, ((32*3-2)*(pchc.health)/pchc.max, 30))
      screen.blit(hfg, hfgrect)
      pygame.display.flip()
      t2 = time.time()
      fullt=t2-t
      updatet=t1-t0
      rendert=t2-t1
      #if fullt != 0:
        #print("# of Entities: " + str(len(world.entities)))
        #print("# of Walls: " + str(len([e for e in world.entities.values() if Shape2D in e.componentTypes and e.getComponent(Shape2D).isSolid])))
        #print("Time: " + str(fullt) + "("+str(fullt*3000)+"%)")
        #print("Update: " + str(updatet/fullt*100) + '%')
        #print("Render: " + str(rendert/fullt*100) + '%')
        #print("Other: " + str((t2-t-updatet-rendert)/fullt*100) + '%\n')
      
if __name__ == '__main__':
  main()
