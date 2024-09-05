import tkinter as tk
from tkinter import ttk

class InterfazDividida:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)

              # Dividir la pantalla en tres partes
        ancho_frame = root.winfo_screenwidth() // 3

        self.frame_izquierdo = ttk.Frame(root, width=ancho_frame, height=root.winfo_screenheight(), relief='solid', borderwidth=2)
        self.frame_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH)

        self.frame_central = ttk.Frame(root, width=ancho_frame, height=root.winfo_screenheight(), relief='solid', borderwidth=2)
        self.frame_central.pack(side=tk.LEFT, fill=tk.BOTH)

        self.frame_derecho = ttk.Frame(root, width=ancho_frame, height=root.winfo_screenheight(), relief='solid', borderwidth=2)
        self.frame_derecho.pack(side=tk.LEFT, fill=tk.BOTH)

        # Texto en la parte superior central
        self.texto = tk.StringVar()
        self.texto.set("VENTANAS DE CONVERSACION")
        label_texto = tk.Label(self.frame_izquierdo, textvariable=self.texto, font=('Helvetica', 16), justify='center')
        label_texto.pack(pady=20)

        # Configurar el estilo para los botones
        root.style = ttk.Style()
        root.style.configure('Boton.TButton', font=('Helvetica', 16), background='#edb15c', foreground='black', borderwidth=1, relief='ridge', focuscolor='#008000')

        # Evento para cerrar la aplicación con la tecla Esc
        root.bind('<Escape>', lambda event: root.destroy())

        # Inicializar los botones
        self.inicializar_botones()

    def inicializar_botones(self):
        self.botones_izquierda = []
        nombres_botones = ["SALUDO", "DESPEDIDA", "RESPUESTAS", "NECESIDADES\nINMEDIATAS", "AYUDA", "CONFIRMACIÓN","INTERACCION\nCON EL\nENTORNO","PREGUNTAS\nFRECUENTES"]

        for i, nombre_boton in enumerate(nombres_botones):
            boton = ttk.Button(self.frame_izquierdo, text=nombre_boton, command=lambda i=i: self.boton_izquierdo_clicado(i), style='Boton.TButton')
            boton.pack(pady=10)
            self.botones_izquierda.append(boton)

        # Inicializar botones ocultos en la columna derecha
        self.botones_derecha_1 = []
        nombres_botones_ayuda = ["SALUDO", "DESPEDIDA", "RESPUESTAS", "NECESIDADES\nINMEDIATAS", "AYUDA", "CONFIRMACIÓN","INTERACCION\nCON EL\nENTORNO","PREGUNTAS\nFRECUENTES"]
        for i, nombre_boton in enumerate(nombres_botones_ayuda):
            boton = ttk.Button(self.frame_derecho, text=nombre_boton, command=lambda i=i: self.boton_derecho_clicado(i), style='Boton.TButton')
            boton.grid(row=i,column=0, padx=10, pady=10)
            boton.grid_remove()  # Ocultar los botones al principio
            self.botones_derecha_1.append(boton)

        self.botones_derecha_2 = []
        for i in range(7, 10):
            boton = ttk.Button(self.frame_derecho, text=f"Botón {i}", command=lambda i=i: self.boton_derecho_clicado(i), style='Boton.TButton')
            boton.grid(row=i - 6, column=1, padx=5, pady=5)
            boton.grid_remove()  # Ocultar los botones al principio
            self.botones_derecha_2.append(boton)

    def ocultar_botones_derecha(self):
        for boton in self.botones_derecha_1:
            boton.grid_remove()

        for boton in self.botones_derecha_2:
            boton.grid_remove()

    def mostrar_botones_derecha_1(self):
        for boton in self.botones_derecha_1:
            boton.grid()

    def mostrar_botones_derecha_2(self):
        for boton in self.botones_derecha_2:
            boton.grid()

    def boton_izquierdo_clicado(self, numero_boton):
        #self.texto.set(f"Botón {numero_boton} clicado")

        # Ocultar todos los botones de la columna derecha
        self.ocultar_botones_derecha()

        # Mostrar los botones correspondientes
        if numero_boton == 1:
            self.mostrar_botones_derecha_1()
        elif numero_boton == 2:
            self.mostrar_botones_derecha_2()

    def boton_derecho_clicado(self, numero_boton):
        self.texto.set(f"Botón {numero_boton} clicado")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazDividida(root)

    # Configurar el estilo para los botones
    root.style = ttk.Style()
    root.style.configure('Boton.TButton', font=('Helvetica', 16), background='#008000', foreground='white', borderwidth=5, relief='ridge', focuscolor='#008000')

    root.mainloop()
