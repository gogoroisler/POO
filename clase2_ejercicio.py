import random

def calcular_notas():
    # Genero los cursos
    cantidad_cursos = int(input("Ingrese la cantidad de cursos a generar: "))
    
    # Genero la lista de notas de cada curso y la lista de promedios 
    notas_cursos = []
    promedios_cursos = []

    # Bucle for para ingresar la cantidad de alumnos por curso y que genere de manera aleatoria las notas de cada uno
    for i in range(cantidad_cursos):
        cantidad_alumnos = int(input(f"Ingrese la cantidad de alumnos del curso {i+1}: "))
        notas_curso = [random.randint(1, 10) for _ in range(cantidad_alumnos)]
        notas_cursos.append(notas_curso)
        print(f"Notas del curso {i+1}: {notas_curso}")
    
    # Dentro del bucle tambien calculamos el promedio del curso y asignamos el valor a la lista general    
        promedio = sum(notas_curso) / cantidad_alumnos
        promedios_cursos.append(promedio)
        print(f"Promedio del curso {i+1}: {promedio}")

    # Con la funcion max() recorremos la lista de promedios para buscar el mayor promedio. (+1 para la busqueda en el index y me indique cual es)
    curso_max_promedio = promedios_cursos.index(max(promedios_cursos))
    print(f"El curso con mayor promedio es el curso {curso_max_promedio + 1} con un promedio de {max(promedios_cursos)}")
    
    # Buscamos la nota mas alta por cada lista por cada curso y luego recorremos cada lista buscando la posicion de esa nota
    nota_maxima = max([max(notas_curso) for notas_curso in notas_cursos])
    for i, notas_curso in enumerate(notas_cursos):
        if nota_maxima in notas_curso:
            alumno_max_nota = notas_curso.index(nota_maxima)
            print(f"El alumno con mayor nota ({nota_maxima}) es el alumno {alumno_max_nota+1} del curso {i+1}")
            break
    
    return notas_cursos


calcular_notas()