"""for valor in range(5,21,3):
    print(valor)"""
"""
numeros = [10,20,30,40,50]

for indice, numero in enumerate(numeros):
    print(indice,numero)"""

"""def saludar(param1):
    print("Hola", param1)"""

def varios(param1,param2,*otros):
    print(param1)
    print(param2)
    for val in otros:
        print(val)
    print(type(otros))

"""varios(1,2)"""
"""varios(1,2,3)"""
varios(1,2,[3,"alumnos"],7)