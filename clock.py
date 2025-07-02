import tkinter as tk
import time


def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)
    current_date = time.strftime("%A, %d %B %Y")
    date_label.config(text=current_date)



window = tk.Tk()
window.title("Digital Clock")
window.configure(bg="black")
window.geometry("600x200")



clock_label = tk.Label(window,font=("Helvetica", 110, "bold"),bg="black",fg="lavender",pady=20)
clock_label.pack(expand=True)


date_label = tk.Label(window,
                      font=("Helvetica", 24),bg="black",fg="pink")
date_label.pack(expand=True)

update_time()
window.mainloop()


