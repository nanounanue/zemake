import pygame
from Fountain.Engine import Engine
from Components.Player import Player
from Components.Velocity2D import Velocity2D

class InputEngine(Engine):
  """A system for processing player input."""
  def __init__(self):
    super(InputEngine, self).__init__(Player, Velocity2D)
    self._speed = 4
    self._buttonsActive = True

  def update(self):
    events = pygame.event.get()
    for entity in self._entities.values():
      vc = entity.getComponent(Velocity2D)
      for event in events:
        if event.type == pygame.QUIT:
          return event
        if self._buttonsActive:
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
              vc.dy -= self._speed
            if event.key == pygame.K_DOWN:
              vc.dy += self._speed
            if event.key == pygame.K_LEFT:
              vc.dx -= self._speed
            if event.key == pygame.K_RIGHT:
              vc.dx += self._speed
          if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
              vc.dy = 0 
            if event.key == pygame.K_DOWN:
              vc.dy = 0
            if event.key == pygame.K_LEFT:
              vc.dx = 0 
            if event.key == pygame.K_RIGHT:
              vc.dx = 0
            
  def activateButtons(self):
    self._buttonsActive = True
    pygame.event.get()
  def deactivateButtons(self):
    self._buttonsActive = False
    pygame.event.get()
    for entity in self._entities.values():
      vc = entity.getComponent(Velocity2D)
      vc.dx = 0
      vc.dy = 0
  def toggleButtonsActive(self):
    if self._buttonsActive:
      self.deactivateButtons()
    else:
      self.activateButtons()
      
