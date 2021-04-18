import turtle
import math

WIDTH = 800
HEIGHT = 800

#Make Window
wn = turtle.Screen()
wn.title("Pluto's Doggy Day Care")
wn.bgcolor("light blue")
wn.setup(WIDTH, HEIGHT)
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()


    
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
        self.water_meter = 100
        self.love_meter = 100
        self.cleanliness_meter = 100
        self.exercise_meter = 100 
        self.width = width
        self.height = height
        
    def stay(self):
        self.x = 0
        self.y = 0
        
    def move_right(self):
        self.x += 10
        
        if self.x > WIDTH/2.0:
            self.x = -WIDTH/2.0
        
    def move_left(self):
        self.x += -10
        
        if self.x < -WIDTH/2.0:
            self.x = WIDTH/2.0
        
    def move_up(self):
        self.y += 10
        
        if self.y > HEIGHT/2.0:
            self.y = -HEIGHT/2.0
            
    def move_down(self):
        self.y += -10
        
        if self.y < -HEIGHT/2.0:
            self.y = HEIGHT/2.0
            
    def get_average(self):
        total = float(self.food_meter + self.water_meter + self.love_meter + self.cleanliness_meter + self.exercise_meter)
        average = total/5
        return(average)
        
    def tick(self):
        self.food_meter -= 0.3
        self.water_meter -= 0.4
        self.love_meter -= 0.2
        self.cleanliness_meter -= 0.1
        self.exercise_meter -= 0.2
        
        print(f"Pluto: Food: {self.food_meter} Water: {self.water_meter} Love: {self.love_meter}")
        print(f"Cleanliness: {self.cleanliness_meter} Exercise: {self.exercise_meter}")
        
class Water(Sprite):
    def __init__(self, x, y, shape, color,width, height):
        Sprite.__init__(self, x, y, shape, color, width, height)
        
class Food(Sprite):
    def __init__(self, x, y, shape, color, width, height):
        Sprite.__init__(self, x, y, shape, color, width, height)
        self.collide = False
        
class Bone(Sprite):
    def __init__(self, x, y, shape, color, width, height):
        Sprite.__init__(self, x, y, shape, color, width, height)

    def tap_to_pet(self):
        pass
        
        
class Bath(Sprite):
    def __init__(self, x, y, shape, color, width, height):
        Sprite.__init__(self, x, y, shape, color, width, height)
        
        
        
class Ball(Sprite):
    def __init__(self, x, y, shape, color, width, height):
       Sprite.__init__(self, x, y, shape, color, width, height)
        

class Meter():
    def __init__ (self, x, y, color, length, value):
        self.x = x
        self.y = y
        self.color = color 
        self.length = length
        self.value = value
                    
    
    
        
pluto = Pluto(0, 0, "arrow", "white", 20, 20)
ball = Ball(300, -335, "circle", "light green", 20, 20)
food = Food(-310, -335, "triangle", "brown", 20, 20)
water = Water(-345, -335, "triangle", "blue", 20, 20)
bath = Bath(-345, 270, "square", "light yellow", 20, 20)
bone = Bone(275, -335, "circle", "white", 20, 20)

sprites = [pluto, ball, food, water, bath, bone]

wn.listen()
wn.onkeypress(pluto.move_left, "Left")
wn.onkeypress(pluto.move_right, "Right")
wn.onkeypress(pluto.move_up, "Up")
wn.onkeypress(pluto.move_down, "Down")


#Create Timer 
def tick():
    print("TICK")
    
    for sprite in sprites:
        sprite.tick()
    # Set timer
    wn.ontimer(tick, 1000)

tick()

while True:
    wn.update()
    pen.clear()

    #RENDER PLUTO
    if pluto:
        pluto.render(pen)
        
    for sprite in sprites:
        sprite.render(pen)
        
    # CHECK COLLISIONS
    if pluto.is_aabb_collision(food) and food.collide == False:
        print("FOOD COLLISION")
        pluto.food_meter += 2
        food.collide = True
        
        
        
    if pluto.is_aabb_collision(water):
        print("WATER COLLISION")
        
    if pluto.is_aabb_collision(ball):
        print("BALL COLLISION")
    
    if pluto.is_aabb_collision(bone):
        print("BONE COLLISION")
        
    if pluto.is_aabb_collision(bath):
        print("BATH COLLISION")
  
    

    
#Main Loop
wn.mainloop()
