a = int(input("Ingresa un número: "))
l=[]
for i in range(0,a+1,1):
	if i == 0:
		pass
	elif i == 1:
		pass
	elif i == 2:
		l.append(i)
	elif i == 3:
		l.append(i)
	elif i == 5:
		l.append(i)
	elif i == 7:
		l.append(i) 
	elif i%2 != 0 and i%3 != 0 and i%5 !=0 and i%7 !=0:
		l.append(i)

print("Estos son los números primos: ",l)





