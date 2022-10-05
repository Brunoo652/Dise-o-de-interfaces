#import os

opcA="A"
opcB="B"
opcC="C"
result=" " 
puntuFinal=0
puntoPos=10
puntuNeg=5

print("Responde a la siguiente pregunta (1/3): ")
print("De que color es el cielo?")
print("A.-Amarillo")
print("B.-Azul")
print("C.-Verde")
result= input()
while result != opcB :
	print("Respuesta incorrecta. Prueba otra opcion")
	puntuFinal= puntuFinal-puntuNeg
	result= input()
	
print("Respuesta Correcta")
puntuFinal=puntuFinal+puntoPos


print("Responde a la siguiente pregunta (2/3): ")
print("Cuanto es 2+2?")
print("A.-4")
print("B.-5")
print("C.-1")
while result != opcA :
	print("Respuesta incorrecta. Prueba otra opcion")
	puntuFinal= puntuFinal-puntuNeg
	result= input()

print("Respuesta Correcta")
puntuFinal=puntuFinal+puntoPos

print("Responde a la siguiente pregunta (3/3): ")
print("En que año se inició la revolución francesa?")
print("A.-1492")
print("B.-1910")
print("C.-1789")
result= input()
while result != opcC :
	print("Respuesta incorrecta. Prueba otra opcion")
	puntuFinal= puntuFinal-puntuNeg
	result= input()
	
print("Respuesta Correcta")
puntuFinal=puntuFinal+puntoPos

#imprimir puntuación final
print("Puntuación final: "+puntuFinal)