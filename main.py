from menu import MenuInicio, MenuAcciones, MenuCuidarCriaturas, MenuDCC, PasarDia
from DCC import DCC, magizoologos, criaturas
from cargar import actualizar_archivos
import parametros as p

menu = MenuInicio()
menu_a = MenuAcciones()
menu_c = MenuCuidarCriaturas()
menu_dcc = MenuDCC()
menu_dia = PasarDia()

print(f"""Bienvenido a DCCriaturas Fantásticas
"""   f"""*****************************************""")

while True:
    while menu.accion():    
        actualizar_archivos(magizoologos, menu.username, p.RUTA_MAGIZOOLOGOS,\
             criaturas, p.RUTA_CRIAT)
        dcc = DCC(str(menu.username))
        while menu_a.accion():
            terminador = 0
            if menu_a.eleccion == "1":
                while terminador == 0 and menu_c.accion():
                    if menu_c.eleccion == "1":
                        dcc.usuario.alimentar()
                        terminador = 1                     
                    elif menu_c.eleccion == "2":
                        dcc.usuario.recuperar()
                        terminador = 1 
                    elif menu_c.eleccion == "3": 
                        dcc.usuario.sanar()
                        terminador = 1     
                    elif menu_c.eleccion == "4":
                        dcc.usuario.usar_habilidad()  
                        terminador = 1
                    elif menu_c.eleccion == "5":
                        dcc.pelea()  
                        terminador = 1
                    actualizar_archivos(magizoologos, menu.username, p.RUTA_MAGIZOOLOGOS,\
                         criaturas, p.RUTA_CRIAT)     
            elif menu_a.eleccion == "2":
                while terminador == 0 and menu_dcc.accion():
                    if menu_dcc.eleccion == "1":
                        dcc.vender_criatura()
                        terminador = 1
                    elif menu_dcc.eleccion == "2":
                        dcc.vender_alimentos()
                        terminador = 1
                    elif menu_dcc.eleccion == "3":
                        print(dcc)
                        terminador = 1
                    actualizar_archivos(magizoologos, menu.username, p.RUTA_MAGIZOOLOGOS,\
                         criaturas, p.RUTA_CRIAT)  
            elif menu_a.eleccion == "3":
                menu_dia.accion()
                dcc.pasar_dia()
                actualizar_archivos(magizoologos, menu.username, p.RUTA_MAGIZOOLOGOS,\
                     criaturas, p.RUTA_CRIAT)
            
            
            
                
