import pygame

class UserGuide():
  font = None

  def __init__(self):
    self.font = pygame.font.SysFont("Arial", 20)

  def draw(self, screen):
    # 操作概要
    text = self.font.render("[a] : display figure,  [s] : display fruit, [d] : display number, [esc] : exit", True, (255, 255, 255))
    screen.blit(text, (10, 540))
    # 表示数変更
    text = self.font.render("[1] - [3] : modify the number of display", True, (255, 255, 255))
    screen.blit(text, (10, 570))