import tkinter as tk

root = tk.Tk()
root.geometry("1366x768")

f1 = tk.Frame(root, background="bisque", width=200, height=768)
f2 = tk.Frame(root, background="pink", width=400, height=768)
f3 = tk.Frame(root, background="bisque", width=766, height=768)

botones_izquierda = []
nombres_botones = ["SALUDO", "DESPEDIDA", "RESPUESTAS", "NECESIDADES\nINMEDIATAS", "AYUDA", "CONFIRMACIÓN","INTERACCION\nCON EL\nENTORNO","PREGUNTAS\nFRECUENTES"]


   # Texto en la parte superior central
texto = tk.StringVar()
texto.set("VENTANAS DE CONVERSACION")
label_texto = tk.Label(f1, textvariable=texto, font=('Helvetica', 16), justify='center')
label_texto.pack(pady=20)



f1.grid(row=0, column=0, sticky="nsew")
f2.grid(row=0, column=1, sticky="nsew")
f3.grid(row=0, column=2, sticky="nsew")

root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(2, weight=0)

root.mainloop()