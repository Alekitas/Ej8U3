import json
from pathlib import Path
from ClaseLista import ListaProgramador
from Docente import Docente
from DocenteInvestigador import DocenteInvestigador
from Investigador import Investigador
from PersonalApoyo import PersonalApoyo
from Personal import Personal

class ObjectEncoder:
    def DecodificarDicc(self,d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_=eval(class_name)
            if class_name=='ListaProgramador':
                listaPersonal=d['Personal']
                unaListaProgramador=class_()
                dPersonal=listaPersonal[0]
                for i in range(len(listaPersonal)):
                    dPersonal=listaPersonal[i]
                    class_name=dPersonal.pop('__class__')
                    class__=eval(class_name)
                    atributos=dPersonal['__atributos__']
                    unPersonal=class__(**atributos)
                    unaListaProgramador.AgregarElemento(unPersonal)
            return unaListaProgramador
            
    def GuardarJSON(self,diccionario,archivo):
        with Path(archivo).open("w",encoding="UTF-8") as destino:
            json.dump(diccionario,destino,indent=4)
            destino.close()

    def LeerJSON(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoaDiccionario(self,texto):
        return json.loads(texto)