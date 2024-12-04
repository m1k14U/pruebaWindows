a=int(input("Introduce un número: "))
b=int(input("Introduce un número: "))
#a=(input("Introduce un número: "))
#b=(input("Introduce un número: "))
print(type(a))
print(type(b))
z = a+b
w = a**2

x = str(z)
y = str(w)
if z > w:
	print("El resultado es más grande, observa: z= "+x+" y a**2= "+y)
elif z== w:
	print("Las variables son iguales")
else: 
	print("El operador es más grande")
