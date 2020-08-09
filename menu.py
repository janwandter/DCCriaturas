from sys import exit
import parametros as p
import random
from DCC import DCC, magizoologos, criaturas
from magizoologos import Docencio, Hibrido, Tareo
from criaturas import Augurey, Niffler, Erkling

class MenuInicio:
    def __init__(self):
        self.username = None
        self.eleccion = ""

    def accion(self):
        print(f"""[1] Crear Magizoólogo
"""          f"""[2] Cargar Magizoólogo
"""          f"""[0] Salir""")
        self.eleccion = input()
        if self.eleccion == "1":
            return self.crear_magizoologo()
        elif self.eleccion == "2":
            return self.cargar_magizoologo()
        elif self.eleccion == "0":
            return exit()
        else: 
            return print(f"Esa opción no existe, vuelve a intentar")

    def crear_magizoologo(self):
        buscando_nombre = True
        while buscando_nombre:
            print(f"""Ingresa el nombre que quieres usar,
"""         f"recuerda utilizar caracteres alfanúmericos""")
            buscando_nombre = False
            nombre_deseado = input()
            bool_menu_errores = True
            while bool_menu_errores:
                bool_menu_errores = False
                if not nombre_deseado.isalnum():
                    print(f"""El nombre no cumple con los requisitos
"""                       f"""[1] Volver a intentar
"""                       f"""[2] Volver atrás
"""                       f"[0] Salir")
                    self.eleccion = input()
                    if self.eleccion == "1":
                        bool_menu_errores = False
                        buscando_nombre = True
                    elif self.eleccion == "2":
                        return False
                    elif self.eleccion == "0":
                        exit()
                    else:
                        print(f"No existe esa opción")
                else:
                    for nombres in magizoologos:
                        if nombre_deseado.lower() == nombres.lower():
                            bool_menu = True
                            while bool_menu:
                                print(f"""Ese nombre de usuario ya existe
"""                                   f"""[1] Volver a intentar
"""                                   f"""[2] Volver atrás
"""                                   f"[0] Salir")
                                self.eleccion = input()
                                if self.eleccion == "1":
                                    bool_menu = False
                                    bool_menu_errores = False
                                    buscando_nombre = True
                                elif self.eleccion == "2":
                                    return False
                                elif self.eleccion == "0":
                                    exit()
                                else:
                                    print(f"No existe esa opción")
        self.username = nombre_deseado
        bool_menu_tipo = True
        while bool_menu_tipo:
            print(f"""Elige que tipo de magizoólogo quieres ser:
"""           f"""[1] Docencio
"""           f"""[2] Tareo
"""           f"[3] Híbrido")
            eleccion_tipo = input()
            bool_menu_tipo = False
            if eleccion_tipo == "1":
                docencio = Docencio(self.username, p.SICKLES_INICIAL, dict(),\
                     list(), p.LICENCIA, p.MAGIA_DOCENCIO, p.DESTREZA_DOCENCIO,\
                         p.ENERGIA_DOCENCIO, p.RESPONSABILIDAD_DOCENCIO, p.HABILIDAD)
                magizoologos[self.username] = docencio
            elif eleccion_tipo == "2":
                tareo = Tareo(self.username, p.SICKLES_INICIAL, dict(), list(),\
                     p.LICENCIA, p.MAGIA_TAREO, p.DESTREZA_TAREO,\
                         p.ENERGIA_TAREO, p.RESPONSABILIDAD_TAREO, p.HABILIDAD)
                magizoologos[self.username] = tareo
            elif eleccion_tipo == "3":
                hibrido = Hibrido(self.username, p.SICKLES_INICIAL, dict(), list(),\
                     p.LICENCIA, p.MAGIA_HIBRIDO, p.DESTREZA_HIBRIDO,\
                         p.ENERGIA_HIBRIDO, p.RESPONSABILIDAD_HIBRIDO, p.HABILIDAD)
                magizoologos[self.username] = hibrido
            else:
                bool_menu_tipo = True
                print(f"No existe esa opción")
        alimento_inicial = random.randint(1,3)
        if alimento_inicial == 1:
            magizoologos[self.username].alimentos.append("Tarta de Melaza")
        elif alimento_inicial == 2:
            magizoologos[self.username].alimentos.append("Hígado de Dragón")
        else:
            magizoologos[self.username].alimentos.append("Buñuelo de Gusarajo")
        while True:
            print(f'''Seleccione la especie de tu primera criatura:
'''             f'''[1] Augurey          
'''             f'''[2] Niffler
'''             f'''[3] Erkling''')
            seleccion_criatura = input()
            if seleccion_criatura == "1":
                requisito = 0
                print(f"Indica el nombre de la criatura")
                nombre_criatura = input()
                for iterador in criaturas:
                    if iterador.lower() == nombre_criatura.lower():
                        print(f"Ese nombre ya está en uso")
                        requisito = 1
                if not nombre_criatura.isalnum():
                    print(f"Ese nombre no cumple los requisitos")
                if nombre_criatura.isalnum() and requisito == 0:
                    salud_a = p.SALUD_AUGUREY
                    augurey = Augurey(nombre_criatura, p.MAGIA_AUGUREY,\
                         p.ESCAPE_AUGUREY, p.ENFERMIZA_AUGUREY, p.ENFERMA_NUEVA,\
                             p.FUGITIVA_NUEVA, salud_a, salud_a, p.HAMBRE_NEW,\
                                  p.AGRESIVIDAD_AUGUREY, p.DIAS_SIN_C_NEW, p.CLEP_AUG_ERK)
                    magizoologos[self.username].criaturas[nombre_criatura] = augurey
                    criaturas[nombre_criatura] = augurey
                    return True
            elif seleccion_criatura == "2":
                requisito = 0
                print(f"Indica el nombre de la criatura")
                nombre_criatura = input()
                for iterador in criaturas:
                    if iterador.lower() == nombre_criatura.lower():
                        print(f"Ese nombre ya está en uso")
                        requisito = 1
                if not nombre_criatura.isalnum():
                    print(f"Ese nombre no cumple los requisitos")
                if nombre_criatura.isalnum() and requisito == 0:
                    salud_n = p.SALUD_NIFFLER
                    niffler = Niffler(nombre_criatura, p.MAGIA_NIFFLER, \
                        p.ESCAPE_NIFFLER, p.ENFERMIZA_NIFFLER, p.ENFERMA_NUEVA,\
                            p.FUGITIVA_NUEVA, salud_n, salud_n, p.HAMBRE_NEW, \
                                p.AGRESIVIDAD_NIFFLER, p.DIAS_SIN_C_NEW, p.CLEP_NIFFLER)
                    magizoologos[self.username].criaturas[nombre_criatura] = niffler
                    criaturas[nombre_criatura] = niffler
                    return True
            elif seleccion_criatura == "3":
                requisito = 0
                print(f"Indica el nombre de la criatura")
                nombre_criatura = input()
                for iterador in criaturas:
                    if iterador.lower() == nombre_criatura.lower():
                        print(f"Ese nombre ya está en uso")
                        requisito = 1
                if not nombre_criatura.isalnum():
                    print(f"Ese nombre no cumple los requisitos")
                if nombre_criatura.isalnum() and requisito == 0:
                    salud_e = p.SALUD_ERKLING
                    erkling = Erkling(nombre_criatura, p.MAGIA_ERKLING, \
                        p.ESCAPE_ERKLING, p.ENFERMIZA_ERKLING, p.ENFERMA_NUEVA,\
                            p.FUGITIVA_NUEVA, salud_e, salud_e, p.HAMBRE_NEW, \
                                p.AGRESIVIDAD_ERKLING, p.DIAS_SIN_C_NEW, p.CLEP_AUG_ERK)
                    magizoologos[self.username].criaturas[nombre_criatura] = erkling
                    criaturas[nombre_criatura] = erkling
                    return True
            else:
                print(f"No existe esa opción")

    def cargar_magizoologo(self):
        iniciando_sesion = True
        while iniciando_sesion:
            print(f"Ingresa tu nombre de magizoólogo:")
            nombre = input()
            for magizoologo in magizoologos:
                if magizoologo.lower() == nombre.lower():
                    self.username = magizoologo
                    return True
            bool_error_inicio = True
            while bool_error_inicio:
                print(f"""El nombre de usuario no está registrado
"""                   f"""[1] Volver a intentar
"""                   f"""[2] Volver atrás
"""                   f"[0] Salir")
                eleccion_error = input()
                if eleccion_error == "1":
                    bool_error_inicio = False
                elif eleccion_error == "2":
                    return False
                elif eleccion_error == "0":
                    exit()
                else:
                    print(f"No existe esa opción")

class MenuAcciones(MenuInicio):
    def __init__(self):
        pass 
    
    def accion(self):
        print(f"""[1] Menu cuidar DCCriaturas
"""          f"""[2] MenuDCC
"""          f"""[3] Pasar al dia siguente
"""          f"""[4] Volver atrás
"""          f"""[0] Salir""")
        self.eleccion = input()
        if self.eleccion in "123":
            return True
        elif self.eleccion == "4":
            return False
        elif self.eleccion == "0":
            return exit()
        else: 
            print(f"Esa opción no existe, vuelve a intentar") 
            return True      

class MenuCuidarCriaturas(MenuInicio):
    def __init__(self):
        super().__init__()

    def accion(self):
        print(f"""[1] Alimentar DCCriatura
"""          f"""[2] Recuperar DCCriatura
"""          f"""[3] Sanar DCCriatura
"""          f"""[4] Usar habilidad especial
"""          f"""[5] Peleas entre DCCriaturas
"""          f"""[6] Volver atrás
"""          f"""[0] Salir""")
        self.eleccion = input()
        if self.eleccion in "12345":
            return True
        elif self.eleccion == "6":
            return False
        elif self.eleccion == "0":
            return exit()
        else: 
            print(f"Esa opción no existe, vuelve a intentar") 
            return True      
       

class MenuDCC(MenuInicio):
    def __init__(self):
        pass
    
    def accion(self):
        print(f"""[1] Adoptar DCCriaturas
"""          f"""[2] Comprar alimentos
"""          f"""[3] Ver mi estado y mis criaturas
"""          f"""[4] Volver atrás
"""          f"""[0] Salir""")
        self.eleccion = input()
        if self.eleccion in "123":
            return True
        elif self.eleccion == "4":
            return False
        elif self.eleccion == "0":
            return exit()
        else: 
            print(f"Esa opción no existe, vuelve a intentar") 
            return True

class PasarDia(MenuInicio):
    def __init__(self):
        super().__init__()

    def accion(self):
        print(f'''¡¡Has pasado al día siguiente!!
'''           f'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''           f'Resumen del día:')

        



