# Funciones
Una función es un bloque de código que se ejecuta una vez que es llamado.
```Python
# Sintaxis
def nombreFuncion():
    bloqueDeCodigo

# Ejemplos
def mensajeHolaMundo():
    print('Hola mundo')
# Si queremos llamar a una función, escribimos su nombre juntos a los paréntesis
mensajeHolaMundo()      # Hola mundo
```
## Parámetro
Es la información que se le puede pasar a una función mediante paréntesis, se puede ingresar cualquier cantidad de parámetros pero separado por comas.
```Python
def mensaje(pais):
print('Soy de '+pais)

mensaje('Peru')         # Soy de Peru
mensaje('Inglaterra')   # Soy de Inglaterra
```
### Valor de parámetro por defecto
Si llamamos a una función sin parámetro, nos va a permitir usar el valor por defecto.
```Python
def imprimirDatosTrabajador(nombre, salario=1000):
    print('Nombre:',nombre,', sueldo:',salario)

imprimirDatosTrabajador('Fabrizio') # Nombre: Fabrizio , sueldo: 1000
```
## Retornar un valor
La palabra clave `return` permite retornar un valor en una función.
```Python
def suma(numero1,numero2):
    return numero1+numero2  # retornara el valor de la suma de numero1 y numero2

print(suma(1,2))    # 3
```
***
Referencias:
- https://www.w3schools.com/python/python_functions.asp