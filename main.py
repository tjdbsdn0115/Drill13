import game_framework
from pico2d import close_canvas, open_canvas
import logo_mode


open_canvas(800, 600)
try:
    game_framework.run(logo_mode)
finally:
    close_canvas()
