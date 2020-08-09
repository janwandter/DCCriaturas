from abc import ABC, abstractmethod
import parametros as p
import random

def str_a_bool(str_cambiar):
    return str_cambiar != "False"

class Criatura(ABC):
    def __init__(self, nombre, magia, p_escape, enfermiza, enferma,\
        fugitiva, salud_max, salud_actual, hambre, agresividad,\
            dias_sin_comida, cleptomania):
        self.nombre = nombre
        self.magia = int(magia) 
        self.p_escape = float(p_escape)
        self.enfermiza = float(enfermiza)
        self.enferma = str_a_bool(enferma)
        self.fugitiva = str_a_bool(fugitiva)
        self.__salud_max = int(salud_max)
        self.__salud_actual = int(salud_actual)
        self.hambre = hambre
        self.agresividad = agresividad
        self.__dias_sin_comida = int(dias_sin_comida)
        self.cleptomania = int(cleptomania)
    
    def __str__(self):
        return (f'Nombre: {self.nombre} ({type(self).__name__}) | '
                f'Magia: {self.magia} | '
                f'Salud actual: {self.salud_actual} | '
                f'Enferma: {self.enferma} | '
                f'Hambre: {self.hambre} | '
                f'Agresividad: {self.agresividad} | '
                f'Fugitiva: {self.fugitiva} | '
                f'Dias sin comida: {self.dias_sin_comida} | ') 

    def archivar(self):
        return (f"{self.nombre},{type(self).__name__},{self.magia},{self.p_escape}"
                f",{self.enfermiza},{self.enferma},{self.fugitiva},"
                f"{self.salud_max},{self.salud_actual}"
                f",{self.hambre},{self.agresividad},{self.dias_sin_comida},{self.cleptomania}")      

    @property
    def salud_actual(self):
        return self.__salud_actual
    @salud_actual.setter
    def salud_actual(self, cambio_salud):
        if cambio_salud > self.salud_max:
            self.__salud_actual = self.salud_max
        elif cambio_salud < 1:
            self.__salud_actual = 1
        else: 
            self.__salud_actual = cambio_salud
    
    @property
    def salud_max(self):
        return self.__salud_max
    @salud_max.setter
    def salud_max(self, cambio_salud_max):
        self.__salud_max = cambio_salud_max
    
    
    @property
    def dias_sin_comida(self):
        return self.__dias_sin_comida
    @dias_sin_comida.setter
    def dias_sin_comida(self, cambio_dia):
        if cambio_dia == 0:
            self.__dias_sin_comida = cambio_dia
        else: 
            self.__dias_sin_comida = cambio_dia

    @abstractmethod
    def hambre_dia(self):
        pass

    def ataque(self):
        efecto_hambre = 0
        efecto_agresividad = 0
        if "ham" in self.hambre:
            efecto_hambre = p.EFECTO_HAMBRE_HAMBRIENTA
        if "aris" in self.agresividad:
            efecto_agresividad = p.EFECTO_AGRESIVIDAD_ARISCA
        elif "peli" in self.agresividad:
            efecto_agresividad = p.EFECTO_AGRESIVIDAD_PELIGROSA
        return min(1, (efecto_hambre + efecto_agresividad) / 100)

    def escape(self):
        if not self.fugitiva and random.random() <= self.p_escape:
            self.fugitiva = True
            return True
        else:
            return False

    def enfermarse(self):
        if not self.enferma and random.random() <= self.enfermiza:
            self.enferma = True
            return True
        else:
            return False

    @abstractmethod
    def hab_especial(self):
        pass

class Augurey(Criatura):
    def __init__(self, nombre, magia, p_escape, enfermiza, enferma,\
        fugitiva, salud_max, salud_actual, hambre, agresividad,\
            dias_sin_comida, cleptomania):
        super().__init__(nombre, magia, p_escape, enfermiza, enferma,\
        fugitiva, salud_max, salud_actual, hambre, agresividad,\
            dias_sin_comida, cleptomania)
    
    def hambre_dia(self):
        super().hambre_dia()
        if self.dias_sin_comida >= 3 and self.hambre == "satisfecha":
            self.hambre = "hambrienta"
            return True
        return False

    def hab_especial(self):
        if self.hambre == "satisfecha" and not self.enferma \
            and self.salud_actual == self.salud_max:
            alimento_entregar = random.randint(1, 3)
            if alimento_entregar == 1:
                return f"Tarta de Melaza"
            elif alimento_entregar == 2:
                return f"Hígado de Dragón"
            else:
                return f"Buñuelo de Gusarajo"

class Niffler(Criatura):
    def __init__(self, nombre, magia, p_escape, enfermiza, enferma,\
        fugitiva, salud_max, salud_actual, hambre, agresividad,\
            dias_sin_comida, cleptomania):
        super().__init__(nombre, magia, p_escape, enfermiza, enferma,\
        fugitiva, salud_max, salud_actual, hambre, agresividad,\
            dias_sin_comida, cleptomania)
    
    def hambre_dia(self):
        super().hambre_dia()
        if self.dias_sin_comida >= 2 and self.hambre == "satisfecha":
            self.hambre = "hambrienta"
            return True
        return False

    def hab_especial(self):
        sickles_entregar = self.cleptomania*2
        if self.hambre == "satisfecha":
            return sickles_entregar
        else:
            return (-1) * sickles_entregar


class Erkling(Criatura):
    def __init__(self, nombre, magia, p_escape, enfermiza, enferma,\
        fugitiva, salud_max, salud_actual, hambre, agresividad,\
            dias_sin_comida, cleptomania):
        super().__init__(nombre, magia, p_escape, enfermiza, enferma,\
        fugitiva, salud_max, salud_actual, hambre, agresividad,\
            dias_sin_comida, cleptomania)
    
    def hambre_dia(self):
        super().hambre_dia()
        if self.dias_sin_comida >= 2 and self.hambre == "satisfecha":
            self.hambre = "hambrienta"
            return True
        return False
    
    def hab_especial(self):
        if self.hambre == "hambrienta":
            return True
        return False

    
