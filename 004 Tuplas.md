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
Como se menciono al principio, las tuplas no pueden cambiar los valores de sus elementos, por lo cual no podemos cambiar sus valores y/o eliminarlos.

## Operaciones con Tuplas
