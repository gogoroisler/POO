
class ListaDeTareas():
    
    def __init__(self):
        self.__lista_tarea = []

    def agregarTarea(self, tarea):
        if tarea in self.__lista_tarea:
            print("La tarea no fue agregada a la lista")
        else:
            self.__lista_tarea.append(tarea) 
            print("La tarea agregada correctamente a la lista")

    def quitarTarea(self,tarea):
        if tarea in self.__lista_tarea or tarea == self.__lista_tarea:
            self.__lista_tarea.remove(tarea)
            print("Tarea eliminada correctamente de la lista")
        else:
            print("La tarea no fue eliminada de la lista")

    def mostrarTarea(self):
        print(self.__lista_tarea) 

lista1 = ListaDeTareas()

lista1.agregarTarea("Tarea 1")

lista1.quitarTarea("Tarea 2")

lista1.mostrarTarea()