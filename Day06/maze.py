"""
The following code must be used on the web application program Reeborg's World - https://reeborg.ca and is used to solve the Maze world.
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Prevent robot from entering an infinite loop in edge case
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()