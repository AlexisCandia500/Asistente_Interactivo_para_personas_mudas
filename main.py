import tkinter as tk
from tkinter import ttk
import pyttsx3
import cv2
from PIL import Image, ImageTk
import subprocess
import os

def boton_clicado(nombre):
    print(f"Botón {nombre} clicado")
    speak(nombre)

def speak(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def mostrar_posicion(event):
    x, y = event.x, event.y
    print(f"Posición del puntero: x={x}, y={y}")

def cerrar_programa():
    root.destroy()

def abrir_teclado():
    # Ruta completa al ejecutable del teclado en pantalla
    ruta_osk = os.path.join(os.getenv("SystemRoot"), "System32", "osk.exe")
    
    # Ejecutar el teclado en pantalla
    subprocess.run([ruta_osk])


def desplegar_botones():
    # Oculta los botones actuales
    for boton in botones:
        boton.grid_forget()

    # Muestra los nuevos botones
    for i, nombre in enumerate(nuevos_nombres):
        boton = ttk.Button(root, text=nombre, command=lambda nombre=nombre: boton_clicado(nombre), width=30, style='New.TButton')
        boton.grid(row=(i // 3) + filas, column=(i % 3), padx=5, pady=5)
        botones_nuevos.append(boton)


def mostrar_camara():
    cap = cv2.VideoCapture(0)

    def actualizar_camara():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(img)
            panel.img = img
            panel.config(image=img)
            root.after(10, actualizar_camara)

    panel = tk.Label(root)
    panel.grid(row=0, column=columnas+1, rowspan=filas+2, padx=5, pady=5)
    actualizar_camara()

# Crear ventana principal
root = tk.Tk()
root.attributes('-fullscreen', True)

filas = 2
columnas = 3

# Crear estilo para los nuevos botones
root.style = ttk.Style()

# Configurar el estilo con fondo naranja, texto negro y tamaño de fuente más grande
root.style.configure('New.TButton', font=('Helvetica', 16), background='#FFA500', foreground='black', borderwidth=5, relief='ridge', bordercolor='#FFA500', focuscolor='#FFA500')

# Crear botones iniciales
botones = []
nombres_botones = ["SALUDO", "DESPEDIDA", "RESPUESTAS", "NECESIDADES INMEDIATAS", "AYUDA", "CONFIRMACIÓN","INTERACCION CON EL ENTORNO","PREGUNTAS FRECUENTES"]

for i, nombre_boton in enumerate(nombres_botones):
    boton = ttk.Button(root, text=nombre_boton, command=lambda nombre=nombre_boton: boton_clicado(nombre), width=10, style='New.TButton')
    boton.grid(row=i // columnas, column=i % columnas, padx=5, pady=5)
    botones.append(boton)

# Divisoria entre los botones y la cámara
divisoria = ttk.Separator(root, orient='vertical')
divisoria.grid(row=0, column=columnas, rowspan=filas, sticky='ns', padx=50)


# Botón para abrir el teclado en pantalla
boton_teclado = ttk.Button(root, text="Teclado", command=abrir_teclado, width=20, style='New.TButton')
boton_teclado.grid(row=filas+2, column=columnas, padx=5, pady=5)

# Botón para desplegar nuevos botones
boton_desplegar = ttk.Button(root, text="Desplegar", command=desplegar_botones, width=10, style='New.TButton')
boton_desplegar.grid(row=filas, column=columnas, padx=5, pady=5)

# Nuevos botones ocultos inicialmente
botones_nuevos = []
nuevos_nombres = ["Nuevo_1", "Nuevo_2", "Nuevo_3", "Nuevo_4", "Nuevo_5", "Nuevo_6", "Nuevo_7", "Nuevo_8"]

# Evento para mostrar la posición del puntero
root.bind("<Motion>", mostrar_posicion)

# Botón para cerrar el programa
boton_cerrar = ttk.Button(root, text="Cerrar", command=cerrar_programa, width=10, style='New.TButton')
boton_cerrar.grid(row=filas+1, column=columnas, padx=5, pady=5)

# Mostrar vista de la cámara
mostrar_camara()

# Iniciar bucle principal
root.mainloop()
