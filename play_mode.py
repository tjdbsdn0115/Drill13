import game_framework
import game_world
from boy import Boy
from grass import Grass
from pico2d import (
    SDL_KEYDOWN,
    SDL_QUIT,
    SDLK_ESCAPE,
    SDLK_p,
    clear_canvas,
    get_events,
    load_image,
    update_canvas,
)
from sdl2 import SDLK_0, SDLK_1, SDLK_2, SDLK_i


boy = None
item_select_image = None
item_selection_open = False


def handle_events():
    global item_selection_open

    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import title_mode

            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            import pause_mode

            game_framework.push_mode(pause_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            item_selection_open = not item_selection_open
            return
        elif item_selection_open:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_0:
                    item_selection_open = False
                    return
                if event.key in (SDLK_1, SDLK_2):
                    boy.fire_ball(1 if event.key == SDLK_1 else 2)
                    item_selection_open = False
                    return
            continue
        else:
            boy.handle_event(event)


def init():
    global boy, item_select_image, item_selection_open

    boy = Boy()
    game_world.add_oject(boy)
    grass = Grass()
    game_world.add_oject(grass, 0)
    item_select_image = load_image('item_select.png')
    item_selection_open = False


def pause():
    boy.pressed_keys.clear()
    if boy.state == 'RUN':
        boy.dir = 0
        boy.stop_run()


def resume():
    pass


def update():
    if not item_selection_open:
        game_world.update()

def render():
    clear_canvas()
    game_world.render()
    if item_selection_open:
        item_select_image.draw(400, 300)
    update_canvas()


def finish():
    global boy, item_select_image, item_selection_open
    game_world.clear()
    boy = None
    item_select_image = None
    item_selection_open = False
