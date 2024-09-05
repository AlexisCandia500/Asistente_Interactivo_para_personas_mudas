from pynput.mouse import Controller
import time

# Inicializar el controlador del ratón
mouse = Controller()

# Definir coordenadas para delimitar cierta área (por ejemplo, un cuadrado)
x_min, y_min = 50, 35
x_max, y_max = 200, 200

# Función para verificar si el puntero está dentro del área delimitada
def is_inside_area(position):
    return x_min <= position[0] <= x_max and y_min <= position[1] <= y_max

try:
    while True:
        # Obtener la posición actual del puntero
        current_position = mouse.position
        print(f'Posición actual del puntero: {current_position}')

        # Verificar si el puntero está dentro del área delimitada
        if is_inside_area(current_position):
            print('El puntero está dentro del área delimitada.')
            # Puedes realizar acciones adicionales aquí cuando el puntero está dentro
        else:
            print('El puntero está fuera del área delimitada.')

        # Esperar un breve período antes de volver a obtener la posición
        time.sleep(0.5)

except KeyboardInterrupt:
    # Manejar la interrupción del teclado (Ctrl+C) para salir del bucle de manera controlada
    print('Saliendo del programa.')
