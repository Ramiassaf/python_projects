from tkinter import *

window = Tk()
window.title("Mile to KM Calculator")
window.minsize(height=85, width=250)

# Entries
entry = Entry(width=10)
# Focuses on entry
entry.focus()
# Add some text to begin with
entry.insert(END, string="")
entry.grid(row=0, column=1)

def onclick():
    miles = entry.get() # Gets the text
    km = int(miles) * 1.60934
    label_3.config(text=km)# Sets the text


# Labels
label_Miles = Label(text="Miles", font=("Arial", 10, "bold"))
label_Miles.grid(row=0, column=2)
label_KM = Label(text="is equal to", font=("Arial", 10, "bold"))
label_KM.grid(row=1, column=0)

label_3 = Label(text="0", font=("Arial", 10, "bold"))
label_3.grid(row=1, column=1)

label_4 = Label(text="Km", font=("Arial", 10, "bold"))
label_4.grid(row=1, column=2)

button = Button(text="Click", command=onclick)
button.grid(row=2, column=1)

window.mainloop()
