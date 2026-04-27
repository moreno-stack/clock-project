import tkinter as tk
from tkinter import ttk

# Importamos las clases desde los otros archivos
from clock_tab import AnalogClockTab
from stopwatch_tab import StopwatchTab
from timer_tab import TimerTab
from alarm_tab import AlarmTab

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Analog Clock & Tools")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        # Creamos el sistema de pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Instanciamos cada clase pasando el notebook como padre
        self.clock_app = AnalogClockTab(self.notebook)
        self.stopwatch_app = StopwatchTab(self.notebook)
        self.timer_app = TimerTab(self.notebook)
        self.alarm_app = AlarmTab(self.notebook)

        # Agregamos los 'frames' de cada clase al notebook
        self.notebook.add(self.clock_app.frame, text="Analog Clock")
        self.notebook.add(self.stopwatch_app.frame, text="Stopwatch")
        self.notebook.add(self.timer_app.frame, text="Timer")
        self.notebook.add(self.alarm_app.frame, text="Alarm")

        # Iniciamos el ciclo de actualización
        self.run_app_loop()

    def run_app_loop(self):
        # Llamamos a los métodos de actualización de cada módulo
        self.clock_app.update_clock()
        self.stopwatch_app.update_logic()
        self.timer_app.update_logic()
        self.alarm_app.update_logic()

        # Repite esta función cada 100 milisegundos
        self.root.after(100, self.run_app_loop)

# Punto de entrada de la aplicación
if __name__ == "__main__":
    app_window = tk.Tk()
    app = MainApplication(app_window)
    app_window.mainloop()