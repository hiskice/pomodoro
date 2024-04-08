import tkinter as tk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        self.seconds = 25 * 60  # 25 minutes converted to seconds
        self.is_running = False

        self.label = tk.Label(root, text="25:00", font=("Helvetica", 48))
        self.label.pack(padx=20, pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        self.is_running = True
        self.update_timer()

    def stop_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.seconds = 25 * 60
        self.update_display()

    def update_timer(self):
        if self.is_running:
            self.seconds -= 1
            if self.seconds < 0:
                self.seconds = 0
                self.is_running = False
            self.update_display()
            self.root.after(1000, self.update_timer)

    def update_display(self):
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        self.label.config(text=f"{minutes:02d}:{seconds:02d}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()