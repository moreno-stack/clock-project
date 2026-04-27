import tkinter as tk
import time

class StopwatchTab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)

        # Variables de estado
        self.running = False
        self.start_time = 0
        self.elapsed = 0

        # Interfaz Gráfica
        self.time_label = tk.Label(self.frame, text="00:00:00.0", font=("Helvetica", 40))
        self.time_label.pack(pady=60)

        button_frame = tk.Frame(self.frame)
        button_frame.pack()

        self.btn_start = tk.Button(button_frame, text="Start", command=self.start, width=10)
        self.btn_start.grid(row=0, column=0, padx=5)

        self.btn_stop = tk.Button(button_frame, text="Stop", command=self.stop, width=10)
        self.btn_stop.grid(row=0, column=1, padx=5)

        self.btn_reset = tk.Button(button_frame, text="Reset", command=self.reset, width=10)
        self.btn_reset.grid(row=0, column=2, padx=5)

    def start(self):
        # Inicia el cronómetro guardando el tiempo actual
        if not self.running:
            self.start_time = time.time() - self.elapsed
            self.running = True

    def stop(self):
        # Detiene el cronómetro
        if self.running:
            self.running = False

    def reset(self):
        # Reinicia los valores a cero
        self.running = False
        self.elapsed = 0
        self.time_label.config(text="00:00:00.0")

    def update_logic(self):
        # Se llama constantemente desde main.py para actualizar el texto si está corriendo
        if self.running:
            self.elapsed = time.time() - self.start_time
            minutes, seconds = divmod(self.elapsed, 60)
            hours, minutes = divmod(minutes, 60)
            decimals = int((self.elapsed % 1) * 10)
            
            time_str = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{decimals}"
            self.time_label.config(text=time_str)