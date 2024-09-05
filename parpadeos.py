import cv2
import dlib
import numpy as np
import clic



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

# Iniciar la captura de video desde la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

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
        # Ejecutar la función al detectar un parpadeo
        on_blink()

        # Reiniciar el contador de parpadeos
        blink_counter = 0

    # Dibujar un contorno alrededor del rostro
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Mostrar el frame resultante
    cv2.imshow('Deteccion de parpadeos', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
