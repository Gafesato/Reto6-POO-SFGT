# Reto 6 POO - Manejo de Excepciones
* Este repositorio tiene la solución al reto 6 de la clase de Programación Orientada a Objetos de la Universidad Nacional de Colombia. La parte 1 consiste en agregar el manejo de excepciones a los ejercicios de un reto pasado. La parte dos es lo mismo, pero para el robusto paquete shape que se ha ido creando a lo largo del semestre.
## Parte 1 - Miniretos

Este repositorio contiene varios retos de programación en Python, con un enfoque en el manejo adecuado de excepciones. A continuación se detallan los ejercicios realizados, junto con las excepciones clave que fueron manejadas y cómo se resolvieron.

### 1. **Calculadora Básica**
**Excepciones**:
- **`ValueError`**: Se manejó en el momento en que el usuario ingresa un valor no numérico, con un mensaje que indica que la entrada debe ser numérica.
- **`ZeroDivisionError`**: Se verifica que no se realice una división entre cero, proporcionando un mensaje específico si esto ocurre.
- **`MyError`**: Se creó una excepción personalizada para manejar operaciones no válidas.
**Código relevante**:
```python
def calculadora(a: int, b: int, operacion: str) -> float | str:
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
```
A continuación podemos ver el uso de las cláusulas try-except:
```python
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
```
### 2. **Verificador de Palíndromos**
**Excepciones**:
- **`MyError`**: Se gestionó para el formato de la palabra que se ingresa, por ejemplo, si el input() está vacío o con espacios.
```python
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
```
Parte que se ejecuta:
```python
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
```
### 3. **Verificador de Números Primos**
**Excepciones**:
- **`ValueError`**: Esta excepción se alza si se pone "izquierda" en una entrada numérica, por ejemplo.
- **Excepciones generales**: Se preparó el código para capturar errores imprevistos y ofrecer un mensaje claro por si se llegase a necesitar.
```python
lista_numeros: list = []
    while True:
        try:
            numero: str = input("Ingrese un número: ")
            if numero.lower() == 's':
                break
            lista_numeros.append(int(numero))  # Intentar convertir la entrada a un número entero
        except ValueError:
            print("¡Error! El valor ingresado no es un número entero válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")

    try:
        lista_primos: list[int] = verificar_primos(lista_numeros)
        print(f"Los números primos en {lista_numeros} son {lista_primos}.")
    except Exception as e:
        print(f"Ocurrió un error al verificar los primos: {e}")
    finally:
        print("Gracias por usar el verificador de primos.")
```
### 4. **Mayor Suma Consecutiva**
**Excepciones**:
- **`ValueError`**: Se maneja cuando el usuario ingresa algo que no es un número entero. Un mensaje informa al usuario sobre la entrada incorrecta.
- También en la función `mator_suma()` se usa `raise ValueError()` cuando se detecte que la lista dada no tiene dos elementos. Pues si eso es así nada corre.
```python
def mayor_suma(lista_enteros: list[int]) -> int:
    """Retorna la mayor suma entre dos elementos consecutivos en una lista."""
    if len(lista_enteros) < 2:
        raise ValueError("La lista debe tener al menos dos elementos para calcular la suma consecutiva.")
```
```python
# Obtener la lista de números
    lista_numeros: list[int] = []
    while True:
        try:
            numero: str = input("Ingrese un número: ")
            if numero == 's':
                break
            lista_numeros.append(int(numero))  # Intentar convertir la entrada a un número entero
        except ValueError:
            print("¡Error! El valor ingresado no es un número entero válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")

    try:
        # Calcular la mayor suma consecutiva
        resultado: int = mayor_suma(lista_numeros)
        print(f"La mayor suma entre números consecutivos en {lista_numeros} es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        print("Gracias por usar el programa.")
```

### 5. **Verificador de Palabras con los Mismos Caracteres**
**Excepciones**:
- **`ValueError`**: Se asegura que solo se ingresen palabras alfabéticas, luego caracteres especiales o vacíos no son permitidos.
- **Excepciones generales**: Se manejan posibles errores en el flujo de ejecución y se informa adecuadamente al usuario->"profesor".
```python
# Recopilar la lista de palabras
    lista_palabras: list[str] = []
    while True:
        try:
            palabra: str = input("Ingrese una palabra: ").strip()
            if palabra.lower() == 's':
                break
            if not palabra.isalpha():
                raise ValueError("Solo se permiten palabras con caracteres alfabéticos.")
            lista_palabras.append(palabra)
        except ValueError as e:
            print(f"¡Error! {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    try:
        # Identificar palabras con los mismos caracteres
        lista_palabras_iguales: list[str] = verificar_palabras(lista_palabras)
        print(f"Las palabras con los mismos caracteres en {lista_palabras} son:")
        print(lista_palabras_iguales)
    except Exception as e:
        print(f"Ocurrió un error inesperado al procesar las palabras: {e}")
    finally:
        print("Gracias por usar el verificador de palabras iguales.")
```

## Parte 2 - Clase Shape mejorada
* Realmente la solución a este ejercicio está permitiendo de dotar mayor funcionalidad al paquete shape, ya que se manejan posibles errores como que un cálculo termine siendo inválido o que al pasar argumentos a las funciones se cometa errores. Así siempre nos aseguramos de que el programa corra y en caso de saltar una excepción, se pueda ver y que no se "petaquee" el script.
