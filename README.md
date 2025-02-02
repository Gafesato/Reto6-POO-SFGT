# Reto 6 POO - Manejo de Excepciones
* Este repositorio tiene la solución al reto 6 de la clase de Programación Orientada a Objetos de la Universidad Nacional de Colombia. La parte 1 consiste en agregar el manejo de excepciones a los ejercicios de un reto pasado. La parte dos es lo mismo, pero para el robusto paquete shape que se ha ido creando a lo largo del semestre.
## Parte 1 - Miniretos

Este repositorio contiene varios retos de programación en Python, con un enfoque en el manejo adecuado de excepciones. A continuación se detallan los ejercicios realizados, junto con las excepciones clave que fueron manejadas y cómo se resolvieron.

### 1. **Calculadora Básica**
**Excepciones**:
- **`ValueError`**: Se manejó en el momento en que el usuario ingresa un valor no numérico, con un mensaje que indica que la entrada debe ser numérica.
- **`ZeroDivisionError`**: Se verifica que no se realice una división entre cero, proporcionando un mensaje específico si esto ocurre.
- **`MyError`**: Se creó una excepción personalizada para manejar operaciones no válidas.

### 2. **Verificador de Palíndromos**
**Excepciones**:
- **`MyError`**: Aunque no se lanzó en este caso específico, se preparó la función para gestionar errores personalizados en caso de una entrada incorrecta o de formatos no esperados.

### 3. **Verificador de Números Primos**
**Excepciones**:
- **`ValueError`**: Si el usuario ingresa algo que no es un número entero, se captura esta excepción y se informa al usuario.
- **Excepciones generales**: Se preparó el código para capturar errores imprevistos y ofrecer un mensaje claro.

### 4. **Mayor Suma Consecutiva**
**Excepciones**:
- **`ValueError`**: Se maneja cuando el usuario ingresa algo que no es un número entero. Un mensaje informa al usuario sobre la entrada incorrecta.

### 5. **Verificador de Palabras con los Mismos Caracteres**
**Excepciones**:
- **`ValueError`**: Se asegura que solo se ingresen palabras alfabéticas, rechazando caracteres especiales o vacíos.
- **Excepciones generales**: Se manejan posibles errores en el flujo de ejecución y se informa adecuadamente al usuario.

## Parte 2 - Clase Shape mejorada
