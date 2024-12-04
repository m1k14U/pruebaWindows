l=[]

"""
print(l)
l.append("Gabriela")
print(l)
a=input("Introduce un nombre: ")
l.append(a)
print(l)
"""
for i in range(0,5,1):
	#print("Soy Gabriela")
	#print(i)
	x = int(input("Dame un numero: ")) 
	l.append(x)
print(l)

s = sorted(l,reverse=True)
print(s)



