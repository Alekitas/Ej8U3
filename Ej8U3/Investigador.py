from Personal import Personal
class Investigador(Personal):
    __areainvestig=None
    __tipoinvestig=None
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,areainvestig,tipoinvestig):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad)
        self.__areainvestig=areainvestig
        self.__tipoinvestig=tipoinvestig

    def getareainvestig(self):
        return self.__areainvestig

    def gettipoinvestig(self):
        return self.__tipoinvestig

    def CalculoSueldo(self):
        importe=self.getsueldobasico()
        return importe+(self.__antiguedad/100)

    def __str__(self):
        return 'Area de investigacion: {} Tipo de investigacion: {}'.format(self.__areainvestig,self.__tipoinvestig)

    def __toJSON__(self):
        d=dict(__class__=self.__class__.__name__,
        __atributos__=dict(
            cuil=self.getcuil(),
            apellido=self.getapellido(),
            nombre=self.getnombre(),
            sueldobasico=self.getsueldobasico(),
            antiguedad=self.getantiguedad(),
            areainvestig=self.getareainvestig(),
            tipoinvestig=self.gettipoinvestig()
            )
        )
        return d