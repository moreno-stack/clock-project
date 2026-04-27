import tkinter as tk
import math
import time

class AnalogClockTab:
    def __init__(self, parent):
        # Creamos el marco principal para esta pestaña
        self.frame = tk.Frame(parent)
        
        # Configuración del lienzo (Canvas)
        self.canvas_size = 400
        self.clock_canvas = tk.Canvas(self.frame, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.clock_canvas.pack(pady=20)

        # Variables para el centro y el radio
        self.center_x = self.canvas_size // 2
        self.center_y = self.canvas_size // 2
        self.clock_radius = 150

        # Etiqueta para el reloj digital
        self.digital_time_label = tk.Label(self.frame, text="", font=("Helvetica", 18, "bold"))
        self.digital_time_label.pack()

    def update_clock(self):
        # Limpiamos el lienzo para redibujar
        self.clock_canvas.delete("all")

        # Círculo exterior
        self.clock_canvas.create_oval(
            self.center_x - self.clock_radius, self.center_y - self.clock_radius,
            self.center_x + self.clock_radius, self.center_y + self.clock_radius,
            width=4, outline="#333"
        )

        # Dibujamos las 60 líneas de los minutos/segundos
        for i in range(60):
            angle = math.radians(i * 6 - 90)
            if i % 5 == 0:
                tick_length = 15
                tick_width = 3
            else:
                tick_length = 8
                tick_width = 1

            outer_x = self.center_x + self.clock_radius * math.cos(angle)
            outer_y = self.center_y + self.clock_radius * math.sin(angle)
            inner_x = self.center_x + (self.clock_radius - tick_length) * math.cos(angle)
            inner_y = self.center_y + (self.clock_radius - tick_length) * math.sin(angle)

            self.clock_canvas.create_line(inner_x, inner_y, outer_x, outer_y, width=tick_width, fill="#333")

        # Dibujamos los números del 1 al 12
        for i in range(1, 13):
            angle = math.radians(i * 30 - 90)
            num_x = self.center_x + (self.clock_radius - 35) * math.cos(angle)
            num_y = self.center_y + (self.clock_radius - 35) * math.sin(angle)
            self.clock_canvas.create_text(num_x, num_y, text=str(i), font=("Arial", 14, "bold"))

        # Obtenemos la hora del sistema
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Dibujamos las manecillas
        self.draw_hand(hours * 30 + (minutes / 2), self.clock_radius - 60, 6, "black")
        self.draw_hand(minutes * 6 + (seconds / 10), self.clock_radius - 40, 4, "blue")
        self.draw_hand(seconds * 6, self.clock_radius - 15, 2, "red")

        # Punto central
        self.clock_canvas.create_oval(
            self.center_x - 6, self.center_y - 6,
            self.center_x + 6, self.center_y + 6,
            fill="black"
        )

        # Actualizamos el texto digital
        self.digital_time_label.config(text=time.strftime('%H:%M:%S'))

    def draw_hand(self, angle_degrees, length, width, color):
        # Cálculo trigonométrico para la posición de la manecilla
        angle_radians = math.radians(angle_degrees - 90)
        end_x = self.center_x + length * math.cos(angle_radians)
        end_y = self.center_y + length * math.sin(angle_radians)
        self.clock_canvas.create_line(
            self.center_x, self.center_y, end_x, end_y,
            width=width, fill=color, capstyle=tk.ROUND
        )