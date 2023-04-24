import random
import string

class Password():
    __longitud = 8
    __caracteres_validos = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    def __init__(self, longitud = __longitud):
        self.longitud = longitud
        contraseña = self.generarPassword()

    @property
    def longitud(self):
        print("Obteniendo longitud...")
        return self.__longitud

    @longitud.setter
    def longitud(self,value):    
        print("Validando contraseña...")
        if value >= 6 and value <= 15:
            self.__longitud = value
            print("contraseña correcta")     
        else:
            raise ValueError("La longitud de la contraseña debe ser como minimo 6 caracteres y como maximo 15 caracteres")
    
    def generarPassword(self):
        return "".join(random.choice(Password.__caracteres_validos) for _ in range(self.longitud)) 
    
    


contraseña1 = Password(8)
print(contraseña1.__dict__)
print(contraseña1.longitud)
print(contraseña1.generarPassword())