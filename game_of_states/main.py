import turtle
import pandas as pd

# initializing the screen and setting the image as a shape on the background
screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# using a Turtle instance to write on the screen the state name
timmy = turtle.Turtle()
timmy.color("black")
timmy.penup()
timmy.hideturtle()


# loading the data frame with the states and their coordinates on the screen where the name should be written
states_df = pd.read_csv('50_states.csv')

# setting up the prompt where user will answer the states
score = 0
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                    prompt=f"Enter State Name\nType 'exit' to exit the game").title()
    location_df = states_df.loc[states_df['state'] == answer_state]
    if answer_state == 'Exit':
        break
    if not location_df.empty:
        x_coor = float(location_df['x'])
        y_coor = float(location_df['y'])
        timmy.goto(x_coor, y_coor)
        timmy.write(answer_state, align='Left', font=('Arial', 10, 'normal'))
        correct_guesses.append(answer_state)
        score += 1

screen.exitonclick()


