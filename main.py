import sys
import pygame
from pygame.locals import *
import random

from figure import *
from fruit import *
from number import *
from user_guide import *

KIND_GENRE = 2

def main():
  pygame.init()

  screen = pygame.display.set_mode((800,600))
  pygame.display.set_caption("Life Kinetic")

  flame = 0
  mode = 0
  figure = Figure(screen)
  fruit = Fruit()
  number = Number()
  user_guide = UserGuide()

  while(True):
    if flame == 0:
      # 背景色の設定（空色）
      screen.fill( (0, 0, 0) )
      # 物体の表示
      num_for_display_genre = random.randint(0, KIND_GENRE-1)
      if mode == 0:
        figure.draw(screen)
      elif mode == 1:
        fruit.draw(screen)
      else:
        number.draw(screen)
      
      # モード選択の文字入力
      user_guide.draw(screen)
      pygame.display.update()

    flame = (flame + 1) % 100
    pygame.time.wait(50)

    for event in pygame.event.get():
      # 終了処理
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == KEYDOWN:
        # 図形モード
        if event.key == K_a:
          mode = 0
        # 果物モード
        if event.key == K_s:
          mode = 1
        # 数字モード
        if event.key == K_d:
          mode = 2
        # 終了処理
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()

if __name__ == '__main__':
  main()
