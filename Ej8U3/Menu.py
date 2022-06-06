from ClaseLista import ListaProgramador
from ObjectEncoder import ObjectEncoder
from Personal import Personal
class Menu:
    __opcion=None
    def __init__(self):
        self.__opcion=None
    def Iniciar(self):
        unaLista=ListaProgramador()
        unObjectEncoder=ObjectEncoder()
        while self.__opcion!='-1':
            print('=>1-Leer JSON')
            print('=>2-Insertar agentes a la coleccion')
            print('=>3-Agregar agentes a la coleccion')
            print('=>4-Dada una posicion mostrar tipo de agente')
            print('=>5-Dado un nombre de carrera obtener listado ordenado de docentes investigadores')
            print('=>6-Dada un area contar docentes-investigadores y cantidad de investigadores')
            print('=>7-Generar listado ordenado de todos los agentes')
            print('=>8-Dada una categoria generar listado de Docentes-Investigadores')
            print('=>9-Guardar JSON')
            self.__opcion=input('\nIngrese numero de opcion: ')

            if self.__opcion=='1':
                d=unObjectEncoder.LeerJSON('personal.json')
                unaLista=unObjectEncoder.DecodificarDicc(d)

            elif self.__opcion=='2':
                unAgente=unaLista.CrearAgente(input('\nIngrese tipo de agente: '))
                if unAgente!=None:
                    unaLista.InsertarElemento(unAgente,int(input('\nIngrese posicion:')))

            elif self.__opcion=='3':
                unAgente=unaLista.CrearAgente(input('\nIngrese tipo de agente: '))
                if unAgente!=None:
                    unAgente=unaLista.AgregarElemento(unAgente)

            elif self.__opcion=='4':
                pos=int(input('\nIngrese posicion de lista: '))
                unaLista.MostrarTipoAgente(pos)

            elif self.__opcion=='5':
                nom=input('\nIngrese nombre de carrera: ')
                unaLista.GenerarListadoDocInv(nom)
            
            elif self.__opcion=='6':
                area=input('\nIngrese area de investigacion: ')
                unaLista.ContarAgentes(area)
            
            elif self.__opcion=='7':
                pass
            
            elif self.__opcion=='8':
                cat=input('\nIngrese categoria I,II,III,IV,V: ')
                unaLista.Listado(cat)
            
            elif self.__opcion=='9':
                unObjectEncoder.GuardarJSON(unaLista.__toJSON__,('personal.json'))
                print('\n--OBJETOS GUARDADOS--\n')