import turtle
import pandas as pd

# Set up the turtle screen and image
screen = turtle.Screen()  # Create a turtle screen object
screen.title("US States Game")  # Set the title of the screen
image = "blank_states_img.gif"  # Specify the image file
screen.addshape(image)  # Add the image shape to the screen
turtle.shape(image)  # Set the turtle shape to the image

# Read the data and initialize variables
data = pd.read_csv("50_states.csv")  # Read the data from the CSV file
all_states = data.state.to_list()
guessed_states = []  # Initialize an empty list to store guessed states
not_guessed = []
# Create a separate turtle object for writing state names
name_writer = turtle.Turtle()
name_writer.penup()
name_writer.hideturtle()

# Main loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50Guess the state", prompt="What's another state name")
    user_input = answer_state.title()  # Convert user input to title case
    if user_input == "Exit":
        # for state in all_states:
        #     if state not in guessed_states:
        #         not_guessed.append(state)
        # not_guessed_df = pd.DataFrame({"State": not_guessed})
        # not_guessed_df.to_csv("not_guessed.csv", index=True)
        # break
        missing_state = [state for state in all_states if state not in guessed_states]   # using list comprehension
        not_guessed_df = pd.DataFrame({"State": missing_state})
        not_guessed_df.to_csv("not_guessed.csv", index=True)
        break
    if user_input in all_states:  # Check if the user's guess is correct
        if user_input in guessed_states:  # Check if the user enter the same answer 2 times
            pass
        else:
            # If the user's guess is correct, record it and display it on the screen
            guessed_states.append(user_input)  # Add the guessed state to the list
            filtered_data = data[data.state == user_input]  # Filter the data for the guessed state
            # x_coordinate = filtered_data.x.values[0]  # Get the x coordinate of the state
            # y_coordinate = filtered_data.y.values[0]  # Get the y coordinate of the state
            name_writer.goto(int(filtered_data.x), int(filtered_data.y))
            name_writer.write(user_input, align="center", font=("Calibre", 7, "normal"))  # Write the state name



