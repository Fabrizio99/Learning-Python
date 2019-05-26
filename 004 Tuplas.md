# Tuplas
Las tuplas es una sequencia de objetos inmutables, son muy parecidos a los enlaces. Las tuplas no pueden cambiar los valores de sus elementos.
## Sintaxis
```Python
tupla = (1,2,'tres',4.0)
print(tupla)    #(1, 2, 'tres', 4.0)
```
Si deseamos recorrer los elementos de una tupla, podemos hacerlo con un ciclo for.
```Python
for x in tupla:
    print(x)

# 1
# 2
# tres
# 4.0
```
## Acceder a sus elementos
Para acceder a sus elementos, indicamos el indice en que se encuentra el elemento.
```Python
tupla[0]    #1
tupla[1:]  #(2, 'tres', 4.0)
```
Si deseamos saber si un elemento existe en una lista, podemos hacerlo con un condicional.
```Python
if 3 in tupla:
    print('Existe')
else:
    print('No existe')

# Resultado:    No existe
```

**Nota:**   
Como se menciono al principio, las tuplas no pueden cambiar los valores de sus elementos, por lo cual no podemos añadir, eliminar y eliminar elementos.

## Operaciones con Tuplas
### Longitud de una tupla
Podemos ver la cantidad de los elementos de una tupla, con el método `len()`
```Python
len(tupla)  #4
```
### Concatenar
Podemos concatenar tuplas con el operador `+`, creando una nueva tupla.
```Python
tupla2 = (5,6,7)
tupla+tupla2    #(1, 2, 'tres', 4.0, 5, 6, 7)
```
### Repetir elementos
Podemos repetir los elementos de una tupla con el operador `*`, creandose una nueva tupla.
```Python
tupla*2     #(1, 2, 'tres', 4.0, 1, 2, 'tres', 4.0)
```
## Métodos
Python tiene incorporados dos métodos que pueden ser usados con las tuplas.
### count()
Retorna el valor de la cantidad de veces que se repite un elemento(indicado como parámetro) en una tupla.
```Python
tupla.count(1)      #1
```
### index()
Retorna indice(indicado como parámetro) de un elemento de la tupla.
```Python
tupla.index('tres')     #2
```
***
Referencias:
- https://www.tutorialspoint.com/python/python_tuples.htm
- https://www.w3schools.com/python/python_tuples.asp