# Condicionales
## if
Permite la ejecucion de una declaración o un conjunto de declaraciones de acuerdo al valor de una expresión (evaluado en un contexto booleano).
```Python
if 20<30:
    print('20 es menor que 30')

# 20 es menor que 30
```
Python a diferencia de otros lenguajes de programación, usa la sangría (espacios en blanco) para definir el scope(alcance) del código mientras que lenguajes como C++ o Java que usan las llaves para su scope.
```Python
if 20<30:
print('20 es menor que 30')

"""  File "<stdin>", line 2
    print('20 es menor que 30')
        ^
IndentationError: expected an indented block"""
```
Vemos que el ejemplo anterior nos da un mensaje de error, ya que `print('20 es menor que 30')` debe estar dentro del bloque de la condición y para eso debemos darle un espaciado en blanco.

## elif
Esta palabra clave es similar a la acción que realiza el `else if` en otros lenguajes de programación. Se interpreta de la siguiente manera: *Si no cumple la condicion anterior, evalua esta condición.*
```Python
if 12>20:
    print('12 es mayor que 20')
elif 12<20:
    print('12 es menor que 20')

# 12 es menor que 20
```
## else
Esta palabra clave significa que si ninguna de las condiciones anteriores se ha cumplido, entonces que se cumpla la condición que esta posee.
```Python
if 12>20:
    print('12 es mayor que 20')
elif 12==20:
    print('12 es igual a 20')
else:
    print('12 es menor que 20')

# 12 es menor que 20
```
## Abreviatura "if"
Si solo se va a ejecutar un enunciado, podemos indicar la condicional en una sola linea.
```Python
if 12<30: print('12 es menor que 30')

# 12 es menor que 30
```
## abreviatura "if...else"
Si solo se tiene un enunciado con solo un if y un else, podemos indicarlo en una sola linea
```Python
print('12 es mayor que 30') if 12>30 else print('12 es menor que 30')
# 12 es menor que 30
```
## Operadores lógicos *or* y *and*
Estos operadores nos permiten combinar enunciados en la condicion.
```Python
# con el operador and, ambos enunciados tiene que ser verdaderos para que la condicion sea verdadera
if 12>2 and 40>1:
    print('ambos enunciados son verdaderos')

# ambos enunciados son verdaderos

# con el operador or, uno de ellos tiene que ser verdadero para que la condicion sea verdadera
if 12>20 or 2>1:
    print('uno de ellos es verdadero')

# uno de ellos es verdadero
```
***
Referencias:
- https://www.w3schools.com/python/python_conditions.asp