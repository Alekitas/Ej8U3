from Personal import Personal
class Docente(Personal):
    __cargo=None
    __catedra=None
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,cargo,catedra):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad)
        self.__cargo=cargo
        self.__catedra=catedra

    def getcargo(self):
        return self.__cargo

    def getcatedra(self):
        return self.__catedra

    def CalculoSueldo(self):
        importe=self.getsueldobasico()
        if self.__cargo=="simple":
            importe+=(self.__antiguedad/100)+(10/100)
        elif self.__cargo=="semiexclusivo":
            importe+=(self.__antiguedad/100)+(20/100)
        elif self.__cargo=="exclusivo":
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
            cargo=self.getcargo(),
            catedra=self.getcatedra()
            )
        )
        return d