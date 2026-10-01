from pico2d import *

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
CELL_SIZE = 256
DRAW_SIZE = 560
FRAME_COUNT = 6

def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    grass = load_image('grass.png')
    character = load_image('hero_sprite_sheet.png')

    for frame in range(FRAME_COUNT):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE, CELL_SIZE, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, DRAW_SIZE, DRAW_SIZE)
        update_canvas()
        delay(0.12)

    close_canvas()


if __name__ == '__main__':
    main()
