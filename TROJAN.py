import tkinter as tk, random
while True:
    root=tk.Tk()
    x = random.randint(-500, 1400)
    y = random.randint(-500, 600)
    root.title("idiot")
    root.geometry("+%d+%d" % (x, y))
    root.update()
    del root
