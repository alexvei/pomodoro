import time
# from playsound import playsound
import tkinter as tk


def window():
    global body, minutes, minuted, minutes
    body = tk.Tk()
    minutes = tk.IntVar()
    minuted = tk.IntVar()
    body.title("Pomodoro")
    body.geometry("300x300")
    body.minsize(300, 300)
    body.maxsize(300, 300)
    label_one = tk.Label(body, text="Welcome to Pomodoro Timer!\n"
                                    "Enter your session in minutes:")
    label_one.pack()

    label_two = tk.Label(body, textvariable=minutes)
    label_two.pack()

    label_three = tk.Label(body, textvariable=minuted)
    label_three.pack()

    entry_one = tk.Entry(body)
    entry_one.bind("<Return>", lambda event: [minutes.set(entry_one.get()), timing()])
    entry_one.pack()

    button_one = tk.Button(body, text=f"Sumbit", command=lambda: [minutes.set(entry_one.get()), timing()])
    button_one.pack()

    body.mainloop()


def timing():
    timer = 0
    while timer != (minutes.get()*60+1):
        minuted.set(timer)
        body.update_idletasks()
        timer += 1
        time.sleep(1)


window()
