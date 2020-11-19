import pygame
from pygame.locals import *
import random

KIND_FIGURE = 3
KIND_COLOR = 3
FIGURE_LEFT = 200
FIGURE_TOP = 100
FIGURE_W = 400
FIGURE_H = 400

class Figure():

  def __init__(self, screen):
    self.surface = pygame.Surface(screen.get_size(), pygame.HWACCEL)
  
  # 図形を描画する
  def draw(self, screen):
    self.surface.fill( (0, 0, 0) )

    num_for_color = random.randint(0, KIND_COLOR-1)
    num_for_figure = random.randint(0, KIND_FIGURE-1)
    if num_for_color == 0:
      rect_color = (255,0,0)
    elif num_for_color == 1: 
      rect_color = (0,255,0)
    else:
      rect_color = (0,0,255)
    
    if num_for_figure == 0:
      pos = (FIGURE_W / 2, FIGURE_H / 2)
      radius = FIGURE_W / 2
      pygame.draw.circle(self.surface, rect_color, pos, radius)
    elif num_for_figure == 1:
      pygame.draw.polygon(self.surface, rect_color, [ [FIGURE_W/2, int(FIGURE_H-FIGURE_W*(1.73/2))], [0, FIGURE_H], [FIGURE_W, FIGURE_H] ])
    else:
      rect = Rect(0, 0, FIGURE_W, FIGURE_H)
      pygame.draw.rect(self.surface, rect_color, rect)
    
    screen.blit(self.surface, (FIGURE_LEFT, FIGURE_TOP))


  