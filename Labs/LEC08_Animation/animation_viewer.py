from dataclasses import dataclass
from pathlib import Path

from pico2d import *

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
CELL_SIZE = 256
DRAW_SIZE = 560
FRAME_COUNT = 6
ASSET_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Animation:
    name: str
    row: int  # zero is the top row of the PNG
    frames: tuple[int, ...]
    fps: float

def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        grass = load_image(str(ASSET_DIR / 'grass.png'))
        character = load_image(str(ASSET_DIR / 'hero_sprite_sheet.png'))

        if (character.w, character.h) != (6 * CELL_SIZE, 4 * CELL_SIZE):
            raise ValueError('hero_sprite_sheet.png must be a 6 x 4 sheet of 256 px cells')

        for frame in range(FRAME_COUNT):
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE, CELL_SIZE, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, DRAW_SIZE, DRAW_SIZE)
            update_canvas()
            delay(0.12)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
