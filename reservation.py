from pathlib import Path
from subprocess import call
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"reservation_assets\frame0")

def about():
    call(["python", "about_us.py"])
def contact_():
    call(["python", "contact.py"])

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def input_page():
    window.destroy()
    call(["python", "input.py"])

def cancel():
    window.destroy()
    call(["python", "cancellation.py"])
window = Tk()

window.geometry("1280x832")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=832,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    52.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: about(),
    relief="flat"
)
button_1.place(
    x=936.0,
    y=31.0,
    width=85.0,
    height=42.0
)



button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: contact_(),
    relief="flat"
)
button_3.place(
    x=1051.0,
    y=31.0,
    width=121.0,
    height=42.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    640.0,
    468.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    601.0,
    409.0,
    image=image_image_3
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: input_page(),
    relief="flat"
)
button_4.place(
    x=430.0,
    y=370.0,
    width=363.0,
    height=47.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: cancel(),
    relief="flat"
)
button_5.place(
    x=430.0,
    y=445.0,
    width=363.0,
    height=47.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    209.5,
    52.5,
    image=entry_image_1
)

window.resizable(False, False)
window.mainloop()
