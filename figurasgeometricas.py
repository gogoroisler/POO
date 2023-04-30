from abc import abstractmethod, ABC
import math

class FiguraGeometrica(ABC):

    def __init__(self, color_fondo, color_borde) -> None:
        self.color_fondo = color_fondo
        self.color_borde = color_borde
    
    @property
    def color_fondo(self):
         return self.__color_fondo
    
    @color_fondo.setter
    def color_fondo(self, value):
         self.__color_fondo = value
        
    @property
    def color_borde(self):
         return self.__color_borde
    
    @color_borde.setter
    def color_borde(self, value):
         self.__color_borde = value
    
    def colores(self):
         print(f"El color de los bordes de este {self.__class__.__name__} es {self.color_borde} y el del fondo es {self.color_fondo}")
    
    @abstractmethod 
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Rectangulo(FiguraGeometrica):
    def __init__(self, color_fondo, color_borde, largo, ancho):
        super().__init__(color_fondo, color_borde)
        self.largo = largo
        self.ancho = ancho
        print("Se ha creado el rectangulo")
    
    @property
    def largo(self):
         return self.__largo
    
    @largo.setter
    def largo(self, value):
         self.__largo = value
    
    @property
    def ancho(self):
         return self.__ancho    
    
    @ancho.setter
    def ancho(self, value):
         self.__ancho = value

    def area(self):
        area = self.largo*self.ancho;
        print("el area del rectangulo es igual a ", area);

    def perimetro(self):
        perimetro = (self.largo *2) + (self.ancho*2);
        print("el perimetro del rectangulo es igual a ", perimetro);

class Circulo(FiguraGeometrica):
        def __init__(self, color_fondo, color_borde, radio):
            super().__init__(color_fondo, color_borde)
            self.radio = radio
            print("Se ha creado el circulo")
        
        @property
        def radio(self):
            return self.__radio
    
        @radio.setter
        def radio(self, value):
            self.__radio = value
    
        def area(self):
            area = "{:.2f}".format(math.pi * self.radio**2)
            print("el area del circulo es igual a ", area)

        def perimetro(self):
            perimetro = "{:.2f}".format(2*math.pi * self.radio)
            print("el perimetro del circulo es igual a ", perimetro)

class Triangulo(FiguraGeometrica):
        def __init__(self, color_fondo, color_borde, l1, l2, l3):
            super().__init__(color_fondo, color_borde)
            self.l1 = l1
            self.l2 = l2
            self.l3 = l3
            print("Se ha creado el triangulo")

        @property
        def l1(self):
            return self.__l1
    
        @l1.setter
        def l1(self, value):
            self.__l1 = value
        
        @property
        def l2(self):
            return self.__l2
    
        @l2.setter
        def l2(self, value):
            self.__l2 = value
        
        @property
        def l3(self):
            return self.__l3
    
        @l3.setter
        def l3(self, value):
            self.__l3 = value
    
        def area(self):
            semiPerim = (self.l1 + self.l2 + self.l3) / 2
            area = "{:.2f}".format(math.sqrt(semiPerim*(semiPerim - self.l1)*(semiPerim-self.l2)*(semiPerim-self.l3)))
            print("el area del triangulo es igual a ", area)

        def perimetro(self):
            perimetro = self.l1+self.l2+self.l3;
            print("el perimetro del rectangulo es igual a ", perimetro)

r1 = Rectangulo("rojo","verde",5,3);
c1 = Circulo("amarillo","indigo",8);
t1 = Triangulo("blanco","azul",5,3,7);

r1.colores()
r1.perimetro()
r1.area()

c1.colores()
c1.perimetro()
c1.area()

t1.colores()
t1.perimetro()
t1.area()
