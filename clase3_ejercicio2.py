# Funcion del ejercicio anterior

def conv_segundos(horas, minutos, segundos):
    total_segundos = (horas*3600)+(minutos*60)+segundos
    return(total_segundos)

# Funcion para pasar de segundos a horas, minutos y segundos

def conv_completo(segundos):
    seg_sob = segundos % 3600
    min = seg_sob // 60
    seg = seg_sob % 60
    hor = segundos // 3600
    return(hor, min, seg)

# Calculo de primer intervalo a segundos
    
print("Introduce los datos del primer intervalo")
horas1 = int(input("ingresar horas : "))
minutos1 = int(input("ingresar minutos : "))
segundos1 = int(input("ingresar segundos : "))

int1 = conv_segundos(horas1, minutos1, segundos1)
print("La cantidad de segundos del primer intervalo es ", conv_segundos(horas1,minutos1,segundos1))

# Calculo de segundo intervalo a segundos

print("Introduce los datos del segundo intervalo")
horas2 = int(input("ingresar horas : "))
minutos2 = int(input("ingresar minutos : "))
segundos2 = int(input("ingresar segundos : "))

int2 = conv_segundos(horas2, minutos2, segundos2)
print("La cantidad de segundos del segundo intervalo es ", conv_segundos(horas2,minutos2,segundos2))

# Suma de intervalos en segundos

segundosTot = int1 + int2

# Conversor de segundos a formato fecha con la funcion nueva y asignar variables a valores de hora, minuto y segundo
hor, min, seg = conv_completo(segundosTot)

# Print con formato
print("La duracion del intervalo total es de {} horas, {} minutos, {} segundos".format(hor,min,seg))