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

