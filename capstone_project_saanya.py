import turtle


WIDTH = 800
HEIGHT = 800

#Make Window
wn = turtle.Screen()
wn.title("Pluto's Doggy Day Care Day")
wn.bgcolor("light blue")
wn.setup(WIDTH, HEIGHT)
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

#Create Pluto
class Pluto():
    def __init__(self, x, y, shape, color):
        self.direction = 90
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.food_meter = 100
        self.water_meter = 100
        self.love_meter = 100
        self.cleanliness_meter = 100
        self.exercise_meter = 100 
    
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
            
    def get_average():
        total = float(self.food_meter + self.water_meter + self.love_meter + self.cleanliness_meter + self.exercise_meter)
        average = total/5
        return(average)
        
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.showturtle()
        pen.setheading(self.direction)
        pen.stamp()
        pen.hideturtle()
        
        
        
class Water():
    def __init__(self, x, y, shape, color):
        self.direction = 90
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.showturtle()
        pen.setheading(self.direction)
        pen.stamp()
        pen.hideturtle()
        
   
        
class Food():
    def __init__(self, x, y, shape, color):
        self.direction = 90
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        
    
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.showturtle()
        pen.setheading(self.direction)
        pen.stamp()
        pen.hideturtle()
        
class Bone():
    def __init__(self, x, y, shape, color):
        self.direction = 90
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.showturtle()
        pen.setheading(self.direction)
        pen.stamp()
        pen.hideturtle()
        
    def tap_to_pet(self):
        pass
        
        
class Bath():
    def __init__(self, x, y, shape, color):
        self.direction = 90
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.showturtle()
        pen.setheading(self.direction)
        pen.stamp()
        pen.hideturtle()
        
class Ball():
    def __init__(self, x, y, shape, color):
        self.direction = 90
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.showturtle()
        pen.setheading(self.direction)
        pen.stamp()
        pen.hideturtle()
        
        
        
        
pluto = Pluto(0, 0, "arrow", "white")
ball = Ball(300, -335, "circle", "light green")
food = Food(-310, -335, "triangle", "brown")
water = Water(-345, -335, "triangle", "blue")
bath = Bath(-345, 270, "square", "light yellow")
bone = Bone(275, -335, "circle", "white")

wn.listen()
wn.onkeypress(pluto.move_left, "Left")
wn.onkeypress(pluto.move_right, "Right")
wn.onkeypress(pluto.move_up, "Up")
wn.onkeypress(pluto.move_down, "Down")

while True:
    wn.update()
    pen.clear()

    
    #RENDER PLUTO
    if pluto:
        pluto.render(pen)
        
        
    ball.render(pen)
    food.render(pen)
    water.render(pen)
    bath.render(pen)
    bone.render(pen)
    

    
#Main Loop
wn.mainloop()
