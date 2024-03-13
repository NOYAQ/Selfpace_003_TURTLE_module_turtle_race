""" 
calls Turtle class from turtle module
creates a new turtle.
"""
from turtle import Turtle, Screen
from random import randint
is_game_on = True
main_screen = Screen()
main_screen.setup(width = 600, height = 400)
# A pop-up window to ask the user's guess
user_guess = main_screen.textinput(title = "Maker your guess!", prompt = "Which turtle will win the race? Select a color: ").lower()
# After creating the turtle, the colors will be assigned.
turtle_color_list = ["blue", "Red", "Green", "Yellow", "Purple", "Black", "Orange"]
# All turtles x coordination pos are the same but, y coordination position
# will be assigned after created the turtles
turtle_y_coordination = [-150, -100, -50, 0, 50, 100, 150]
# After creating the turtle, store it in the list
turtle_list = []
# Creating turtles, assigning color and starting coordination.
for turtle_index in range(0,7):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color (turtle_color_list[turtle_index])
    new_turtle.goto(-260,turtle_y_coordination[turtle_index])
    turtle_list.append(new_turtle)

while is_game_on:

    for turtle in turtle_list:
        # Checking the turtle x position, if the turtle reaches the finish line
        # then compare the turtle's color and user's guess, if it is the same
        # color sends a congrats message, If not send the winner a color message
        if turtle.xcor() >= 260:
            if turtle.pencolor() == user_guess:
                print(f"Congrats, You have won!, the winner turtle is {turtle.pencolor()}")
                is_game_on = False
            else:
                print(f"Unfortunately, You have lost!, the winner turtle is {turtle.pencolor()}")
                is_game_on = False
        # random speed is assigned between 1&10 to the turtle.
        turtle.forward(randint(1, 11))

main_screen.exitonclick()
