import turtle

def draw_pentagram(size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

def main():
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')
    size = 200
    while size <= 300:
        draw_pentagram(size)
        size += 20
    turtle.exitonclick()

if __name__ == '__main__':
    main()