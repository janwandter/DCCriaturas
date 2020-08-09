from abc import ABC, abstractmethod
import parametros as p
from criaturas import Augurey, Niffler, Erkling, str_a_bool
import random

class Magizoologo(ABC):
    def __init__(self, nombre, sickles, criaturas, alimentos, licencia,\
        magia, destreza, energia, responsabilidad, habilidad):
        self.nombre = nombre
        self.__sickles = int(sickles)
        self.criaturas = criaturas
        self.alimentos = alimentos
        self.licencia = str_a_bool(licencia)
        self.magia = int(magia)
        self.destreza = int(destreza)
        self.energia_total = int(energia)
        self.__energia = int(energia)
        self.responsabilidad = int(responsabilidad)
        self.habilidad = str_a_bool(habilidad)
        self.aprobacion = 0
        self.copia_energia = 0
        self.copia_sickles = 0
        self.criatura_elegida = ""
        self.criat_elegida = None

    def __str__(self):
        n_tartas = self.alimentos.count("Tarta de Melaza")
        n_higados = self.alimentos.count("Hígado de Dragón")
        n_buñuelos = self.alimentos.count("Bueñuelo de Gusarajo")
        return (f'Nombre: {self.nombre} ({type(self).__name__}) | '
                f'Sickles: {self.sickles} | '
                f'Energia actual: {self.energia} | '
                f'Licencia: {self.licencia} | '
                f'Aprobación: {self.aprobacion} | '
                f'Magia: {self.magia} | '
                f'Destreza: {self.destreza} | '
                f'Habilidad: {self.habilidad} | '
                f'''Responsabilidad: {self.responsabilidad} |
'''             f'''Alimento           Cantidad   Salud
'''             f'Tarta de Melaza        {n_tartas}'
                f'''        {p.SALUD_TARTA}            
'''             f'Hígado de Dragón       {n_higados}'
                f'''        {p.SALUD_HIGADO} 
'''             f'Bueñuelo de Gusarajo   {n_buñuelos:}'
                f'        {p.SALUD_BUÑUELO}')

    def archivar(self):
        mis_alim = ""
        mis_criat = ""
        for criat in self.criaturas:
            mis_criat += f"{criat};"
        for alim in self.alimentos:
            mis_alim += f"{alim};"
        return (f"{self.nombre},{type(self).__name__},{self.sickles},{mis_criat[:-1]}"
                f",{mis_alim[:-1]},{self.licencia},{self.magia},"
                f"{self.destreza},{self.energia_total}"
                f",{self.responsabilidad},{self.habilidad}")         

    @property
    def sickles(self):
        if self.copia_sickles != self.__sickles:
            return self.__sickles
        else:
            self.copia_sickles = -5
            return False
    @sickles.setter
    def sickles(self, cambio_sickles):
        self.copia_sickles = self.__sickles
        if cambio_sickles < 0:
            print(f"No tienes suficientes sickles")
        else:
            self.__sickles = cambio_sickles  
    
    @property
    def energia(self):
        if self.copia_energia != self.__energia:
            return self.__energia
        else:
            self.copia_energia = -1 #es un valor que nunca va a tener la energia así retorna en las otras la energia y no False
            return False
    @energia.setter
    def energia(self, cambio_energia):
        self.copia_energia = self.__energia
        if cambio_energia > self.energia_total:
            self.__energia = self.energia_total
        elif cambio_energia < 0:
            print(f"No tienes suficiente energía")
        else:
            self.__energia = cambio_energia
    
    @abstractmethod
    def alimentar(self):
        p_ataque = 0
        self.energia -= p.ENERGIA_ALIMENTAR
        while self.energia != False:
            if len(self.alimentos) == 0:
                self.energia += 5 
                print(f"No tienes alimentos, anda al menú DCC para comprar más")
                return False
            print(f"Seleccione que criatura quiere alimentar:")
            iterador = 1
            for nombres in self.criaturas:
                print(f"[{iterador}] {nombres}")
                iterador += 1
            criatura_a_alimentar = input()
            if criatura_a_alimentar.isnumeric():
                if int(criatura_a_alimentar) in range(1, len(self.criaturas) + 1):
                    iterador = 1
                    for nombre_posible in self.criaturas:
                        if int(criatura_a_alimentar) == iterador:
                            self.criatura_elegida = nombre_posible
                        iterador += 1
                    self.criat_elegida = self.criaturas[self.criatura_elegida]
                    if not self.criat_elegida.fugitiva:    
                        while True:
                            print(f"Seleccione el alimento que le quiere dar:")
                            for num_alimentos in range(len(self.alimentos)):
                                print(f"[{num_alimentos}] {self.alimentos[num_alimentos]}")
                            alimento_seleccionado = input()
                            if alimento_seleccionado.isnumeric():
                                if int(alimento_seleccionado) in range(len(self.alimentos)):
                                    alimento_seleccionado = int(alimento_seleccionado)
                                    dias_sin_c_copia = self.criat_elegida.dias_sin_comida
                                    if "Tarta" in self.alimentos[alimento_seleccionado]:
                                        self.criat_elegida.salud_actual += p.SALUD_TARTA
                                        self.criat_elegida.hambre = "satisfecha"
                                        if type(self.criat_elegida).__name__ == "Niffler":
                                            if random.random() <= 0.15:
                                                self.criat_elegida.agresividad = "inofensiva"
                                        p_ataque = self.criat_elegida.ataque()
                                        self.criat_elegida.dias_sin_comida -= dias_sin_c_copia
                                    elif "Hígado" in self.alimentos[alimento_seleccionado]:
                                        self.criat_elegida.salud_actual += p.SALUD_HIGADO
                                        self.criat_elegida.enferma = False
                                        p_ataque = self.criat_elegida.ataque()
                                        self.criat_elegida.dias_sin_comida -= dias_sin_c_copia
                                        self.criat_elegida.hambre = "satisfecha"
                                    else:
                                        if random.random() <= 0.65:
                                            self.criat_elegida.salud_actual += p.SALUD_BUÑUELO
                                            self.criat_elegida.hambre = "satisfecha"
                                            self.criat_elegida.dias_sin_comida -= dias_sin_c_copia
                                        else:
                                            print(f"Tu criatura ha rechazado el buñuelo")
                                        p_ataque = self.criat_elegida.ataque()
                                    self.alimentos.pop(alimento_seleccionado)
                                    if random.random() <= p_ataque:
                                        energia_ataque = max(10, \
                                            self.magia - self.criat_elegida.magia)
                                        print(f"Tu mascota te ha atacado")
                                        if energia_ataque < self.energia:
                                            self.energia -= energia_ataque
                                            self.energia
                                        else:
                                            self.energia = 1
                                    return True
                            print(f"No existe esa opción")
                    print(f"Esa mascota ha escapado, no puedes darle alimento, vuelves al menú")
                    return True
            print(f"No existe esa opción")        
    
    @abstractmethod
    def recuperar(self):
        self.energia -= p.ENERGIA_RECUPERAR
        while self.energia != False:
            print(f"Seleccione que criatura quiere recuperar:")
            iterador = 1
            for nombres in self.criaturas:
                if self.criaturas[nombres].fugitiva:
                    print(f"[{iterador}] {nombres}")
                    iterador += 1
            if iterador == 1:
                self.energia += 10
                return print("No tienes criaturas que recuperar")
            criatura_recuperar = input()
            if criatura_recuperar.isnumeric():
                if int(criatura_recuperar) in range(1,len(self.criaturas)+1):
                    iterador = 1
                    for nombre_posible in self.criaturas:
                        if self.criaturas[nombre_posible].fugitiva:
                            if int(criatura_recuperar) == iterador:
                                self.criatura_elegida = nombre_posible
                            iterador += 1
                    self.criat_elegida = self.criaturas[self.criatura_elegida]
                    destreza_magia = self.destreza + self.magia
                    magia_criat = self.criat_elegida.magia
                    p_esc = min(1, max(0, (destreza_magia - magia_criat)\
                         / (destreza_magia + magia_criat)))
                    if random.random() <= p_esc:
                        self.criat_elegida.fugitiva = False
                        print("Tiene su criatura de vuelta")
                        return False
                    print(f"No ha podido recuperar a su criatura")
                    return True
            print(f"No existe esa opción") 
        return True

    def sanar(self):
        self.energia -= p.ENERGIA_SANAR
        while self.energia != False:
            print(f"Seleccione que criatura quiere sanar:")
            iterador = 0
            for nombres in self.criaturas:
                if self.criaturas[nombres].enferma and not self.criaturas[nombres].fugitiva:
                    print(f"[{iterador}] {nombres}")
                    iterador += 1
            if iterador == 0:
                self.energia += p.ENERGIA_SANAR
                return print("No tienes criaturas enfermas en cautiverio")
            criatura_sanar = input()
            if criatura_sanar.isnumeric():
                if int(criatura_sanar) in range(len(self.criaturas)):
                    iterador = 0
                    for nombre_posible in self.criaturas:
                        if self.criaturas[nombre_posible].enferma and\
                             not self.criaturas[nombres].fugitiva:
                            if int(criatura_sanar) == iterador:
                                self.criatura_elegida = nombre_posible
                            iterador += 1
                    self.criat_elegida = self.criaturas[self.criatura_elegida]
                    magia_criatura = self.criat_elegida.magia
                    p_sanar = min(1, max(0, (self.magia - magia_criatura)\
                         / (self.magia + magia_criatura)))
                    if random.random() <= p_sanar:
                        self.criat_elegida.enferma = False
                        print("Su criatura se ha sanado")
                        return False
                    print(f"No ha podido sanar a su criatura")
                    return True
            print(f"No existe esa opción") 
        return True

    @abstractmethod
    def usar_habilidad(self):
        pass

class Docencio(Magizoologo):
    def __init__(self, nombre, sickles, criaturas, alimentos, licencia,\
        magia, destreza, energia, responsabilidad, habilidad):
        super().__init__(nombre, sickles, criaturas, alimentos, licencia,\
        magia, destreza, energia, responsabilidad, habilidad)

    def alimentar(self):
        if super().alimentar():
            if self.energia == False:
                return None
            self.criat_elegida.salud_max += p.ALIMENTO_DOCENCIO

    def recuperar(self):
        fugitivas = super().recuperar()
        if not fugitivas:
            self.criat_elegida.salud_actual -= 7
        return fugitivas
    
    def usar_habilidad(self):
        if self.habilidad:
            for criaturas in self.criaturas:
                if not self.criaturas[criaturas].fugitiva:
                    dias_sin_c = self.criaturas[criaturas].dias_sin_comida
                    self.criaturas[criaturas].hambre = "satisfecha"
                    self.criaturas[criaturas].dias_sin_comida -= dias_sin_c
            print("Todas tus criaturas en cautiverio están satisfechas")
        else:
            print(f"Ya no puedes ocupar la habilidad")
        self.habilidad = False

class Tareo(Magizoologo):
    def __init__(self, nombre, sickles, criaturas, alimentos, licencia,\
        magia, destreza, energia, responsabilidad, habilidad):
        super().__init__(nombre, sickles, criaturas, alimentos, licencia,\
        magia, destreza, energia, responsabilidad, habilidad)
          
    def alimentar(self):
        if super().alimentar():
            if self.energia == False:
                return None
            if random.random() <= 0.7:
                sal_max = self.criat_elegida.salud_max 
                self.criat_elegida.salud_actual += sal_max
                   
    def recuperar(self):
        return super().recuperar()
    
    def usar_habilidad(self):
        if self.habilidad:
            for criaturas in self.criaturas:
                if self.criaturas[criaturas].fugitiva:
                    self.criaturas[criaturas].fugitiva = False
            print("Todas tus criaturas han sido recuperadas")
        else:
            print(f"Ya no puedes ocupar la habilidad")       
        self.habilidad = False

class Hibrido(Magizoologo):
    def __init__(self, nombre, sickles, criaturas, alimentos, licencia,\
        magia, destreza, energia, responsabilidad, habilidad):
        super().__init__(nombre, sickles, criaturas, alimentos, licencia,\
        magia, destreza, energia, responsabilidad, habilidad)
        
    
    def alimentar(self):
        if super().alimentar():
            if self.energia == False:
                return None
            self.criat_elegida.salud_actual += p.ALIMENTO_HIBRIDO

    def recuperar(self):
        return super().recuperar()
    
    def usar_habilidad(self):
        if self.habilidad:
            for criaturas in self.criaturas:
                if not self.criaturas[criaturas].fugitiva:
                    self.criaturas[criaturas].enferma = False
            print("Todas tus criaturas en cautiverio están sanadas")
        else:
            print(f"Ya no puedes ocupar la habilidad")
        self.habilidad = False
