import abc
from abc import ABC
class Personal(ABC):
    __cuil=None
    __apellido=None
    __nombre=None
    __sueldobasico=None
    __antiguedad=None
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldobasico=sueldobasico
        self.__antiguedad=antiguedad

    def getcuil(self):
        return self.__cuil

    def getapellido(self):
        return self.__apellido 

    def getnombre(self):
        return self.__nombre

    def getsueldobasico(self):
        return self.__sueldobasico

    def getantiguedad(self):
        return self.__antiguedad
        
    def setantiguedad(self, value):
        self.__antiguedad = value
    
    def __gt__(self,otro):
        if isinstance(otro,Personal):
            return self.__nombre < otro.getnombre()

    def __str__(self):
        return 'Cuil: {} Apellido: {} Nombre: {} SueldoBasico: {} Antiguedad: {}'.format(self.__cuil,self.__apellido,self.__nombre,self.__sueldobasico,self.__antiguedad)
    
    @abc.abstractclassmethod
    def CalculoSueldo(self):
        pass