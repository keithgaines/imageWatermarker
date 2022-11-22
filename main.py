import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

window = tk.Tk()
window.title("Image Watermarker")
canvas = tk.Canvas(window)
canvas.pack()
canvas.place()

upload = filedialog.askopenfilename(initialdir='/',
                                    title="Select an Image",
                                    filetypes=(('png files', '*.png'), ('jpeg files', '*.jpeg')))

img = ImageTk.PhotoImage(Image.open(upload))

h = img.height()
w = img.width()
canvas = tk.Canvas(window, width=w, height=h, highlightthickness=0)
canvas.create_image(w/2, h/2, anchor="center", image=img)
canvas.pack()

canvas.create_text(w/2, h/2, text="This is a text watermark", fill="black", font=("Times New Roman", 30))
canvas.pack()
tk.mainloop()