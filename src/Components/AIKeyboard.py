from Fountain.Component import Component
import pygame
from pygame.event import Event
import random

class AIKeyboard(Component):
  def __init__(self):
    random.seed()
    self._counter = 0
    self._buttons = []
  
  def getButtons(self):
    if not self._counter:
      kup = []
      for b in self._buttons:
        if b.key == pygame.K_UP:
          kup = [Event(pygame.KEYUP, key=pygame.K_UP)]
        if b.key == pygame.K_DOWN:
          kup = [Event(pygame.KEYUP, key=pygame.K_DOWN)]
        if b.key == pygame.K_LEFT:
          kup = [Event(pygame.KEYUP, key=pygame.K_LEFT)]
        if b.key == pygame.K_RIGHT:
          kup = [Event(pygame.KEYUP, key=pygame.K_RIGHT)]
      dir = random.randint(0,4)
      time = random.randint(15,90)
      
      self._counter = time
      if dir == 0:
        self._buttons = [Event(pygame.KEYDOWN, key=pygame.K_UP)]
      if dir == 1:
        self._buttons = [Event(pygame.KEYDOWN, key=pygame.K_LEFT)]
      if dir == 2:
        self._buttons = [Event(pygame.KEYDOWN, key=pygame.K_RIGHT)]
      if dir == 3:
        self._buttons = [Event(pygame.KEYDOWN, key=pygame.K_DOWN)]
      if dir == 4:
        pass
       
      return kup + self._buttons
      
        
    else:
      self._counter -= 1
      return self._buttons