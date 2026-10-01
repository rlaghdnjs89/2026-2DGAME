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


WALK = Animation('Walk', 0, (0, 1, 2, 3, 4, 5), 8.0)
RUN = Animation('Run', 1, (0, 1, 2, 3, 4, 5), 11.0)
JUMP = Animation('Jump', 2, (0, 1, 2, 3, 4, 5), 8.0)
ATTACK = Animation('Attack', 3, (0, 1, 2, 3, 4), 10.0)
ANIMATIONS = (WALK, RUN, JUMP, ATTACK)

# Per-cell opaque bounds: left, top, right, bottom in image coordinates.
# Computed from alpha > 8; source_rect adds a two-pixel safety margin.
FRAME_BOUNDS = {
    0: (
        (35, 48, 228, 238), (31, 47, 227, 238),
        (30, 47, 228, 238), (28, 48, 227, 238),
        (33, 48, 226, 238), (33, 48, 224, 238),
    ),
    1: (
        (35, 41, 253, 227), (39, 40, 255, 227),
        (30, 42, 251, 228), (32, 38, 255, 255),
        (0, 41, 255, 228), (0, 42, 237, 228),
    ),
    2: (
        (41, 81, 239, 247), (39, 40, 245, 255),
        (33, 13, 235, 204), (23, 0, 221, 177),
        (18, 25, 243, 231), (40, 77, 236, 247),
    ),
}

def source_rect(animation: Animation, frame_index: int) -> tuple[int, int, int, int]:
    column = animation.frames[frame_index]
    return column * CELL_SIZE, (3 - animation.row) * CELL_SIZE, CELL_SIZE, CELL_SIZE


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        grass = load_image(str(ASSET_DIR / 'grass.png'))
        character = load_image(str(ASSET_DIR / 'hero_sprite_sheet.png'))

        if (character.w, character.h) != (6 * CELL_SIZE, 4 * CELL_SIZE):
            raise ValueError('hero_sprite_sheet.png must be a 6 x 4 sheet of 256 px cells')

        for animation in ANIMATIONS:
            for frame in range(len(animation.frames)):
                clear_canvas()
                grass.draw(400, 30)
                character.clip_draw(
                    *source_rect(animation, frame),
                    CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, DRAW_SIZE, DRAW_SIZE,
                )
                update_canvas()
                delay(1 / animation.fps)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
