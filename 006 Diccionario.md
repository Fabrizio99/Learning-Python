# Diccionario
Es una colección que no esta ordenada pero sí indexada, además que sus elementos son mutables. Se escriben entre llaves y esta conformada por palabras clave y sus valores.
```Python
diccionario={'nombre':'Fabrizio','edad':20}
print(diccionario)  #{'nombre': 'Fabrizio', 'edad': 20}
```
Podemos acceder a sus elementos gracias a las palabras clave.
```Python
print(diccionario['nombre'])    #'Fabrizio'
```
o podemos usar el metodo `get()`, resultando lo mismo
```Python
print(diccionario.get('edad'))  #20
```
## Elementos del diccionario
Podemos cambiar el valor de un elemento especificando su palabra clave.
```Python
diccionario['nombre']='Raul'
print(diccionario)  #{'nombre': 'Raul', 'edad': 20}
```
Tambien podemos acceder a los elementos de un diccionario con el ciclo *for*.
```Python
for elemento in diccionario:
    print(elemento,": ", diccionario[elemento])

# nombre :  Raul
# edad :  20
```
Podemos iterar solo los valores de los elementos del diccionario con el método `values()`
```Python
for elemento in diccionario.values():
    print(elemento)

# Raul
# 20
```
o iterar las palabras claves y los valores de los elementos con el método `items()`
```Python
for palabra_clave,elemento in diccionario.items():
    print(palabra_clave,elemento)

# nombre Raul
# edad 20
```
## Longitud
Para obtener la longitud de un diccionario, usamos el método `len()`
```Python
len(diccionario)    #2
```
## Añadir elementos
Para añadir un elementos, solo se debe escribir una nueva palabra clave con su valor.
```Python
diccionario['pais'] = 'Perú'
print(diccionario)  #{'nombre': 'Raul', 'edad': 20, 'pais': 'Perú'}
```
## Eliminar elementos
Existen distintos tipos de métodos:
- `pop()`
    ```Python
    diccionario.pop('nombre')
    'Raul'
    print(diccionario)  #{'edad': 20, 'pais': 'Perú'}
    ```
- `popitem()`  
    Elimina el último elemento.
    ```Python
    diccionario = {'nombre': 'Raul', 'edad': 20, 'pais': 'Perú'}
    diccionario.popitem()   #('pais', 'Perú')
    print(diccionario)  #{'nombre': 'Raul', 'edad': 20}
    ```
- del
    ```Python
    diccionario = {'nombre': 'Raul', 'edad': 20, 'pais': 'Perú'}
    del diccionario['edad']
    print(diccionario)  #{'nombre': 'Raul', 'pais': 'Perú'}
    ```
    Si no colocamos la palabra clave del elemento, se elimina el diccionario completo.
    ```Python
    diccionario = {'nombre': 'Raul', 'edad': 20, 'pais': 'Perú'}
    del diccionario
    print(diccionario)
    """Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'diccionario' is not defined"""
    ```
- `clear()`
    Este método vacía el diccionario, no lo elimina.
    ```Python
    diccionario = {'nombre': 'Raul', 'edad': 20, 'pais': 'Perú'}
    diccionario.clear()
    print(diccionario)  #{}
    ```
## Copiar un diccionario
Para copiar un diccionario, usamos el método `copy()`. 
No podemos simplemente crear un segundo diccionario e igualarlo al que ya existe (primero)ya que produciria un enlace al primer diccionario, si cambiaramos algun elemento del primer diccionario entonces tambien cambiaria el segundo debido que estan enlazados.
```Python
diccionario = {'nombre': 'Raul', 'edad': 20, 'pais': 'Perú'}
diccionario2=diccionario.copy()
print(diccionario2) #{'nombre': 'Raul', 'edad': 20, 'pais': 'Perú'}
```
***
Referencias:
- https://www.w3schools.com/python/python_dictionaries.asp