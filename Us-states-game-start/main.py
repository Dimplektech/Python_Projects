import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.State Game")
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)

# As we have 50_states.csv, we dont need this function now to get coordinate
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
state_data = pandas.read_csv("50_states.csv")
all_states = state_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states Correct", prompt="what's another state name?").title()
    # If answer state is one of the state from that 50 states
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_row =state_data[state_data["state"] == answer_state]
        t.goto(state_row.x.item(), state_row.y.item())
        t.write(answer_state)


screen.exitonclick()


