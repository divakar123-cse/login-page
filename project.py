import tkinter as tk

# --- Calculator functions ---
def click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# --- GUI Setup ---
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

entry = tk.Entry(window, font=("Arial", 24), borderwidth=2, relief="ridge", justify='right')
entry.pack(fill="both", ipadx=8, ipady=15, pady=10, padx=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

frame = tk.Frame(window)
frame.pack()

row = 0
col = 0

for button_text in buttons:
    btn = tk.Button(frame, text=button_text, width=5, height=2, font=("Arial", 18),
                    command=lambda b=button_text: click(b))
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
