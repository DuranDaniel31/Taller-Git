"""
 Fecha 20/09/2023 
 Autor: Daniel Bedoya 
 Objetivo: Se requiere un software que calcule si un aprendiz tiene el estilo de aprendizaje Asimilador. 
 Para ello deben realizarse 7 preguntas de respuesta SI o NO.
 Si el aprendiz obtuvo 4 o más respuestas en SI
entonces el sistema deberá indicarle que es Asimilador, de lo contrario le dirá que su estilo de aprendizaje es otro.
"""

result = 0 
option1 =  int(input("Cuando aprendes algo nuevo, ¿prefieres que te presenten teorías o conceptos antes que ejemplos prácticos? \n 1.SI \n 2.NO \n"))
while option1 != 1 and option1 != 2:
    print ("Respuesta incorrecta")
    option1 = int(input("Digite 1. SI 2. NO "))
if option1 == 1: 
    result += 1

option2 =  int(input("¿Te sientes más cómodo aprendiendo a través de la lectura de libros o materiales escritos? \n 1.SI \n 2.NO \n "))
while option2 != 1 and option2 != 2:
    print ("Respuesta incorrecta")
    option2 = int(input("Digite 1. SI 2. NO "))
if option2 == 1: 
    result += 1

option3 =  int(input("¿Encuentras útil hacer esquemas, resúmenes o diagramas para organizar la información que estás aprendiendo? \n 1.SI \n 2.NO \n "))
while option3 != 1 and option3 != 2:
    print ("Respuesta incorrecta")
    option3 = int(input("Digite 1. SI 2. NO "))
if option3 == 1: 
    result += 1

option4 =  int(input("¿Te gusta analizar y reflexionar sobre las ideas y conceptos antes de ponerlos en práctica? \n 1.SI \n 2.NO \n "))
while option4 != 1 and option4 != 2:
    print ("Respuesta incorrecta")
    option4 = int(input("Digite 1. SI 2. NO "))
if option4 == 1: 
    result += 1



  