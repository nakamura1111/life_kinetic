import os.path
import pygame
import sys

# exeファイル作成時の参照先を変化に対応する
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
  # file = os.path.join(main_dir, 'data', file)
  relative_path = os.path.join('data', file)
  file = resource_path(relative_path)
  try:
    surface = pygame.image.load(file)
  except pygame.error:
    raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()) )
  return surface.convert()