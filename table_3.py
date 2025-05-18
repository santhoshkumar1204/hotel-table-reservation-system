from subprocess import call
from pathlib import Path
from Time_slots import *
from confirmation import *
from tkinter import Tk, Canvas, Button, PhotoImage, ttk, Label
from booking import get_and_edit_value_in_excel
import tkinter.messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"table_3_assets\frame0")

path_of_exel = "schedule.xlsx"


def about():
    call(["python", "about_us.py"])


def contact_():
    call(["python", "contact.py"])


def home():
    window.destroy()
    call(["python", "reservation.py"])


def input_page():
    window.destroy()
    call(["python", "input.py"])


def print_date():
    selected_date = date_box.get()
    label = Label(text=selected_date, font=20, bg="#D9D9D9")
    label.place(x=390, y=375)


def slot_pick(e):
    if time_box.get() == "AM":
        slot_box.config(values=time_slots_am)
        slot_box.current(0)
    if time_box.get() == "PM":
        slot_box.config(values=time_slots_pm)
        slot_box.current(0)


def print_time():
    slot = slot_box.get()
    label = Label(text=slot, font=20, bg="#D9D9D9")
    label.place(x=390, y=498)


def checking():
    dat = date_box.get()
    time = time_box.get()
    slot_time = slot_box.get()
    if time == "AM":
        status = get_and_edit_value_in_excel(path_of_exel, "Table 3 AM", dat, slot_time)
        if status == "not available":
            tkinter.messagebox.showinfo("Welcome to GFG.", "No Seats Available.Please Book On Other Slot")
        elif status == "available":
            table_id = "table_2_am"
            window.destroy()
            confirmation_page(table_id, dat, slot_time)
        elif status == "invalid input":
            tkinter.messagebox.showinfo("Welcome to GFG.", 'Invalid Input Please Choose Correct Option')
    elif time == "PM":
        status = get_and_edit_value_in_excel(path_of_exel, "Table 3 PM", dat, slot_time)
        if status == "not available":
            tkinter.messagebox.showinfo("Welcome to GFG.", "No Seats Available.Please Book On Other Slot")
        elif status == "available":
            table_id = "table_2_pm"
            window.destroy()
            confirmation_page(table_id, dat, slot_time)
        elif status == "invalid input":
            tkinter.messagebox.showinfo("Welcome to GFG.", 'Invalid Input Please Choose Correct Option')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    command=lambda: [print_time(), print_date(), checking()],
    relief="flat"
)
button_4.place(
    x=59.0,
    y=512.0,
    width=163.0,
    height=66.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    255.0,
    198.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    141.0,
    389.0,
    image=image_image_4
)
image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))

back_button = Button(
    image=image_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: input_page(),
    relief="flat"
)
back_button.place(x=50, y=700)

time_box = ttk.Combobox(window, values=time_format, width=5)
time_box.current(0)
time_box.place(x=923, y=500)
time_box.bind("<<ComboboxSelected>>", slot_pick)

slot_box = ttk.Combobox(window, values=[" "], width=12)
slot_box.current(0)
slot_box.place(x=800, y=500)

date_box = ttk.Combobox(window, values=dates, width=10)
date_box.current(0)
date_box.place(x=900, y=378)

window.resizable(False, False)
window.mainloop()
