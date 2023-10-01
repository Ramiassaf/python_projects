from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Generates a random password based on predefined criteria.


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]  # int these 3 list we are padding
    # we password elements

    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number  # here we are padding the password elements
    shuffle(password_list)

    password = "".join(password_list)  # joining the password
    password_entry.insert(0, password)  # inserting the password
    pyperclip.copy(password)  # copying the password


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Saves the website, email, and password to a file.
def save():
    file = open("data.txt", "a")
    website = website_entry.get()  # gets the text from the entry
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                                f" \nPassword: {password} \nIs it okay to save?")
        if is_okay:
            file.write(f"website: {website} | email: {email} | password: {password}\n")  # filling the file
            # with the data
            website_entry.delete(0, END)  # clears the entry
            # email_entry.delete(0, END)
            password_entry.delete(0, END)  # clears the entry
            file.close()
# ---------------------------- UI SETUP ------------------------------- #
# Set up the GUI for the password manager.


window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)  # creates a canvas
logo = PhotoImage(file="logo.png")  # loads the image
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# labels
label_website = Label(text="Website:", font=("Cardamon", 12))
label_website.grid(row=1, column=0)
label_email = Label(text="Email/Username:", font=("Cardamon", 12))
label_email.grid(row=2, column=0)
label_password = Label(text="Password:", font=("Cardamon", 12))
label_password.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
# Add some text to begin with
website_entry.insert(END, string="")
website_entry.focus()
# Gets text in entry
print(website_entry.get())
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(END, string="")
email_entry.insert(END, string="")
# Gets text in entry
print(email_entry.get())
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=25)
password_entry.insert(END, string="")
# Gets text in entry
print(password_entry.get())
password_entry.grid(row=3, column=1, sticky="e")  # sticky="w" moves to the right

# Buttons
generate_button = Button(text="Generate Password", command=generate_password, highlightthickness=0)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save, width=36, highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
