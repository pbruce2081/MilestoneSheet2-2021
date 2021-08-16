#task 3

import simplegui, random
from user305_o32FtUyCKk_0 import Vector

#initialise global variables
WIDTH = 500
HEIGHT = 500
r = 255
g = 255
b = 255

circles =[]
removed = []

def create_random_circle():
    x = random.randrange(-100, 100)
    y = random.randrange(-100, 100)
    vel_x = random.randrange(-5,5)
    vel_y = random.randrange(-5,5)
    radius = random.randrange(10, 50)
    
    return Circle(Vector(x, y), Vector(vel_x, vel_y), radius, 'Pink')

def add_circle():
    global circles
    circles.append(create_random_circle())
def remove_circle():
    global circles
    if Circle(radius) < 1 or Circle(Vector(x, y)) < -100 or Circle(Vector(x, y)) < 100:
        removedCircles = circles.remove(create_random_circle())
        removed.append(removedCircles)

#function that generates a random colour 
def colorChanger():
    global r,g,b
    r0 = random.randrange (0, 256)
    g0 = random.randrange (0, 256)
    b0 = random.randrange (0, 256)
    r = r0
    g = g0
    b = b0
def randCol ():
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

class Circle:
    def __init__(self, pos, vel, radius, color):
        self.pos = pos
        self.vel = vel
        self.radius = radius
        self.color = color

    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(), self.radius, 1, randCol(), randCol())

    def update(self):
        self.pos.add(self.vel)
        self.pos.add(self.vel)

class Movement:
    def __init__(self, circles):
        self.circles = circles

    def draw(self, canvas):
        self.update()
        for circle in self.circles:  
            circle.draw(canvas)

    def update(self):
        for circle in self.circles:
            circle.update()

movement = Movement(circles)

frame = simplegui.create_frame('Circles', WIDTH, HEIGHT)
frame.set_draw_handler(movement.draw)
#create timers
colorTimer = simplegui.create_timer(500, colorChanger)
addTimer = simplegui.create_timer(100, add_circle)
removeTimer = simplegui.create_timer(100, remove_circle)
# Start the frame animation and timer
frame.start()
addTimer.start()
removeTimer
colorTimer.start()