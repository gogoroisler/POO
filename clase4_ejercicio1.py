class Persona:
    
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        print("La persona creada tiene:\n", "nombre: "
        , nombre,"\n edad: ", edad, "\n dni: ", dni)
    
    def mostrar_edad(self):
        print(self.nombre, "tiene", self.edad, "años") 
        
    
    def es_mayor_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
    
    