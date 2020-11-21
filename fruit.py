import pygame
from pygame.locals import *
import random

from load_image import *
from placement_data import *

KIND_FRUIT = 5
# FRUIT_LEFT = 200
# FRUIT_TOP = 100
# FRUIT_W = 400
# FRUIT_H = 400

class Fruit():
  images = []
  # rect = Rect(FRUIT_LEFT, FRUIT_TOP, FRUIT_W, FRUIT_H)

  def __init__(self):
    for i in range(1, KIND_FRUIT+1):
      self.images.append( load_image("fruit_%i.png"  % i ) )
      self.images[i-1] = pygame.transform.scale(self.images[i-1], (400, 400))
      # print(self.images[i-1], )
    # print(self.images)
  
  # 描画する
  def draw(self, screen, n_display):
    for rect in placement_data[n_display]:
      if rect == None:
        continue
      num_for_fruit = random.randint(0, KIND_FRUIT-1)

      self.images[num_for_fruit] = pygame.transform.scale(self.images[num_for_fruit], (rect.width, rect.height))
      screen.blit(self.images[num_for_fruit], rect)
