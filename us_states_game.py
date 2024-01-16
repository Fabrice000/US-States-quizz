import turtle
import pandas 
FONT = ("Arial",10,"normal")
screen = turtle.Screen()
image = "/home/carlos/Bureau/100 days of python/Day 25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

class Write(turtle.Turtle):
    def __init__(self,answer,position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(f"{answer}",align="center",font=FONT)

# def get_mouse(x,y):
#     print(x,y)
    
# turtle.onscreenclick(get_mouse)

# turtle.mainloop()
states_data = pandas.read_csv("/home/carlos/Bureau/100 days of python/Day 25/50_states.csv")
states_list = states_data["state"].to_list()
score = 0

guessed_states = []
is_running = True
while is_running:
    answer_state = screen.textinput(title=f"Guess the state{score}/50", prompt="What's another state's name?").title()


    if answer_state == "Exit":
        is_running = False
        states_to_learn = [state for state in states_list if state not in  guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
    if answer_state in states_list:
        state = states_data[states_data.state == answer_state]
        guessed_states.append(answer_state)
        pos_x = int(state.x)
        pos_y = int(state.y)
        pos = (pos_x,pos_y)
        Write(answer=answer_state,position=pos)
        print(guessed_states)
        score += 1
        if score == 50:
            print("Congratulations you finish the guess!")
            is_running = False
    