import tkinter as tk
from PIL import Image, ImageTk
import os, random
import requests

root = tk.Tk()
root.title("Image Quote Generator")

width= root.winfo_screenwidth() 
height= root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))

quoteAPI = "https://api.quotable.io/random?size=1"
imageAPI = "https://source.unsplash.com/random/1280x720"

def generate():
    rq = requests.get(quoteAPI)
    quote = rq.json()
    full_quote = "\"" + quote["content"] + "\""

    img = requests.get(imageAPI)
    file = open('image.jpg', 'wb')
    file.write(img.content)
    image = Image.open(r"image.jpg")
    image = ImageTk.PhotoImage(image)
    file.close()

    image_label = tk.Label(root, image=image)
    image_label.grid(row=0, column=0, padx=5, pady=10)
    image_label.image = image
    quote_frame.grid(row=1, column=0, padx=5, pady=5)
    label.configure(text=full_quote)
    label2.configure(text=quote["author"])

quote_frame = tk.Frame(root)
quote_frame.grid(row=1, column=0, padx=350, pady=250)

label = tk.Label(quote_frame, text="Placeholder Quote", fg="white", wraplength=900, justify="center", font=("Helvetica", 20, "bold italic"))
label.pack()

label2 = tk.Label(quote_frame, text="Placeholder Author", fg="white", wraplength=600, justify="center", font=("Roman", 18))
label2.pack()

button = tk.Button(root, text="Generate!", command=generate)
button.grid(row=0, column=1, padx=1, pady=5, sticky="nwe")

# Launches application with randomly generated image and quote
generate()

root.mainloop()