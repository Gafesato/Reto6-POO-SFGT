# Autor: Samuel Fernando Garzón Toro
# Reto 6

"""
Hice una función que verifica si los números en una lista son primos. 
Para cada número, se evalúan tres casos: si es menor a 2, si es igual 
a 2, o si es mayor a 2, aquí se calcula la raíz cuadrada del número y 
se verifica si tiene divisores dentro del rango [2, raíz]. Si no tiene
divisores, el número es primo y se añade a la lista de salida.
"""

def verificar_primos(lista_numeros: list[int]) -> list[int]:
    """Filtra los números primos de una lista de enteros."""
    lista_primos: list = []
    for numero in lista_numeros:
        if numero < 2:
            continue  # No es primo si es menor que 2
        elif numero == 2:
            lista_primos.append(numero)  # El 2 es primo
        else:
            primo: bool = True
            # Verificar en el rango del número completo es más largo
            # La raíz es buena aproximación matemática
            raiz: float = (numero**0.5) + 1
            for i in range(2, raiz):
                if numero % i == 0:
                    primo = False
                    break
            if primo:
                lista_primos.append(numero)

    return lista_primos


if __name__ == "__main__":
    print("Bienvenido al verificador de primos.")
    print("A continuación va a digitar cuantos números quiera presionándo ENTER.")
    print("Cuando desee terminar presione la tecla 's'.")
    # Aquí voy a obtener la lista de números
    lista_numeros: list = []
    while True:
        numero: str = input("Ingrese un número: ")
        if numero == 's':
            break
        try:
            lista_numeros.append(int(numero))
        except ValueError:
            print("¡Error! El valor ingresado no es un número entero.")

    lista_primos: list[int] = verificar_primos(lista_numeros)
    print(f"Los números primos en {lista_numeros} son {lista_primos}.")