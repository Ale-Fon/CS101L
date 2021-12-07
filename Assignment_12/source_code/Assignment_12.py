import turtle

class Point(object):
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color
  def draw(self):
    turtle.penup()
    turtle.goto(self.x, self.y)
    turtle.pendown()
    turtle.color(self.color)
    turtle.setheading(0)
    self.draw_action()
  def draw_action(self):
    turtle.dot()

class Box(Point):
  def __init__(self, x1, y1, width, height, color):
    super().__init__(x1, y1, color)
    self.width = width
    self.height = height

  def draw_action(self):
    for turn in range(2):
      turtle.forward(self.width)
      turtle.right(90)
      turtle.forward(self.height)
      turtle.right(90)

class BoxFilled(Box):
  def __init__(x1, y1, width, height, color, fillcolor):
    super().__init__(x1, y1, color, fillcolor)
    #fillcolor = 
  def draw_action(self,fillcolor):
    self.fillcolor(fillcolor)
    self.begin_fill()
    Box.draw_action(self)
    self.end_fill()

class Circle(Point):
  def __init__(self,x1,y1,radius,color):
    super()._init__(x1,y1,color)
    self.radius = radius
  def draw_action(self):
    turtle.circle()


class CircleFilled(Circle):
  def __init__(x1, y1, radius,color,fillcolor):
    super().__init__(x1, y1, color, fillcolor)
    #fillcolor = 
  def draw_action(self,fillcolor):
    self.fillcolor(fillcolor)
    self.begin_fill()
    Box.draw_action(self)
    self.end_fill()

p = Point(-100,100, "blue")
p.draw()

b = Box(100,110,50,40, "red")
b.draw()

b1 = BoxFilled(180,150,100,50,'green','blue')
b1.draw()

c = Circle(-200,210,50,"green")
c.draw()

c1 = CircleFilled(-200,210,50,"green","red")
c1.draw()