palabras = ["Elefante", "Estrella", "España", "Escuela", "Elevar", "Ejemplo"]

def mostrar_palabras_con_e():
    palabras_con_e = [palabra for palabra in palabras if palabra.startswith('E')]
    print(palabras_con_e)

while True:
    entrada = input("Presiona la letra 'E' (o 'q' para salir): ")
    
    if entrada == 'E':
        mostrar_palabras_con_e()
    elif entrada == 'q':
        break
