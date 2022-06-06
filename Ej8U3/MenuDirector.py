class MenuDirector:
    __opcion=None
    def __init__(self):
        self.__opcion=0
    def Iniciar(self):
        user=None
        cont=None
        user="uTesoreso"
        cont="ag@74ck"
        usuario=input('\nIngrese su usuario: ')
        contraseña=input('Ingrese su contraseña: ')
        if usuario==user:
            if contraseña==cont:
                print('\n--ACCESO ACEPTADO--\n')
                while self.__opcion!='-1':
                    print('=>1-Modificar basico')
                    print('=>2-Modificar porcentaje por cargo')
                    print('=>3-Modificar importe extra')
                    self.__opcion=input('\nIngrese numero de opcion: ')
                    if self.__opcion=='1':
                        pass