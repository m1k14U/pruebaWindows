def suma(a,b):
    r = a + b
    print(r)

def Chicharronera(a,b,c):
    r1 = -b + (b**2-4*a*c)**(0.5)/2*a
    r2 = -b - (b**2-4*a*c)**(0.5)/2*a
    print("Las raíces son ",r1,r2)

def SaludoTerrestre():
    n=str(input("Introduce tu nombre: "))
    print("Hola ", n,"! es un placer conocerte")
    s = ["México","Brasil","Argentina","Colombia"]
    pp = str(input("¿De qué país vienes? "))
    if pp in s:
        print("Tu pais se encuentra dentro de mi base de datos, amo ese país")
    else:
        print("Lo siento, al parecer tu país no se encuentra dentro de mi base de datos :/!")



suma(3,4)
Chicharronera(1,-3,9)
Chicharronera(2,4,5)
suma(5,6)
suma(1000,3435)
SaludoTerrestre(a)



"""
#Ejercicio 2
class Cuenta:
	def __init__(self, titular="", cantidad=0.0):
		self.titular=titular
		self.cantidad=cantidad

	def set_titular(self,titular):
		self.titular=titular
	def get_titular(self):
		return self.titular
	def set_cantidad(self,cantidad):
		self.cantidad=cantidad 
	def get_cantidad(self):
		return self.cantidad
	def Mostrar(self):
		print("Titular:",self.titular)
		print("Cantidad: $",self.cantidad)
	def ingresar(self,cantidad):
		if cantidad > 0:
			self.cantidad+=cantidad 
		else:
			pass
	def retirar(self,cantidad):
		self.cantidad-=cantidad 

# p1=Cuenta("Miguel")
# p1.Mostrar()
# p1.ingresar(2500)
# p1.retirar(500)
# p1.Mostrar()


#Ejercicio 3
class CuentaJoven(Cuenta):
	def __init__(self, bonificacion=10):
		super().__init__()
		self.__bonificacion = bonificacion

	def TitularValido(self,edad):
		if edad > 18 and edad < 25:
			return True
		else:
			return False
	def Aumento(self):
		self.cantidad = self.cantidad + self.cantidad*self.__bonificacion/100
	def Mostrar(self):
		print("Cuenta Joven")
		print("Titular: ", self.titular)
		print("Monto: ",self.cantidad)
		print("Bonificacion del",self.__bonificacion,"%")

p3=CuentaJoven(30)
p3.set_titular("Alberto")
p3.set_cantidad(4000)
p3.Mostrar()
p3.Aumento()
p3.Mostrar()





PROYECTO!!!
import random
palabras={1:"farmaco",
          2:"inteligencia",
          3:"positivismo",
          4:"derrota",
          5:"otorrinolaringologo",
          6:"pilares",
          7:"analograma",
          8:"deshidrogenacion"}

class Ahorcado:
    __select = 0
    def __init__(self):
        self.palabra=""
        self.longitud=0
        self.aciertos=0
        self.errores=0
        self.letras_supuestas=[]
        self.limite=6
    
    def fijarPalabra(self):
        self.__select=random.randint(1,8) 
        self.palabra=palabras[self.__select]
        self.longitud = len(self.palabra)
        """
    