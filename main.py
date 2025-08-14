import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import os

def build_site():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("erreur", "need url")
        return
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        messagebox.showerror("erreur", f"nt work :\n{e}")
        return
    if not os.path.exists("built"):
        os.makedirs("built")
    filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
    filepath = os.path.join("built", filename)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response.text)
        messagebox.showinfo("le train de la hyyyyyyyyyype", f"here : {filepath}")
    except Exception as e:
        messagebox.showerror("eereur", f"na :\n{e}")

root = tk.Tk()
root.title("Kirby54 C'Est Finis")
root.geometry("600x400")

try:
    bg_image = Image.open("kirby54cfinis.png")
    bg_image = bg_image.resize((600, 400))
    bg_photo = ImageTk.PhotoImage(bg_image)
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
except FileNotFoundError:
    messagebox.showwarning("image", "image pas trv default backg set")
    canvas = tk.Canvas(root, width=600, height=400, bg="gray")
    canvas.pack(fill="both", expand=True)

canvas.create_text(300, 50, text="url :", font=("Arial", 14), fill="white")
url_entry = tk.Entry(root, font=("Arial", 12), width=40)
url_entry_window = canvas.create_window(300, 80, window=url_entry)
build_button = tk.Button(root, text="Build", font=("Arial", 12), command=build_site)
canvas.create_window(300, 120, window=build_button)

root.mainloop()
