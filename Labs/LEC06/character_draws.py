from pico2d import *

open_canvas(800,600)
boy=load_image('character.png')

clear_canvas()
boy.draw(400,300)
update_canvas()
delay(1)
close_canvas()

def move_circle():
    theta=math.radians(degree)
    x=400+200*math.cos(theta)

def move_rectangle():
      pass
def move_triangle():
   pass
 
while True:
      move_circle()
      move_rectangle()
      move_triangle()