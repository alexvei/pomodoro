import time


def pomodoro(a):
    for n in range(a):
        print(n)
        time.sleep(1)
        if n == a  :
            break
    return "Pomodoro Session Complete!"


a = int(input("Enter the session time: "))
print(pomodoro(a))
input("Press enter to exit")
