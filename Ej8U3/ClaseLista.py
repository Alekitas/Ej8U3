from zope.interface import interface
from zope.interface import implementer
from Interface import Interface
from ClaseNodo import Nodo
from Personal import Personal
from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
from PersonalApoyo import PersonalApoyo

@implementer(Interface)
class ListaProgramador():
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0

    def __init__(self)->None:
        self.__comienzo=None
        self.__actual=None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            Personal=self.__actual.getPersonal()
            self.__actual=self.__actual.getSiguiente()
            return Personal

    def AgregarElemento(self,elemento):
        unNodo=Nodo(elemento)
        unNodo.setSiguiente(self.__comienzo)
        self.__comienzo=unNodo
        self.__actual=unNodo
        self.__tope+=1

    def InsertarElemento(self,elemento,pos):
        aux=self.__comienzo
        ant=None
        i=1
        while aux!=None and i<=pos:
            if pos==i:
                self.AgregarElemento(elemento)
            else:
                unNodo=Nodo(elemento)
                unNodo.setSiguiente(aux)
                ant.setSiguiente(unNodo)
            i+=1
            ant=aux
            aux=aux.getSiguiente()

    def CrearAgente(self,elemento):
        unAgente=None
        if elemento!=None:
            if elemento=="docente":
                unAgente=Docente(input('\nIngrese cuil:'),input('\nIngrese apellido: '),input('\nIngrese nombre: '),input('\nIngrese sueldo basico: '),input('\nIngrese antiguedad: '),input('\nIngrese cargo: '),input('\nIngrese catedra: '))
            elif elemento=="docente investigador":
                unAgente=DocenteInvestigador(input('\nIngrese cuil:'),input('\nIngrese apellido: '),input('\nIngrese nombre: '),input('\nIngrese sueldo basico: '),input('\nIngrese antiguedad: '),input('\nIngrese cargo: '),input('\nIngrese catedra: '),input('\nIngrese area de investigacion: '),input('\nIngrese tipo de investigacion: '),input('\nIngrese carrera: '),input('\nIngrese categoria de programa: '),input('\nIngrese importe extra por Docencia e Investigacion: '))
            elif elemento=="investigador":
                unAgente=Investigador((input('\nIngrese cuil:'),input('\nIngrese apellido: '),input('\nIngrese nombre: '),input('\nIngrese sueldo basico: '),input('\nIngrese antiguedad: '),input('\nIngrese cargo: '),input('\nIngrese catedra: '),input('\nIngrese area de investigacion: '),input('\nIngrese tipo de investigacion: ')))
            elif elemento=="personal de apoyo":
                unAgente=PersonalApoyo(input('\nIngrese cuil:'),input('\nIngrese apellido: '),input('\nIngrese nombre: '),input('\nIngrese sueldo basico: '),input('\nIngrese antiguedad: '),input('\nIngrese categoria: '))
        else:
            print('\n--ERROR EN ELEMENTO ENVIADO--\n')
        return (unAgente)
    
    def MostrarTipoAgente(self,pos):
        aux=self.__comienzo
        encontro=False
        i=1
        while aux!=None and encontro==False:
            if pos==i:
                print(aux.getPersonal().__class__.__name__)
                encontro=True
            i+=1
            aux=aux.getSiguiente()
    
    def GenerarListadoDocInv(self,nom):
        ListaDocentesinvestigadores=[]
        for i in self:
            if isinstance(i,DocenteInvestigador):
                if i.getcarrera()==nom:
                    ListaDocentesinvestigadores.append(i)

        ListaDocentesinvestigadores.sort()
        for i in ListaDocentesinvestigadores:
            print(i)
    
    def ContarAgentes(self,area):
        cont1=0
        cont2=0
        for i in self:
            if isinstance(i,DocenteInvestigador):
                if area==i.getareainvestig():
                    cont1+=1
        print('\nLa cantidad de agentes Docente-Investigador que trabajan en el area ingresada es: ',cont1)
        for i in self:
            if isinstance(i,Investigador):
                if area==i.getareainvestig():
                    cont2+=1
        print('\nLa cantidad de investigadores que trabajan en el area ingresada es: ',cont2)
    
    def ListadoAgentes(self):
        listaagentes = []
        for i in self:
            listaagentes.append(i)
        listaagentes.sort()
        for i in listaagentes:
            print('Nombre: {}'.format(i.getnombre()))
            print('Apellido: {}'.format(i.getapellido()))
            print('Tipo de agente: {}'.format(i.__class__.__name__))
            print('Sueldo: {}'.format(i.CalculoSueldo()))

    def Listado(self,cat):
        acum=0
        for i in self:
            if isinstance(i,DocenteInvestigador):
                if cat==i.getcategoria():
                    print('Apellido: ',i.getapellido())
                    print('Nombre: ',i.getnombre())
                    print('Importe Extra: ',i.getimporteextra())
                    acum+=i.getimporteextra()
        print('Total: ',acum)

    def __toJSON__(self):
        d=dict(__class__=self.__class__.__name__,
        Personal=[Personal.__toJSON__() for Personal in self])
        return d