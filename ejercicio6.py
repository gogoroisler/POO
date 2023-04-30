import random
import string

class Password():
    __longitud = 8
    __caracteres_validos = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    def __init__(self, longitud = __longitud):
        self.longitud = longitud
        self.__contraseña = self.generarPassword()

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
    
    @property
    def contraseña(self):
        return self.__contraseña
    
    @contraseña.setter
    def contraseña(self, value):
        self.__contraseña = value

    def esFuerte(self):
        mayusculas = 0
        minusculas = 0
        numeros = 0
        especiales = 0
        
        for i in self.__contraseña:
            if i.isupper():
                mayusculas += 1
            elif i.islower():
                minusculas += 1
            elif i.isdigit():
                numeros += 1
            elif i in Password.__CARACTERES_VALIDOS:
                especiales += 1
        return mayusculas > 1 and minusculas > 1 and numeros > 1 and especiales > 1

    def generarPassword(self):
        return ''.join(random.choice(Password._CARACTERES_VALIDOS) for i in range(self._longitud))

    def main():
        Passwords=[]
        contraseñas_creadas=int(input("Ingrese cuantas contraseñas desea crear "))
        for contras in range(contraseñas_creadas):
            longitud=int(input("Ingrese cuantos caracteres tendra la contraseña "))
            if longitud ==0:
                longitud= 8
            contraseña_nueva=Password(longitud)
            Passwords.append(contraseña_nueva)
        for i, contraseña in enumerate(Passwords):
            print(f"Password {i+1}: {contraseña}")

    main()

