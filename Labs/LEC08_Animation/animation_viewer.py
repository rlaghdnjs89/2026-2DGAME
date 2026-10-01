from pico2d import *

open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('hero_sprite_sheet.png')

for frame in range(6):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 256, 768, 256, 256, 400, 300, 560, 560)
    update_canvas()
    delay(0.12)

close_canvas()
