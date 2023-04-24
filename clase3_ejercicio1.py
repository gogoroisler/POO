#Funcion convertidor a segundos

def conv_segundos(horas, minutos, segundos):
    total_segundos = (horas*3600)+(minutos*60)+segundos
    return(total_segundos)
    
# Ingreso de informacion 

print("Introduce los datos del intervalo")
horas1 = int(input("ingresar horas : "))
minutos1 = int(input("ingresar minutos : "))
segundos1 = int(input("ingresar segundos : "))

# Salida
print("La cantidad de segundos del intervalo es ", conv_segundos(horas1,minutos1,segundos1))