import tkinter
from pathlib import Path
from booking import get_and_minus_value_in_excel
import tkinter.messagebox
from Time_slots import *
from subprocess import call
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"cancellation_assets\frame0")

path_of_exel = "schedule.xlsx"


def about():
    call(["python", "about_us.py"])


def contact_():
    call(["python", "contact.py"])


def home():
    window.destroy()
    call(["python", "reservation.py"])


def slot_pick(e):
    if time_box.get() == "AM":
        slot_box.config(values=time_slots_am)
        slot_box.current(0)
    if time_box.get() == "PM":
        slot_box.config(values=time_slots_pm)
        slot_box.current(0)


def cancel():
    booking_id = entry_1.get()
    if len(booking_id) == 0:
        tkinter.messagebox.showinfo("Welcome to GFG.", "Please Enter Valid Booking ID")
    else:
        spl = booking_id.split("_")
        sheet_name = f"{spl[0].capitalize()} {spl[1]} {spl[2].upper()}"
        dat = date_box.get()
        if dat not in dates[1:]:
            tkinter.messagebox.showinfo("Welcome to GFG.", 'Invalid Input Please Choose Correct Option')
            return
        slot_time = slot_box.get()
        if spl[2].upper() == "AM":
            status = get_and_minus_value_in_excel(path_of_exel, sheet_name, dat, slot_time)
            if status == "wrong":
                tkinter.messagebox.showinfo("Welcome to GFG.", "Please Enter Valid Booking ID")
            elif status == "success":
                tkinter.messagebox.showinfo("Welcome to GFG.", "Successfully Cancelled")
            elif status == "invalid input":
                tkinter.messagebox.showinfo("Welcome to GFG.", 'Invalid Input Please Choose Correct Option')
        elif spl[2].upper() == "PM":
            status = get_and_minus_value_in_excel(path_of_exel, sheet_name, dat, slot_time)
            if status == "wrong":
                tkinter.messagebox.showinfo("Welcome to GFG.", "No Seats Available.Please Book On Other Slot")
            elif status == "success":
                tkinter.messagebox.showinfo("Welcome to GFG.", "Successfully Cancelled")
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

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    640.0,
    468.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    209.5,
    52.5,
    image=entry_image_1
)
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: cancel(),
    relief="flat"
)
button_4.place(
    x=498.0,
    y=586.0,
    width=283.0,
    height=57.0
)
entry_1 = Entry(
    font=20,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=400.0,
    y=328.0,
    width=400.0,
    height=40.0
)

time_box = ttk.Combobox(window, values=time_format, width=5)
time_box.current(0)
time_box.place(x=960, y=490)
time_box.bind("<<ComboboxSelected>>", slot_pick)

slot_box = ttk.Combobox(window, values=[" "], width=12)
slot_box.current(0)
slot_box.place(x=837, y=490)

date_box = ttk.Combobox(window, values=dates[1:], width=10)
date_box.current(0)
date_box.place(x=930, y=417)

window.resizable(False, False)
window.mainloop()
