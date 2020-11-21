import pygame
from pygame.locals import *

placement_data = ( 
  (
    None
  ),(
    (Rect(200, 100, 400, 400), None)
  ),(
    (Rect(50, 150, 300, 300), Rect(450, 150, 300, 300))
  ),(
    (Rect(275, 50, 200, 200), Rect(75, 350, 200, 200), Rect(475, 350, 200, 200))
  ),
)

font_data = ( 
  (
    None
  ),(
    ({'size': 400, 'left': 300, 'top': 100}, None)
  ),(
    ({'size': 300, 'left': 100, 'top': 150}, {'size': 300, 'left': 500, 'top': 150} )
  ),(
    ({'size': 200, 'left': 350, 'top': 50}, {'size': 200, 'left': 125, 'top': 325}, {'size': 200, 'left': 525, 'top': 325} )
  )
)