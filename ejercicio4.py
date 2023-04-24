numeros = []

for i in range(5):
    numero = int(input("Ingresa un numero: "))
    numeros.append(numero)

if len(numeros) == len(set(numeros)):
    print("SON TODOS DISTINTOS")
else:
    print("HAY DUPLICADOS")

print(len(numeros))
print(len(set(numeros)))

