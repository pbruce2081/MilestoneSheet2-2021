#task 1

import simplegui, random
from user305_o32FtUyCKk_0 import Vector

#initialise global variables
WIDTH = 500
HEIGHT = 500
r = 255
g = 255
b = 255
radius = random.randrange(10, 50)
x = random.randrange(-400, 400)
y = random.randrange(-400, 400)
velocity = random.randrange(-5,5)
circles =[]

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

    def addBall(self):
        global circles
        


class Movement:
    def __init__(self, circle):
        self.circle = circle

    def draw(self, canvas):
        self.update()
        self.circle.draw(canvas)

    def update(self):
        self.circle.update()

circle = Circle(Vector(x, y), Vector(velocity, velocity), radius, 'Pink')
movement = Movement(circle)

frame = simplegui.create_frame('Circles', WIDTH, HEIGHT)
frame.set_draw_handler(movement.draw)
#create timer
colorTimer = simplegui.create_timer(500, colorChanger)
# Start the frame animation and timer
frame.start()
colorTimer.start()