'''
    绘制树
'''
import turtle

def draw_tree(node_size, node_step, pensize):
    if pensize < 1:
        pensize = 1
    turtle.pensize(pensize)
    if node_size < 20:
        turtle.pencolor('green')
    else:
        turtle.pencolor('grey')

    # 绘制树干
    turtle.forward(node_size)
    if node_size > 10:
        # 绘制右树枝
        turtle.right(20)
        draw_tree(node_size - node_step, node_step, pensize - 2)
        turtle.left(20)

        # 绘制左树枝
        turtle.left(20)
        draw_tree(node_size - node_step, node_step, pensize - 2)
        turtle.right(20)
    turtle.backward(node_size)

def main():
    size = 95
    pensize = 10
    turtle.left(90)
    turtle.penup()
    turtle.backward(250)
    turtle.pendown()
    turtle.pencolor('grey')


    draw_tree(size, 10, pensize)
    turtle.exitonclick()

if __name__ == '__main__':
    main()