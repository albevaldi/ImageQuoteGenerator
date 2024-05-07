import tkinter as tk
from PIL import Image, ImageTk
import os, random
import requests

root = tk.Tk()
root.title("Image Quote Generator")

width= root.winfo_screenwidth() 
height= root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))

url = "https://api.quotable.io/random?size=1"

height -= 300
width -= 100
def generate():

    print(height, width, "HEEERE")
    r = requests.get(url)
    quote = r.json()
    full_quote = "\"" + quote["content"] + "\"" + " " + quote["author"]

    image_path = "./Images/" + random.choice(os.listdir("./Images"))
    image = Image.open(image_path)
    image = image.resize((width, height))
    image = ImageTk.PhotoImage(image)

    image_label = tk.Label(root, image=image)
    image_label.grid(row=0, column=0, padx=5, pady=10)
    image_label.image = image
    quote_frame.grid(row=1, column=0, padx=5, pady=5)
    label.configure(text=full_quote)

quote_frame = tk.Frame(root, bg="white")
quote_frame.grid(row=1, column=0, padx=350, pady=250)

label = tk.Label(quote_frame, text="Image Quote Generator", fg="blue", bg="white", wraplength=600, justify="center", font=("Helvetica", 18, "bold"))
label.pack()

button = tk.Button(root, text="Generate!", command=generate)
button.grid(row=2, column=0, padx=5, pady=5, sticky="s")

root.mainloop()