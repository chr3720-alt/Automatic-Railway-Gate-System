import tkinter as tk

class RailwayGateSystem:

    def __init__(self, root):

        self.root = root
        self.root.title("Automatic Railway Gate System")
        self.root.geometry("600x400")

        self.gate_status = "OPEN"
        self.train_status = "NOT DETECTED"

        title = tk.Label(root, text="Automatic Railway Gate System", font=("Arial",18))
        title.pack(pady=15)

        self.train_label = tk.Label(root, text="Train Status: NOT DETECTED", font=("Arial",14))
        self.train_label.pack(pady=10)

        self.gate_label = tk.Label(root, text="Gate Status: OPEN", font=("Arial",14))
        self.gate_label.pack(pady=10)

        self.status_label = tk.Label(root, text="System Ready", font=("Arial",14))
        self.status_label.pack(pady=20)

        self.button = tk.Button(root, text="Simulate Train Arrival", command=self.train_detected, width=25)
        self.button.pack(pady=20)


    def train_detected(self):

        self.train_status = "APPROACHING"
        self.train_label.config(text="Train Status: APPROACHING")
        self.status_label.config(text="Train Detected! Closing Gate...")

        self.root.after(2000, self.close_gate)


    def close_gate(self):

        self.gate_status = "CLOSED"
        self.gate_label.config(text="Gate Status: CLOSED")
        self.status_label.config(text="Train Passing...")

        self.root.after(4000, self.open_gate)


    def open_gate(self):

        self.gate_status = "OPEN"
        self.train_status = "PASSED"

        self.gate_label.config(text="Gate Status: OPEN")
        self.train_label.config(text="Train Status: PASSED")
        self.status_label.config(text="Crossing Safe")


root = tk.Tk()
app = RailwayGateSystem(root)
root.mainloop()