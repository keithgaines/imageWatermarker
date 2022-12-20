import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageGrab

 

def save_as_png(canvas, file_name):
    # Save postscript image
    canvas.postscript(file=file_name + '.eps')
    # Use PIL to convert to PNG
    img = Image.open(file_name + '.eps')
    img.save(file_name + '.png', 'png')

 

# Create Tkinter window and canvas
window = tk.Tk()
window.title("Image Watermarker")
canvas = tk.Canvas(window)

 

# Prompt user to select an image file
upload = filedialog.askopenfilename(initialdir='/',
                                    title="Select an Image",
                                    filetypes=(('png files', '*.png'), ('jpeg files', '*.jpeg')))

 

# Load image and get dimensions
img = ImageTk.PhotoImage(Image.open(upload))
h = img.height()
w = img.width()

 

# Create canvas with image dimensions
canvas = tk.Canvas(window, width=w, height=h, highlightthickness=0)
canvas.create_image(w/2, h/2, anchor="center", image=img)
canvas.pack()

 

# Add watermark text to canvas
canvas.create_text(w/2, h/2, text="This is a text watermark", fill="black", font=("Times New Roman", 30))
canvas.pack()

 

# Save canvas as a PNG file
save_as_png(canvas, "watermarked_image")

 

# Start Tkinter event loop
tk.mainloop()
