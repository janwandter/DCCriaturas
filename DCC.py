from cargar import cargar_magizoologos, cargar_criaturas
from criaturas import Augurey, Niffler, Erkling
import parametros as p
from sys import exit
import random

magizoologos = cargar_magizoologos(p.RUTA_MAGIZOOLOGOS)
criaturas = cargar_criaturas(p.RUTA_CRIAT)

class DCC:
    def __init__(self, username):
        self.username = username
        self.usuario = magizoologos[self.username]
        self.mis_criaturas = magizoologos[self.username].criaturas
        self.dia = 0
        self.aprov = 0
        self.list_enfermos_dia = list()
        self.list_escapes_dia = list()
        self.list_hambrientas_dia = list()
    
    def __str__(self):
        enumerador_criaturas = 1
        str_criaturas = ''
        for criaturas_propias in self.usuario.criaturas:
            str_criaturas += f'''Criatura {enumerador_criaturas}:
'''             f'''{self.mis_criaturas[criaturas_propias]}
'''         
            enumerador_criaturas += 1
        return (f'''{self.usuario}
'''             f'{str_criaturas}')

    def calcular_aprobacion(self):
        criat_sanas = 0
        criat_cautiv = 0
        n_criat = len(self.usuario.criaturas)
        for criatura in self.usuario.criaturas:
            if not self.usuario.criaturas[criatura].enferma:
                criat_sanas += 1
            if not self.usuario.criaturas[criatura].fugitiva:
                criat_cautiv += 1
        return int(min(100, max(0, (criat_sanas + criat_cautiv) * 100 // (2 * n_criat))))

    def pasar_dia(self):
        str_enfermos = ""
        str_escaparon = ""
        str_hambrientas = ""
        str_perdi_salud_enferma = ""
        str_perdi_salud_hambre = ""
        for criatura in self.mis_criaturas:
            self.mis_criaturas[criatura].dias_sin_comida += 1
            if self.mis_criaturas[criatura].enfermarse():
                str_enfermos += f"{criatura},"
            if self.mis_criaturas[criatura].escape():
                str_escaparon += f"{criatura},"
            if self.mis_criaturas[criatura].hambre_dia():
                str_hambrientas += f"{criatura},"
            if self.mis_criaturas[criatura].enferma:
                self.mis_criaturas[criatura].salud_actual -= p.ENFERMA_DIA
                str_perdi_salud_enferma += f"{criatura},"
            if self.mis_criaturas[criatura].hambre == "hambrienta":
                self.mis_criaturas[criatura].salud_actual -= p.HAMBRE_DIA
                str_perdi_salud_hambre += f"{criatura},"
            hab_criat = self.mis_criaturas[criatura].hab_especial()
            if type(hab_criat) == str:
                self.usuario.alimentos.append(hab_criat)
                print(f"{criatura} te ha regalado: {hab_criat}")
            elif type(hab_criat) == int:
                self.usuario.sickles += hab_criat
                if hab_criat < 0:
                    print(f"{criatura} te ha robado {(-1)*hab_criat} sickles por hambre")
                else:
                    print(f"{criatura} te ha regalado {hab_criat} sickles")
            else:
                if len(self.usuario.alimentos) > 0 and hab_criat:
                    alim_robado = self.usuario.alimentos.pop(0)
                    print(f"{criatura} te ha robado {alim_robado} por hambre")
                    if "Tarta" in alim_robado:
                        self.mis_criaturas[criatura].salud_actual += p.SALUD_TARTA
                    elif "Hígado" in alim_robado:
                        self.mis_criaturas[criatura].salud_actual += p.SALUD_HIGADO
                        self.mis_criaturas[criatura].enferma = False
                    else:
                        if random.random() <= 0.65:
                            self.mis_criaturas[criatura].salud_actual += p.SALUD_BUÑUELO
        self.list_enfermos_dia = str_enfermos[:-1].split(",")
        self.list_escapes_dia = str_escaparon[:-1].split(",")
        self.list_hambrientas_dia = str_hambrientas[:-1].split(",")
        self.aprov = self.calcular_aprobacion()
        self.usuario.aprobacion = self.aprov
        self.usuario.energia += self.usuario.energia_total
        self.usuario.energia
        print(f'''
'''           f'''Criaturas que se enfermaron: {str_enfermos[:-1]}
'''           f'''Criaturas que se escaparon: {str_escaparon[:-1]}
'''           f'''Criaturas hambrientas: {str_hambrientas[:-1]}
'''           f'''{str_perdi_salud_enferma[:-1]} tiene(n) menos salud por enfermedad
'''           f'''{str_perdi_salud_hambre[:-1]} tiene(n) menos salud por hambre
'''           f'''********************************************
'''           f'Nivel de aprobación: {self.aprov}')
        if not self.usuario.licencia and self.aprov < 60:
            print(f"Sin licencia, te la han quitado anteriormente")
        elif self.usuario.licencia and self.aprov < 60:
            self.usuario.licencia = False
            print(f"Te han quitado tu licencia por baja aprobación")
        elif self.usuario.licencia and self.aprov >=60: 
            print(f"Felicitaciones continúas con tu licencia")
        else:
            self.usuario.licencia = True
            print(f"Felicitaciones has recuperado tu licencia")
        print(f'''El DCC te ha pagado {self.pago_diario()} Sickles
'''           f'''Se te descontaron {self.fiscalizar()} Sickles en multas
'''           f'''Tu saldo actual es: {self.usuario.sickles}
'''           f'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''           f' ')
        
    def pago_diario(self):
        n_alimento = 2
        # n_alimento = len(self.usuario.alimentos)
        n_magia = self.usuario.magia
        pago = self.aprov * 4 + n_alimento * 15 + n_magia * 3
        self.usuario.sickles += int(pago)
        return pago
    
    def fiscalizar(self):
        multa = 0
        str_multa_escape = ""
        str_multa_enfermo = ""
        for criatura in self.list_enfermos_dia:
            if random.random() <= 0.7:
                str_multa_enfermo += f"{criatura},"
                multa += p.DCC_ENFERMEDAD
        if len(str_multa_enfermo) == 0:
            print("No recibiste multa por enfermedad de criaturas")
        else:
            print(f"Recibiste multa por la enfermedad de: {str_multa_escape[:-1]}")

        for criatura in self.list_escapes_dia:
            if random.random() <= 0.5:
                str_multa_escape += f"{criatura},"
                multa += p.DCC_ESCAPE
        if str_multa_escape == "":
            print("No recibiste multa por escape de criaturas")
        else:
            print(f"Recibiste multa por el escape de: {str_multa_escape[:-1]}")
        for criatura in self.mis_criaturas:
            if self.mis_criaturas[criatura].salud_actual == 1:
                multa += p.DCC_BAJA_SALUD
        if self.usuario.sickles >= multa:
            self.usuario.sickles -= multa
        else:
            self.usuario.sickles = 0
        return multa    

    def vender_criatura(self):
        while self.usuario.licencia:
            print(f'''Seleccione una opción:
'''             f'''CRIATURA           PRECIO
'''             f'''[1] Augurey         {p.COSTO_AUGUREY}           
'''             f'''[2] Niffler         {p.COSTO_NIFFLER}
'''             f'''[3] Erkling         {p.COSTO_ERKLING}
'''             f'''[4] Volver atrás
'''             f'[0] Salir')
            seleccion_criatura = input()
            if seleccion_criatura == "1":
                self.usuario.sickles -= p.COSTO_AUGUREY
                while self.usuario.sickles != False:
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
                        augurey = Augurey(nombre_criatura, p.MAGIA_AUGUREY, \
                            p.ESCAPE_AUGUREY, p.ENFERMIZA_AUGUREY, p.ENFERMA_NUEVA,\
                                p.FUGITIVA_NUEVA, salud_a, salud_a, p.HAMBRE_NEW, \
                                    p.AGRESIVIDAD_AUGUREY, p.DIAS_SIN_C_NEW, p.CLEP_AUG_ERK)
                        self.usuario.criaturas[nombre_criatura] = augurey
                        criaturas[nombre_criatura] = augurey
                        return True
            elif seleccion_criatura == "2":
                self.usuario.sickles -= p.COSTO_NIFFLER
                while self.usuario.sickles != False:
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
                        niffler = Niffler(nombre_criatura, p.MAGIA_NIFFLER,\
                             p.ESCAPE_NIFFLER, p.ENFERMIZA_NIFFLER, p.ENFERMA_NUEVA,\
                                 p.FUGITIVA_NUEVA, salud_n, salud_n, p.HAMBRE_NEW,\
                                      p.AGRESIVIDAD_NIFFLER, p.DIAS_SIN_C_NEW, p.CLEP_NIFFLER)
                        self.usuario.criaturas[nombre_criatura] = niffler
                        criaturas[nombre_criatura] = niffler
                        return True
            elif seleccion_criatura == "3":
                self.usuario.sickles -= p.COSTO_ERKLING
                while self.usuario.sickles != False:
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
                        self.usuario.criaturas[nombre_criatura] = erkling
                        criaturas[nombre_criatura] = erkling
                        return True
            elif seleccion_criatura == "4":
                return None
            elif seleccion_criatura == "0":
                exit()
            else:
                print("Esa opción no existe")
        print(f"No tienes tu licencia, no puedes comprar criaturas")

    def vender_alimentos(self):
        while True:
            print(f'''Seleccione una opción:
'''             f'''ALIMENTO                   PRECIO
'''             f'''[1] Tarta de Melaza          {p.COSTO_TARTA}           
'''             f'''[2] Hígado de Dragón         {p.COSTO_HIGADO}
'''             f'''[3] Bueñuelo de Gusarajo     {p.COSTO_BUÑUELOS}
'''             f'''[4] Volver atrás
'''             f'[0] Salir')
            seleccion_alimento = input()
            if seleccion_alimento == "1":
                self.usuario.sickles -= p.COSTO_TARTA
                if self.usuario.sickles != False:
                    self.usuario.alimentos.append("Tarta de Melaza")
                    return None
            elif seleccion_alimento == "2":
                self.usuario.sickles -= p.COSTO_HIGADO
                if self.usuario.sickles != False:
                    self.usuario.alimentos.append("Hígado de Dragón")
                    return None
            elif seleccion_alimento == "3":
                self.usuario.sickles -= p.COSTO_BUÑUELOS
                if self.usuario.sickles != False:
                    self.usuario.alimentos.append("Bueñuelo de Gusarajo")
                    return None
            elif seleccion_alimento == "4":
                return None
            elif seleccion_alimento == "0":
                exit()
            else:
                print("Esa opción no existe")

    def pelea(self):
        ## Parte el usuario
        criat_cautiv = []
        for criat in self.mis_criaturas:
            if not self.mis_criaturas[criat].fugitiva:
                criat_cautiv.append(criat)
        while len(criat_cautiv) > 1:
            print(f"Elige tu representante")
            n_opcion = 1
            for criat in criat_cautiv:
                print(f"[{n_opcion}] {criat}")
                n_opcion +=1
            n_repr = input()
            if n_repr.isnumeric():
                if int(n_repr) in range(1, len(criat_cautiv) + 1):
                    iterador = 1
                    for criat in criat_cautiv:
                        if int(n_repr) == iterador:
                            criat_user = criat
                            criat_cautiv.pop(iterador-1)
                        iterador += 1
                    while True:
                        print(f"Elige tu contrincante (representante DCC)")
                        n_opcion = 1
                        for criat in criat_cautiv:
                            if criat != criat_user:
                                print(f"[{n_opcion}] {criat}")
                                n_opcion +=1
                        n_contr = input()
                        if n_contr.isnumeric():
                            if int(n_contr) in range(1, len(criat_cautiv) + 1):
                                iterador = 1
                                for criat in criat_cautiv:
                                    if iterador == int(n_contr):
                                        criat_dcc = criat
                                    iterador +=1
                                self.usuario.sickles -= p.APUESTA
                                atac_dict = {"inofensiva": p.ATAQ_INOF, \
                                    "arisca": p.ATAQ_ARISCA, "peligrosa": p.ATAQ_PELIGROSA}
                                agresiva_user = self.mis_criaturas[criat_user].agresividad
                                magia_user = self.mis_criaturas[criat_user].magia
                                ataq_user = magia_user * atac_dict[agresiva_user]
                                agresiva_dcc = self.mis_criaturas[criat_dcc].agresividad
                                magia_dcc = self.mis_criaturas[criat_dcc].magia
                                ataq_dcc = magia_dcc * atac_dict[agresiva_dcc]
                                esquivar_user = (1 - \
                                    self.mis_criaturas[criat_user].p_escape) * p.ESQUIVAR
                                esquivar_dcc = (1 - \
                                    self.mis_criaturas[criat_dcc].p_escape) * p.ESQUIVAR
                                if self.usuario.sickles != False:
                                    salud_user = self.mis_criaturas[criat_user].salud_actual
                                    salud_dcc = self.mis_criaturas[criat_dcc].salud_actual
                                    turno = "user"
                                    print(f"¡El combate entre {criat_user} "
                                          f"""y {criat_dcc} ha comenzado!
"""                                       f"*******************************"
                                          f"*****************************")
                                    while self.mis_criaturas[criat_user].salud_actual\
                                        > 1 and self.mis_criaturas[criat_dcc].salud_actual > 1:
                                        print(f"")
                                        if "user" in turno:
                                            print(f"{criat_user} ha atacado a {criat_dcc}")
                                            if random.random() <= esquivar_dcc:
                                                print(f"{criat_dcc} ha recibido "
                                                      f"un daño de {ataq_user}")
                                                self.mis_criaturas[criat_dcc].salud_actual\
                                                     -= ataq_user
                                            else:
                                                print(f"{criat_dcc} ha esquivado el ataque")
                                            print(f"Puntos de salud de {criat_dcc}"
                                                f" {self.mis_criaturas[criat_dcc].salud_actual}")
                                            turno = "dcc"
                                        else:
                                            print(f"{criat_dcc} ha atacado a {criat_user}")
                                            if random.random() <= esquivar_user:
                                                print(f"{criat_user} ha recibido un daño de"
                                                      f" {ataq_dcc}")
                                                self.mis_criaturas[criat_user].salud_actual -= \
                                                    ataq_dcc
                                            else:
                                                print(f"{criat_user} ha esquivado el ataque")
                                            print(f"Puntos de salud de {criat_user}"
                                                f" {self.mis_criaturas[criat_user].salud_actual}")
                                            turno = "user"
                                        
                                        print(f""" 
"""                                           f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                                              f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    if self.mis_criaturas[criat_dcc].salud_actual == 1:
                                        print(f"""Felicidades! Tu criatura ha ganado el combate
"""                                           f"El DCC te ha pagado 60 Sickles")
                                        self.usuario.sickles += 60
                                    else:
                                        print(f"Ouch! tu criatura ha sido derrotada." 
                                             f"""¡Mejor suerte la próxima!
"""                                          f"El DCC se ha quedado con tus Sickles")
                                    print(f"Tus criaturas vuelven al estado de salud previo al combate")
                                    self.mis_criaturas[criat_user].salud_actual = salud_user
                                    self.mis_criaturas[criat_dcc].salud_actual = salud_dcc
                                    return None
                        print(f"Esa opción no existe")      
            print(f"Esa opción no existe")                   
        return print(f"Tienes que tener por lo menos 2 criaturas en cautiverio")

                            




            
        