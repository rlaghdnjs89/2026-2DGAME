from pico2d import *
import math

open_canvas(800,600)
boy=load_image('character.png')


def move_circle():
    for degree in range(360):
        theta=math.radians(degree)
        x=400+200*math.cos(theta)
        y=300+200*math.sin(theta)

        clear_canvas()
        boy.draw(x,y)
        update_canvas()
        

def move_rectangle():
      pass
def move_triangle():
      pass
 
while True:
      move_circle()
      move_rectangle()
      move_triangle()