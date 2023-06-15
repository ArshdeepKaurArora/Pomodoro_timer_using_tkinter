from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
ticks = ''
timer = None
# state = True

window = Tk()
window.title('Pomodoro Timer')
window.minsize(width=200, height=250)
window.config(padx=50, pady=50, bg=YELLOW)

# For changing the title of game.
def title_change(name, color):
    title.config(text=name, fg=color)


# to reset the timer.
def reset_timer():
    global REPS, ticks, timer
    window.after_cancel(timer)
    REPS = 0
    title_change('TiMeR',RED)
    text1.config(text='')
    canvas.itemconfig(timer_text,text='00:00')

# for adjusting timer
def time_countdown(count):
    global ticks, timer, state
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"

    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        timer = window.after(1000, time_countdown, count - 1)
    else:
        start_timer()
        if REPS % 2 != 0:
            ticks += '✔'
            text1.config(text=ticks)


# For connecting timer with start button
def start_timer():
    global REPS
    REPS += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        time_countdown(long_break)
        title_change('BrEaK TiMe', RED)
    elif REPS % 2 == 0:
        time_countdown(short_break)
        title_change('BrEak TiMe', PINK)
    elif REPS % 2 != 0:
        time_countdown(work_time)
        title_change('WoRk TiMe', GREEN)


# Adjusting timer for reps
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 111, image=image)

timer_text = canvas.create_text(101, 119, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

button1 = Button(text='START', command=start_timer)
button1.grid(row=3, column=0)

text1 = Label(bg=YELLOW, fg=GREEN, font='bold')
text1.grid(row=4, column=1)

title = Label(text='TiMeR', font=("Courier", 35, 'bold'), bg=YELLOW, fg=RED)
title.grid(row=0, column=1)

button2 = Button(text='RESET',command=reset_timer)
button2.grid(row=3, column=2)

window.mainloop()
