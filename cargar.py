from magizoologos import Docencio, Tareo, Hibrido
from criaturas import Augurey, Niffler, Erkling
from parametros import RUTA_CRIAT

def cargar_magizoologos(archivo_magizoologos):
    magizoologo = dict()
    with open(archivo_magizoologos, "r", encoding = "utf-8") as archivo:
        for linea in archivo.readlines():
            nombre, tipo, sickles, criaturas, alimentos, licencia, magia, destreza,\
                 energia, responsabilidad, habilidad = linea.strip().split(",")
            criaturas = criaturas.split(";")
            dict_criaturas = dict()
            for nombre_criaturas in criaturas:
                dict_criaturas[nombre_criaturas] = cargar_criaturas(RUTA_CRIAT)[nombre_criaturas]
            if len(alimentos) > 0: #Por si no le quedan alimentos
                alimentos = alimentos.split(";")
            else:
                alimentos = []
            if tipo == "Docencio":
                docencio = Docencio(nombre, sickles, dict_criaturas, alimentos, \
                    licencia, magia, destreza, energia, responsabilidad, habilidad)
                magizoologo[nombre] = docencio
            elif tipo == "Tareo":
                tareo = Tareo(nombre, sickles, dict_criaturas, alimentos, licencia,\
                     magia, destreza, energia, responsabilidad, habilidad)
                magizoologo[nombre] = tareo
            else:
                hibrido = Hibrido(nombre, sickles, dict_criaturas, alimentos, \
                    licencia, magia, destreza, energia, responsabilidad, habilidad)
                magizoologo[nombre] = hibrido
        return magizoologo

def actualizar_archivos(magizoologos, nombre_usuario, file_magi, criaturas, archivo_criaturas):
    with open(archivo_criaturas, "w", encoding = "utf-8") as file:
        for nombre_criat in criaturas:
            if nombre_criat in magizoologos[nombre_usuario].criaturas:
                file.write(f"{magizoologos[nombre_usuario].criaturas[nombre_criat].archivar()}\n")
            else:
                file.write(f"{criaturas[nombre_criat].archivar()}\n")
    with open(file_magi, "w", encoding = "utf-8") as archivo:
        for nombre_magi in magizoologos:
            archivo.write(f"{magizoologos[nombre_magi].archivar()}\n")

def cargar_criaturas(archivo_criaturas):
    criaturas = dict()
    with open(archivo_criaturas, "r", encoding = "utf-8") as archivo:
        for linea in archivo.readlines():
            nombre, tipo, magia, p_escape, enfermiza, enferma,\
                fugitiva, salud_max, salud_actual, hambre, agresividad,\
                    dias_sin_comida, cleptomania = linea.strip().split(",")
            if tipo == "Augurey":
                augurey = Augurey(nombre, magia, p_escape, enfermiza, enferma,\
                    fugitiva, salud_max, salud_actual, hambre, agresividad,\
                        dias_sin_comida, cleptomania)
                criaturas[nombre] = augurey
            elif tipo == "Niffler":
                niffler = Niffler(nombre, magia, p_escape, enfermiza, enferma,\
                    fugitiva, salud_max, salud_actual, hambre, agresividad,\
                        dias_sin_comida, cleptomania)
                criaturas[nombre] = niffler
            else:
                erkling = Erkling(nombre, magia, p_escape, enfermiza, enferma,\
                    fugitiva, salud_max, salud_actual, hambre, agresividad,\
                        dias_sin_comida, cleptomania)
                criaturas[nombre] = erkling
        return criaturas

    
    


            



