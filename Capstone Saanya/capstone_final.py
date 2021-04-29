import turtle
import math
import time
import os

WIDTH = 800
HEIGHT = 800

#Make Window
wn = turtle.Screen()
wn.title("Pluto's Doggy Day Care")
wn.bgcolor("light blue")
wn.setup(WIDTH, HEIGHT)
wn.tracer(0)
wn.bgpic("splash_screen.gif")
wn.update()
time.sleep(6)
wn.bgpic("background.gif")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

#TEXT
title = turtle.Turtle()
title.color("white")
title.speed(0)
title.penup()
title.goto(0, 340)
title.hideturtle()
title.write("Pluto's Doggy Day Care Day", move=False, align = "center", font=("Impact", 32,))

food_title = turtle.Turtle()
food_title.color("white")
food_title.speed(0)
food_title.penup()
food_title.goto(200, 260)
food_title.hideturtle()
food_title.write("Hunger:", move=False, align = "center", font=("Impact", 17,))

water_title = turtle.Turtle()
water_title.color("white")
water_title.speed(0)
water_title.penup()
water_title.goto(200, 290)
water_title.hideturtle()
water_title.write("Thirst:", move=False, align = "center", font=("Impact", 17,))

love_title = turtle.Turtle()
love_title.color("white")
love_title.speed(0)
love_title.penup()
love_title.goto(200, 230)
love_title.hideturtle()
love_title.write("Love:", move=False, align = "center", font=("Impact", 17,))

cleanliness_title = turtle.Turtle()
cleanliness_title.color("white")
cleanliness_title.speed(0)
cleanliness_title.penup()
cleanliness_title.goto(190, 200)
cleanliness_title.hideturtle()
cleanliness_title.write("Cleanliness:", move=False, align = "center", font=("Impact", 17,))

exercise_title = turtle.Turtle()
exercise_title.color("white")
exercise_title.speed(0)
exercise_title.penup()
exercise_title.goto(200, 170)
exercise_title.hideturtle()
exercise_title.write("Exercise:", move=False, align = "center", font=("Impact", 17,))

#TIME LIMIT
time_limit = 60
start_time = time.time()

time_title = turtle.Turtle()
time_title.color("white")
time_title.speed(0)
time_title.penup()
time_title.goto(-300, 350)
time_title.hideturtle()



titles = [title, love_title, food_title, water_title, exercise_title, cleanliness_title]
#REGISTER SHAPE
shapes = ["left_walking.gif","sponge_pluto.gif","splash_screen.gif", "pluto.gif", "food_bowl.gif", "water_bowl.gif", "walking_pluto.gif", "dog_bone.gif", "ball.gif", "sponge.gif", "balloon_pluto.gif", "background.gif", "mickey_mouse.gif", "speech_bubble.gif"]
for shape in shapes:
    wn.register_shape(shape)
    


#Sprite (PARENT CLASS)
class Sprite():
    def __init__(self, x, y, shape, color, width, height):
        self.direction = 90
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.width = width
        self.height = height
    
    
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.showturtle()
        pen.setheading(self.direction)
        pen.stamp()
        pen.hideturtle
        
    def is_aabb_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)
        
    def tick(self):
        pass
    
#Create Pluto
class Pluto(Sprite):
    def __init__(self, x, y, shape, color, width, height):
        Sprite.__init__(self, x, y, shape, color, width, height)
        self.food_meter = 100
        self.food_collision = False
        self.water_meter = 100
        self.water_collision = False
        self.love_meter = 100
        self.love_collision = False
        self.cleanliness_meter = 100
        self.cleanliness_collision = False
        self.exercise_meter = 100 
        self.exercise_collision = False
        self.width = width
        self.height = height
        
    def check_max(self):
        if self.food_meter > 100:
            self.food_meter = 100
        if self.water_meter > 100:
            self.water_meter = 100
        if self.love_meter > 100:
            self.love_meter = 100
        if self.cleanliness_meter > 100:
            self.cleanliness_meter = 100
        if self.exercise_meter > 100:
            self.exercise_meter = 100 
        
        
    def reset_food_collision(self):
        self.food_collision = False
        
    def reset_water_collision(self):
        self.water_collision = False
        
    def reset_love_collision(self):
        self.love_collision = False
        
    def reset_cleanliness_collision(self):
        self.cleanliness_collision = False
        
    def reset_exercise_collision(self):
        self.exercise_collision = False
        
    def stay(self):
        self.x = 0
        self.y = 0
        
    def move_right(self):
        self.x += 20
        self.shape = "walking_pluto.gif"
        
        if self.x > WIDTH/2.0:
            self.x = -WIDTH/2.0
        
    def move_left(self):
        self.x += -20
        #self.shape = "walking_pluto.gif"
        self.shape = "left_walking.gif"
        
        if self.x < -WIDTH/2.0:
            self.x = WIDTH/2.0
        
    def move_up(self):
        self.y += 20
        self.shape = "walking_pluto.gif"
        
        if self.y > HEIGHT/2.0:
            self.y = -HEIGHT/2.0
            
    def move_down(self):
        self.y += -20
        self.shape = "left_walking.gif"
        
        if self.y < -HEIGHT/2.0:
            self.y = HEIGHT/2.0
            
    def pet(self, x, y):
        self.love_meter += 3
        self.shape = "balloon_pluto.gif"
        if self.love_meter >= 100:
            self.love_meter = 100
            
    def get_average(self):
        total = float(self.food_meter + self.water_meter + self.love_meter + self.cleanliness_meter + self.exercise_meter)
        average = total/5
        return(average)
        
    def tick(self):
        self.food_meter -= 0.6
        self.water_meter -= 0.65
        self.love_meter -= 0.7
        self.cleanliness_meter -= 0.7
        self.exercise_meter -= 0.6
        
        
class Water(Sprite):
    def __init__(self, x, y, shape, color,width, height):
        Sprite.__init__(self, x, y, shape, color, width, height)
        self.collide = False
        
class Food(Sprite):
    def __init__(self, x, y, shape, color, width, height):
        Sprite.__init__(self, x, y, shape, color, width, height)
        self.collide = False
        
class Bone(Sprite):
    def __init__(self, x, y, shape, color, width, height):
        Sprite.__init__(self, x, y, shape, color, width, height)
        self.collide = False
        
class Bath(Sprite):
    def __init__(self, x, y, shape, color, width, height):
        Sprite.__init__(self, x, y, shape, color, width, height)
        self.collide = False
    
class Ball(Sprite):
    def __init__(self, x, y, shape, color, width, height):
       Sprite.__init__(self, x, y, shape, color, width, height)
       self.collide = False
        
class Mickey(Sprite):
    def __init__(self, x, y, shape, color, width, height):
       Sprite.__init__(self, x, y, shape, color, width, height)
    
    def pluto_pick_up(self):
        self.x = 250

class Speech(Sprite):
    def __init__(self, x, y, shape, color, width, height):
       Sprite.__init__(self, x, y, shape, color, width, height)
    
    def speech_move(self):
        self.x = 200
        self.y = 250
    
class Meter():
    def __init__ (self, x, y, color, length, value):
        self.x = x
        self.y = y
        self.color = color 
        self.length = length
        self.value = value
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.color(self.color)
        pen.pensize(20)
        pen.setheading(0)
        pen.pendown()
        pen.forward(self.length * (self.value / 100))
        pen.penup()
                    
water_meter = Meter(250, 300, "blue", 100, 100)
food_meter = Meter(250, 270, "brown", 100, 100)
love_meter = Meter(250, 240, "light pink", 100, 100)
cleanliness_meter = Meter(250, 210, "light yellow", 100, 100)
exercise_meter = Meter(250, 180, "light green", 100, 100)
        
pluto = Pluto(0, 0, "pluto.gif", "white", 82, 91)
ball = Ball(-310, 30, "ball.gif", "light pink", 90, 90)
food = Food(-180, -310, "food_bowl.gif", "brown", 70, 90)
water = Water(-315, -335, "water_bowl.gif", "blue", 20, 20)
bath = Bath(-310, 250, "sponge.gif", "light yellow", 50, 70)
bone = Bone(260, -335, "dog_bone.gif", "white", 70, 60)
mickey = Mickey(500, 100, "mickey_mouse.gif", "white", 200, 200)
speech_bubble = Speech(500, 100, "speech_bubble.gif", "white", 100, 100)

sprites = [pluto, ball, food, water, bath, bone, mickey, speech_bubble]

wn.listen()
wn.onkeypress(pluto.move_left, "Left")
wn.onkeypress(pluto.move_right, "Right")
wn.onkeypress(pluto.move_up, "Up")
wn.onkeypress(pluto.move_down, "Down")
wn.onclick(pluto.pet, 1)

#Create Timer 
def tick():
    
    for sprite in sprites:
        sprite.tick()
    # Set timer
    wn.ontimer(tick, 1000)

tick()

while True:
    wn.update()
    pen.clear()
    
    water_meter.value = pluto.water_meter
    water_meter.render(pen)
    
    food_meter.value = pluto.food_meter
    food_meter.render(pen)
    
    love_meter.value = pluto.love_meter
    love_meter.render(pen)

    cleanliness_meter.value = pluto.cleanliness_meter
    cleanliness_meter.render(pen)
    
    exercise_meter.value = pluto.exercise_meter
    exercise_meter.render(pen)

    #RENDER PLUTO

    for sprite in sprites:
        sprite.render(pen)
        
    # CHECK COLLISIONS
    if pluto.is_aabb_collision(food) and pluto.food_collision == False and pluto.food_meter < 100:
        #print("FOOD COLLISION")
        pluto.food_meter += 4
        pluto.food_collision = True
        wn.ontimer(pluto.reset_food_collision, 6000)
        pluto.check_max()
        
    if pluto.is_aabb_collision(water) and pluto.water_collision == False and pluto.water_meter < 100:
        #print("WATER COLLISION")
        pluto.water_meter += 3
        pluto.water_collision = True
        wn.ontimer(pluto.reset_water_collision, 6000)
        pluto.check_max()
        
    if pluto.is_aabb_collision(ball) and pluto.exercise_collision == False and pluto.exercise_meter < 100:
        #print("BALL COLLISION")
        pluto.exercise_meter += 2.75
        os.system("afplay ball_sound.mp3&")
        pluto.exercise_collision = True
        wn.ontimer(pluto.reset_exercise_collision, 6000)
        pluto.check_max()
    
    if pluto.is_aabb_collision(bone) and pluto.love_collision == False and pluto.love_meter < 100:
        #print("BONE COLLISION")
        pluto.love_meter += 3
        pluto.love_collision = True
        wn.ontimer(pluto.reset_love_collision, 6000)
        pluto.check_max()
        
    if pluto.is_aabb_collision(bath) and pluto.cleanliness_collision == False and pluto.cleanliness_meter < 100:
        pluto.cleanliness_meter += 3
        pluto.cleanliness_collision = True
        wn.ontimer(pluto.reset_cleanliness_collision, 6000)
        pluto.check_max()
  
    if (pluto.food_meter <= 0) or (pluto.water_meter <= 0) or (pluto.love_meter <= 0) or (pluto.cleanliness_meter <= 0) or (pluto.exercise_meter <= 0):
        exit()
    
    
    #TIMER
    elapsed_time = time.time() - start_time
    #print(time_limit - int(elapsed_time))
    time_left = (time_limit - int(elapsed_time))
    time_title.clear()
    time_title.write(f"Time left (seconds):{time_left}", move=False, align = "center", font=("Impact", 17,))
    if elapsed_time > time_limit:
        mickey.pluto_pick_up()
        speech_bubble.speech_move()
        os.system("afplay yay.mp3&")
        pen.clear()
        for sprite in sprites:
            sprite.render(pen)
        for title in titles:
            title.clear()
        wn.update()
        time.sleep(5)
        exit()
    
    
#Main Loop
wn.mainloop()
