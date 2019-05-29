# Bucles
Sabemos que la ejecucion de instrucciones se dan de manera secuencial pero un buble permite que se ejecute una o un bloque de instrucciones multiple veces.
## While
El bucle `while` puede ejecutar un conjunto de instrucciones hasta que la condicion que tenga sea verdadera
```Python
while condicion:
    conjunto de instrucciones

# mientras se cumpla la condicion, se ejecutara el conjunto de instrucciones

#Ejemplo
i=1
while i<10:
    print(i)
    i+=1
```
Tener en cuenta que en el ejemplo anterior tenemos que hacer que la variable `i` cambie de valor (en este caso aumente en 1, hasta llegar a 10) sino se va a producir un bucle infinito.
### break
La instruccion `break` nos permite interrumpir la ejecucion del bucle, incluso si la condición es verdadera.
```Python
i=1
while i<10:
    print(i)
    if i==6:
        break   #cuando i sea igual a 6 con la instruccion break se interrumpirá el bucle
    i+=1

#1
#2
#3
#4
#5
#6
```
### continue
La instruccion `continue` interrumpe la iteración actual, y va a la siguiente.
```Python
i=0
while i<10:
    i+=1
    if i==6:
        continue
    print(i)

# 1
# 2
# 3
# 4
# 5
# 7
# 8
# 9
# 10
```
## for
Este bucle es utilizado para iterar sobre una secuencia como listas, tuplas, diccionarios, conjuntos o cadenas de texto.
Este tipo de bucle no es similar al bucle `for` que existe en otro lenguajes de programación como C++, Java.
```Python
lista=[1,2,3,4,5]
for x in lista:
    print(x)

# 1
# 2
# 3
# 4
# 5
```
Podemos hacer lo mismo con las cadenas de texto.
```Python
for x in 'python':
    print(x)

# p
# y
# t
# h
# o
# n
```
**Nota**    
Podemos usar las instrucciones `break` y `continue` en el bucle for.
```Python
paises=['peru','argentina','chile','brasil']
for x in paises:
    print(x)
    if x=='chile':
        break
# peru
# argentina
# chile

for x in paises:
    if x=='chile':
        continue
    print(x)
# peru
# argentina
# brasil
```
### range()
Es una función que retorna una secuencia de números, comenzando desde cero incrementandose en 1 y termina en un determinado número (indicado como parámetro).
```Python
for x in range(10):
    print(x)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```
Podemos cambiarle el valor inicial e incremento de la secuencia.
```Python
# Estructura
range(valorInicial,valorFinal,incremento)

# Ejemplo
for x in range(3,11,2):
    print(x)
# 3
# 5
# 7
# 9
```
### else
Podemos usar la palabra clave `else` en este tipo de bucle para indicar que se ejecute una instrucción cuando el bucle finalice.
```Python
for x in range(5):
    print(x)
else:
    print('Números del 0 al 4')
# 0
# 1
# 2
# 3
# 4
# Números del 0 al 4
```
***
Referencias:
- https://www.w3schools.com/python/python_while_loops.asp
- https://www.tutorialspoint.com/python/python_loops.htm
