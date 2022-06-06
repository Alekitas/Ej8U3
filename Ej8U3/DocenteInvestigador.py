from Docente import Docente
from Investigador import Investigador

class DocenteInvestigador(Docente,Investigador):
    __carrera=None
    __categoriaprograma=None
    __importeextra=None
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,cargo,catedra,areainvestig,tipoinvestig,carrera,categoriaprograma,importeextra):
        Docente.__init__(cuil,apellido,nombre,sueldobasico,antiguedad,cargo,catedra)
        Investigador.__init__(cuil,apellido,nombre,sueldobasico,antiguedad,areainvestig,tipoinvestig)
        self.__carrera=carrera
        self.__categoriaprograma=categoriaprograma
        self.__importeextra=importeextra

    def getcarrera(self):
        return self.__carrera

    def getcategoria(self):
        return self.__categoriaprograma

    def getimporteextra(self):
        return self.__importeextra
    
    def CalculoSueldo(self):
        return Docente.CalculoSueldo()+self.__importeextra
    
    def __str__(self):
        return 'Carrera: {} Categoria de programa: {} Importe Extra: {}'.format(self.__carrera,self.__categoriaprograma,self.__importeextra)
    
    def __toJSON__(self):
        d=dict(__class__=self.__class__.__name__,
        __atributos__=dict(
            cuil=self.getcuil(),
            apellido=self.getapellido(),
            nombre=self.getnombre(),
            sueldobasico=self.getsueldobasico(),
            antiguedad=self.getantiguedad(),
            cargo=self.getcargo(),
            catedra=self.getcatedra(),
            areainvestig=self.getareainvestig(),
            tipoinvestig=self.gettipoinvestig(),
            carrera=self.getcarrera(),
            categoriaprograma=self.getcategoria(),
            importeextra=self.getimporteextra()
            )
        )
        return d