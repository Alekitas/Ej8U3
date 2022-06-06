from Personal import Personal
class PersonalApoyo(Personal):
    __categoria=None
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,categoria):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad)
        self.__categoria=categoria

    def getcategoria(self):
        return self.__categoria
    
    def CalculoSueldo(self):
        importe=self.getsueldobasico()
        if self.__categoria >= '11' and self.__categoria <= '20':
            importe+=(self.__antiguedad/100)+(20/100)
        elif self.__categoria >= '21' and self.__categoria <= '22':
            importe+=(self.__antiguedad/100)+(30/100)
        return importe

    def __toJSON__(self):
        d=dict(__class__=self.__class__.__name__,
        __atributos__=dict(
            cuil=self.getcuil(),
            apellido=self.getapellido(),
            nombre=self.getnombre(),
            sueldobasico=self.getsueldobasico(),
            antiguedad=self.getantiguedad(),
            categoria=self.getcategoria()
            )
        )
        return d