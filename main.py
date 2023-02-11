import time
from playsound import playsound


def pomodoro(minu):
    """
    This function implements a Pomodoro timer.
    It takes the length of the Pomodoro session in minutes as input and
    runs a timer that counts down the minutes and seconds in the session.
    """
    # Convert minutes to seconds
    min_to_sec = minu * 60
    # Initialize the timer and minute counter
    timer = 1
    minuter = 0
    # Run the timer until the desired time has passed
    while timer != (min_to_sec + 1):
        print(timer, end='\r')
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


# Get the length of the Pomodoro session in minutes
minutes = int(input("Enter the session time: "))

# Run the Pomodoro function
pomodoro(minutes)

# Play a sound to indicate that the session is complete
playsound('sound.wav')

# Wait for the user to press enter before closing the program
input("Press enter to exit")
exit()
