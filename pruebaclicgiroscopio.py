import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pyttsx3
import cv2
import dlib
import numpy as np
import clic
import threading
import time
########################################PARPADEOS######################################
# Cargar el detector de caras de Dlib y el predictor de puntos de referencia faciales
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Asegúrate de tener el archivo descargado

# Índices de los puntos de referencia faciales correspondientes a los ojos
left_eye_indices = list(range(36, 42))
right_eye_indices = list(range(42, 48))

# Inicializar el contador de parpadeos y el umbral de parpadeo
blink_counter = 0
blink_threshold = 3  # Ajustado a un valor menor para aumentar la sensibilidad

# Función que se ejecutará al detectar un parpadeo
def on_blink():
    print("¡Parpadeo detectado!")
    clic.on_press(1)
#####################################FIN PARPADEOS#####################################

def boton_clicado(nombre):
    print(f"Botón {nombre} clicado")
    speak(nombre)

def speak(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

class InterfazDividida:
    def __init__(self, root):
        self.root = root
        root.geometry("1366x768")
        self.root = root
        self.tiempo_inicial = None
        self.clics = 0  # Contador de clics
        self.f1 = tk.Frame(root, background="bisque", width=250, height=768)
        self.f2 = tk.Frame(root, background="pink", width=400, height=768)
        self.f3 = tk.Frame(root, background="bisque", width=766, height=768)

        # Texto en la parte superior central
        texto = tk.StringVar()
        texto.set("VENTANA DE CONVERSACION")
        label_texto = tk.Label(self.f1, textvariable=texto, font=('Helvetica', 16), justify='center')
        label_texto.grid(padx=5, pady=20)

        texto2 = tk.StringVar()
        texto2.set("INTERACCION")
        label_texto = tk.Label(self.f2, textvariable=texto2, font=('Helvetica', 16), justify='center')
        label_texto.grid(padx=50, pady=20)

        # Configurar el estilo para los botones
        root.style = ttk.Style()
        root.style.configure('Boton.TButton', font=('Helvetica', 16), background='#edb15c', foreground='black',
                             borderwidth=1, relief='ridge', focuscolor='#008000')

        # Evento para cerrar la aplicación con la tecla Esc
        root.bind('<Escape>', lambda event: root.destroy())

        # Inicializar los botones
        self.inicializar_botones()
        self.iniciar_temporizador()
        # Configuración de la geometría y organización de columnas
        self.f1.grid(row=0, column=0, sticky="nsew")
        self.f2.grid(row=0, column=1, sticky="nsew")
        self.f3.grid(row=0, column=2, sticky="nsew")

        self.root.grid_columnconfigure(0, weight=0)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        # Agregar visualización de la cámara en self.f3
        self.cargar_camara_en_frame()

    def inicializar_botones(self):
        self.botones_izquierda = []
        nombres_botones = ["SALUDOS", "DESPEDIDAS", "RESPUESTAS", "NECESIDADES\nINMEDIATAS", "AYUDA", "CONFIRMACIÓN","INTERACCION\nCON EL\nENTORNO","PREGUNTAS\nFRECUENTES"]
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

    def iniciar_temporizador(self):
        self.tiempo_inicial = time.time()
        # Crear un hilo para el temporizador
        threading.Thread(target=self.actualizar_tiempo).start()

    def reiniciar_temporizador(self):
        self.clics += 1  # Incrementar el contador de clics
        if self.clics % 2 == 0:  # Reiniciar solo en el segundo clic
            #SE HA HECHO CLIC EN EL BOTON
            print(f" {self.boton_clicado_nombre}")
            self.tiempo_inicial = time.time()
        
    def actualizar_tiempo(self):
        while True:
            if self.tiempo_inicial is not None:
                tiempo_actual = int(time.time() - self.tiempo_inicial)
                print(f"Tiempo transcurrido: {tiempo_actual} segundos")

            # Esperar 1 segundo antes de la próxima actualización
            time.sleep(1)
                
    def boton_izquierdo_clicado(self, numero_boton):
        if numero_boton == 0:
            self.mostrar_botones_SALUDOS()
            self.boton_clicado_nombre ="Seleccionado con Giroscopio"
        elif numero_boton == 1:
            self.mostrar_botones_DESPEDIDAS()
            self.boton_clicado_nombre ="Seleccionado con Giroscopio"
        elif numero_boton == 2:
            self.mostrar_botones_RESPUESTAS()
            self.boton_clicado_nombre ="Seleccionado con Giroscopio"
        elif numero_boton == 3:
            self.mostrar_botones_NECESIDADES()
            self.boton_clicado_nombre ="Seleccionado con Giroscopio"
        elif numero_boton == 4:
            self.mostrar_botones_AYUDA()
            self.boton_clicado_nombre ="Seleccionado con Giroscopio"
        elif numero_boton == 5:
            self.mostrar_botones_CONFIRMACION()
            self.boton_clicado_nombre ="Seleccionado con Giroscopio"
        elif numero_boton == 6:
            self.mostrar_botones_INTERACCION()
            self.boton_clicado_nombre ="Seleccionado con Giroscopio"
        elif numero_boton == 7:
            self.mostrar_botones_PREGUNTAS()
            self.boton_clicado_nombre ="Seleccionado con Giroscopio"

        # Actualizar tiempo al hacer clic
      
        self.reiniciar_temporizador()
        
    def boton_derecho_clicado(self, nombre_boton):
        print(nombre_boton)
        # Llama a la función que falta, reemplázala con la acción que desees realizar
        # boton_clicado(nombre_boton)
        self.tiempo_inicial = None

    def cargar_camara_en_frame(self):
        # Configurar la captura de video desde la cámara
        cap = cv2.VideoCapture(0)

        # Configurar el widget Label para mostrar la imagen de la cámara
        label_camara = tk.Label(self.f3)
        label_camara.grid(row=0, column=0, padx=10, pady=10)

        def mostrar_camara():
            # Declarar blink_counter como global
            global blink_counter

            # Capturar un fotograma de la cámara
            ret, frame = cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector(gray)

            for face in faces:
                landmarks = predictor(gray, face)

                # Obtener las coordenadas de los puntos de referencia de los ojos
                left_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in left_eye_indices]
                right_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in right_eye_indices]

                # Convertir a numpy array para satisfacer los requisitos de OpenCV
                left_eye = np.array(left_eye, dtype=np.int32)
                right_eye = np.array(right_eye, dtype=np.int32)

                # Dibujar los contornos de los ojos
                cv2.polylines(frame, [left_eye], isClosed=True, color=(0, 255, 0), thickness=1)
                cv2.polylines(frame, [right_eye], isClosed=True, color=(0, 255, 0), thickness=1)

                # Calcular la relación de apertura de los ojos
                eye_aspect_ratio = (cv2.norm(left_eye[1] - left_eye[5]) + cv2.norm(left_eye[2] - left_eye[4])) / (2.0 * cv2.norm(left_eye[0] - left_eye[3]))

                # Dibujar la relación de apertura de los ojos en el frame
                cv2.putText(frame, f'Relacion de apertura de los ojos: {eye_aspect_ratio:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                # Verificar si la relación de apertura de los ojos está por debajo del umbral
                if eye_aspect_ratio < 0.2:
                    blink_counter += 1

            # Verificar si se ha producido un parpadeo
            if blink_counter >= blink_threshold:
                cv2.putText(frame, 'Parpadeo detectado!', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                # Ejecutar la función en un hilo aparte para evitar bloquear el hilo principal
                threading.Thread(target=on_blink).start()

                # Reiniciar el contador de parpadeos
                blink_counter = 0

            # Dibujar un contorno alrededor del rostro
            for face in faces:
                x, y, w, h = face.left(), face.top(), face.width(), face.height()
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Mostrar el frame resultante
            #cv2.imshow('Deteccion de parpadeos', frame)

            # Actualizar la imagen en el Label
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img_tk = ImageTk.PhotoImage(image=img)
            label_camara.img_tk = img_tk  # Para evitar que se borre por el recolector de basura
            label_camara.config(image=img_tk)

            # Llamar a la función nuevamente después de un cierto tiempo (en milisegundos)
            label_camara.after(1, mostrar_camara)

        # Llamar a la función inicialmente
        mostrar_camara()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazDividida(root)

    # Configurar el estilo para los botones (debería estar antes del mainloop)
    root.style = ttk.Style()
    root.style.configure('Boton.TButton', font=('Helvetica', 16), background='#008000', foreground='white',
                         borderwidth=5, relief='ridge', focuscolor='#008000')

    root.mainloop()
