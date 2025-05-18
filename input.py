from pathlib import Path
from subprocess import call
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"input_assets\frame0")


def about():
    call(["python", "about_us.py"])


def contact_():
    call(["python", "contact.py"])


def home():
    window.destroy()
    call(["python", "reservation.py"])


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def table_1_page():
    window.destroy()
    call(["python", "table_1.py"])


def table_2_page():
    window.destroy()
    call(["python", "table_2.py"])


def table_3_page():
    window.destroy()
    call(["python", "table_3.py"])


def table_4_page():
    window.destroy()
    call(["python", "table_4.py"])


def reservation_page():
    window.destroy()
    call(["python", "reservation.py"])


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

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: home(),
    relief="flat"
)
button_2.place(
    x=821.0,
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

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    209.5,
    52.5,
    image=entry_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    640.0,
    468.0,
    image=image_image_2
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: table_1_page(),
    relief="flat"
)
button_4.place(
    x=24.0,
    y=543.0,
    width=163.0,
    height=66.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    109.0,
    393.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1030.0,
    528.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    637.0,
    393.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    327.0,
    527.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    255.0,
    198.0,
    image=image_image_7
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: table_2_page(),
    relief="flat"
)
button_5.place(
    x=235.0,
    y=682.0,
    width=163.0,
    height=66.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: table_3_page(),
    relief="flat"
)
button_6.place(
    x=558.0,
    y=549.0,
    width=163.0,
    height=66.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: table_4_page(),
    relief="flat"
)
button_7.place(
    x=949.0,
    y=682.0,
    width=163.0,
    height=66.0
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))

back_button = Button(
    image=image_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: reservation_page(),
    relief="flat"
)
back_button.place(x=50, y=700)

window.resizable(False, False)
window.mainloop()
