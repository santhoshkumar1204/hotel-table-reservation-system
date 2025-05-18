# coding: utf8
import tkinter as tk
from tkinter import scrolledtext

# Create the main window
root = tk.Tk()
root.title("Hotel About Content")

# Set the size of the window
root.geometry("700x400")

# Create a Label widget as a title
label = tk.Label(root, text="About Our Hotel")
label.pack(pady=10)

# Create a ScrolledText widget for the about content
about_content_box = scrolledtext.ScrolledText(root, height=30,width=100,bg='lightgrey')
about_content_box.pack(pady=10)

# Predefined about content for the hotel
predefined_about_content = """\
Step into the world of **Hotel Royal Embassy**, a 3-star sanctuary where comfort meets elegance,
right on the vibrant Perundurai Road in Erode. Our hotel is a testament to the city's spirit,
offering guests a harmonious blend of traditional hospitality and contemporary luxury.

**Rooms & Accommodation**
At Hotel Royal Embassy,each room is a private oasis of tranquility.Designed with a touch
of class and equipped with modern amenities, our rooms provide the perfect setting for
relaxation after a day of exploration or business. With plush bedding, complimentary
Wi-Fi, and round-the-clock room service, your stay is guaranteed to be as comfortable
as it is memorable.

**Culinary Experience**
Dining at Hotel Royal Embassy is a journey through the flavors of the region and
beyond. Our chefs take pride in preparing dishes that not only tantalize your taste buds
but also nourish your soul. From local delicacies to international cuisine, our menu is
curated to cater to every palate. Enjoy a sumptuous meal in our elegant dining area or
order in and savor the tastes in the comfort of your room.

**Unmatched Services**
As a 3-star establishment, we are committed to providing exceptional service that exceeds
expectations. Our dedicated staff is at your service to ensure your experience is seamless,
from check-in to departure. Whether you need assistance with travel arrangements or
recommendations for local attractions, we are here to make your stay as enjoyable as possible.

At **Hotel Royal Embassy**, we don't just offer a place to sleep; we offer an experience
that captures the essence of Erode's warmth and charm. We invite you to be our guest and
discover the comfort, cuisine, and culture that make our hotel truly royal.

**Royal Embassy Hotel devaraj PVT. LTD**
Perundurai Road, Erode
"""

# Insert the predefined about content into the ScrolledText widget
about_content_box.insert(tk.INSERT, predefined_about_content)

# Disable editing of the content box to make it read-only
about_content_box.config(state=tk.DISABLED)

# Run the main loop
root.resizable(False, False)
root.mainloop()
