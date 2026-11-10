import game_framework
import title_mode
from pico2d import (
    SDL_KEYDOWN,
    SDL_QUIT,
    SDLK_ESCAPE,
    clear_canvas,
    get_events,
    get_time,
    load_image,
    update_canvas,
)


def init():
    global image, logo_start_time
    image = load_image('tuk_credit.png')
    logo_start_time = get_time()

def finish():
    global image
    image = None

def update():
    if get_time() - logo_start_time >= 2.0:
        game_framework.change_mode(title_mode)

def render():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            game_framework.quit()
            return