import re
from tkinter import messagebox
from confirmation_mail import *


def confirmation_page(id_, dat, tim):
    from pathlib import Path
    from subprocess import call
    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label

    output_path = Path(__file__).parent
    assets_path = output_path / Path(r"confirmation_assets\frame0")

    def about():
        call(["python", "about_us.py"])

    def contact_():
        call(["python", "contact.py"])

    def confirm():
        email = entry_1.get()
        if email == "":
            messagebox.showinfo("Welcome to Royal Embassy.", "Please Enter Your Mail.")
        elif not is_valid_email(email):
            messagebox.showinfo("Welcome to Royal Embassy.", "Invalid Email Format. Please Enter a Valid Email.")
        else:
            messagebox.showinfo("Welcome to Royal Embassy.", "Successfully Booked")
            send_email(email, id_, dat, tim)
            send_email_admin(email, id_, dat, tim)
            window.destroy()
            call(["python", "reservation.py"])

    def is_valid_email(email):
        # Regular expression for validating an email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    def relative_to_assets(path: str) -> Path:
        return assets_path / Path(path)

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
        file=relative_to_assets("button_3.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: contact_(),
        relief="flat"
    )
    button_2.place(
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
        609.0,
        423.0,
        image=image_image_3
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        209.5,
        52.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        font=17,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=550.0,
        y=462.0,
        width=283.0,
        height=27.0
    )
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: confirm(),
        relief="flat"
    )
    button_4.place(
        x=419.0,
        y=528.0,
        width=363.0,
        height=47.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        709.1771117337471,
        480.883164734009,
        image=entry_image_2
    )

    label1 = Label(text=id_, font=20, bg="#FCE4B7")
    label1.place(x=572, y=340)
    label2 = Label(text=dat, font=20, bg="#FCE4B7")
    label2.place(x=529, y=377)
    label3 = Label(text=tim, font=20, bg="#FCE4B7")
    label3.place(x=537, y=417)

    window.resizable(False, False)
    window.mainloop()
