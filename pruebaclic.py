import tkinter as tk
from tkinter import ttk

def boton_clicado(nombre):
    print(f"Botón {nombre} clicado")
    # Aquí puedes agregar la lógica que deseas realizar cuando se hace clic en un botón
    # Por ejemplo, puedes llamar a la función clic.on_press(nombre) o realizar otras acciones.

class InterfazDividida:
    def __init__(self, root):
        self.root = root

        # Obtener las dimensiones de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Configurar las dimensiones de los frames
        frame1_width = 250
        frame2_width = 400
        frame3_width = screen_width - frame1_width - frame2_width

        # Crear los frames con las dimensiones calculadas
        self.f1 = tk.Frame(root, background="bisque", width=frame1_width, height=screen_height)
        self.f2 = tk.Frame(root, background="pink", width=frame2_width, height=screen_height)
        self.f3 = tk.Frame(root, background="bisque", width=frame3_width, height=screen_height)

        # Configuración de la geometría y organización de columnas
        self.f1.grid(row=0, column=0, sticky="nsew")
        self.f2.grid(row=0, column=1, sticky="nsew")
        self.f3.grid(row=0, column=2, sticky="nsew")

        root.grid_columnconfigure(0, weight=0)
        root.grid_columnconfigure(1, weight=0)
        root.grid_columnconfigure(2, weight=1)

        # Texto en la parte superior central
        texto = tk.StringVar()
        texto.set("VENTANA DE CONVERSACION")
        label_texto = tk.Label(self.f1, textvariable=texto, font=('Helvetica', 16), justify='center')
        label_texto.grid(padx=5, pady=20)

        label_texto = tk.Label(self.f2, text="INTERACCION", font=('Helvetica', 16), justify='center', anchor='w')
        label_texto.grid(padx=50, pady=20)

        # Configurar el estilo para los botones
        root.style = ttk.Style()
        root.style.configure('Boton.TButton', font=('Helvetica', 16), background='#edb15c', foreground='black',
                             borderwidth=1, relief='ridge', focuscolor='#008000')

        # Inicializar los botones
        self.inicializar_botones()

        # Configuración de la geometría y organización de columnas
        self.f1.grid(row=0, column=0, sticky="nsew")
        self.f2.grid(row=0, column=1, sticky="nsew")
        self.f3.grid(row=0, column=2, sticky="nsew")

        self.root.grid_columnconfigure(0, weight=0)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

    def inicializar_botones(self):
        self.botones_izquierda = []
        nombres_botones = ["DESPEDIDA", "SALUDO", "RESPUESTAS", "NECESIDADES\nINMEDIATAS", "AYUDA", "CONFIRMACIÓN","INTERACCION\nCON EL\nENTORNO","PREGUNTAS\nFRECUENTES"]

        for i, nombre_boton in enumerate(nombres_botones):
            boton = ttk.Button(self.f1, text=nombre_boton, command=lambda i=i: self.boton_izquierdo_clicado(i), style='Boton.TButton')
            boton.grid(pady=10)
            self.botones_izquierda.append(boton)

        # Inicializar botones ocultos en la columna derecha
        self.SALUDOS = []
        nombres_botones_ayuda = ["Hola", "Saludos", "Buenos días", "Buenas Tardes", "Buenas Noches", "Cómo estas?","Qué tal?","Cómo le va","Saludos Cordiales","Bienvenido", "Hola amigo", "Hola amiga", "Encantado de verte"]
        for i, nombre_boton in enumerate(nombres_botones_ayuda):
            boton = ttk.Button(self.f2, text=nombre_boton, command=lambda nombre=nombre_boton: self.boton_derecho_clicado(nombre), style='Boton.TButton')
            boton.grid(row=i,column=0, padx=50, pady=7)
            boton.grid_remove()  # Ocultar los botones al principio
            self.SALUDOS.append(boton)

        self.DESPEDIDAS = []
        nombres_botones_ayuda = ["Adios", "Hasta luego", "Nos vemos", "Cuidate!", "Chau!", "Hasta pronto","Que tengas exito!","Buen viaje!","Hasta la proxima!","Nos vemos otro dia!"]
        for i, nombre_boton in enumerate(nombres_botones_ayuda):
            boton = ttk.Button(self.f2, text=nombre_boton, command=lambda nombre=nombre_boton: self.boton_derecho_clicado(nombre), style='Boton.TButton')
            boton.grid(row=i,column=0, padx=50, pady=7)
            boton.grid_remove()  # Ocultar los botones al principio
            self.DESPEDIDAS.append(boton)

        self.RESPUESTAS = []
        nombres_botones_ayuda = ["Bien, gracias", "Bien y tu?", "Pasando el dia", "Estupendo", "Muy bien", "Gracias, igualmente","Normal","Aceptable","Estoy genial","Estupendo", "Mas o menos", "En la normalidad"]
        for i, nombre_boton in enumerate(nombres_botones_ayuda):
            boton = ttk.Button(self.f2, text=nombre_boton, command=lambda nombre=nombre_boton: self.boton_derecho_clicado(nombre), style='Boton.TButton')
            boton.grid(row=i,column=0, padx=50, pady=7)
            boton.grid_remove()  # Ocultar los botones al principio
            self.RESPUESTAS.append(boton)

        self.NECESIDADES = []
        nombres_botones_ayuda = ["Tengo sed", "Agua, por favor", "Tengo hambre", "Quiero comer", "Necesito ir al baño", "Baño, por favor","Cambiame de ropa","Esto incomodo","Almohada, por favor","Tengo frio","Tengo calor","Necesito abrigo"]
        for i, nombre_boton in enumerate(nombres_botones_ayuda):
            boton = ttk.Button(self.f2, text=nombre_boton, command=lambda nombre=nombre_boton: self.boton_derecho_clicado(nombre), style='Boton.TButton')
            boton.grid(row=i,column=0, padx=50, pady=7)
            boton.grid_remove()  # Ocultar los botones al principio
            self.NECESIDADES.append(boton)

        self.AYUDA = []
        nombres_botones_ayuda = ["¿Puedes ayudarme?", "Necesito asistencia", "Puedo pedirte un favor?", "Puedes orientarme", "Puedes guiarme?", "Explicame esto","Necesito ver a un medico","Siento dolor","Quiero saber mas","Como funciona esto?","Estoy perdido, me ayudas?"]
        for i, nombre_boton in enumerate(nombres_botones_ayuda):
            boton = ttk.Button(self.f2, text=nombre_boton, command=lambda nombre=nombre_boton: self.boton_derecho_clicado(nombre), style='Boton.TButton')
            boton.grid(row=i,column=0, padx=50, pady=7)
            boton.grid_remove()  # Ocultar los botones al principio
            self.AYUDA.append(boton)

        self.CONFIRMACION = []
        nombres_botones_ayuda = ["Si", "Claro", "Correcto", "No", "Incorrecto", "Entendido","Comprendido","Si, confirmo","Acepto","Estoy de acuerdo", "No estoy de acuerdo", "Confirmo que no", "No, lo rechazo"]
        for i, nombre_boton in enumerate(nombres_botones_ayuda):
            boton = ttk.Button(self.f2, text=nombre_boton, command=lambda nombre=nombre_boton: self.boton_derecho_clicado(nombre), style='Boton.TButton')
            boton.grid(row=i,column=0, padx=50, pady=7)
            boton.grid_remove()  # Ocultar los botones al principio
            self.CONFIRMACION.append(boton)

        self.INTERACCION = []
        nombres_botones_ayuda = ["Enciende las luces", "Apaga las luces", "Ajusta la intensidad de la luz", "Abre la puerta", "Cierra la puerta", "Sube la persiana","Baja la persiana","Prende el ventilador","Apaga el ventilador","Lee las noticias", "Consulta mi agenda", "Consulta mi agenda"]
        for i, nombre_boton in enumerate(nombres_botones_ayuda):
            boton = ttk.Button(self.f2, text=nombre_boton, command=lambda nombre=nombre_boton: self.boton_derecho_clicado(nombre), style='Boton.TButton')
            boton.grid(row=i,column=0, padx=50, pady=7)
            boton.grid_remove()  # Ocultar los botones al principio
            self.INTERACCION.append(boton)

        self.PREGUNTAS = []
        nombres_botones_ayuda = ["¿Como funciona este asistente?", "Explicame las funciones principales", "¿Que puedo realizar con este sistema?", "¿Puedo personalizarlo?", "Hablame de la seguridad del dispositivo"]
        for i, nombre_boton in enumerate(nombres_botones_ayuda):
            boton = ttk.Button(self.f2, text=nombre_boton, command=lambda nombre=nombre_boton: self.boton_derecho_clicado(nombre), style='Boton.TButton')
            boton.grid(row=i,column=0, padx=50, pady=7)
            boton.grid_remove()  # Ocultar los botones al principio
            self.PREGUNTAS.append(boton)



    def ocultar_botones_derecha(self):
        for boton in self.SALUDOS:
            boton.grid_remove()

        for boton in self.DESPEDIDAS:
            boton.grid_remove()

        for boton in self.RESPUESTAS:
            boton.grid_remove()

        for boton in self.NECESIDADES:
            boton.grid_remove()

        for boton in self.AYUDA:
            boton.grid_remove()

        for boton in self.CONFIRMACION:
            boton.grid_remove()

        for boton in self.INTERACCION:
            boton.grid_remove()

        for boton in self.PREGUNTAS:
            boton.grid_remove()


    def mostrar_botones_SALUDOS(self):
        for boton in self.SALUDOS:
            boton.grid()
    def mostrar_botones_DESPEDIDAS(self):
        for boton in self.DESPEDIDAS:
            boton.grid()
    def mostrar_botones_RESPUESTAS(self):
        for boton in self.RESPUESTAS:
            boton.grid()
    def mostrar_botones_NECESIDADES(self):
        for boton in self.NECESIDADES:
            boton.grid()
    def mostrar_botones_AYUDA(self):
        for boton in self.AYUDA:
            boton.grid()
    def mostrar_botones_CONFIRMACION(self):
        for boton in self.CONFIRMACION:
            boton.grid()
    def mostrar_botones_INTERACCION(self):
        for boton in self.INTERACCION:
            boton.grid()
    def mostrar_botones_PREGUNTAS(self):
        for boton in self.PREGUNTAS:
            boton.grid()

    def boton_izquierdo_clicado(self, numero_boton):
        #self.texto.set(f"Botón {numero_boton} clicado")
        print(f"Ventana izquierda clic en boton numero: {numero_boton}")

        # Ocultar todos los botones de la columna derecha
        self.ocultar_botones_derecha()



        # Mostrar los botones correspondientes
        if numero_boton == 0:
            self.mostrar_botones_SALUDOS()
        elif numero_boton == 1:
            self.mostrar_botones_DESPEDIDAS()
        elif numero_boton == 2:
            self.mostrar_botones_RESPUESTAS()
        elif numero_boton == 3:
            self.mostrar_botones_NECESIDADES()
        elif numero_boton == 4:
            self.mostrar_botones_AYUDA()
        elif numero_boton == 5:
            self.mostrar_botones_CONFIRMACION()
        elif numero_boton == 6:
            self.mostrar_botones_INTERACCION()
        elif numero_boton == 7:
            self.mostrar_botones_PREGUNTAS()



    def boton_derecho_clicado(self, nombre_boton):
        print(nombre_boton)
        boton_clicado(nombre_boton)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazDividida(root)

    # Configurar el estilo para los botones (debería estar antes del mainloop)
    root.style = ttk.Style()
    root.style.configure('Boton.TButton', font=('Helvetica', 16), background='#008000', foreground='white',
                         borderwidth=5, relief='ridge', focuscolor='#008000')

    root.mainloop()
