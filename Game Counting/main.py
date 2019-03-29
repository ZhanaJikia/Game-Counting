import pygame
from tkinter import *
import random
time = 0
score = 0

def generate_example():
    num = random.randint(2,4)
    example = ""
    valid = False
    while not valid:
        example = ""
        for i in range(num - 1):
            example += str(random.randint(0,10))
            example += random.choice(["+","-","/","*"])
        example += str(random.randint(0, 10))
        try:
            solved = eval(example)
            if isinstance(solved, int):
                valid = True
        except:
            pass
    return example


def add_digit(i):
    if i != "-" and len(answer_label['text']) < 30 or answer_label['text'] == "":
        answer_label['text'] = answer_label['text'] + i

def delete_digit():
    answer_label['text'] = answer_label['text'][: -1]

def skip_example():
    global score
    score = score - 1
    example_label['text'] = generate_example()
    answer_label['text'] = ""
    score_label['text'] = "Score :" + str(score)

def check_answer():
    global score
    if answer_label['text'] != "":
        if eval(example_label['text']) == int(answer_label['text']):
            print(1)
            answer_label['text'] = ""
            example_label['text'] = generate_example()
            score = score + 1
            score_label['text'] = " Score :" + str(score)

def start_level():
    global time
    global score
    show()
    time = 30
    score = 0
    score_label['text'] = "Score :" + str(score)
    time_label['text'] = "Time :" + str(time)
    answer_label['text'] = ""
    example_label['text'] = generate_example()
    update_display()

def hide():
    example_label.grid_remove()
    answer_label.grid_remove()
    for button in buttons:
        button.grid_remove()
    delete_button.grid_remove()
    skip_button.grid_remove()
    enter_button.grid_remove()
    score_label.grid_remove()
    time_label.grid_remove()
    window['bg'] = "yellow"
    start_button.place(x = 80, y = 350)
    result_label.place(x = 0,y = 150)
    result_label['text'] = "Your Score is :  " + str(score)

def show():
    example_label.grid()
    answer_label.grid()
    for button in buttons:
        button.grid()
    delete_button.grid()
    skip_button.grid()
    enter_button.grid()
    score_label.grid()
    time_label.grid()
    window['bg'] = "yellow"
    start_button.place_forget()
    result_label.place_forget()

def update_display():
    global time
    if time == -1:
        hide()
    else:
        time_label['text'] = "Time :" + str(time)
        time = time - 1
        window.after(1000, update_display)

def keys_control(event):
    if event.char.isdigit() or event.char == "-":
        add_digit(event.char) #event metyvis romels vacher



window = Tk()
window.title("Funny-Count Game")
window.resizable(width = False, height = False)
window.geometry("456x650")



buttons = ["1", "2", "3",
           "4", "5", "6",
           "7","8", "9",
           "0", "-"]

example_label = Label(window, height = 3, bg = "yellow",font = "Areal 20", text = generate_example())
example_label.grid(columnspan = 4, row = 1, sticky = "ew")

answer_label = Label(window, height = 3, bg = "yellow", font = "Areal 20")
answer_label.grid(columnspan = 4, row = 6, sticky = "ew")



current_column = 0
current_row = 2
for i in range(len(buttons)):
    buttons[i] = Button(window, width =10, height = 5, bg = "green", text = buttons[i], font = "Areal 10",
                        command = lambda x = buttons[i] : add_digit(x))
    buttons[i].grid(column = current_column, row = current_row)
    current_column = current_column + 1
    if current_column > 2:
        current_column = 0
        current_row = current_row + 1

delete_button = Button(window, bg="green",font = "Areal 10", text = "Delete", command = delete_digit)
delete_button.grid(column=2, row=5, sticky="ewsn")

enter_button = Button(window, width = 22, bg = "green", font = "Areal 10", text = "Enter", command = check_answer)
enter_button.grid(column = 3, row = 2, rowspan = 3, sticky = "ns")

skip_button = Button(window, bg = "green", text = "Skip", font = "Areal 10", command = skip_example)
skip_button.grid(row = 5, column = 3, sticky = "ewns")

start_button = Button(window, bg = "green", text = "Start", height = 3, width = 25, font = "Areal 15",
                      command = start_level)
time_label = Label(window, height = 3, bg = "yellow", font = "Areal 15")
time_label.grid(column = 0, columnspan=2, row = 0, sticky="ew")

score_label = Label(window, height = 3, bg = "yellow", font = "Areal 15")
score_label.grid(row = 0, column = 3, sticky = "ew")

result_label = Label(window, height = 5, width = 42, bg = "yellow", font = "Areal 15")

hide()
result_label.place_forget()

window.bind("<Return>", lambda event: check_answer())  #for keyboard
window.bind("<BackSpace>", lambda event: delete_digit())
window.bind("<space>", lambda event: skip_example())
window.bind("<Key>", keys_control)


window.mainloop()