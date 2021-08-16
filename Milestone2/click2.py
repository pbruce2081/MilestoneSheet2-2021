import simplegui
import math

# intialize globals
WIDTH = 450
HEIGHT = 300
ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0,0]
i = 0

BALL_RADIUS = 30
BALL_RADIUS_2 = BALL_RADIUS
ball_color = "Red"
pos_history = None

class Ball:
    def __init__(self, ball_pos, BALL_RADIUS, vel):
        self.ball_pos = ball_pos
        self.BALL_RADIUS = BALL_RADIUS 
        self.vel = vel
        
    def draw(self, canvas):
        canvas.draw_circle(self.ball_pos, self.BALL_RADIUS, 1, "Black", ball_color)
        
    def update(self, vel): 
        
        self.ball_pos[0] += vel[0]
        self.ball_pos[1] += vel[1]  
                  
class Mouse:
    def __init__(self, pos_history):
        self.pos_history = pos_history
        
    def click(self, pos):
        global BALL_RADIUS, BALL_RADIUS_2
        BALL_RADIUS = BALL_RADIUS_2
        self.pos_history = list(pos)
        
    def click_pos(self):
        if self.pos_history != None:
            return self.pos_history
        else:
            return None
        self.pos_history = None

class Interaction:
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2
        
    def draw(self,canvas):
        global vel, BALL_RADIUS, i
        if self.obj2.click_pos() != None:
            dist = self.distance(self.obj2.click_pos(), self.obj1.ball_pos)
            
            if dist > BALL_RADIUS:
                vel = [0,0]
                i = 0
                self.update()
                print(dist)
                BALL_RADIUS = BALL_RADIUS_2
            if 0 < dist < BALL_RADIUS:
                if i == 0:
                    vel[0] = self.obj2.pos_history[0] - self.obj1.ball_pos[0]
                    vel[1] = self.obj2.pos_history[1] - self.obj1.ball_pos[1]
                    i = 1  
                BALL_RADIUS = 999999
                
            self.obj1.update(vel)
        self.obj1.draw(canvas)
               
    def distance(self, pt1, pt2):
        return math.sqrt( (pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
    
    def update(self):
        self.obj1.ball_pos = self.obj2.click_pos()
    
obj1 = Ball(ball_pos, BALL_RADIUS, vel) 
obj2 = Mouse(pos_history)                        
obj3 = Interaction(obj1, obj2)

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(obj2.click)
frame.set_draw_handler(obj3.draw)

# start frame
frame.start()