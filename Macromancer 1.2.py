#!/usr/bin/env python
# Este archivo usa el encoding: utf-8

import sys
from time import sleep

def typing(str):
    for char in str:
        sleep(0.0005)
        print(char, end = '', flush = True)
    print()

def ayuda():
    typing("\nBloque de ayuda:\n\n\tSi necesitas incorporar una tirada de dados (por ej., para calcular el nú-\n\tmero de criaturas afectadas), emplea [[corchetes dobles]] para que el valor\n\tse calcule en este mismo campo.")
    typing("\tej.: \n\t\t[[1d4]]criaturas (excepto inconscientes, constructos y muertos\n\t\tvivientes) en una explosión de 10’ de radio\n")
    typing("\tSi el objetivo depende del nivel de lanzador, por ej. 'longitud de\n\t50´ + 5´/2 niveles', escríbelo de la forma:\n\n\t\tuna cuerda de [[50+5*NIVEL/2]]pies de longitud*\n\t\t*(NIVEL debe estar en mayúsculas)\n")
    typing("\tTambién puedes definir un máximo empleando la forma //ValorCalc//MAX:ValorMax//,\n\tpor ej., 'long. de 50´ + 5´/2 niveles, hasta un máximo de +25´' se escribe asi:\n\n\t\tuna pared de [[50+//5*NIVEL/2//MAX:25//]]pies de longitud\n")
    typing("Bloque de ejemplos:\n\n\tAntipatía (p200, MJ1), Objetivo: un lugar de hasta 10' cúbicos/nivel;\n\tModo de escribirlo: 'una lugar de hasta [[10*NIVEL]]pies cúbicos'")
    typing("\n\tAnimar cuerda (p200, MJ1), Objetivo: una cuerda de longitud máxima 50'+5'/nivel;\n\tModo de escribirlo: 'un cuerda de [[50+5*NIVEL]]pies de longitud'")
    typing("\n\tQuitar el miedo (p278, MJ1), Objetivo: una criatura, más 1 cada 4 niveles\n\tModo de escribirlo: '[[1+NIVEL/4]]criaturas'")
    typing("\n\tPuerta etérea (p277, MJ1), Efecto: abertura de 5×8' y 10' de prof. + 5'/3 niveles;\n\tModo de escribirlo: 'abertura de 5×8 pies y [[10+5*NIVEL/3]]pies de profunidad'")
    typing("\n\tCurar heridas leves (p225, MJ1), Descrip.: curación 1d8 puntos +1 por nivel, máx +5;\n\tModo de escribirlo: 'curación de [[1d8+//NIVEL//MAX:5//]]puntos de golpe'")
    typing("\n\tImagen múltiple (p249, MJ1), Descrip.: crea 1d4 imágenes +1/3 niveles, máx total 8;\n\tModo de escribirlo: '[[//1d4+NIVEL/3//MAX:5//]]figuras de ti'\n")

def ayuda2():
    typing("\nAquí se pueden añadir otros componentes. Si son más de uno, serpáralos con\nla barra vertical | (Alt Gr + 1 del teclado no numérico)\nej.: \n\t\tSacrificio\n\t\tCelestial | Abstención de alcohol | Luna llena")

def levelandmax(varfunction):
    for i in range(0,10):
        varfunction = varfunction.replace("NIVEL/"+str(i),"floor("+level+"/"+str(i)+")")
    varfunction = varfunction.replace("NIVEL","floor("+level+")")
    while True:
        if "//MAX:" in varfunction:
            maxpos = varfunction.find("//MAX:")
            #print("\n",maxpos)
            openpos = varfunction.rfind("//",0,maxpos)
            #print("\n",openpos)
            closepos = varfunction.find("//",maxpos+2)
            #print("\n",closepos)
            varfunction = varfunction[0:openpos]+"{"+varfunction[openpos+2:maxpos]+","+varfunction[maxpos+6:closepos]+"}dh1"+varfunction[closepos+2:]
            #print()
            #print(varfunction)
            #input()
        else:
            #print("\nDone!")
            return varfunction
            break

print(' 														     ')
print(' $$\      $$\                                                                                                         ')
print(' $$$\    $$$ |                                                                                                        ')
print(' $$$$\  $$$$ | $$$$$$\   $$$$$$$\  $$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\   $$$$$$$\  $$$$$$\   $$$$$$\  ')
print(' $$\$$\$$ $$ | \____$$\ $$  _____|$$  __$$\ $$  __$$\ $$  _$$  _$$\  \____$$\ $$  __$$\ $$  _____|$$  __$$\ $$  __$$\ ')
print(' $$ \$$$  $$ | $$$$$$$ |$$ /      $$ |  \__|$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  $$ |$$ /      $$$$$$$$ |$$ |  \__|')
print(' $$ |\$  /$$ |$$  __$$ |$$ |      $$ |      $$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |$$ |      $$   ____|$$ |      ')
print(' $$ | \_/ $$ |\$$$$$$$ |\$$$$$$$\ $$ |      \$$$$$$  |$$ | $$ | $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$\ \$$$$$$$\ $$ |      ')
print(' \__|     \__| \_______| \_______|\__|       \______/ \__| \__| \__| \_______|\__|  \__| \_______| \_______|\__|      ')
print('                                                                                                                      ')
typing("\n\t\t\t\t\t   De Neckar para Masteronomicón.")
typing("\t\t\t\t\t\t\t\t\t\t\t\t Versión actual: v1.2")
typing("\n\nBienvenidos al programador de macros de conjuros para Roll20.")
askfast = True
charcdboost = [0, 0, 0, 0, 0, 0, 0, 0, 0]
cdboostrep = False
charclboost = [0, 0, 0, 0, 0, 0, 0, 0, 0]
clboostrep = False
iteration = False
selfw = None
levelini = None
while True:
    #
    #  ____  _____ ____  _____    _  _____ 
    # |  _ \| ____|  _ \| ____|  / \|_   _|
    # | |_) |  _| | |_) |  _|   / _ \ | |  
    # |  _ <| |___|  __/| |___ / ___ \| |  
    # |_| \_\_____|_|   |_____/_/   \_\_|  
    #                                      
    #
    if iteration is not False:
        while True:
            typing("\n\n¿Quieres programar la macro de otro conjuro? (s/n)")
            repeat=input(">>> ")
            repeat=repeat.lower().strip()
            if repeat == "exit" or repeat == "no" or repeat == "n":
                typing("\n\tTERMINATING...\n\n")
                input("Presiona Enter para cerrar...")
                import os
                os._exit(0)
            elif repeat == "s" or repeat == "si" or repeat == "sí" or repeat == "y" or repeat == "yes":
                typing("\nIniciando nueva macro.\n")
                break
            else:
                typing("\nIndica sólo s/n, según quieras o no iniciar una nueva macro.")
                continue
    #
    #  _____ _    ____ _____   __  __  ___  ____  _____ 
    # |  ___/ \  / ___|_   _| |  \/  |/ _ \|  _ \| ____|
    # | |_ / _ \ \___ \ | |   | |\/| | | | | | | |  _|  
    # |  _/ ___ \ ___) || |   | |  | | |_| | |_| | |___ 
    # |_|/_/   \_\____/ |_|   |_|  |_|\___/|____/|_____|
    #
    #
    if askfast is True:
        typing("\n\tRECUERDA: SIEMPRE PUEDES SALIR ESCRIBIENDO EL COMANDO 'exit'\n\t(en minúsculas y sin comillas).\n")
        typing("¿Quieres utilizar el modo de escritura rápida? (Aparecerán los bloques de texto\ncompletos, y no letra por letra.) (s/n)")
        while True:
            fastmode=input(">>> ")
            if fastmode == "exit":
                typing("\n\tTERMINATING...\n\n")
                input("Presiona Enter para cerrar...")
                import os
                os._exit(0)
            fastmode=fastmode.lower().strip()
            if fastmode == "s" or fastmode == "si" or fastmode == "sí" or fastmode == "y" or fastmode == "yes":
                def typing(str):
                    for char in str:
                        print(char, end = '', flush = True)
                    print()
                typing("\nModo de escritura rápida activado.")
                askfast = False
                break
            elif fastmode == "n" or fastmode == "no":
                def typing(str):
                    for char in str:
                        sleep(0.0005)
                        print(char, end = '', flush = True)
                    print()
                typing("\nModo de escritura rápida desactivado.")
                break
            else:
                typing("\nIndica sólo s/n, según corresponda.")
    #
    #   ____ _   _    _    ____      _    ____ _____ _____ ____    ____   ____ 
    #  / ___| | | |  / \  |  _ \    / \  / ___|_   _| ____|  _ \  |  _ \ / ___|
    # | |   | |_| | / _ \ | |_) |  / _ \| |     | | |  _| | |_) | | | | | |    
    # | |___|  _  |/ ___ \|  _ <  / ___ \ |___  | | | |___|  _ <  | |_| | |___ 
    #  \____|_| |_/_/   \_\_| \_\/_/   \_\____| |_| |_____|_| \_\ |____/ \____|
    #                                                                          
    #
    if iteration is False:
        typing("\n\nPor raza o clase (por ej., por ser gnomo, o por la dote Soltura con una escuela\nde magia), ¿tu personaje lanza conjuros de alguna ESCUELA en particular (no sólo\neste conjuro) con UNA CD MAYOR? (s/n)")
        while True:
            if cdboostrep is True:
                typing("\n\n¿Quieres potenciar alguna otra escuela? (s/n)")
            cdboostyn=input(">>> ")
            if cdboostyn == "exit":
                typing("\n\tTERMINATING...\n\n")
                input("Presiona Enter para cerrar...")
                import os
                os._exit(0)
            cdboostyn=cdboostyn.lower().strip()
            if cdboostyn == "s" or cdboostyn == "si" or cdboostyn == "sí" or cdboostyn == "y" or cdboostyn == "yes":
                typing("\n\nIndica la escuela de CD a potenciar:\n\t(Ab)juración\n\t(Ad)ivinación\n\t(Co)njuración\n\t(En)cantamiento\n\t(Ev)ocación\n\t(Il)usión\n\t(Ni)gromancia\n\t(Tr)ansmutación\n\t(Un)iversal")
                while True:
                    cdboostsch=input(">>> ").lower()
                    if cdboostsch == "exit":
                        typing("\n\tTERMINATING...\n\n")
                        input("Presiona Enter para cerrar...")
                        import os
                        os._exit(0)
                    elif not (cdboostsch == "ab" or cdboostsch == "ad" or cdboostsch == "co" or cdboostsch == "en" or cdboostsch == "ev" or cdboostsch == "il" or cdboostsch == "ni" or cdboostsch == "tr" or cdboostsch == "un"):
                        typing("\nError: Usa sólo las dos letras indicadas según la escuela")
                        continue
                    elif cdboostsch == "ab":
                        ischool = 0
                    elif cdboostsch == "ad":
                        ischool = 1
                    elif cdboostsch == "co":
                        ischool = 2
                    elif cdboostsch == "en":
                        ischool = 3
                    elif cdboostsch == "ev":
                        ischool = 4
                    elif cdboostsch == "il":
                        ischool = 5
                    elif cdboostsch == "ni":
                        ischool = 6
                    elif cdboostsch == "tr":
                        ischool = 7
                    elif cdboostsch == "un":
                        ischool = 8
                    break
                typing("\n\nIndica en cuánto aumenta la CD de esta escuela:")
                while True:
                    cdboost=input(">>> ")
                    if cdboost == "exit":
                        typing("\n\tTERMINATING...\n\n")
                        input("Presiona Enter para cerrar...")
                        import os
                        os._exit(0)
                    cdboost = cdboost.strip()
                    try:
                        cdboost = int(cdboost)
                    except:
                        typing("\nError. Debes introducir un número entero.")
                        continue
                    charcdboost[ischool] = charcdboost[ischool] + cdboost
                    typing("\nSumando bonificador...")
                    break
                cdboostrep = True
                continue
            elif cdboostyn == "n" or cdboostyn == "no":
                break
            else:
                typing("\nIndica sólo s/n, según corresponda.")
    #
    #   ____ _   _    _    ____       ____    _    ____ _____ _____ ____    _     _______     _______ _     
    #  / ___| | | |  / \  |  _ \     / ___|  / \  / ___|_   _| ____|  _ \  | |   | ____\ \   / / ____| |    
    # | |   | |_| | / _ \ | |_) |   | |     / _ \ \___ \ | | |  _| | |_) | | |   |  _|  \ \ / /|  _| | |    
    # | |___|  _  |/ ___ \|  _ < _  | |___ / ___ \ ___) || | | |___|  _ <  | |___| |___  \ V / | |___| |___ 
    #  \____|_| |_/_/   \_\_| \_(_)  \____/_/   \_\____/ |_| |_____|_| \_\ |_____|_____|  \_/  |_____|_____|
    #                                                                                                       
    #
    if iteration is False:
        typing("\n\nPor raza o clase (por ej., gracias a la dote Lanzador de conjuros veterano), ¿tu\npersonaje lanza conjuros de alguna ESCUELA en particular (no sólo este conjuro)\ncon MAYOR NIVEL DE LANZADOR? (s/n)")
        while True:
            if clboostrep is True:
                typing("\n\n¿Quieres potenciar alguna otra escuela? (s/n)")
            clboostyn=input(">>> ")
            if clboostyn == "exit":
                typing("\n\tTERMINATING...\n\n")
                input("Presiona Enter para cerrar...")
                import os
                os._exit(0)
            clboostyn=clboostyn.lower().strip()
            if clboostyn == "s" or clboostyn == "si" or clboostyn == "sí" or clboostyn == "y" or clboostyn == "yes":
                typing("\n\nIndica la escuela de NIVEL DE LANZADOR a potenciar:\n\t(Ab)juración\n\t(Ad)ivinación\n\t(Co)njuración\n\t(En)cantamiento\n\t(Ev)ocación\n\t(Il)usión\n\t(Ni)gromancia\n\t(Tr)ansmutación\n\t(Un)iversal")
                while True:
                    clboostsch=input(">>> ").lower()
                    if clboostsch == "exit":
                        typing("\n\tTERMINATING...\n\n")
                        input("Presiona Enter para cerrar...")
                        import os
                        os._exit(0)
                    elif not (clboostsch == "ab" or clboostsch == "ad" or clboostsch == "co" or clboostsch == "en" or clboostsch == "ev" or clboostsch == "il" or clboostsch == "ni" or clboostsch == "tr" or clboostsch == "un"):
                        typing("\nError: Usa sólo las dos letras indicadas según la escuela")
                        continue
                    elif clboostsch == "ab":
                        ischool = 0
                    elif clboostsch == "ad":
                        ischool = 1
                    elif clboostsch == "co":
                        ischool = 2
                    elif clboostsch == "en":
                        ischool = 3
                    elif clboostsch == "ev":
                        ischool = 4
                    elif clboostsch == "il":
                        ischool = 5
                    elif clboostsch == "ni":
                        ischool = 6
                    elif clboostsch == "tr":
                        ischool = 7
                    elif clboostsch == "un":
                        ischool = 8
                    break
                typing("\n\nIndica en cuánto aumenta el NIVEL DE LANZADOR de esta escuela:")
                while True:
                    clboost=input(">>> ")
                    if clboost == "exit":
                        typing("\n\tTERMINATING...\n\n")
                        input("Presiona Enter para cerrar...")
                        import os
                        os._exit(0)
                    clboost = clboost.strip()
                    try:
                        clboost = int(clboost)
                    except:
                        typing("\nError. Debes introducir un número entero.")
                        continue
                    charclboost[ischool] = charclboost[ischool] + clboost
                    typing("\nSumando bonificador...")
                    break
                clboostrep = True
                continue
            elif clboostyn == "n" or clboostyn == "no":
                break
            else:
                typing("\nIndica sólo s/n, según corresponda.")         
    #
    #  ____  _____ _     _____      ____        __
    # / ___|| ____| |   |  ___|    / /\ \      / /
    # \___ \|  _| | |   | |_      / /  \ \ /\ / / 
    #  ___) | |___| |___|  _|    / /    \ V  V /  
    # |____/|_____|_____|_|     /_/      \_/\_/   
    #                                             
    #
    macro = "&{template:DnD35StdRoll} {{spellflag=true}} {{name=@{character_name} @{character-name2} }} {{subtags=Lanza "
    if selfw is None:
        while True:
            typing("\n\nSe recomienda activar la pregunta Autosusurro, para visualizar el\nconjuro antes de lanzarlo. ¿Quieres incorporarla a tus conjuros? (s/n)")
            selfyn=input(">>> ")
            selfyn=selfyn.lower().strip()
            if selfyn == "exit":
                typing("\n\tTERMINATING...\n\n")
                input("Presiona Enter para cerrar...")
                import os
                os._exit(0)
            elif selfyn == "no" or selfyn == "n":
                typing("\nNo se añade Autosusurro.\n")
                selfw = 0
                print()
                break
            elif selfyn == "s" or selfyn == "si" or selfyn == "sí" or selfyn == "y" or selfyn == "yes":
                typing("\nSe añade pregunta de Autosusurro.\n")
                macro = "?{¿Autosusurro? |No, |Sí,/w @{character_name}} " + macro
                selfw = 1
                print()
                break
            else:
                typing("\nIndica sólo s/n, según quieras o no iniciar añadir la pregunta Autosusurro.")
                continue
    elif selfw == 1:
        macro = "?{¿Autosusurro? |No, |Sí,/w @{character_name}} " + macro
    #
    #  _______   ______  _____ 
    # |_   _\ \ / /  _ \| ____|
    #   | |  \ V /| |_) |  _|  
    #   | |   | | |  __/| |___ 
    #   |_|   |_| |_|   |_____|
    #                          
    #   
    if levelini is None:
        typing("Determina si estos conjuros serán de tipo (a)rcano o (d)ivino (para Full\nMode), o (g)eneral (para Base Mode).\n\nFull o Base se eligen en la pestaña Hechizos(Spells) en la ficha de Roll20,\nen la parte más superior (ver https://i.imgur.com/Wa1Q0kq.png):")
        while True:
            shtype=input(">>> ").lower()
            if shtype == "exit":
                typing("\n\tTERMINATING...\n\n")
                input("Presiona Enter para cerrar...")
                import os
                os._exit(0)
            elif shtype == "a":
                levelini="@{arcanecasterlevel}"
                print("\n")
                break
            elif shtype == "d":
                levelini="@{divinecasterlevel}"
                print("\n")
                break
            elif shtype == "g":
                levelini="@{casterlevel}"
                print("\n")
                break
            else:
                typing("\nMala entrada. Escribe a, d o g, según el tipo de conjuros a programar.")     
    #
    #  _   _    _    __  __ _____ 
    # | \ | |  / \  |  \/  | ____|
    # |  \| | / _ \ | |\/| |  _|  
    # | |\  |/ ___ \| |  | | |___ 
    # |_| \_/_/   \_\_|  |_|_____|
    #                             
    #
    if iteration is False:
        typing("Iniciando programación de conjuros...")
    print("\n\n")
    typing("Escribe el nombre del conjuro:")
    while True:
        spname=input(">>> ")
        if spname == "":
            typing("\nIntroduce al menos un caracter.")
            continue
        spname2 = spname.upper().strip()
        break
    macro=macro+"**"+spname2+"**}}"
    print("\n\n")
    #
    #  ____   _    ____ _____ 
    # |  _ \ / \  / ___| ____|
    # | |_) / _ \| |  _|  _|  
    # |  __/ ___ \ |_| | |___ 
    # |_| /_/   \_\____|_____|
    #                         
    #
    typing("Indica el número de página del libro en el que se encuentra el conjuro y a continua-")
    typing("ción, luego de una coma, las siglas del libro donde está definido.\n")
    typing("Escribe los libros con dos a cinco caracteres, como MJ1 (Manual del Jugador 1), MM1")
    typing("Manual de Monstruos 1), MAG (Magia de Faerun), GJ (Guía del Jugador de Faerun)...\n")
    typing("Ej.: \n\t245, MJ1\n\t75, MAG; 233, GJ\n\t201, DM1\n")
    while True:
        typing("Si no conoces la ubicación, escribe 'no'.")
        locat=input(">>> ")
        if locat == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        elif locat == "":
            typing("\nIntroduce al menos un caracter.")
            continue
        elif not locat == "no":
            locat2 = " {{Ubicación:= p"+locat.strip()+"}}"
            macro = macro + locat2
        break
    macro = macro + " {{Escuela:= "
    print("\n\n")
    #
    #  ____  ____  _____ _     _       _     _______     _______ _     
    # / ___||  _ \| ____| |   | |     | |   | ____\ \   / / ____| |    
    # \___ \| |_) |  _| | |   | |     | |   |  _|  \ \ / /|  _| | |    
    #  ___) |  __/| |___| |___| |___  | |___| |___  \ V / | |___| |___ 
    # |____/|_|   |_____|_____|_____| |_____|_____|  \_/  |_____|_____|
    #                                                                  
    #
    typing("Escribe el nivel del conjuro según el tipo de tipo de lanzador que vayas a utilizar,")
    typing("ej.: \n\tPara un conjuro tipo Brd 2, Hcr/Mag 3, escribe 2 si lo utili-")
    typing("\tzarás como bardo, o 3 si lo emplearás como hechicero o mago.")
    typing("\n(Si por alguna razón el nivel REAL del conjuro es mayor, como ser por uso de la dote")
    typing("Intensificar conjuro (ESTE CONJURO), escribe el nivel efectivo del conjuro. Ten en")
    typing("cuenta que tus bonificadores de personaje por ESCUELA ya están incluidos.)")
    while True:
        splvl=input(">>> ")
        if splvl == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        splvl2 = splvl.strip()
        if splvl2 != "0" and splvl2 != "1" and splvl2 != "2" and splvl2 != "3" and splvl2 != "4" and splvl2 != "5" and splvl2 != "6" and splvl2 != "7" and splvl2 != "8" and splvl2 != "9" and splvl2 != "10":
            typing("\nError. Debes introducir un número entero entre 0 y 10.")
            continue
        else:
            spelldc="@{spelldc"+splvl2+"}"
        break
    #print()
    #print(spelldc)
    print("\n\n")
    #
    #  ____   ____ _   _  ___   ___  _     
    # / ___| / ___| | | |/ _ \ / _ \| |    
    # \___ \| |   | |_| | | | | | | | |    
    #  ___) | |___|  _  | |_| | |_| | |___ 
    # |____/ \____|_| |_|\___/ \___/|_____|
    #                                      
    #
    typing("Indica si tu conjuro pertenece a la escuela de:\n\t(Ab)juración\n\t(Ad)ivinación\n\t(Co)njuración\n\t(En)cantamiento\n\t(Ev)ocación\n\t(Il)usión\n\t(Ni)gromancia\n\t(Tr)ansmutación\n\t(Un)iversal")
    while True:
        school=input(">>> ").lower()
        if school == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        elif not (school == "ab" or school == "ad" or school == "co" or school == "en" or school == "ev" or school == "il" or school == "ni" or school == "tr" or school == "un"):
            typing("\nError: Usa sólo las dos letras indicadas según la escuela.")
            continue
        elif school == "ab":
            school2 = "Abjuración "
            iii = 0
        elif school == "ad":
            school2 = "Adivinación "
            iii = 1
        elif school == "co":
            school2 = "Conjuración "
            iii = 2
        elif school == "en":
            school2 = "Encantamiento "
            iii = 3
        elif school == "ev":
            school2 = "Evocación "
            iii = 4
        elif school == "il":
            school2 = "Ilusión "
            iii = 5
        elif school == "ni":
            school2 = "Nigromancia "
            iii = 6
        elif school == "tr":
            school2 = "Transmutación "
            iii = 7
        elif school == "un":
            school2 = "Universal "
            iii = 8
        break
    macro = macro+school2
    print("\n\n")
    #
    #  ____  _   _ ____ ____   ____ _   _  ___   ___  _     
    # / ___|| | | | __ ) ___| / ___| | | |/ _ \ / _ \| |    
    # \___ \| | | |  _ \___ \| |   | |_| | | | | | | | |    
    #  ___) | |_| | |_) |__) | |___|  _  | |_| | |_| | |___ 
    # |____/ \___/|____/____/ \____|_| |_|\___/ \___/|_____|
    #                                                       
    #
    typing("Indica el nombre de una (Subescuela), evitando errores ortográficos,")
    typing("ej.: \n\tCompulsión\n\tEngaño\n\tFantasmagoría\n")
    typing("Si no tiene o no conoces la subescuela, escribe 'no' o presiona Enter")
    subsch=input(">>> ")
    if subsch == "exit":
        typing("\n\tTERMINATING...\n\n")
        input("Presiona Enter para cerrar...")
        import os
        os._exit(0)
    if subsch != "no" and subsch != "":
        subsch2 = subsch.lower().strip()
        subsch2 = subsch2[0].upper()+subsch2[1:]
        subsch2 = "(" + subsch2 + ")"
        macro = macro + subsch2
    macro = macro + "}}"
    #print()
    #try:
    #    print(subsch2)
    print("\n\n")
    #
    #  ____  _____ ____   ____ ____  ___ ____ _____ ___  ____  
    # |  _ \| ____/ ___| / ___|  _ \|_ _|  _ \_   _/ _ \|  _ \ 
    # | | | |  _| \___ \| |   | |_) || || |_) || || | | | |_) |
    # | |_| | |___ ___) | |___|  _ < | ||  __/ | || |_| |  _ < 
    # |____/|_____|____/ \____|_| \_\___|_|    |_| \___/|_| \_\
    #                                                          
    #
    typing("Indica el/los [Descriptor(es)] del conjuro, de poseerlo(s),")
    typing("ej.: \n\tEnajenador, Dependiente del Idioma\n\tOscuridad\n\tLegal, Fuego\n")
    typing("Si no los tiene o no los conoces, escribe 'no' o presiona Enter")
    descrip=input(">>> ")
    if descrip == "exit":
        typing("\n\tTERMINATING...\n\n")
        input("Presiona Enter para cerrar...")
        import os
        os._exit(0)
    elif descrip != "no" and descrip != "" and descrip != " ":
        descrip2 = descrip.lower().strip()
        descrip2 = descrip2.replace("  "," ")
        descrip2 = descrip2.replace(" ,",",")
        descrip2 = descrip2.replace(", ",",")
        if "," in descrip2:
            i = descrip2.find(",")
            descrip2 = descrip2[:i+1]+" "+descrip2[i+1].upper()+descrip2[i+2:]
        descrip2 = descrip2[0].upper()+descrip2[1:]
        descrip2 = " {{Descriptor:= " + descrip2 + "}}"
        macro = macro + descrip2
    print("\n\n")
    #
    #  ____   ___   ___  ____ _____ ____  
    # | __ ) / _ \ / _ \/ ___|_   _/ ___| 
    # |  _ \| | | | | | \___ \ | | \___ \ 
    # | |_) | |_| | |_| |___) || |  ___) |
    # |____/ \___/ \___/|____/ |_| |____/ 
    #                                     
    #
    typing("Este conjuro en particular, ¿posee una CD mayor a la normal (por ej., por\nuso de la dote Agotamiento arcano)? (s/n)")
    while True:
        cdboostcase=input(">>> ")
        if cdboostcase == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        cdboostcase = cdboostcase.lower().strip()
        if cdboostcase == "s" or cdboostcase == "si" or cdboostcase == "sí" or cdboostcase == "y" or cdboostcase == "yes":
            typing("\nIndica el bonificador de CD puntual para este conjuro:")
            while True:
                cdboostcasevalue=input(">>> ")
                if cdboostcasevalue == "exit":
                    typing("\n\tTERMINATING...\n\n")
                    input("Presiona Enter para cerrar...")
                    import os
                    os._exit(0)
                cdboostcasevalue = cdboostcasevalue.strip()
                try:
                    cdboostcasevalue = int(cdboostcasevalue)
                except:
                    typing("\nError. Debes introducir un número entero.")
                    continue
                spelldc = spelldc + "+" + str(cdboostcasevalue)
                typing("\nSumando bonificador...")
                break
            break
        elif cdboostcase == "n" or cdboostcase == "no" or cdboostcase == "":
            typing("\nNo posee bonificador puntual a la CD.")
            break
        else:
            typing("\nIndica sólo s/n, según corresponda.")
    print("\n\n")
    typing("Este conjuro en particular, ¿es como si fuera lanzado por un NIVEL DE LAN-\nZADOR mayor al normal (por ej., por la dote Tesis arcana)? (s/n)")
    while True:
        clboostcase=input(">>> ")
        if clboostcase == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        clboostcase = clboostcase.lower().strip()
        if clboostcase == "s" or clboostcase == "si" or clboostcase == "sí" or clboostcase == "y" or clboostcase == "yes":
            typing("\nIndica el bonificador de NIVEL DE LANZADOR puntual para este conjuro:")
            while True:
                clboostcasevalue=input(">>> ")
                if clboostcasevalue == "exit":
                    typing("\n\tTERMINATING...\n\n")
                    input("Presiona Enter para cerrar...")
                    import os
                    os._exit(0)
                clboostcasevalue = clboostcasevalue.strip()
                try:
                    clboostcasevalue = int(clboostcasevalue)
                except:
                    typing("\nError. Debes introducir un número entero.")
                    continue
                level = levelini + "+" + str(clboostcasevalue)
                typing("\nSumando bonificador...")
                break
            break
        elif clboostcase == "n" or clboostcase == "no" or clboostcase == "":
            typing("\nNo posee bonificador puntual de NIVEL DE LANZADOR.")
            level = levelini
            break
        else:
            typing("\nIndica sólo s/n, según corresponda.")
    spelldc = "(" + spelldc + "+" + str(charcdboost[iii]) + ")"
    level = "(" + level + "+" + str(charclboost[iii]) + ")"
    print("\n\n")
    #
    #   ____    _    ____ _____ _____ ____     ___     _     _______     _______ _     
    #  / ___|  / \  / ___|_   _| ____|  _ \   ( _ )   | |   | ____\ \   / / ____| |    
    # | |     / _ \ \___ \ | | |  _| | |_) |  / _ \/\ | |   |  _|  \ \ / /|  _| | |    
    # | |___ / ___ \ ___) || | | |___|  _ <  | (_>  < | |___| |___  \ V / | |___| |___ 
    #  \____/_/   \_\____/ |_| |_____|_| \_\  \___/\/ |_____|_____|  \_/  |_____|_____|
    #                                                                                  
    #
    typing("Para que aparezca en el bloque, indica las clases lanzadoras y niveles\nque pueden lanzar este conjuro. Recuerda emplear la nomenclatura del manual.")
    typing("ej.: \n\tBrd 2, Hcr/Mag 3\n\tViaje, Brd 0, Drd 1, Clr 1\n\tHcr/Mag 6 (mago rojo)\n")
    while True:
        castclass=input(">>> ")
        if castclass == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        elif castclass.strip() == "":
            typing("\nError. Introduzca la clase y nivel del conjuro.")
            continue
        else:
            castclass2 = " {{Nivel:= " + castclass.strip() + "}}"
            macro = macro + castclass2
            break
    #print()
    #print(castclass2)
    #print(macro)
    #
    # __     __   ____ ___  __  __ ____   ___  _   _ _____ _   _ _____ 
    # \ \   / /  / ___/ _ \|  \/  |  _ \ / _ \| \ | | ____| \ | |_   _|
    #  \ \ / /  | |  | | | | |\/| | |_) | | | |  \| |  _| |  \| | | |  
    #   \ V /   | |__| |_| | |  | |  __/| |_| | |\  | |___| |\  | | |  
    #    \_/     \____\___/|_|  |_|_|    \___/|_| \_|_____|_| \_| |_|  
    #                                                                  
    #
    print("\n\n")
    macro = macro + " {{Comp:= "
    while True:
        typing("El conjuro, ¿tiene componente verbal (V)? (s/n)")
        q1=input(">>> ")
        if q1 == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        q1=q1.lower().strip()
        if q1 == "s" or q1 == "si" or q1 == "sí" or q1 == "y" or q1 == "yes" or q1 == "v":
            macro = macro + "V | "
            typing("\nSí tiene V.")
            break
        elif q1 == "n" or q1 == "no":
            typing("No posee componente verbal.")
            break
        else:
            typing("\nIndica sólo s/n, según corresponda.")
    print("\n\n")
    #
    #  ____     ____ ___  __  __ ____   ___  _   _ _____ _   _ _____ 
    # / ___|   / ___/ _ \|  \/  |  _ \ / _ \| \ | | ____| \ | |_   _|
    # \___ \  | |  | | | | |\/| | |_) | | | |  \| |  _| |  \| | | |  
    #  ___) | | |__| |_| | |  | |  __/| |_| | |\  | |___| |\  | | |  
    # |____/   \____\___/|_|  |_|_|    \___/|_| \_|_____|_| \_| |_|  
    #                                                                
    #
    while True:
        typing("El conjuro, ¿tiene componente somático (S)? (s/n)")
        q2=input(">>> ")
        if q2 == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        q2=q2.lower().strip()
        if q2 == "s" or q2 == "si" or q2 == "sí" or q2 == "y" or q2 == "yes" or q2 == "s":
            typing("\nSí tiene S.")
            macro = macro + "S | "
            break
        elif q2 == "n" or q2 == "no":
            typing("No posee componente somático.")
            break
        else:
            typing("\nIndica sólo s/n, según corresponda.")
    print("\n\n")
    #
    #  __  __    ____ ___  __  __ ____   ___  _   _ _____ _   _ _____ 
    # |  \/  |  / ___/ _ \|  \/  |  _ \ / _ \| \ | | ____| \ | |_   _|
    # | |\/| | | |  | | | | |\/| | |_) | | | |  \| |  _| |  \| | | |  
    # | |  | | | |__| |_| | |  | |  __/| |_| | |\  | |___| |\  | | |  
    # |_|  |_|  \____\___/|_|  |_|_|    \___/|_| \_|_____|_| \_| |_|  
    #                                                                 
    #
    while True:
        typing("El conjuro, ¿tiene componente material (M)? (s/n)")
        q3=input(">>> ")
        if q3 == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        q3=q3.lower().strip()
        if q3 == "s" or q3 == "si" or q3 == "sí" or q3 == "y" or q3 == "yes" or q3 == "m":
            typing("\nSí tiene M.")
            macro = macro + "M | "
            break
        elif q3 == "n" or q3 == "no":
            typing("No posee componente material.")
            break
        else:
            typing("\nIndica sólo s/n, según corresponda.")
    print("\n\n")
    #
    #  _____    ____ ___  __  __ ____   ___  _   _ _____ _   _ _____ 
    # |  ___|  / ___/ _ \|  \/  |  _ \ / _ \| \ | | ____| \ | |_   _|
    # | |_    | |  | | | | |\/| | |_) | | | |  \| |  _| |  \| | | |  
    # |  _|   | |__| |_| | |  | |  __/| |_| | |\  | |___| |\  | | |  
    # |_|      \____\___/|_|  |_|_|    \___/|_| \_|_____|_| \_| |_|  
    #                                                                
    #
    while True:
        typing("El conjuro, ¿emplea foco (F), foco divino (FD), ambos (F/FD) o ninguno (no)? (f/fd/ffd/no)")
        q4=input(">>> ")
        if q4 == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        q4=q4.lower().strip()
        if q4 == "f":
            macro = macro + "F | "
            typing("\nEl conjuro tiene foco (F).")
            break
        elif q4 == "fd":
            macro = macro + "FD | "
            typing("\nEl conjuro tiene foco divino (FD).")
            break
        elif q4 == "ffd":
            macro = macro + "F/FD | "
            typing("\nEl conjuro tiene foco/foco divino (F/FD).")
            break
        elif q4 == "n" or q4 == "no":
            typing("\nNo posee foco de ningún tipo.")
            break
        else:
            typing("\nIndica sólo f, fd, ffd, o no, según corresponda.")
    print("\n\n")
    #
    #   ___     ____ ___  __  __ ____   ___  _   _ _____ _   _ _____ 
    #  / _ \   / ___/ _ \|  \/  |  _ \ / _ \| \ | | ____| \ | |_   _|
    # | | | | | |  | | | | |\/| | |_) | | | |  \| |  _| |  \| | | |  
    # | |_| | | |__| |_| | |  | |  __/| |_| | |\  | |___| |\  | | |  
    #  \___/   \____\___/|_|  |_|_|    \___/|_| \_|_____|_| \_| |_|  
    #                                                                
    #
    typing("Indica aquí si el conjuro posee otro tipo de componente.")
    typing("Para visualizar el bloque de ayuda, escribe 'ayuda' (sin comillas) y presiona Enter")
    typing("\nSi no tiene más componentes, escribe 'no' o presiona Enter")
    while True:
        q5=input(">>> ")
        if q5 == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        elif q5.lower().strip() == "ayuda":
            ayuda2()
            continue
        elif q5.lower().strip() == "no" or q5.lower().strip() == "n" or q5.lower().strip() == "":
            typing("\nEl conjuro no tiene más componentes.")
            break
        else:
            q52 = q5.strip()
            q52 = q52[0].upper()+q52[1:]
            macro = macro + q52 + " | "
            typing("\nComponente(s) añadido(s).")
            break
    macro = macro[:len(macro)-3]+"}}"
    print("\n\n")
    #
    #  _        _   _   _ _   _  ____ _   _   _____ ___ __  __ _____ 
    # | |      / \ | | | | \ | |/ ___| | | | |_   _|_ _|  \/  | ____|
    # | |     / _ \| | | |  \| | |   | |_| |   | |  | || |\/| |  _|  
    # | |___ / ___ \ |_| | |\  | |___|  _  |   | |  | || |  | | |___ 
    # |_____/_/   \_\___/|_| \_|\____|_| |_|   |_| |___|_|  |_|_____|
    #                                                                
    #
    typing("Indica la unidad de tiempo de lanzamiento:")
    typing("\t(1): 1 acción estándar")
    typing("\t(ac): accion(es) de asalto completo")
    typing("\t(m): minuto(s)")
    typing("\t(h): hora(s)")
    typing("\t(d): día(s)")
    typing("\t(o)tro, a definir")
    while True:
        ltime=input(">>> ")
        if ltime == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        ltime2=ltime.lower().strip()
        if ltime2 != "1" and ltime2 != "ac" and ltime2 != "m" and ltime2 != "h" and ltime2 != "d" and ltime2 != "o":
            typing("\nPor favor, indica alguna de las anteriores opciones.")
            continue
        elif ltime2 == "1":
            ltime2 = " {{Tlanz:= 1 acción estándar}}"
            break
        elif ltime2 == "ac":
            ltime2 = " accion(es) de asalto completo}}"
            break
        elif ltime2 == "m":
            ltime2 = " minuto(s)}}"
            break
        elif ltime2 == "h":
            ltime2 = " hora(s)}}"
            break
        elif ltime2 == "d":
            ltime2 = " día(s)}}"
            break
        else:
            typing("\nIndica la unidad de tiempo de lanzamiento:")
            ltime2 = input(">>>").lower().strip()+"}}"
            break
    if ltime.lower().strip() != "1":
        print("\n\n")
        typing("Indica el número de unidades de tiempo de lanzamiento:")
        typing("\tej.: 1, 1.5, 10...")
        while True:
            numltime = input(">>> ")
            if numltime == "exit":
                typing("\n\tTERMINATING...\n\n")
                input("Presiona Enter para cerrar...")
                import os
                os._exit(0)
            numltime2=numltime.lower().strip()
            try:
                float(numltime2)
                ltime2 = " {{Tlanz:= " + str(numltime2) + " " + ltime2
                break
            except:
                typing("\nPor favor, introduce un número.")
                continue
    macro = macro + ltime2   
    #print()
    #print(ltime)
    #print(ltime2)
    print("\n\n")
    #
    #  ____      _    _   _  ____ _____ 
    # |  _ \    / \  | \ | |/ ___| ____|
    # | |_) |  / _ \ |  \| | |  _|  _|  
    # |  _ <  / ___ \| |\  | |_| | |___ 
    # |_| \_\/_/   \_\_| \_|\____|_____|
    #                                   
    #
    typing("Selecciona un alcance de conjuro (más de una opción es posible, se vol-\nverá a preguntar):")
    rangeif = 0
    while True:
        if rangeif == 1:
            macro = macro + lrange2
            #print()
            #print(macro)
            print()
            typing("\n\n¿Quieres añadir un alcance de conjuro adicional?")
        if rangeif != 2:
            typing("\t(p)ersonal")
            typing("\t(t)oque")
            typing("\t(c)orto (25' + 5'/2 niveles de lanzador)")
            typing("\t(i)ntermedio (100' + 10'/nivel de lanzador)")
            typing("\t(l)argo (400' + 40'/nivel de lanzador)")
            typing("\t(f)ijo, en pies")
            typing("\t(o)tro, a definir")
            typing("\t(n)o, pasar a la siguiente pregunta")
        rangeif = 1
        lrange=input(">>> ")
        if lrange == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        lrange2=lrange.lower().strip()
        if lrange2 != "p" and lrange2 != "t" and lrange2 != "c" and lrange2 != "i" and lrange2 != "l" and lrange2 != "f" and lrange2 != "o" and lrange2 != "n" and lrange2 != "no":
            typing("\nPor favor, indica alguna de las anteriores opciones; se podrá añadir más de un alcance.")
            rangeif = 2
            continue
        #
        #  ____  _____ ____  ____   ___  _   _    _    _     
        # |  _ \| ____|  _ \/ ___| / _ \| \ | |  / \  | |    
        # | |_) |  _| | |_) \___ \| | | |  \| | / _ \ | |    
        # |  __/| |___|  _ < ___) | |_| | |\  |/ ___ \| |___ 
        # |_|   |_____|_| \_\____/ \___/|_| \_/_/   \_\_____|
        #                                                    
        #
        elif lrange2 == "p":
            typing("\nEl conjuro tiene alcance personal")
            lrange2 = " {{Alcance:= Personal}}"
            continue
        #
        #  _____ ___  _   _  ____ _   _ 
        # |_   _/ _ \| | | |/ ___| | | |
        #   | || | | | | | | |   | |_| |
        #   | || |_| | |_| | |___|  _  |
        #   |_| \___/ \___/ \____|_| |_|
        #                               
        #
        elif lrange2 == "t":
            typing("\nEl conjuro tiene alcance de toque.\n\n\n¿Requiere de una tirada de ataque? (s/n)")
            while True:
                attackr=input(">>> ").lower().strip()
                if attackr == "exit":
                    typing("\n\tTERMINATING...\n\n")
                    input("Presiona Enter para cerrar...")
                    import os
                    os._exit(0)
                elif attackr == "s" or attackr == "si" or attackr == "sí" or attackr == "y" or attackr == "yes":
                    typing("\nSí, se añade tirada de ataque.")
                    lrange2 = " {{Alcance:= Toque}} {{Ataque c/c:= [[1d20+@{meleeattackbonus}]]vs CA de Toque}}"
                    typing("\n\n¿Tiene posibilidad de crítico? Por defecto, todos los conjuros que\nexigen tiradas de ataque (como contacto electrizante y flecha ácida\nde Melf) pueden dar lugar a un crítico, mientras que rayo relampa-\ngueante no. Recuerda que, por ej., Curar Heridas no da lugar a crí-\ntico, pero utilizar 'curar' para herir a muertos vivientes implica\nuna tirada de ataque con posibilidad de crítico. Ante la duda, se-\nlecciona que sí; luego puedes borrarlo. (s/n)")
                    while True:
                        crchance=input(">>> ").lower().strip()
                        if crchance == "exit":
                            typing("\n\tTERMINATING...\n\n")
                            input("Presiona Enter para cerrar...")
                            import os
                            os._exit(0)
                        elif crchance == "s" or crchance == "si" or crchance == "sí" or crchance == "y" or crchance == "yes":
                            typing("\nSí, se añade confirmación de crítico.")
                            lrange2 = lrange2 + " {{En caso de Crítico:= Confirmación c/c [[1d20+@{meleeattackbonus}]]vs CA de Toque}}"
                            break
                        elif crchance == "n" or crchance == "no":
                            typing("\nNo tiene posibilidad de crítico.")
                            break
                        else:
                            typing("\nIndica sólo s/n, según corresponda.")
                    break
                elif attackr == "n" or attackr == "no":
                    typing("\nNo posee tirada de ataque.")
                    lrange2 = " {{Alcance:= Toque}}"
                    break
                else:
                    typing("\nIndica sólo s/n, según corresponda.")
            continue
        #
        #  ____  _   _  ___  ____ _____ 
        # / ___|| | | |/ _ \|  _ \_   _|
        # \___ \| |_| | | | | |_) || |  
        #  ___) |  _  | |_| |  _ < | |  
        # |____/|_| |_|\___/|_| \_\|_|  
        #                               
        #
        elif lrange2 == "c":
            typing("\nEl conjuro tiene alcance corto.\n\n\n¿Requiere de una tirada de ataque? (s/n)")
            while True:
                attackr=input(">>> ").lower().strip()
                if attackr == "exit":
                    typing("\n\tTERMINATING...\n\n")
                    input("Presiona Enter para cerrar...")
                    import os
                    os._exit(0)
                elif attackr == "s" or attackr == "si" or attackr == "sí" or attackr == "y" or attackr == "yes":
                    typing("\nSí, se añade tirada de ataque.")
                    lrange2 = " {{Alcance:= Corto ([[25+5*floor("+level+"/2)]]pies)}} {{Ataque de toque a distancia:= [[1d20+@{rangedattackbonus}]]vs CA de Toque}}"
                    typing("\n\n¿Tiene posibilidad de crítico? Por defecto, todos los conjuros que\nexigen tiradas de ataque (como contacto electrizante y flecha ácida\nde Melf) pueden dar lugar a un crítico, mientras que rayo relampa-\ngueante no. Recuerda que, por ej., Curar Heridas no da lugar a crí-\ntico, pero utilizar 'curar' para herir a muertos vivientes implica\nuna tirada de ataque con posibilidad de crítico. Ante la duda, se-\nlecciona que sí; luego puedes borrarlo. (s/n)")
                    while True:
                        crchance=input(">>> ").lower().strip()
                        if crchance == "exit":
                            typing("\n\tTERMINATING...\n\n")
                            input("Presiona Enter para cerrar...")
                            import os
                            os._exit(0)
                        elif crchance == "s" or crchance == "si" or crchance == "sí" or crchance == "y" or crchance == "yes":
                            typing("\nSí, se añade confirmación de crítico.")
                            lrange2 = lrange2 + " {{En caso de Crítico:= Confirmación a dist. [[1d20+@{rangedattackbonus}]]vs CA de Toque}}"
                            break
                        elif crchance == "n" or crchance == "no":
                            typing("\nNo tiene posibilidad de crítico.")
                            break
                        else:
                            typing("\nIndica sólo s/n, según corresponda.")
                    break
                elif attackr == "n" or attackr == "no":
                    typing("\nNo posee tirada de ataque.")
                    lrange2 = " {{Alcance:= Corto ([[25+5*floor("+level+"/2)]]pies)}}"
                    break
                else:
                    typing("\nIndica sólo s/n, según corresponda.")
            continue
        #
        #  ___ _   _ _____ _____ ____  __  __ _____ ____ ___    _  _____ _____ 
        # |_ _| \ | |_   _| ____|  _ \|  \/  | ____|  _ \_ _|  / \|_   _| ____|
        #  | ||  \| | | | |  _| | |_) | |\/| |  _| | | | | |  / _ \ | | |  _|  
        #  | || |\  | | | | |___|  _ <| |  | | |___| |_| | | / ___ \| | | |___ 
        # |___|_| \_| |_| |_____|_| \_\_|  |_|_____|____/___/_/   \_\_| |_____|
        #                                                                      
        #
        elif lrange2 == "i":
            typing("\nEl conjuro tiene alcance intermedio.\n\n\n¿Requiere de una tirada de ataque? (s/n)")
            while True:
                attackr=input(">>> ").lower().strip()
                if attackr == "exit":
                    typing("\n\tTERMINATING...\n\n")
                    input("Presiona Enter para cerrar...")
                    import os
                    os._exit(0)
                elif attackr == "s" or attackr == "si" or attackr == "sí" or attackr == "y" or attackr == "yes":
                    typing("\nSí, se añade tirada de ataque.")
                    lrange2 = " {{Alcance:= Intermedio ([[100+10*floor("+level+")]]pies)}} {{Ataque de toque a distancia:= [[1d20+@{rangedattackbonus}]]vs CA de Toque}}"
                    typing("\n\n¿Tiene posibilidad de crítico? Por defecto, todos los conjuros que\nexigen tiradas de ataque (como contacto electrizante y flecha ácida\nde Melf) pueden dar lugar a un crítico, mientras que rayo relampa-\ngueante no. Recuerda que, por ej., Curar Heridas no da lugar a crí-\ntico, pero utilizar 'curar' para herir a muertos vivientes implica\nuna tirada de ataque con posibilidad de crítico. Ante la duda, se-\nlecciona que sí; luego puedes borrarlo. (s/n)")
                    while True:
                        crchance=input(">>> ").lower().strip()
                        if crchance == "exit":
                            typing("\n\tTERMINATING...\n\n")
                            input("Presiona Enter para cerrar...")
                            import os
                            os._exit(0)
                        elif crchance == "s" or crchance == "si" or crchance == "sí" or crchance == "y" or crchance == "yes":
                            typing("\nSí, se añade confirmación de crítico.")
                            lrange2 = lrange2 + " {{En caso de Crítico:= Confirmación a dist. [[1d20+@{rangedattackbonus}]]vs CA de Toque}}"
                            break
                        elif crchance == "n" or crchance == "no":
                            typing("\nNo tiene posibilidad de crítico.")
                            break
                        else:
                            typing("\nIndica sólo s/n, según corresponda.")
                    break
                elif attackr == "n" or attackr == "no":
                    typing("\nNo posee tirada de ataque.")
                    lrange2 = " {{Alcance:= Intermedio ([[100+10*floor("+level+")]]pies)}}"
                    break
                else:
                    typing("\nIndica sólo s/n, según corresponda.")
            continue
        #
        #  _     ___  _   _  ____ 
        # | |   / _ \| \ | |/ ___|
        # | |  | | | |  \| | |  _ 
        # | |__| |_| | |\  | |_| |
        # |_____\___/|_| \_|\____|
        #                         
        #
        elif lrange2 == "l":
            typing("\nEl conjuro tiene alcance largo.\n\n\n¿Requiere de una tirada de ataque? (s/n)")
            while True:
                attackr=input(">>> ").lower().strip()
                if attackr == "exit":
                    typing("\n\tTERMINATING...\n\n")
                    input("Presiona Enter para cerrar...")
                    import os
                    os._exit(0)
                elif attackr == "s" or attackr == "si" or attackr == "sí" or attackr == "y" or attackr == "yes":
                    typing("\nSí, se añade tirada de ataque.")
                    lrange2 = " {{Alcance:= Largo ([[400+40*floor("+level+")]]pies)}} {{Ataque de toque a distancia:= [[1d20+@{rangedattackbonus}]]vs CA de Toque}}"
                    typing("\n\n¿Tiene posibilidad de crítico? Por defecto, todos los conjuros que\nexigen tiradas de ataque (como contacto electrizante y flecha ácida\nde Melf) pueden dar lugar a un crítico, mientras que rayo relampa-\ngueante no. Recuerda que, por ej., Curar Heridas no da lugar a crí-\ntico, pero utilizar 'curar' para herir a muertos vivientes implica\nuna tirada de ataque con posibilidad de crítico. Ante la duda, se-\nlecciona que sí; luego puedes borrarlo. (s/n)")
                    while True:
                        crchance=input(">>> ").lower().strip()
                        if crchance == "exit":
                            typing("\n\tTERMINATING...\n\n")
                            input("Presiona Enter para cerrar...")
                            import os
                            os._exit(0)
                        elif crchance == "s" or crchance == "si" or crchance == "sí" or crchance == "y" or crchance == "yes":
                            typing("\nSí, se añade confirmación de crítico.")
                            lrange2 = lrange2 + " {{En caso de Crítico:= Confirmación a dist. [[1d20+@{rangedattackbonus}]]vs CA de Toque}}"
                            break
                        elif crchance == "n" or crchance == "no":
                            typing("\nNo tiene posibilidad de crítico.")
                            break
                        else:
                            typing("\nIndica sólo s/n, según corresponda.")
                    break
                elif attackr == "n" or attackr == "no":
                    typing("\nNo posee tirada de ataque.")
                    lrange2 = " {{Alcance:= Largo ([[400+40*floor("+level+")]]pies)}}"
                    break
                else:
                    typing("\nIndica sólo s/n, según corresponda.")
            continue
        #
        #  _____ _____  _______ ____  
        # |  ___|_ _\ \/ / ____|  _ \ 
        # | |_   | | \  /|  _| | | | |
        # |  _|  | | /  \| |___| |_| |
        # |_|   |___/_/\_\_____|____/ 
        #                             
        #
        elif lrange2 == "f":
            typing("\nEl conjuro tiene alcance fijo, en pies.")
            print("\n\n")
            while True:
                typing("Indica la distancia del conjuro, en pies\nej.: 20, 50, 5...")
                lrangefix = input(">>> ")
                try:
                    float(lrangefix)
                    typing("\nEl conjuro tiene un alcance fijo.\n\n\n¿Requiere de una tirada de ataque? (s/n)")
                    while True:
                        attackr=input(">>> ").lower().strip()
                        if attackr == "exit":
                            typing("\n\tTERMINATING...\n\n")
                            input("Presiona Enter para cerrar...")
                            import os
                            os._exit(0)
                        elif attackr == "s" or attackr == "si" or attackr == "sí" or attackr == "y" or attackr == "yes":
                            typing("\nSí, se añade tirada de ataque.")
                            lrange2 = " {{Alcance:= "+lrangefix+" pies)}} {{Ataque de toque a distancia:= [[1d20+@{rangedattackbonus}]]vs CA de Toque}}"
                            typing("\n\n¿Tiene posibilidad de crítico? Por defecto, todos los conjuros que\nexigen tiradas de ataque (como contacto electrizante y flecha ácida\nde Melf) pueden dar lugar a un crítico, mientras que rayo relampa-\ngueante no. Recuerda que, por ej., Curar Heridas no da lugar a crí-\ntico, pero utilizar 'curar' para herir a muertos vivientes implica\nuna tirada de ataque con posibilidad de crítico. Ante la duda, se-\nlecciona que sí; luego puedes borrarlo. (s/n)")
                            while True:
                                crchance=input(">>> ").lower().strip()
                                if crchance == "exit":
                                    typing("\n\tTERMINATING...\n\n")
                                    input("Presiona Enter para cerrar...")
                                    import os
                                    os._exit(0)
                                elif crchance == "s" or crchance == "si" or crchance == "sí" or crchance == "y" or crchance == "yes":
                                    typing("\nSí, se añade confirmación de crítico.")
                                    lrange2 = lrange2 + " {{En caso de Crítico:= Confirmación a dist. [[1d20+@{rangedattackbonus}]]vs CA de Toque}}"
                                    break
                                elif crchance == "n" or crchance == "no":
                                    typing("\nNo tiene posibilidad de crítico.")
                                    break
                                else:
                                    typing("\nIndica sólo s/n, según corresponda.")
                            break
                        elif attackr == "n" or attackr == "no":
                            typing("No posee tirada de ataque.")
                            lrange2 = " {{Alcance:= "+lrangefix+" pies)}}"
                            break
                        else:
                            typing("\nIndica sólo s/n, según corresponda.") 
                    break
                except:
                    typing("\nPor favor, introduce sólo un número.")
                    continue
            continue
        #
        #   ___ _____ _   _ _____ ____  
        #  / _ \_   _| | | | ____|  _ \ 
        # | | | || | | |_| |  _| | |_) |
        # | |_| || | |  _  | |___|  _ < 
        #  \___/ |_| |_| |_|_____|_| \_\
        #                               
        #
        elif lrange2 == "o":
            typing("\nIndica el número y la unidad de alcance del conjuro,\nej.: 5 pulgadas, Toque y 25'+5'/2 niveles...")
            lrange2 = input(">>> ").lower().strip()
            lrange2 = lrange2[0].upper() + lrange2[1:]
            typing("\nEl conjuro tiene el alcance definido por el usuario.\n\n\n¿Requiere de una tirada de ataque DE TOQUE CUERPO A CUERPO? (s/n)")
            while True:
                attackr=input(">>> ").lower().strip()
                if attackr == "exit":
                    typing("\n\tTERMINATING...\n\n")
                    input("Presiona Enter para cerrar...")
                    import os
                    os._exit(0)
                elif attackr == "s" or attackr == "si" or attackr == "sí" or attackr == "y" or attackr == "yes":
                    typing("\nSí, se añade tirada de ataque de toque c/c.")
                    lrange2 = " {{Alcance:= "+lrange2+"}} {{Ataque c/c:= [[1d20+@{meleeattackbonus}]]vs CA de Toque}}"
                    typing("\n\n¿Tiene posibilidad de crítico? Por defecto, todos los conjuros que\nexigen tiradas de ataque (como contacto electrizante y flecha ácida\nde Melf) pueden dar lugar a un crítico, mientras que rayo relampa-\ngueante no. Recuerda que, por ej., Curar Heridas no da lugar a crí-\ntico, pero utilizar 'curar' para herir a muertos vivientes implica\nuna tirada de ataque con posibilidad de crítico. Ante la duda, se-\nlecciona que sí; luego puedes borrarlo. (s/n)")
                    while True:
                        crchance=input(">>> ").lower().strip()
                        if crchance == "exit":
                            typing("\n\tTERMINATING...\n\n")
                            input("Presiona Enter para cerrar...")
                            import os
                            os._exit(0)
                        elif crchance == "s" or crchance == "si" or crchance == "sí" or crchance == "y" or crchance == "yes":
                            typing("\nSí, se añade confirmación de crítico.")
                            lrange2 = lrange2 + " {{En caso de Crítico:= Confirmación c/c [[1d20+@{meleeattackbonus}]]vs CA de Toque}}"
                            break
                        elif crchance == "n" or crchance == "no":
                            typing("\nNo tiene posibilidad de crítico.")
                            break
                        else:
                            typing("\nIndica sólo s/n, según corresponda.")
                    break
                elif attackr == "n" or attackr == "no":
                    typing("No posee tirada de ataque de toque c/c.")
                    lrange2 = " {{Alcance:= "+lrange2+"}}"
                    break
                else:
                    typing("\nIndica sólo s/n, según corresponda.")
            typing("\n\n¿Requiere de una tirada de ataque DE TOQUE A DISTANCIA? (s/n)")
            while True:
                attackr=input(">>> ").lower().strip()
                if attackr == "exit":
                    typing("\n\tTERMINATING...\n\n")
                    input("Presiona Enter para cerrar...")
                    import os
                    os._exit(0)
                elif attackr == "s" or attackr == "si" or attackr == "sí" or attackr == "y" or attackr == "yes":
                    typing("\nSí, se añade tirada de ataque de toque a distancia.")
                    lrange2 = lrange2 + " {{Ataque de toque a distancia:= [[1d20+@{rangedattackbonus}]]vs CA de Toque}}"
                    typing("\n\n¿Tiene posibilidad de crítico? Por defecto, todos los conjuros que\nexigen tiradas de ataque (como contacto electrizante y flecha ácida\nde Melf) pueden dar lugar a un crítico, mientras que rayo relampa-\ngueante no. Recuerda que, por ej., Curar Heridas no da lugar a crí-\ntico, pero utilizar 'curar' para herir a muertos vivientes implica\nuna tirada de ataque con posibilidad de crítico. Ante la duda, se-\nlecciona que sí; luego puedes borrarlo. (s/n)")
                    while True:
                        crchance=input(">>> ").lower().strip()
                        if crchance == "exit":
                            typing("\n\tTERMINATING...\n\n")
                            input("Presiona Enter para cerrar...")
                            import os
                            os._exit(0)
                        elif crchance == "s" or crchance == "si" or crchance == "sí" or crchance == "y" or crchance == "yes":
                            typing("\nSí, se añade confirmación de crítico.")
                            lrange2 = lrange2 + " {{En caso de Crítico:= Confirmación a dist. [[1d20+@{rangedattackbonus}]]vs CA de Toque}}"
                            break
                        elif crchance == "n" or crchance == "no":
                            typing("\nNo tiene posibilidad de crítico.")
                            break
                        else:
                            typing("\nIndica sólo s/n, según corresponda.")
                    break
                elif attackr == "n" or attackr == "no":
                    typing("No posee tirada de ataque de toque a distancia.")
                    break
                else:
                    typing("\nIndica sólo s/n, según corresponda.")
            continue
        else:
            typing("\nNo añadir alcance adicional.")
            break
    #print()
    #print(lrange2)
    print("\n\n")
    #
    #   ___  ____      _ _____ ____ _____ _____     _______ 
    #  / _ \| __ )    | | ____/ ___|_   _|_ _\ \   / / ____|
    # | | | |  _ \ _  | |  _|| |     | |  | | \ \ / /|  _|  
    # | |_| | |_) | |_| | |__| |___  | |  | |  \ V / | |___ 
    #  \___/|____/ \___/|_____\____| |_| |___|  \_/  |_____|
    #                                                       
    #
    typing("Indica aquí si el conjuro posee un OBJETIVO particular.")
    typing("Para visualizar el bloque de ayuda, escribe 'ayuda' (sin comillas) y presiona Enter")
    typing("\nSi no tiene o no conoces el objetivo del conjuro, escribe 'no' o presiona Enter")
    while True:
        obj=input(">>> ")
        if obj == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        elif obj.lower().strip() == "ayuda":
            ayuda()
            continue
        elif obj.lower().strip() == "no" or obj.lower().strip() == "":
            typing("\nEl conjuro no tiene objetivo en particular")
            break
        else:
            obj2 = obj.strip()
            obj2 = obj2[0].upper()+obj2[1:]
            obj2 = " {{Objetivo:= " + obj2 + "}}"
            obj2 = levelandmax(obj2)
            macro = macro + obj2
            break
    #print()
    #try:
    #    print(obj2,"\n")
    #except:
    #    print("none")
    #print()
    #print(macro)
    #print()
    #macro = levelandmax(macro)
    #print(macro)
    print("\n\n")
    #
    #  _____ _____ _____ _____ ____ _____ 
    # | ____|  ___|  ___| ____/ ___|_   _|
    # |  _| | |_  | |_  |  _|| |     | |  
    # | |___|  _| |  _| | |__| |___  | |  
    # |_____|_|   |_|   |_____\____| |_|  
    #                                     
    #
    typing("Indica aquí si el conjuro tiene un EFECTO particular.")
    typing("Para visualizar el bloque de ayuda, escribe 'ayuda' (sin comillas) y presiona Enter")
    typing("\nSi no tiene o no conoces el efecto del conjuro, escribe 'no' o presiona Enter")
    while True:
        eff=input(">>> ")
        if eff == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        elif eff.lower().strip() == "ayuda":
            ayuda()
            continue
        elif eff.lower().strip() == "no" or eff.lower().strip() == "n" or eff.lower().strip() == "":
            typing("\nEl conjuro no tiene efecto en particular")
            break
        else:
            eff2 = eff.strip()
            eff2 = eff2[0].upper()+eff2[1:]
            eff2 = " {{Efecto:= " + eff2 + "}}"
            eff2 = levelandmax(eff2)
            macro = macro + eff2
            break
    #print()
    #try:
    #    print(eff2,"\n")
    #except:
    #    print("none")
    #print()
    #print(macro)
    #print()
    #macro = levelandmax(macro)
    print("\n\n")
    #
    #  ____  _   _ ____      _  _____ ___ ___  _   _ 
    # |  _ \| | | |  _ \    / \|_   _|_ _/ _ \| \ | |
    # | | | | | | | |_) |  / _ \ | |  | | | | |  \| |
    # | |_| | |_| |  _ <  / ___ \| |  | | |_| | |\  |
    # |____/ \___/|_| \_\/_/   \_\_| |___\___/|_| \_|
    #                                                
    #
    typing("Indica la duración de los efectos del conjuro:")
    typing("\t(i)nstantánea")
    typing("\t(p)ermanente")
    typing("\t(c)oncentración")
    typing("\t(d)escarga")
    typing("\t(a)saltos/nivel(es)")
    typing("\t(m)inutos/nivel(es)")
    typing("\t(h)oras/nivel(es)")
    typing("\t(di)as/nivel(es)")
    typing("\t(f)ijo, en asaltos")
    typing("\t(v)er texto")
    typing("\t(o)tro, a definir")
    typing("\t(ayuda), ver ayuda y ejemplos")
    while True:
        durat=input(">>> ")
        if durat == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        durat2=durat.lower().strip()
        if durat2 != "i" and durat2 != "p" and durat2 != "c" and durat2 != "d" and durat2 != "a" and durat2 != "m" and durat2 != "h" and durat2 != "di" and durat2 != "f" and durat2 != "v" and durat2 != "o" and durat2 != "ayuda":
            typing("\nPor favor, indica alguna de las anteriores opciones.")
            continue
        if durat2 == "ayuda":
            ayuda()
            continue
        #
        #  ___ _   _ ____ _____  _    _   _ _____ 
        # |_ _| \ | / ___|_   _|/ \  | \ | |_   _|
        #  | ||  \| \___ \ | | / _ \ |  \| | | |  
        #  | || |\  |___) || |/ ___ \| |\  | | |  
        # |___|_| \_|____/ |_/_/   \_\_| \_| |_|  
        #                                         
        #
        elif durat2 == "i":
            typing("\nEl conjuro tiene duración instantánea")
            durat2 = " {{Duración:= Instantánea"
            break
        #
        #  ____  _____ ____  __  __    _    _   _ _____ _   _ _____ 
        # |  _ \| ____|  _ \|  \/  |  / \  | \ | | ____| \ | |_   _|
        # | |_) |  _| | |_) | |\/| | / _ \ |  \| |  _| |  \| | | |  
        # |  __/| |___|  _ <| |  | |/ ___ \| |\  | |___| |\  | | |  
        # |_|   |_____|_| \_\_|  |_/_/   \_\_| \_|_____|_| \_| |_|  
        #                                                           
        #
        elif durat2 == "p":
            typing("\nEl conjuro tiene duración permanente")
            durat2 = " {{Duración:= Permanente"
            break
        #
        #   ____ ___  _   _  ____ _____ _   _ _____ ____      _  _____ ___ ___  _   _ 
        #  / ___/ _ \| \ | |/ ___| ____| \ | |_   _|  _ \    / \|_   _|_ _/ _ \| \ | |
        # | |  | | | |  \| | |   |  _| |  \| | | | | |_) |  / _ \ | |  | | | | |  \| |
        # | |__| |_| | |\  | |___| |___| |\  | | | |  _ <  / ___ \| |  | | |_| | |\  |
        #  \____\___/|_| \_|\____|_____|_| \_| |_| |_| \_\/_/   \_\_| |___\___/|_| \_|
        #                                                                             
        #
        elif durat2 == "c":
            typing("\nEl conjuro tiene duración dependiente de la concentración")
            durat2 = " {{Duración:= Concentración"
            print("\n\n")
            typing("Indica el número de asaltos adicionales luego de dejar de concentrarse, ej.: 3, 1d6, 2*NIVEL/3")
            typing("Si no posee asaltos adicionales, escribe 'no' o presiona Enter")
            durcon=input(">>> ")
            if durcon == "exit":
                typing("\n\tTERMINATING...\n\n")
                input("Presiona Enter para cerrar...")
                import os
                os._exit(0)
            elif durcon.lower().strip() != "no" and durcon.lower().strip() != "n" and durcon.lower().strip() != "":
                durcon = levelandmax(durcon)
                durat2 = durat2 + " +[[" + durcon.lower().strip() + "]]asaltos"
            break
        #
        #  ____ ___ ____   ____ _   _    _    ____   ____ _____ 
        # |  _ \_ _/ ___| / ___| | | |  / \  |  _ \ / ___| ____|
        # | | | | |\___ \| |   | |_| | / _ \ | |_) | |  _|  _|  
        # | |_| | | ___) | |___|  _  |/ ___ \|  _ <| |_| | |___ 
        # |____/___|____/ \____|_| |_/_/   \_\_| \_\\____|_____|
        #                                                       
        #
        elif durat2 == "d":
            typing("\nEl conjuro está activo hasta su descarga")
            durat2 = " {{Duración:= Descarga"
            break
        #
        #  ____   ___  _   _ _   _ ____  ____  
        # |  _ \ / _ \| | | | \ | |  _ \/ ___| 
        # | |_) | | | | | | |  \| | | | \___ \ 
        # |  _ <| |_| | |_| | |\  | |_| |___) |
        # |_| \_\\___/ \___/|_| \_|____/|____/ 
        #                                      
        #
        elif durat2 == "a":
            typing("\nEl conjuro tiene una duración de X asaltos cada Y niveles")
            print("\n\n")
            typing("Indica el número de asaltos por nivel,\nej.:\n\tPara 2 asaltos por nivel, escribe: 2*NIVEL\n\tPara 5 asaltos más 1 cada 2 niveles, escribe: 5+NIVEL/2\n\tPara 1d4 asaltos más 1 cada 5 niveles escribe: 1d4+NIVEL/5")
            asalt1 = input (">>> ").upper().strip()
            asalt1 = levelandmax(asalt1)
            durat2 = " {{Duración:= [[" + asalt1 + "]]asalto(s)"
            break
        #
        #  __  __ ___ _   _ _   _ _____ _____ ____  
        # |  \/  |_ _| \ | | | | |_   _| ____/ ___| 
        # | |\/| || ||  \| | | | | | | |  _| \___ \ 
        # | |  | || || |\  | |_| | | | | |___ ___) |
        # |_|  |_|___|_| \_|\___/  |_| |_____|____/ 
        #                                           
        #
        elif durat2 == "m":
            typing("\nEl conjuro tiene una duración de X minutos cada Y niveles")
            print("\n\n")
            typing("Indica el número de minutos por nivel,\nej.:\n\tPara 2 minutos por nivel, escribe: 2*NIVEL\n\tPara 5 minutos más 1 cada 2 niveles, escribe: 5+NIVEL/2\n\tPara 1d4 minutos más 1 cada 5 niveles escribe: 1d4+NIVEL/5")
            asalt1 = input (">>> ").upper().strip()
            asalt1 = levelandmax(asalt1)
            durat2 = " {{Duración:= [[" + asalt1 + "]]minuto(s)"
            break
        #
        #  _   _  ___  _   _ ____  ____  
        # | | | |/ _ \| | | |  _ \/ ___| 
        # | |_| | | | | | | | |_) \___ \ 
        # |  _  | |_| | |_| |  _ < ___) |
        # |_| |_|\___/ \___/|_| \_\____/ 
        #                                
        #
        elif durat2 == "h":
            typing("\nEl conjuro tiene una duración de X horas cada Y niveles")
            print("\n\n")
            typing("Indica el número de horas por nivel,\nej.:\n\tPara 2 horas por nivel, escribe: 2*NIVEL\n\tPara 5 horas más 1 cada 2 niveles, escribe: 5+NIVEL/2\n\tPara 1d4 horas más 1 cada 5 niveles escribe: 1d4+NIVEL/5")
            asalt1 = input (">>> ").upper().strip()
            asalt1 = levelandmax(asalt1)
            durat2 = " {{Duración:= [[" + asalt1 + "]]hora(s)"
            break
        #
        #  ____    _ __   ______  
        # |  _ \  / \\ \ / / ___| 
        # | | | |/ _ \\ V /\___ \ 
        # | |_| / ___ \| |  ___) |
        # |____/_/   \_\_| |____/ 
        #                         
        #
        elif durat2 == "di":
            typing("\nEl conjuro tiene una duración de X días cada Y niveles")
            print("\n\n")
            typing("Indica el número de días por nivel,\nej.:\n\tPara 2 días por nivel, escribe: 2*NIVEL\n\tPara 5 días más 1 cada 2 niveles, escribe: 5+NIVEL/2\n\tPara 1d4 días más 1 cada 5 niveles escribe: 1d4+NIVEL/5")
            asalt1 = input (">>> ").upper().strip()
            asalt1 = levelandmax(asalt1)
            durat2 = " {{Duración:= [" + asalt1 + "]día(s)"
            break
        #
        #  _____ _____  _______ ____  
        # |  ___|_ _\ \/ / ____|  _ \ 
        # | |_   | | \  /|  _| | | | |
        # |  _|  | | /  \| |___| |_| |
        # |_|   |___/_/\_\_____|____/ 
        #                             
        #
        elif durat2 == "f":
            typing("\nEl conjuro tiene una duración fija de asaltos")
            print("\n\n")
            typing("Indica el número de asaltos,\nej.:\n\t1\n\t2d6+2")
            asalt1 = input (">>> ").upper().strip()
            asalt1 = levelandmax(asalt1)
            durat2 = " {{Duración:= [[" + asalt1 + "]]asalto(s)"
            break
        #
        #  ____  _____ _____   _____ _______  _______ 
        # / ___|| ____| ____| |_   _| ____\ \/ /_   _|
        # \___ \|  _| |  _|     | | |  _|  \  /  | |  
        #  ___) | |___| |___    | | | |___ /  \  | |  
        # |____/|_____|_____|   |_| |_____/_/\_\ |_|  
        #                                             
        #
        elif durat2 == "v":
            typing("\nLa duración del conjuro requiere de 'Ver texto'")
            durat2 = " {{Duración:= Ver texto"
            break
        #
        #   ___ _____ _   _ _____ ____  
        #  / _ \_   _| | | | ____|  _ \ 
        # | | | || | | |_| |  _| | |_) |
        # | |_| || | |  _  | |___|  _ < 
        #  \___/ |_| |_| |_|_____|_| \_\
        #                               
        #
        else:
            print("\n\n")
            typing("Indica la duración del efecto,\nej.: 1 noche, 2 semanas (D); ver texto, Hasta la luna llena...")
            durat2 = input(">>> ").strip()
            durat2 = durat2[0].upper()+durat2[1:]
            durat2 = levelandmax(durat2)
            durat2 = " {{Duración:= " + durat2 + "}}"
            break
    macro = macro + durat2
    #
    #  _   _ _   _ ____   ___  
    # | | | | \ | |  _ \ / _ \ 
    # | | | |  \| | | | | | | |
    # | |_| | |\  | |_| | |_| |
    #  \___/|_| \_|____/ \___/ 
    #                          
    #
    while True:
        if durat.lower().strip() == "o":
            break
        print("\n\n")
        typing("El conjuro, ¿permite Deshacer (D)? (s/n)")
        undo=input(">>> ")
        if undo == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        undo=undo.lower().strip()
        if undo == "s" or undo == "si" or undo == "sí" or undo == "y" or undo == "yes" or undo == "d":
            typing("\nEl conjuro permite Deshacer (D)")
            macro = macro + " (D)}}"
            break
        elif undo == "n" or undo == "no":
            typing("\nNo se puede deshacer a voluntad, o depende de la concentración")
            macro = macro + "}}"
            break
        else:
            typing("\nIndica sólo s/n, según corresponda.")
    #print()
    #print(durat2, undo)
    print("\n\n")
    #
    #  ____    ___     _____ _   _  ____   _____ _   _ ____   _____        __
    # / ___|  / \ \   / /_ _| \ | |/ ___| |_   _| | | |  _ \ / _ \ \      / /
    # \___ \ / _ \ \ / / | ||  \| | |  _    | | | |_| | |_) | | | \ \ /\ / / 
    #  ___) / ___ \ V /  | || |\  | |_| |   | | |  _  |  _ <| |_| |\ V  V /  
    # |____/_/   \_\_/  |___|_| \_|\____|   |_| |_| |_|_| \_\\___/  \_/\_/   
    #                                                                        
    #
    typing("Indica el tipo de tiro de salvación:")
    typing("\t(v)oluntad")
    typing("\t(f)ortaleza")
    typing("\t(r)eflejos")
    typing("\t(n)inguno")
    typing("\t(ve)r texto")
    typing("\t(o)tro, a definir")
    while True:
        ts=input(">>> ")
        if ts == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        ts2=ts.lower().strip()
        if ts2 != "v" and ts2 != "f" and ts2 != "r" and ts2 != "n" and ts2 != "ve" and ts2 != "o":
            typing("\nPor favor, indica alguna de las anteriores opciones.")
            continue
        elif ts2 == "v":
            typing("\nEl conjuro tiene salvación por voluntad.")
            ts2 = " {{TS:= Voluntad"
            break
        elif ts2 == "f":
            typing("\nEl conjuro tiene salvación por fortaleza.")
            ts2 = " {{TS:= Fortaleza"
            break
        elif ts2 == "r":
            typing("\nEl conjuro tiene salvación por reflejos.")
            ts2 = " {{TS:= Reflejos"
            break
        elif ts2 == "n":
            typing("\nEl conjuro no tiene tiro de salvación.")
            ts2 = " {{TS:= Ninguno}}"
            break
        elif ts2 == "ve":
            typing("\nAclaración 'ver texto' introducida.")
            ts2 = " {{TS:= Ver texto}}"
            break
        else:
            typing("\nIndica la tirada de salvación especial,\nej.:\n\tVoluntad niega o parcial; ver texto")
            ts2 = input(">>> ").strip()
            ts2 = ts2[0].upper()+ts2[1:]
            ts2 = " {{TS:= "+ts2+" (CD:[[" + spelldc + "]])}}"
            break
    #
    #  ____    ___     _____ _   _  ____   _____ _____ _____ _____ ____ _____ 
    # / ___|  / \ \   / /_ _| \ | |/ ___| | ____|  ___|  ___| ____/ ___|_   _|
    # \___ \ / _ \ \ / / | ||  \| | |  _  |  _| | |_  | |_  |  _|| |     | |  
    #  ___) / ___ \ V /  | || |\  | |_| | | |___|  _| |  _| | |__| |___  | |  
    # |____/_/   \_\_/  |___|_| \_|\____| |_____|_|   |_|   |_____\____| |_|  
    #                                                                         
    #
    if ts.lower().strip() == "v" or ts.lower().strip() == "f" or ts.lower().strip() == "r":
        print("\n\n")
        typing("Indica el efecto de la tirada de salvación:")
        typing("\t(n)iega")
        typing("\t(p)arcial")
        typing("\t(m)itad")
        typing("\t(d)escree")
        typing("\t(o)tro, a definir")
        while True:
            effts=input(">>> ")
            if effts == "exit":
                typing("\n\tTERMINATING...\n\n")
                input("Presiona Enter para cerrar...")
                import os
                os._exit(0)
            effts2=effts.lower().strip()
            if effts2 != "n" and effts2 != "p" and effts2 != "m" and effts2 != "d" and effts2 != "o":
                typing("\nPor favor, indica alguna de las anteriores opciones.")
                continue
            elif effts2 == "n":
                typing("\nTS niega efecto")
                ts2 = ts2 + " niega (CD:[[" + spelldc + "]])"
                break
            elif effts2 == "p":
                typing("\nTS hace efecto parcial")
                ts2 = ts2 + " parcial (CD:[[" + spelldc + "]])"
                break
            elif effts2 == "m":
                typing("\nTS hace mitad de efecto")
                ts2 = ts2 + " mitad (CD:[[" + spelldc + "]])"
                break
            elif effts2 == "d":
                typing("\nTS descree")
                ts2 = ts2 + " descree (CD:[[" + spelldc + "]])"
                break
            else:
                typing("\nIndica el efecto especial,\nej.:\n\tniega o parcial; ver texto")
                ts3 = input(">>> ").lower().strip()
                ts2 = ts2 + " " + ts3 + "(CD:[[" + spelldc + "]])}}"
                break
        #
        #  _   _    _    ____  __  __ _     _____ ____ ____  
        # | | | |  / \  |  _ \|  \/  | |   | ____/ ___/ ___| 
        # | |_| | / _ \ | |_) | |\/| | |   |  _| \___ \___ \ 
        # |  _  |/ ___ \|  _ <| |  | | |___| |___ ___) |__) |
        # |_| |_/_/   \_\_| \_\_|  |_|_____|_____|____/____/ 
        #                                                    
        #
        if effts.lower().strip() == "n" or effts.lower().strip() == "p" or effts.lower().strip() == "m" or effts.lower().strip() == "d":
            print("\n\n")
            typing("El conjuro, ¿provoca un efecto (inofensivo)? (s/n)")
            while True:
                inof=input(">>> ")
                if inof == "exit":
                    typing("\n\tTERMINATING...\n\n")
                    input("Presiona Enter para cerrar...")
                    import os
                    os._exit(0)
                inof2=inof.lower().strip()
                if inof2 == "s" or inof2 == "si" or inof2 == "sí" or inof2 == "y" or inof2 == "yes" or inof2 == "i":
                    typing("\nInofensivo")
                    ts2 = ts2 + " (inofensivo)}}"
                    break
                elif inof2 == "n" or inof2 == "no":
                    typing("\nNo inofensivo")
                    ts2 = ts2 + "}}"
                    break
                else:
                    typing("\nIndica sólo s/n, según corresponda.")
    macro = macro + ts2
    #print()
    #print(ts2)
    print("\n\n")
    #
    #  ____  ____  _____ _     _       ____  _____ ____ ___ ____ _____ _____ _   _  ____ _____ 
    # / ___||  _ \| ____| |   | |     |  _ \| ____/ ___|_ _/ ___|_   _| ____| \ | |/ ___| ____|
    # \___ \| |_) |  _| | |   | |     | |_) |  _| \___ \| |\___ \ | | |  _| |  \| | |   |  _|  
    #  ___) |  __/| |___| |___| |___  |  _ <| |___ ___) | | ___) || | | |___| |\  | |___| |___ 
    # |____/|_|   |_____|_____|_____| |_| \_\_____|____/___|____/ |_| |_____|_| \_|\____|_____|
    #                                                                                          
    #
    while True:
        typing("El conjuro, ¿tiene Resistencia a Conjuros (RC)? (s/n)")
        spres=input(">>> ")
        if spres == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        spres=spres.lower().strip()
        if spres == "s" or spres == "si" or spres == "sí" or spres == "y" or spres == "yes" or spres == "v":
            print("\n\n")
            while True:
                typing("Tiene RC, ¿tiene efecto (inofensivo)? (s/n)")
                spres2 = input(">>> ")
                spres2=spres2.lower().strip()
                if spres2 == "s" or spres2 == "si" or spres2 == "sí" or spres2 == "y" or spres2 == "yes" or spres2 == "v":
                    typing("\nInofensivo")
                    macro = macro + " {{RC:= Sí ([[1d20+" + level + "+@{spellpen}]]vs RC) (inofensivo)"
                    break
                elif spres2 == "n" or spres2 == "no":
                    typing("\nNo inofensivo")
                    macro = macro + " {{RC:= Sí ([[1d20+" + level + "+@{spellpen}]]vs RC)"
                    break
                else:
                    typing("\nIndica sólo si/no, según corresponda.")
                    continue
                break
            print("\n\n")
            #
            #  ____  _____ _____   _____ _______  _______ 
            # / ___|| ____| ____| |_   _| ____\ \/ /_   _|
            # \___ \|  _| |  _|     | | |  _|  \  /  | |  
            #  ___) | |___| |___    | | | |___ /  \  | |  
            # |____/|_____|_____|   |_| |_____/_/\_\ |_|  
            #                                             
            #
            while True:
                typing("Tiene RC, ¿requiere detalles (ver texto)? (s/n)")
                spres2 = input(">>> ")
                spres2=spres2.lower().strip()
                if spres2 == "s" or spres2 == "si" or spres2 == "sí" or spres2 == "y" or spres2 == "yes" or spres2 == "v":
                    typing("\nTiene RC, ver texto")
                    macro = macro + ", ver texto}}"
                    break
                elif spres2 == "n" or spres2 == "no":
                    typing("\nTiene RC, sin más")
                    macro = macro + "}}"
                    break
                else:
                    typing("\nIndica sólo si/no, según corresponda.")
                    continue
                break
            break
        elif spres == "n" or spres == "no":
            typing("No tiene RC")
            macro = macro + " {{RC:= No}}"
            break
        else:
            typing("\nIndica sólo si/no, según corresponda.")
    #print()
    #print(macro)
    print("\n\n")
    #
    #  ____  ____  _____ ____ ___    _    _       _     ___ _   _ _____ 
    # / ___||  _ \| ____/ ___|_ _|  / \  | |     | |   |_ _| \ | | ____|
    # \___ \| |_) |  _|| |    | |  / _ \ | |     | |    | ||  \| |  _|  
    #  ___) |  __/| |__| |___ | | / ___ \| |___  | |___ | || |\  | |___ 
    # |____/|_|   |_____\____|___/_/   \_\_____| |_____|___|_| \_|_____|
    #                                                                   
    #
    typing("Aquí puedes agregar una línea especial adicional (como Tiempo de disipación,\nTesis arcana, Escuela predilecta, etc.)\n\nSi no quieres agregar nada, escribe 'no' o pulsa Enter.")
    subtag=input(">>> ")
    subtag2 = subtag.lower().strip()
    if subtag == "exit":
        typing("\n\tTERMINATING...\n\n")
        input("Presiona Enter para cerrar...")
        import os
        os._exit(0)
    if subtag != "no" and subtag != "n" and subtag != "":
        subtag2 = subtag2[0].upper()+subtag2[1:]
        typing("\nEscribe el valor correspondiente, ej.: sí, no, 5 pies, [[1d6+2*NIVEL/3]]asaltos...")
        subtagcond=input(">>> ").upper().strip()
        if subtagcond == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        subtagcond = levelandmax(subtagcond)
        subtagcond2 = subtagcond[0].upper()+subtagcond[1:].lower()
        subtagall = "{{" + subtag2 + ":= " + subtagcond2 + "}}" 
        macro = macro + subtagall
    #print()
    #try:
    #    print(subtagall)
    #except:
    #    print("none")
    print("\n\n")
    macro = macro + " ?{¿Concentración a la Defensiva con Conjurar en combate?|No, 0|Sí, 4} {{compcheck= Conc: [[{1d20 + [[@{concentration} + ?{¿Concentración a la Defensiva con Conjurar en combate?}]]}>?{Concentración CD=15+Nivel de conjuro o 10+Daño Recibido+Nivel del conjuro|" + str(15+int(splvl2))+ "}]]}} {{succeedcheck= Concentración Éxito!}} {{failcheck= Concentración Fallo!}} {{check= }} {{checkroll= }} {{checkroll=\n"
    #
    #  ____  _____ ____   ____ ____  ___ ____ _____ ___ ___  _   _ 
    # |  _ \| ____/ ___| / ___|  _ \|_ _|  _ \_   _|_ _/ _ \| \ | |
    # | | | |  _| \___ \| |   | |_) || || |_) || |  | | | | |  \| |
    # | |_| | |___ ___) | |___|  _ < | ||  __/ | |  | | |_| | |\  |
    # |____/|_____|____/ \____|_| \_\___|_|    |_| |___\___/|_| \_|
    #                                                              
    #
    typing("Ahora escribe todo el texto que quieras como descripción del conjuro.\nSigue las siguientes recomendaciones:\n\t·Las frases encerradas entre *asteriscos* aparecerán escritas en cursiva\n\t·Las frases encerradas entre **asteriscos dobles** serán negritas\n\t·Si necesitas algún cálculo en el texto (ej.: 1d6 criaturas más una cada\n\t dos niveles), escríbelo de la forma '[[1d6+1*NIVEL/2]]criaturas'\n\t·Para crear una nueva línea usa la barra invertida+n, o edíta la macro luego\nej.:\n\t")
    print("Una pequeña figura de un guerrero en plomo es consumida completamente luego de que pronuncias y gesticulas el conjuro. Una legión de centinelas sombríos emana allí donde apuntes, con sus armas desenvainadas y listas para atacar a quien ose atravesarlos. En cada casilla del área de efecto aparecerá un **guerrero incorporal que amenaza sus casillas adyacentes**, y podrá compartir espacio con criaturas y objetos. Cada guerrero puede efectuar **un ataque de oportunidad por asalto.** No obstaculizan ni ocultan la visión o efectos de ninguna manera, y **podrán flanquear** entre sí, o con tu ayuda o la de tus aliados. Cada guerrero tiene [[2*NIVEL]] puntos de golpe y una CA de **25**. Sus pruebas de habilidad y TS se realizan con un bonificador de **+**[[NIVEL]]. *Componente material arcano: Una pequeña figura de plomo con forma de guerrero.*")
    print()
    typing("Para visualizar el bloque de ayuda, escribe 'ayuda' (sin comillas) y presiona Enter")
    while True:
        text=input(">>> ").strip()
        if text == "exit":
            typing("\n\tTERMINATING...\n\n")
            input("Presiona Enter para cerrar...")
            import os
            os._exit(0)
        elif text.lower() == "ayuda":
            ayuda()
            continue
        elif text == "":
            typing("\nSin descripción. Podrás añadirla más tarde.")
            text2 = "INGRESE DESCRIPCIÓN AQUÍ"
            break
        else:
            text = levelandmax(text)
            text2 = text[0].upper()+text[1:]
            break
    macro = macro + text2 + "\n\n"
    print("\n\n")
    #
    #  ___ __  __    _    ____ _____    ______ ___ _____ 
    # |_ _|  \/  |  / \  / ___| ____|  / / ___|_ _|  ___|
    #  | || |\/| | / _ \| |  _|  _|   / / |  _ | || |_   
    #  | || |  | |/ ___ \ |_| | |___ / /| |_| || ||  _|  
    # |___|_|  |_/_/   \_\____|_____/_/  \____|___|_|    
    #                                                    
    #
    typing("Por último, si quieres introducir la URL de una imagen o gif para tu conjuro,\npuedes pegarla a continuación. Asegúrate de que el enlace termine en .jpg, .png, .gif...\nLa extensión .gifv no está soportada en Roll20.")
    typing("Si no quieres añadir imagen aún, escribe 'no' o presiona Enter")
    pict=input(">>> ").strip()
    if pict == "exit":
        typing("\n\tTERMINATING...\n\n")
        input("Presiona Enter para cerrar...")
        import os
        os._exit(0)
    elif pict.lower() != "no" and pict.lower() != "":
        typing("\nSe ha añadido la URL ")
        typing(pict)
        typing("Si no funciona, es posible que el tipo de imagen no esté soportada por Roll20.\nPodrás cambiarla más tarde.")
        pict = "[x](" + pict + ")}}"
        macro = macro + pict
    else:
        typing("\nAún no tienes una imagen. Podrás añadirla más tarde.")
        macro = macro + "}}"
    #
    #  _____ _   _ ____  
    # | ____| \ | |  _ \ 
    # |  _| |  \| | | | |
    # | |___| |\  | |_| |
    # |_____|_| \_|____/ 
    #                    
    #
    typing("\n\nLa macro del conjuro queda así:\n")
    print(macro,"\n")
    with open(spname2+".txt", "wb") as f:
        f.write(macro.encode("cp1252"))
        f.flush()
    typing("Se ha creado el siguiente archivo:\n")
    print(spname2+".txt")
    typing("\nLo encontrarás en la carpeta donde tienes este ejecutable. Ábrelo y edítalo como quieras.\n\nNo podían faltar algunas recomendaciones:")
    typing("\n\t·Algunos conjuros tienen condiciones del tipo '1d8 pts. de daño +1 adicional")
    typing("\t por nivel de lanzador (máx. +5)'. En estos casos conviene utilizar la función")
    typing("\t {A,B}dh1, que significa A ó B, el que sea menor, ej.: Curar heridas leves es")
    typing("\t 1d8 + 1/nivel lanzador (hasta +5) -> [[1d8+{@{casterlevel},5}dh1]], donde")
    typing("\t @{casterlevel} puede ser @{arcanecasterlevel} o @{divinecasterlevel}, según")
    typing("\t se utilicen Base mode (casterl.) o Full mode (arcane/divinecasterl.)\n")
    typing("\t·Otros conjuros requieren de una relación del tipo 'cada dos niveles de lan-")
    typing("\t zador'. Salvo excepciones, esto siempre es redondeado a la baja. El comando")
    typing("\t ya fue programado así en esta macro, y lo verás como floor(@{casterlevel}/2).")
    typing("\t De querer cambiarlo a la alza, reemplazar por ceil: ceil(@{casterlevel}/2)\n")
    typing("\t·Los dos puntos anteriores se combinan en [[1d8+{floor(@{casterlevel}/2),5}dh1]]\n")
    typing("\t·Puedes añadir una imagen o gif al conjuro. Para hacerlo, al pie de la macro")
    typing("\t y antes de las dos llaves de cierra }}, copia la URL de la imagen/gif entre")
    typing("\t paréntesis, precedida por [x], ej.: [x](https://i.imgur.com/CbtFuAt.gif)")
    typing("\nEso es todo...")
    iteration = True
    input("\n\nPresiona Enter para continuar...")
