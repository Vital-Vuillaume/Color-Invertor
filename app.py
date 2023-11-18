import tkinter as tk
from tkinter import PhotoImage, Canvas
import platform

def on_image_click(event):
    pass

def on_image_hover(event):
    canvas.config(cursor="hand2")
    canvas2.config(cursor="hand1")
    canvas3.config(cursor="hand1")

def on_image_leave(event):
    canvas.config(cursor="")
    canvas2.config(cursor="")
    canvas3.config(cursor="")

def toggle_image2_visibility(event=None):
    current_width = app.winfo_width()
    if current_width >= 1700:
        canvas2.pack(side=tk.LEFT)
        canvas3.pack_forget()
    else:
        canvas3.pack()
        canvas2.pack_forget()

app = tk.Tk()
app.title("Ma première application")

app.configure(bg="#1a1a30")
global_font = ('Ubuntu',)
app.option_add("*Font", global_font)

if platform.system() == "Windows":
    app.iconbitmap("icone.ico")

app.attributes('-zoomed', True)

app.minsize(width=700, height=400)

frame = tk.Frame(app, bg="#1a1a30")
frame.pack(expand=True, fill=tk.BOTH, padx=100)

canvas = Canvas(frame, bg="#1a1a30", width=300, height=320, highlightthickness=0, bd=0)
canvas.pack()
image = PhotoImage(file="image.png")
image_button = canvas.create_image(25, 60, anchor=tk.NW, image=image, tags="img")
canvas.tag_bind("img", '<Enter>', on_image_hover)
canvas.tag_bind("img", '<Leave>', on_image_leave)
canvas.tag_bind("img", '<Button-1>', on_image_click)

frame_title_canvas2 = tk.Frame(frame, bg="#1a1a30")
frame_title_canvas2.pack()

titre = "Discover the Beauty of Black and White: Your images take on a new life without color."
label_titre = tk.Text(frame_title_canvas2, wrap=tk.WORD, width=40, height=5, bg="#1a1a30", highlightthickness=0, bd=0, fg="white", font=(global_font, 36))
label_titre.insert(tk.END, titre)
label_titre.pack(side=tk.LEFT)

canvas2 = Canvas(frame_title_canvas2, bg="#1a1a30", width=350, height=350, highlightthickness=0, bd=0)
image2 = PhotoImage(file="image2.png")
image_button2 = canvas2.create_image(0, 0, anchor=tk.NW, image=image2, tags="img2")
canvas2.tag_bind("img2", '<Enter>', on_image_hover)
canvas2.tag_bind("img2", '<Leave>', on_image_leave)
canvas2.tag_bind("img2", '<Button-1>', on_image_click)

canvas3 = Canvas(frame, bg="#1a1a30", width=300, height=320, highlightthickness=0, bd=0)
image3 = PhotoImage(file="image2.png")
image3_button = canvas3.create_image(25, 60, anchor=tk.NW, image=image3, tags="img3")
canvas3.tag_bind("img3", '<Enter>', on_image_hover)
canvas3.tag_bind("img3", '<Leave>', on_image_leave)
canvas3.tag_bind("img3", '<Button-1>', on_image_click)

app.bind("<Configure>", toggle_image2_visibility)

app.mainloop()
