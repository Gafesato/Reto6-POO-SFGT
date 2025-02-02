# Autor: Samuel Fernando Garzón Toro
# Reto 5

"""
La función toma una lista de palabras e identifica aquellas que tienen los mismos
caracteres, devolviendo solo las palabras que cumplen esta condición. Se utiliza
un bucle bidimensional para comparar pares de palabras mediante sus caracteres
ordenados.
"""

def verificar_palabras(lista_palabras: list[str]) -> list[str]:
    """Retorna las palabras con los mismos caracteres en una lista."""
    lista_palabras_iguales: list[str] = []
    n: int = len(lista_palabras)
    for i in range(n):
        for j in range(i + 1, n):
            palabra_a: str = lista_palabras[i]
            palabra_b: str = lista_palabras[j]
            if sorted(palabra_a) == sorted(palabra_b):
                # Añadir palabras si no están ya en la lista
                if palabra_a not in lista_palabras_iguales:
                    lista_palabras_iguales.append(palabra_a)
                if palabra_b not in lista_palabras_iguales:
                    lista_palabras_iguales.append(palabra_b)

    return lista_palabras_iguales


if __name__ == "__main__":
    print("Bienvenido al verificador de palabras iguales.")
    print("Ingrese cuantas palabras desee, presionando ENTER después de cada una.")
    print("Cuando quiera terminar, escriba 's'.")

    # Recopilar la lista de palabras
    lista_palabras: list[str] = []
    while True:
        palabra: str = input("Ingrese una palabra: ").strip()
        if palabra == 's':
            break
        lista_palabras.append(palabra)

    # Identificar palabras con los mismos caracteres
    lista_palabras_iguales: list[str] = verificar_palabras(lista_palabras)
    print(f"Las palabras con los mismos caracteres en {lista_palabras} son:")
    print(lista_palabras_iguales)
