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
***
Referencias:
- https://www.w3schools.com/python/python_while_loops.asp
- https://www.tutorialspoint.com/python/python_loops.htm
