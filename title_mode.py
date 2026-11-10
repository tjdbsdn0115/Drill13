import game_framework
import play_mode
from pico2d import (
    SDL_KEYDOWN,
    SDL_QUIT,
    SDLK_ESCAPE,
    SDLK_SPACE,
    clear_canvas,
    get_events,
    load_image,
    update_canvas,
)


image = None


def init():
    global image
    image = load_image('title.png')


def finish():
    global image
    image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT or (
            event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
        ):
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)
            return


def update():
    pass


def render():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
