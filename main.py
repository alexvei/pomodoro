import time
# from playsound import playsound
import tkinter as tk

def pomodoro(mini):
    """
    This function implements a Pomodoro timer.
    It takes the length of the Pomodoro session in minutes as input and
    runs a timer that counts down the minutes and seconds in the session.
    """
    minu = int(mini)
    # Convert minutes to seconds
    min_to_sec = minu * 60
    # Initialize the timer and minute counter
    timer = 1
    minuter = 0

    # Run the timer until the desired time has passed
    while timer != (min_to_sec + 1):
        print(timer, end='\r')
        thetime(timer)
        time.sleep(1)
        timer += 1
        if timer == 60:
            break
    # Reset the timer to 0
    timer = 0
    minuter += 1
    
   # Run the timer for the remaining minutes
    while minuter != minu:
        if timer == 60:
            # Reset the timer to 0
            timer = 0
            minuter += 1
        print(f'{minuter}:{timer}', end='\r')
        time.sleep(1)
        timer += 1
    # Return a message indicating that the Pomodoro session is complete
    
    return "\nPomodoro Session Complete!"


def printInput():
    setting_time = time_var.get()
    pomodoro(setting_time)
    time_set_label = tk.Label(root, text=f'Time set to: {setting_time}')
    time_set_label.grid(row=1, column=0)
    time_var.set("")

def thetime(timi):
    timi_label = tk.Label(root, text=timi)
    timi_label.grid(row=2, column=0)


# Play a sound to indicate that the session is complete
# playsound('sound.wav')


# Set the window name
root = tk.Tk()
root.title("Pomodoro")

# Sizing
root.geometry("300x300")
root.minsize(300, 300)
root.maxsize(300, 300)

# Declare time variable
time_var = tk.StringVar()

time_label = tk.Label(root, text= 'Set the time in minutes:')
time_entry = tk.Entry(root, textvariable = time_var)
sub_btn = tk.Button(root,text = 'Set the time', command = printInput)

time_label.grid(row=0, column=0)
time_entry.grid(row=0, column=1)
sub_btn.grid(row=1, column=1)

root.mainloop()
