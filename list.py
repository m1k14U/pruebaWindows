l=["rojo","azul","verde","gris","negro","cafe","amarillo"]
print(l)
print(l[2])
print(l[-1])
print(l[-2])
l[3]="blanco"
l[6]="morado" 
print(l)

print(l.index("negro"))
del(l[5])
#l.remove("cafe")
print(l.count("rojo"))
print(l)
l2=["dorado","violeta","naranja","carnita","rosa"]
l.extend(l2)
print(l)

print(l[0:3])
print(l[4:])
print(l[:4]) 