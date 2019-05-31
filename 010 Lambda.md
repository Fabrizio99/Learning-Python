# Lambda
Una función lambda es una función anonima, puede tomar cualquier cantidad de argumentos pero solo puede tener una expresión.
```Python
# Sintaxis
lambda argumentos : expresion
```
**Nota:** Toda función lambda puede transformarse a una función creada con la palabra clave `def` pero no sucede lo mismo inversamente, debido a que una función lambda solo puede tener una sola expresion.
```Python
def funcionPotencia(numero):
    return numero**2

potenciaCuadrado = lambda x: x**2

print(potenciaCuadrado(2))  # 4
print(funcionPotencia(3))   # 6
```
Vemos que `potenciaCuadrado` poseen la misma función que `funcionPotencia()`, pero escrita de una manera más simplificada.
## Uso de lambdas
- Podemos ver un uso de las funciones lambdas cuando las usamos dentro de una función.
    ```Python
    def suma(a):
        return lambda b:a+b
    
    valor1=suma(2)  # "a" toma el valor de 2
    print(valor1(3))    # "b" toma el valor de 3
    ```
    Primero indicamos que `valor1=suma(2)`, haciendo que `a` tome el valor de 2, pero no se ha indicado el valor de `b` por lo cual si imprimimos `valor1` nos retornará la función lambda.
    ```Python
    print(valor1)   #<function suma.<locals>.<lambda> at 0x033C9468>
    ```
    Luego indicamos que valor1(3), así indicandole el valor de `b`, por lo cual retornará el valor de la función lambda ya que tiene tanto los valores de `a` y `b` que necesita, por eso al imprimir retorna el valor de la función lambda.

***
Referencias:
- https://www.w3schools.com/python/python_lambda.asp
- https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/