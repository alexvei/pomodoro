import time
import tkinter as tk
import threading
from playsound import playsound
from PIL import Image, ImageTk


# Global Variables
body = tk.Tk()
minutes = tk.IntVar()
minuted = tk.IntVar()

# Tomato icon
icon = ImageTk.PhotoImage(Image.open("tomato.png"))


def window():
    """Create a graphical user interface for the Pomodoro timer."""
    # Create the window and set its properties
    body.title("Pomodoro")
    body.geometry("300x300")
    body.minsize(300, 300)
    body.maxsize(300, 300)
    body.iconphoto(True, icon)

    # Add a label asking the user to enter the session time
    label_one = tk.Label(body, text="Welcome to Pomodoro Timer!\n"
                                    "Enter your session in minutes:")
    label_one.pack()

    # Add a label to display the time entered by the user
    label_two = tk.Label(body, textvariable=minutes)
    label_two.pack()

    # Add a label to display the time remaining in the session
    label_three = tk.Label(body, textvariable=minuted)
    label_three.pack()

    # Add an entry to input the session time
    entry_one = tk.Entry(body)
    entry_one.bind("<Return>", lambda event: [minutes.set(entry_one.get()), timing()])
    entry_one.pack()

    # Create a new timer thread each time the submit button is clicked
    def start_timer():
        timer_thread = threading.Thread(target=timing)
        timer_thread.start()

    # Add a button to submit the session time entered by the user
    button_one = tk.Button(body, text=f"Sumbit", command=lambda: [minutes.set(entry_one.get()), start_timer()])
    button_one.pack()

    # Start the main event loop of the GUI
    body.mainloop()


def timing():
    """Start the Pomodoro timer and display the remaining time in the session."""
    # Declare global variables to be used in this function
    global body, minutes, minuted

    # Initialize the timer to 0
    timer = 0

    # Loop
    while timer != (minutes.get() * 60 + 1):
        # Update the remaining time label with the current timer value and update GUI
        minuted.set(timer)
        body.update_idletasks()

        # Increment the timer by 1 second and pause for 1 second
        timer += 1
        time.sleep(1)
    # When the timer reaches the end of the session time, play a sound (optional)
    playsound('sound.wav')


# Call the window function to start the Pomodoro timer GUI
window()

