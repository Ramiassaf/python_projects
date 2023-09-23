from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def resert_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_tick.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN )
        label_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        label_timer.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN)
        label_timer.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global reps
    global timer
    count_min = math.floor(count / 60)  # floor rounds down to the nearest integer
    count_sec = count % 60
    if count_sec < 10:  # dynamic type
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):  # each time work cycle ends a check is made
            mark += "✔"
        label_tick.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW) # bg is the background color
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # heghtlightthickness is set to 0 in order to remove the outline
fig_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=fig_tomato)  # image is set to be in the middle of the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
fg = "lightGreen"

# Labels
label_timer = Label(text="Timer", font=("Cardamon", 40, "bold"), fg=fg)
label_timer.grid(row=0, column=1)
label_tick = Label( font=("Cardamon", 15, "bold"), fg=fg)
label_tick.grid(row=3, column=1)

# Buttons
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0, )

stop_button = Button(text="Reset", command=resert_timer, highlightthickness=0)
stop_button.grid(row=2, column=2)





window.mainloop()
