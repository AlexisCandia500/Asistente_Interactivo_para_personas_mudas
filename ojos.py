import cv2
import numpy as np
import pyautogui
import pygame
from pygame.locals import *

# Desactivar fail-safe
pyautogui.FAILSAFE = False

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Configuración para el seguimiento ocular
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Variables para el seguimiento de parpadeo
blink_counter = 0
blink_threshold = 3  # Ajusta este umbral según sea necesario

# Inicializar Pygame
pygame.init()

# Obtener el tamaño de la imagen de la cámara
_, sample_frame = cap.read()
window_width, window_height = sample_frame.shape[1], sample_frame.shape[0]

# Configuración de la ventana
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Control de Parpadeo')

# Colores
button_color = (255, 0, 0)
background_color = (255, 255, 255)
blink_color = (0, 0, 255)  # Color del indicador de parpadeo

# Crear el botón
button_rect = pygame.Rect(50, 50, 200, 100)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            cap.release()
            cv2.destroyAllWindows()
            exit()

    # Leer la imagen de la cámara
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir la imagen a formato RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convertir la imagen a formato Pygame
    frame_pygame = np.rot90(np.fliplr(frame_rgb))
    frame_pygame = pygame.surfarray.make_surface(frame_pygame)
    screen.blit(frame_pygame, (0, 0))

    # Detectar rostros
    faces = face_cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1.3, 5)
    for (x, y, w, h) in faces:
        roi_gray = cv2.cvtColor(frame[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY)

        # Detectar ojos
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            # Calcular la posición del centro del ojo
            eye_center_x = x + ex + ew // 2
            eye_center_y = y + ey + eh // 2

            # Verificar el estado de parpadeo
            _, eye_thresh = cv2.threshold(roi_gray[ey:ey + eh, ex:ex + ew], 30, 255, cv2.THRESH_BINARY)
            eye_ratio = cv2.countNonZero(eye_thresh) / (ew * eh)

            if eye_ratio < 0.2:  # Ajusta este umbral según sea necesario
                blink_counter += 1
            else:
                blink_counter = 0

            # Realizar clic derecho con cada parpadeo
            if blink_counter >= blink_threshold:
                pyautogui.rightClick()

                # Cambiar color del botón
                button_color = (0, 255, 0)

                # Imprimir en la consola cada vez que se detecta un parpadeo
                print("¡Parpadeo detectado!")

    # Dibujar el botón
    pygame.draw.rect(screen, button_color, button_rect)

    # Dibujar el indicador de parpadeo
    if blink_counter > 0:
        pygame.draw.circle(screen, blink_color, (window_width - 30, 30), 10)

    pygame.display.flip()

    # Romper el bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
