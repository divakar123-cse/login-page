import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

# ------------------ Database Setup ------------------
def connect_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                  (username, hash_password(password)))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

def login_user(username, password):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?",
              (username, hash_password(password)))
    result = c.fetchone()
    conn.close()
    return result is not None

# ------------------ GUI Setup ------------------
def register_window():
    def register():
        user = username_entry.get()
        pwd = password_entry.get()
        if register_user(user, pwd):
            messagebox.showinfo("Success", "Registered successfully!")
            win.destroy()
        else:
            messagebox.showerror("Error", "Username already exists.")

    win = tk.Toplevel(root)
    win.title("Register")

    tk.Label(win, text="Username").pack()
    username_entry = tk.Entry(win)
    username_entry.pack()

    tk.Label(win, text="Password").pack()
    password_entry = tk.Entry(win, show="*")
    password_entry.pack()

    tk.Button(win, text="Register", command=register).pack()

def login():
    user = username_var.get()
    pwd = password_var.get()
    if login_user(user, pwd):
        messagebox.showinfo("Success", f"Welcome, {user}!")
    else:
        messagebox.showerror("Failed", "Invalid username or password.")

# ------------------ Main Window ------------------
connect_db()

root = tk.Tk()
root.title("College Login System")

username_var = tk.StringVar()
password_var = tk.StringVar()

tk.Label(root, text="College Login", font=("Helvetica", 16)).pack(pady=10)

tk.Label(root, text="Username").pack()
tk.Entry(root, textvariable=username_var).pack()

tk.Label(root, text="Password").pack()
tk.Entry(root, textvariable=password_var, show="*").pack()

tk.Button(root, text="Login", command=login).pack(pady=5)
tk.Button(root, text="Register", command=register_window).pack()

root.mainloop()
