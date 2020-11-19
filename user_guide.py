import pygame

class UserGuide():
  font = None

  def __init__(self):
    self.font = pygame.font.SysFont("Arial", 20)

  def draw(self, screen):
    # 操作概要
    text = self.font.render("[a] : display figure,  [s] : display fruit, esc : exit", True, (255, 255, 255))
    screen.blit(text, (10, 550))