import tkinter as tk
import platform

def on_button_click():
    label.config(state=tk.NORMAL)
    label.delete("1.0", tk.END)
    label.insert(tk.END, "Bonjour, Tkinter!\n")
    label.config(state=tk.DISABLED)

app = tk.Tk()
app.title("Ma première application")

app.configure(bg="#14131e")
global_font = ('Ubuntu')
app.option_add("*Font", global_font)

if platform.system() == "Windows":
    app.iconbitmap("icone.ico")

app.attributes('-zoomed', True)

app.minsize(width=700, height=400)

# Créer un cadre pour contenir le texte et le bouton
frame = tk.Frame(app, bg="#14131e")
frame.pack(expand=True, fill=tk.BOTH, pady=5, padx=40)

# Ajouter une zone de texte déroulante pour afficher du texte long
text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" * 1000
label = tk.Text(frame, wrap=tk.WORD, height=10, bg="#14131e", highlightthickness=0, bd=0, fg="white")
label.insert(tk.END, text)

button = tk.Button(frame, text="Cliquez-moi!", command=on_button_click, bg="#1f1c42", fg="white")
button_window = label.window_create(tk.END, window=button)

label.pack(expand=True, fill=tk.BOTH, padx=10)

app.mainloop()
