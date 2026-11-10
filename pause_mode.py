import game_framework
import game_world
from pico2d import (
    SDL_KEYDOWN,
    SDL_QUIT,
    SDLK_p,
    TTF_CloseFont,
    clear_canvas,
    get_events,
    load_font,
    update_canvas,
)


title_font = None
instruction_font = None


def init():
    global title_font, instruction_font
    font_path = r'C:\Windows\Fonts\malgun.ttf'
    title_font = load_font(font_path, 48)
    instruction_font = load_font(font_path, 24)


def finish():
    global title_font, instruction_font
    if title_font is not None:
        TTF_CloseFont(title_font.font)
        title_font = None
    if instruction_font is not None:
        TTF_CloseFont(instruction_font.font)
        instruction_font = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
            return


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    title_font.draw(304, 350, '일시정지', (255, 255, 0))
    instruction_font.draw(300, 300, 'P를 눌러 계속', (255, 255, 255))
    update_canvas()
