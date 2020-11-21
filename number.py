import pygame
from pygame.locals import *
import random

from placement_data import *

KIND_NUMBER = 10
KIND_COLOR = 3
# NUMBER_LEFT = 300
# NUMBER_TOP = 100

class Number():
  font = None

  def __init__(self):
    self.font = pygame.font.SysFont("Arial", 400)
  
  # 描画する
  def draw(self, screen, n_display):
    # print(font_data[n_display])
    for font_info in font_data[n_display]:
      if font_info == None:
        continue
      # print(font_info)
      self.font = pygame.font.SysFont("Arial", font_info['size'])
      num_for_color = random.randint(0, KIND_COLOR-1)
      num_for_number = random.randint(0, KIND_NUMBER-1)
      if num_for_color == 0:
        number_color = (255,0,0)
      elif num_for_color == 1: 
        number_color = (0,255,0)
      else:
        number_color = (0,0,255)
      
      text = self.font.render("%i " % num_for_number, True, number_color)
      screen.blit(text, (font_info['left'], font_info['top']))



  