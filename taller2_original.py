# TALLER 2 PYTHON
#AUTOR(A): JUAN CAMILO PEREZ
#FECHA: 07 OCTUBRE 2022
from datetime import date
hoy = date.today()	#fecha actual
print("Hoy es el dia: ", hoy)
a=int(input("digite	el	primer	número:	"))
b=int(input("digite	el	segundo	número:	"))
c=int(input("digite	el	tercer	número:	"))
x = [a, b, c]
print ("El valor maximo es: ", max(x))
print ("El valor mínimo es: ", min(x))
print ("La suma de los 3 numeras es: ", sum(x))
print()
z=float(input("digite un número con decimales: "))
redondo=round(z)
print ("El valor de ", z, "redondeado es: ", redondo)
print()
frase=input("digite una oración: ")
print("La frase en mayuscula es: ", frase.upper())
print("La frase en mlnuscula es: ", frase.lower())
print("La frase con mayuscula inicial es: ", frase.capitalize())
print("La frase con palabras en mayusculas es: ", frase.title())
print("La longitud de la frase es: ", len(frase), "caracteres")
print()
print("FIN")
