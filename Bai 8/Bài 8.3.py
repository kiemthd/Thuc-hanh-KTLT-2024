print('Hoàng Thanh Kiếm MSSV 235752021610003')
import turtle
import random
colors = ["red", "green", "blue"]
painter = turtle.Turtle()
painter.pensize(2) 
painter.speed(5)   
def draw_circles():
    for i in range(12): 
        color = random.choice(colors) 
        painter.pencolor(color)        
        painter.circle(100)            
        painter.right(30)             
draw_circles()
painter.hideturtle()  # Ẩn con trỏ vẽ
turtle.done()
