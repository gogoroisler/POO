numeros = []

for i in range(5):
    numero = int(input("Ingresar numero: "))
    numeros.append(numero)

max = max(numeros)
min = min(numeros)

print("El numero mas grande es:", max)
print("El numero mas chico es:", min)