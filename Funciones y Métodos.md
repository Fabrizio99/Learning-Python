# Funciones y Métodos
## `max()`
Es un método que retorna los elementos de una lista con el valor máximo.
```Python
lista=[1,4,9,2,3]
max(lista)  #9
lista2=['C++','Python','JavaScript']
max(lista2) #'Python'
```
Supongamos el caso que tenemos una lista con números, pero todos con tipo de dato `String`.
```Python
lista=['1','10','2']
max(lista)  #'2'
```
Vemos que retorna 2, pero 10 es el mayor. Lo que pasa es que al ser de tipo de dato `String`, el criterio de comparación es lexicográfico, quiere decir, compara los valores ASCII de los caracteres. Como el valor ASCII de 2 (50) es mayor que el de 1 (49), el mayor de la lista es `'2'`.   
Si queremos comparar números con tipo de dato `String`, debemos transformar los elementos a enteros.
Podemos realizar esto gracias a la palabra clave `key`, ésta es una función lambda que nos va a permitir definir como se va a determinar al elemento máximo.    
**Nota:** Preferible haber leido la sección Lambda.
```Python
lista = ['1', '10', '2', '25', '3']
max(lista, key=lambda x: int(x))    #'25'
```
**Explicación:**
Definimos a `key` como una función lambda, donde toma el parámetro `x` y este transformara a `x` en un tipo de dato entero, permitiendo que se haga una comparación de cada elemento de la lista en su tipo entero.

## `translate()`
Función que crea un nuevo `String` pudiendose reemplazar los valores de cada caracter.
En la tabla de traducción, se debe indicar indicar el caracter que se desea cambiar y el valor que va a tomar, pero se realiza de la siguiente manera.
- Ordinal Unicode del caracter a cambiar -> el Ordinal Unicode del nuevo valor.
- Ordinal Unicode del caracter a cambiar -> la letra misma del nuevo valor.
- Ordinal Unicode del caracter a cambiar -> none (eliminar el caracter).

La tabla de traducción se crea usando la función `maketrans()` o hacerlo manualmente mediante diccionarios.
La función `maketrans()` puede tomar hasta 3 argumentos.
- Si solo tiene **1 argumento**, esta debe ser un diccionario donde se indique el Ordinal Unicode hacia otro Ordinal Unicode, `String` o `None`.
```Python
# de ordinal Unicode hacia ordinal Unicode
cadena = "abcdef"
traduccion = cadena.maketrans({ord('a') : ord('A')})
nuevaCadena = cadena.translate(traduccion)
nuevaCadena #'Abcdef'

# de ordinal Unicode hacia String
cadena = "abcdef"
traduccion = cadena.maketrans({ord('a') : 'A'})
nuevaCadena = cadena.translate(traduccion)
nuevaCadena #'Abcdef'

# de ordinal Unicode hacia None
cadena = "abcdef"
traduccion = cadena.maketrans({ord('a') : None})    # None permite eliminar el caracter
nuevaCadena = cadena.translate(traduccion)
nuevaCadena #'bcdef'
```
Para entender más del método `ord` visitar https://www.programiz.com/python-programming/methods/built-in/ord

- Si se tiene **2 argumentos**, estos deben ser de tipo `String` de igual longitud. Cada caracter en la posicion "x" de la primera cadena será reemplazado por el caracter en la posición "x" de la segunda cadena.
```Python
cadena="pythom"
traduccion = cadena.maketrans('pm','Pn')
nuevaCadena = cadena.translate(traduccion)
nuevaCadena #'Python'
```
- Si se tiene **3 argumentos**, el tercer argumento es un `String` donde todos sus caracteres pertenecientes se le asignaran a nulo (None).
```Python
cadena = "abcde"
traduccion = cadena.maketrans('ac','AC','ade')
nuevaCadena = cadena.translate(traduccion)
nuevaCadena #'bC'
```
Primero `'a'` es reeemplazado por `'A'` y luego este és reemplazado a `None` ya que `a` se encuentra en el tercer argumento, lo mismo pasa con la letra `'c'`. `'d'` y `'e'` también son convertidos a `None` debido a que estos son caracteres del tercer argumento.
***
References:
- https://www.tutorialspoint.com/python3/list_max.htm
- https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression
- https://docs.python.org/3/howto/sorting.html
- https://www.journaldev.com/23697/python-string-translate