import tkinter as tk
from tkinter import ttk
from datetime import datetime
from PIL import ImageGrab
import os
from .Curso import Curso

class InterfazGrafica:
    @staticmethod
    def crear_interfaz(cursos):
        root = tk.Tk()
        root.title("Horario de Clases")

        days = ["LUN", "MAR", "MIÉ", "JUE", "VIE", "SÁB"]
        day_map = {
            "LUNES": "LUN",
            "MARTES": "MAR",
            "MIERCOLES": "MIÉ",
            "JUEVES": "JUE",
            "VIERNES": "VIE",
            "SABADO": "SÁB"
        }
        hours = [f"{h:02}:00" for h in range(7, 22)]

        for i, day in enumerate(days):
            tk.Label(root, text=day).grid(row=0, column=i+1)

        for i, hour in enumerate(hours):
            tk.Label(root, text=hour).grid(row=i+1, column=0)

        for curso in cursos:
            for dia in curso.getDias():
                dia_abbr = day_map[dia.getDia()]
                dia_index = days.index(dia_abbr)
                start_time = dia.getHorarioInicio()
                end_time = dia.getHorarioFin()
                start_index = hours.index(start_time.strftime("%H:00"))
                end_index = hours.index(end_time.strftime("%H:00"))
                for i in range(start_index, end_index):
                    label = tk.Label(root, text=curso.getNombre(), bg="lightblue")
                    label.grid(row=i+1, column=dia_index+1, sticky="nsew")

        # Añadir botón para guardar la imagen
        save_button = tk.Button(root, text="Guardar como imagen", command=lambda: InterfazGrafica.guardar_imagen(root))
        save_button.grid(row=len(hours) + 1, column=0, columnspan=len(days) + 1)

        root.mainloop()
    
    @staticmethod
    def guardar_imagen(widget):
        # Obtener la geometría de la ventana
        widget.update_idletasks()
        x = widget.winfo_rootx() + 37
        y = widget.winfo_rooty()-1.5
        x1 = x + widget.winfo_width()+268
        y1 = y + widget.winfo_height()+60

        # Crear el directorio si no existe
        image_dir = os.path.join(os.getcwd(), 'src', 'images')
        os.makedirs(image_dir, exist_ok=True)
        
        # Ruta completa del archivo
        image_path = os.path.join(image_dir, "horario.jpg")

        # Capturar la pantalla y guardarla
        ImageGrab.grab(bbox=(x, y, x1, y1)).save(image_path)
        print(f"Imagen guardada en: {image_path}")

    @staticmethod
    def run(cursos):
        InterfazGrafica.crear_interfaz(cursos)
