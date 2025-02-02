# Autor: Samuel Fernando Garzón Toro
# Reto 4

"""
La función toma una lista de enteros y calcula la mayor suma
entre dos elementos consecutivos de la lista. Si la lista tiene
menos de dos elementos, retorna 0.
"""

def mayor_suma(lista_enteros: list[int]) -> int:
    """Retorna la mayor suma entre dos elementos consecutivos en una lista."""
    if len(lista_enteros) < 2:
        return 0

    mayor: int = 0  # Inicializar con el menor valor posible
    for i in range(len(lista_enteros) - 1):
        suma: int = lista_enteros[i] + lista_enteros[i + 1]
        if suma > mayor:
            mayor = suma

    return mayor


if __name__ == "__main__":
    print("Bienvenido al programa de suma de números consecutivos.")
    print("Ingrese cuantos números desee, presionando ENTER después de cada uno.")
    print("Cuando quiera terminar, escriba 's'.")

    # Obtener la lista de números
    lista_numeros: list[int] = []
    while True:
        numero: str = input("Ingrese un número: ")
        if numero == 's':
            break
        try:
            lista_numeros.append(int(numero))
        except ValueError:
            print("¡Error! El valor ingresado no es un número entero.")

    # Calcular la mayor suma consecutiva
    resultado: int = mayor_suma(lista_numeros)
    print(f"La mayor suma entre números consecutivos en {lista_numeros} es: {resultado}")
