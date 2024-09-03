# A text writer which erases text if you stop writing (to improve you writing)

import tkinter as tk
from tkinter import messagebox
import threading

class WritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Writing App")

        self.time_limit = 10  # Time limit in seconds
        self.remaining_time = self.time_limit

        self.timer_label = tk.Label(root, text=f"Time left: {self.remaining_time} seconds", font=("Arial", 12))
        self.timer_label.pack(pady=10)

        self.text_area = tk.Text(root, width=60, height=20, font=("Arial", 14))
        self.text_area.pack(padx=20, pady=20)

        self.text_area.bind("<Key>", self.reset_timer)
        self.text_area.bind("<FocusOut>", self.pause_timer)

        self.timer = None
        self.start_timer()

    def start_timer(self):
        self.update_timer_label()
        self.timer = threading.Timer(1, self.update_timer)
        self.timer.start()

    def reset_timer(self, event=None):
        if self.timer:
            self.timer.cancel()
        self.remaining_time = self.time_limit
        self.start_timer()

    def pause_timer(self, event=None):
        if self.timer:
            self.timer.cancel()

    def update_timer(self):
        self.remaining_time -= 1
        if self.remaining_time <= 0:
            self.erase_text()
        else:
            self.update_timer_label()
            self.start_timer()

    def update_timer_label(self):
        self.timer_label.config(text=f"Time left: {self.remaining_time} seconds")

    def erase_text(self):
        self.text_area.delete("1.0", tk.END)
        messagebox.showwarning("Warning", "You stopped typing for 10 seconds. All progress is lost!")
        self.remaining_time = self.time_limit
        self.update_timer_label()
        self.start_timer()

if __name__ == "__main__":
    root = tk.Tk()
    app = WritingApp(root)
    root.mainloop()
