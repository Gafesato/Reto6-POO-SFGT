# Autor: Samuel Fernando Garzón Toro
# Reto 6

"""
He creado una función que verifica si una palabra es un palíndromo 
utilizando dos iteradores: uno desde el inicio y otro desde el final. 
En cada iteración se comparan los caracteres correspondientes; si son 
distintos, se devuelve `False`. Si al terminar el bucle no se encuentran 
diferencias, se retorna `True`.
"""

class MyError(Exception):
    """
    Excepción personalizada para un caso específico.

    Args:
        message: Mensaje informativo sobre la excepción.
    """

    def __init__(self, message):
        super().__init__(message)


def verificar_palindromo(palabra: str) -> bool:
    """Verifica si una palabra es un palíndromo."""
    # Validación de entrada para asegurarse que la palabra no esté vacía
    if not palabra:
        raise MyError("La palabra no puede estar vacía.")

    # Asegurarse de que la palabra sea solo en minúsculas y sin espacios
    if ' ' in palabra or not palabra.islower():
        raise MyError("La palabra debe estar en minúsculas y no debe contener espacios.")

    iterador_normal: int = 0
    iterador_reverso: int = len(palabra) - 1

    while iterador_reverso >= iterador_normal:
        if palabra[iterador_reverso] != palabra[iterador_normal]:
            return False
        iterador_normal += 1
        iterador_reverso -= 1

    return True


if __name__ == "__main__":
    print("Bienvenido al verificador de palíndromos.")
    try:
        palabra: str = input("Introduce una palabra sin espacios y en minúscula: ")
        resultado = verificar_palindromo(palabra)
        print(f"La palabra '{palabra}' es palíndromo: {resultado}")
    except MyError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Ha ocurrido un error inesperado: {error}")
    finally:
        print("Gracias por usar el verificador de palíndromos.")
