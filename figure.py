import pygame
from pygame.locals import *
import random

from placement_data import *

KIND_FIGURE = 3
KIND_COLOR = 3
# FIGURE_LEFT = 200
# FIGURE_TOP = 100
# FIGURE_W = 400
# FIGURE_H = 400

class Figure():

  def __init__(self, screen):
    self.surface = pygame.Surface(screen.get_size(), pygame.HWACCEL)
  
  # 図形を描画する
  def draw(self, screen, n_display):
    # print(placement_data[n_display])
    for rect_figure in placement_data[n_display]:
      self.surface.fill( (0, 0, 0) )
      if rect_figure == None:
        continue
      # print(rect_figure)
      num_for_color = random.randint(0, KIND_COLOR-1)
      num_for_figure = random.randint(0, KIND_FIGURE-1)
      if num_for_color == 0:
        figure_color = (255,0,0)
      elif num_for_color == 1: 
        figure_color = (0,255,0)
      else:
        figure_color = (0,0,255)
      
      if num_for_figure == 0:
        pos = (rect_figure.width / 2, rect_figure.height / 2)
        radius = rect_figure.width / 2
        pygame.draw.circle(self.surface, figure_color, pos, radius)
      elif num_for_figure == 1:
        pygame.draw.polygon(self.surface, figure_color, [ [rect_figure.width/2, int(rect_figure.height-rect_figure.width*(1.73/2))], [0, rect_figure.height], [rect_figure.width, rect_figure.height] ])
      else:
        rect = Rect(0, 0, rect_figure.width, rect_figure.height)
        pygame.draw.rect(self.surface, figure_color, rect)
      
      screen.blit(self.surface, (rect_figure.left, rect_figure.top))


  