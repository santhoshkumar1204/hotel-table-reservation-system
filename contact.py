# coding: utf8
import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Hotel About Content")
root.geometry("500x400")

label = tk.Label(root, text="Contact US")
label.pack(pady=10)

about_content_box = scrolledtext.ScrolledText(root, height=20, width=60)
about_content_box.pack(pady=10)
predefined_about_content = """\
Get in Touch with Hotel Royal Embassy

We’re here to ensure your stay is impeccable. For any
inquiries or assistance, please reach out to us:

📞 Phone: +91 123 456 7890
✉ Email: shruthidevarajan@gmail.com

Our dedicated team is available around the clock to
help you with your booking, provide local
recommendations, or answer any questions you may have.

Hotel Royal Embassy
Royal Embassy Hotel devaraj PVT. LTD
Perundurai Road, Erode
"""

about_content_box.insert(tk.INSERT, predefined_about_content)
about_content_box.config(state=tk.DISABLED)
root.resizable(False, False)
root.mainloop()
