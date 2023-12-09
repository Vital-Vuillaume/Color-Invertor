import tkinter as tk
from tkinter import PhotoImage, Canvas, filedialog
from PIL import Image, ImageTk, ImageOps
import platform

system = platform.system().lower()

def on_image_click(event):
    file_path = filedialog.askopenfilename(filetypes=[("","ㅤ.pngㅤ.jpegㅤ.jpgㅤ.icoㅤ.gifㅤ.webmㅤ")], title="Select a file")
    if file_path:
        update_image(file_path)

def on_image_hover(event):
    canvas.config(cursor="hand2")
    canvas2.config(cursor="hand1")

def on_image_leave(event):
    canvas.config(cursor="")
    canvas2.config(cursor="")

def toggle_image2_visibility(event=None):
    current_width = app.winfo_width()
    if current_width >= 1720:
        canvas2.config(width=waist, height=waist)
        label_titre.config(font=(global_font, 34), state="disabled")
        canvas2.pack(side=tk.LEFT)
        app.minsize(width=970, height=900)
    else:
        canvas2.config(width=300, height=300)
        label_titre.config(font=(global_font, 16), state="disabled")
        app.minsize(width=970, height=685)

def save_transformed_image(event):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", title="Save As")
    if file_path:
        transformed_image = ImageTk.getimage(canvas2.image)
        transformed_image.save(file_path)

def update_image(file_path):
    global image2, image_button2
    image = Image.open(file_path)
    bg_color = "#e5e5cf"
    bg_image = Image.new("RGB", image.size, bg_color)
    image = image.convert("RGBA")
    bg_image.paste(image, (0, 0), image)   
    inverted_image = ImageOps.invert(bg_image)
    inverted_image = inverted_image.convert("RGBA")
    inverted_image = ImageTk.PhotoImage(inverted_image)
    canvas2.itemconfig(image_button2, image=inverted_image)
    canvas2.image = inverted_image
    canvas2.tag_bind("img2", '<Button-1>', save_transformed_image)

app = tk.Tk()
app.title("ColorInvertor")

app.configure(bg="#1a1a30")
global_font = ('Ubuntu',)
app.option_add("*Font", global_font)

if system == "windows":
    app.iconbitmap("icone.ico")

app.attributes('-zoomed', True)

app.minsize(width=970, height=685)

waist = 500

frame = tk.Frame(app, bg="#1a1a30")
frame.pack(expand=True, fill=tk.BOTH, padx=90)

canvas = Canvas(frame, bg="#1a1a30", width=300, height=320, highlightthickness=0, bd=0)
canvas.pack()
image = PhotoImage(file="image1.png")
image_button = canvas.create_image(25, 60, anchor=tk.NW, image=image, tags="img")
canvas.tag_bind("img", '<Enter>', on_image_hover)
canvas.tag_bind("img", '<Leave>', on_image_leave)
canvas.tag_bind("img", '<Button-1>', on_image_click)

frame_title_canvas2 = tk.Frame(frame, bg="#1a1a30")
frame_title_canvas2.pack()

titre = "Embrace Color Inversion: Watch your images transform with captivating contrast."
label_titre = tk.Text(frame_title_canvas2, wrap=tk.WORD, width=40, height=5, bg="#1a1a30", highlightthickness=0, bd=0, fg="white", font=(global_font, 34))
label_titre.insert(tk.END, titre)
label_titre.pack(side=tk.LEFT)

canvas2 = Canvas(frame_title_canvas2, bg="#1a1a30", width=waist, height=waist, highlightthickness=0, bd=0)
image2 = Image.open("image2.png")
image2 = ImageTk.PhotoImage(image2)
image_button2 = canvas2.create_image(0, 0, anchor=tk.NW, image=image2, tags="img2")
canvas2.tag_bind("img2", '<Enter>', on_image_hover)
canvas2.tag_bind("img2", '<Leave>', on_image_leave)

app.bind("<Configure>", toggle_image2_visibility)

app.mainloop()