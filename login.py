import tkinter
import update_exel
from login_backend import *
import tkinter.messagebox
from subprocess import call
from pathlib import Path
from login_backend import *
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"login_assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def about():
    call(["python", "about_us.py"])


def contact_():
    call(["python", "contact.py"])


def sign_up():
    window.destroy()
    call(["python", "signup.py"])


def log_in():
    user_name = entry_1.get()
    password = entry_2.get()
    if len(user_name) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo("Welcome to Royal Embassy.", "Invalid Username Or Password")
    else:
        login_class = PersistentHashTable()
        status = login_class.login(user_name, password)
        if status == "successfully":
            window.destroy()
            call(["python", "reservation.py"])
        elif status == "invalid":
            tkinter.messagebox.showinfo("Welcome to Royal Embassy.", "Invalid Username Or Password")


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
    416.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    918.5,
    258.0,
    image=entry_image_1
)
entry_1 = Entry(
    font=20,
    bd=0,
    bg="#E0E0E0",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=716.0,
    y=319.0,
    width=400.0,
    height=40.0
)

canvas.create_rectangle(
    640.0,
    311.0,
    1186.0,
    368.0,
    fill="#E0E0E0",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    687.0,
    339.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: sign_up(),
    relief="flat"
)
button_1.place(
    x=766.0,
    y=628.0,
    width=293.0,
    height=26.0
)

canvas.create_rectangle(
    640.0,
    418.0,
    1186.0,
    475.0,
    fill="#E0E0E0",
    outline="")

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    687.0,
    445.0,
    image=image_image_3
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    719.5,
    289.0,
    image=entry_image_2
)
entry_2 = Entry(
    font=20,
    show="*",
    bd=0,
    bg="#E0E0E0",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=716.0,
    y=426.0,
    width=400.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: log_in(),
    relief="flat"
)
button_2.place(
    x=771.0,
    y=559.0,
    width=288.0,
    height=57.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    718.0,
    393.0,
    image=entry_image_3
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: about(),
    relief="flat"
)
button_4.place(
    x=1002.0,
    y=31.0,
    width=85.0,
    height=42.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: contact_(),
    relief="flat"
)
button_5.place(
    x=1125.0,
    y=31.0,
    width=121.0,
    height=42.0
)

window.resizable(False, False)
window.mainloop()
