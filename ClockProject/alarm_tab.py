import tkinter as tk
from tkinter import messagebox
import time

class AlarmTab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)

        # Variables de estado
        self.active = False
        self.time_set = None

        # Interfaz Gráfica
        instruction = tk.Label(self.frame, text="Set alarm (HH:MM 24h format):", font=("Arial", 12))
        instruction.pack(pady=20)

        self.entry = tk.Entry(self.frame, font=("Arial", 18), justify='center', width=10)
        self.entry.pack()

        self.status_label = tk.Label(self.frame, text="No alarm set", fg="gray", font=("Arial", 12))
        self.status_label.pack(pady=20)

        self.btn_set = tk.Button(self.frame, text="Set Alarm", command=self.set_alarm)
        self.btn_set.pack()

    def set_alarm(self):
        # Validación y configuración de la alarma
        alarm_input = self.entry.get().strip()
        if len(alarm_input) == 5 and ":" in alarm_input:
            self.time_set = alarm_input
            self.active = True
            self.status_label.config(text=f"Alarm set for {self.time_set}", fg="green")
        else:
            messagebox.showwarning("Format Error", "Please use HH:MM format (e.g. 14:30)")

    def update_logic(self):
        # Verifica constantemente si la hora del sistema coincide con la alarma
        if self.active and self.time_set:
            current_time_str = time.strftime('%H:%M')
            if current_time_str == self.time_set:
                self.active = False
                self.status_label.config(text="No alarm set", fg="gray")
                self.entry.delete(0, tk.END)
                messagebox.showinfo("ALARM!", "Wake up! It's time.")