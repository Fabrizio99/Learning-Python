# Listas
Las listas es Python es una estructura de dato, es similar a los arreglos de otros lenguajes de programación (C++, Java,etc). Ésta nos permite almacenar elementos de distintos tipos.
```Python
x=[1,'2',[3,4],5.0] #lista con elementos enteros, cadenas de texto, flotantes e incluso tiene una lista dentro de esta
```
Para ingresar a un elemento de la lista, podemos hacerlo indicando su indice (recuerde que el primer elemento posee el indice 0 no 1).
```Python
print(x[0])     #1
print(x[2])     #[3,4]
```

## Métodos
### `append()`
Nos permite agregar un elemento a la lista
```Python
x.append(6)
print(x)    #[1,'2',[3,4],5.0,6] 
x.append([7,8])
print(x)    #[1,'2',[3,4],5.0,6,[7,8]]
```
Se puede apreciar que al agregar varios elementos, estas se agregan como si fueran un solo elemento.
### extend()
Nos permite agregar elementos como `append()`, la diferencia es que si se agrega una lista de elementos, no se agregan como si todas fueran un solo elemento, sino que cada uno se agrega como un elemento en la lista.
```Python
x.extend([9])
print(x)    # [1,'2',[3,4],5.0,6,[7,8],9]
x.extend([10,11])
print(x)    # [1,'2',[3,4],5.0,6,[7,8],9,10,11]
```
### remove()
Permite remover el elemento que le indiquemos como parámetro.
```Python
x.remove(9)
print(x)    #[1,'2',[3,4],5.0,6,[7,8],10,11]
```
### index()
retorna el indice que le pasemos por parámetro
```Python
x.index('2')    #1
```
### count()
retorna el valor de cuantas veces se repite un elemento en la lista
```Python
x.extend([1,1])
print(x)    # [1,'2',[3,4],5.0,6,[7,8],10,11,1,1]
x.count(1)  # 3
```
### reverse()
Invierte los elemento de la lista original
```Python
x.reverse()
print(x)    #[1, 1, 11, 10, [7, 8], 6, 5.0, [3, 4], '2', 1]
```
***
Referencia: https://devcode.la/tutoriales/listas-python/
