# @Samuel Fernando Garzón Toro
# Reto 6

"""
He creado una función calculadora con la estructura `match-case` 
para cada operación, gestionando la división entre cero y ninguna 
operación indicada. Se solicitan los 3 datos y al final se muestra 
al usuario la salida.
"""

class MyError(Exception):
    """
    Excepción personalizada para un caso específico.

    Args:
        message: Mensaje informativo sobre la excepción.
    """

    def __init__(self, message):
        super().__init__(message)


def calculadora(a: int, b: int, operacion: str) -> float | str:
    """Realiza una operación básica entre dos números."""
    match operacion:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                raise ZeroDivisionError("¡División entre 0!")
            return a / b
        case _:
            raise MyError("Operación no válida.")


print("Bienvenido a la calculadora!")

try:
    a: int = int(input("Primer número: "))
    b: int = int(input("Segundo número: "))
    operacion: str = input("Operación (+, -, *, /): ")

    # Verificar si la operación ingresada es válida
    if operacion not in ["+", "-", "*", "/"]:
        raise MyError("Operación no válida.")

    resultado = calculadora(a, b, operacion)
    print(f"({a}, {b}, '{operacion}') -> {resultado}")

except ValueError:
    print("La entrada debe ser numérica. Por favor ingrese un número válido.")
except ZeroDivisionError as error:
    print(f"Error: {error}")
except MyError as error:
    print(f"Error: {error}")
except Exception as error:
    print(f"Ha ocurrido un error inesperado: {error}")
finally:
    print("Gracias por usar la calculadora. ¡Hasta pronto!")