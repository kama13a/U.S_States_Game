import time
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

screen.setup(750, 510)
turtle.shape(image)

# TODO 1: In the title keep the score/50 to see and update in each true answer
# TODO 2: Move the answer to the right place in map
    # Get hold of the user's answer
    # Turn the .csv into dict make it like state is key and coordinates are key in tuple
    # Check if the answer is in the dictionary
        # Yes: Move the state to the place(key in dict) and update the number of correct answers
        # No: Update the input box and ask the state again
    # If user finishes the game, message in the center

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
x_cor = data["x"].to_list() # Turning into the list in order to get dictionary
y_cor = data["y"].to_list() # Turning into the list in order to get dictionary

my_tuple = tuple(zip(x_cor, y_cor)) # Created tuple using two lists

state_dict = dict(zip(state_list, my_tuple)) # Created a dictionary using list of States and tuple of coordinates

game_on = True
screen.tracer(0)

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()

guessed_states = []
unguessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"States {len(guessed_states)}/50", prompt="What's another state's name")

    if answer_state is None or answer_state == "Exit":
        tim.goto(0, 50)
        tim.write(f"Game Over! You got {len(guessed_states)}/50", align="center", font=("Arial", 24, "bold"))

        # TODO 3: Show all the left states in red so they can know
        for state, cor in state_dict.items():
            if state not in guessed_states:
                tim.color("red")
                tim.goto(cor[0]-10, cor[1])
                tim.write(state, font=("Arial", 8 , "normal"))
                unguessed_states.append(state)
        learn = pandas.DataFrame(unguessed_states)
        learn.to_csv('learn.csv')


        screen.update()
        break

    answer_state = answer_state.title()


    if answer_state in state_dict and answer_state not in guessed_states:
        guessed_states.append(answer_state) # excluding the found states and saving in the list
        x, y = state_dict[answer_state]
        tim.goto(x-10, y)
        tim.write(answer_state, font=("Arial", 8, "normal"))

    else:
        pass

    if len(guessed_states) == 50:
        tim.goto(0, 0)
        tim.write("Congratulations You Found all the States", align="center", font=("Arial", 24, "bold"))

    screen.update()
screen.exitonclick()

