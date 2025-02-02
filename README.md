# Reto 6 POO - Manejo de Excepciones
## Samuel Fernando Garzón Toro - Universidad Nacional de Colombia
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
---
Se ha creado una función que permite probar los errores en `main.py`. Aquí se incluye la Clase `ValorInválidoArgs` que se ha creado para manejar excepciones personalizadas y que impriman lo que se desee.
```python
def main2():
try:
    # ERROR 1
    # Este levanta ValueError diciendo que no se
    # selecciono método válido al inicializar
    #shape = Shape(0)

    # ERROR 2
    # Como toda figura debe tener 3 vértices o más
    # Al instanciar Shape solo con 2 puntos, va a levantar
    # el error personalizado.
    # Funciona igual al instanciar solo con 2 aristas
    shape = Shape(1, Point(), Point(2,2), Point(4,4), Point(5,5), Point(6,6))

    # ERROR 3
    # Se genera cuando se llama al método compute_area()
    # directamente desde el objeto shape. Esto debe alzar
    # un error porque no se sabe qué polígono es
    #print(shape.compute_area())
    print(shape.compute_perimeter())

except ValorInvalidoArgs as e:
    print(f"Error de argumentos-> {e}")
except NotImplementedError as e:
    print(f"Error de implementación-> {e}")
except Exception as e:
    print(f"Error inesperado-> {e}")
```
Como vemos en la instancia de shape del código anterior. Lo he definido con puntos correctamente, pero todos forman una línea recta, por lo tanto no es una figura. Así que cree un nuevo método protegido, funciona solo para la clase en cuestión, donde hace un par de verificaciones junto con la colinealidad de los puntos.
Cabe mencionar que usé un LLM para poder crear el algoritmo de recorrido que corresponde a `DepthFirstSearch`.
```python
def _check_is_valid_shape(self) -> bool:
    """Verifica si la figura es válida (es una figura cerrada y no colineal)."""
    if len(self.edges) != len(self.vertices):  
        return [False, "El número de aristas y vértices no es el mismo."]  # Debe haber el mismo número de aristas y vértices

    # Verificar si al menos 3 puntos consecutivos son colineales
    for i in range(len(self.vertices)):
        p1 = self.vertices[i - 2]
        p2 = self.vertices[i - 1]
        p3 = self.vertices[i]

        # Determinante para verificar colinealidad
        det = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
        if det == 0:
            return [False, "Hay puntos colineales que no forman una figura."]  # Si el determinante es 0, los puntos son colineales

    # Crear un conjunto de conexiones para verificar si cada vértice está bien conectado
    connections = {vertex: [] for vertex in self.vertices}
    
    for edge in self.edges:
        connections[edge.start_point].append(edge.end_point)
        connections[edge.end_point].append(edge.start_point)

    # Empezar desde un vértice y recorrer toda la figura para verificar que es un ciclo
    visited = set()
    stack = [self.vertices[0]]  # Iniciar desde cualquier punto

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(connections[current])  # Agregar los puntos conectados

    return [True, len(visited)]
```
En el constrcutor de Shape, cree dos verificaciones, que el número de args sea correcto y que los argumentos que se pasen, sean instancias de Point() o Line():
```python
if len(args) <= 2:
    raise ValorInvalidoArgs("No se han proporcionado el número adecuado de vértices o aristas para la Figura.")

if not all(isinstance(arg, (Point, Line)) for arg in args):
    raise ValorInvalidoArgs("Todos los argumentos deben ser instancias de Point o Line.")
```
Luego de inicializar el objeto en el constructor con los dos métodos, termino de verificar si en general se trata de una figura
```python
# Verificar que es una Figura bien definida
flag, issue = self._check_is_valid_shape()
if not flag:
    raise ValorInvalidoArgs(f"La Figura no es correcta: {issue}")
```
Finalmente, pongo la verificación que se realiza para ver si un triángulo dado es en efecto este tipo de figura. Este método le corresponde a Triangle.
```python
def _check_triangle_type(self, unique_sides: int) -> bool:
    sides: list[float] = [edge.length for edge in self.edges]
    # Uso set() ya que solo permite valores únicos
    # En caso de que len(set(...)) == unique_sides,
    # es porque hay unique_sides iguales
    # tomo 7 valores de redondeo para verificar bien
    return len(set(round(side, 7) for side in sides)) == unique_sides
```
Pero como tal, veamos como llamo a la verificación en una clase que herede de Triangle, como TriRectangle.
```python
from shape.triangle import Triangle

class TriRectangle(Triangle):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        if not self._is_right_triangle() and not self._check_triangle_type(3):
            raise ValueError("Los vértices dados no forman un triángulo rectángulo.")

    def _is_right_triangle(self) -> bool:
        """Verifica que el triángulo sea rectángulo usando El Teorema de Pitágoras."""
        c1, c2, hyp = sorted(edge.length**2 for edge in self.edges)
        return round(c1+c2, 7) == round(hyp, 7)
```
