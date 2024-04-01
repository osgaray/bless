#importando librerias
import csv
import random
from colorama import init, Fore
 
#agregar repeticiones a cada lista de verbo
def agregarreps():
    with open("C:\\Users\\OSCAR GARAY\\Documents\\página\\python\\study_english\\verbs.csv", "r", encoding="UTF-8") as verbs:
        reader = csv.reader(verbs)
        listaverbos = list(reader)
        repeticiones = ["0","1","2","3","4","5","6","7","8","9","10"]
        for fila in listaverbos:
            ult_elemento = fila[-1]
            if ult_elemento in repeticiones:
                fila.pop()            
            fila.append("0")
            fila[-2].replace(' ','')
    with open("C:\\Users\\OSCAR GARAY\\Documents\\página\\python\\study_english\\verbs.csv", "w", encoding="UTF-8") as verbs:
        escritor = csv.writer(verbs,lineterminator="\n")
        escritor.writerows(listaverbos)
    
#función para actualizar la lista de verbos al estudiarlos
def actualizar(listas,nombre):
    with open(f"C:\\Users\\OSCAR GARAY\\Documents\\página\\python\\study_english\\{nombre}.csv", "w", encoding="UTF-8") as news:    
        escritor = csv.writer(news,lineterminator="\n")
        escritor.writerows(listas)
        
#inicializando colorama
init()

#consultando la opción a realizar
opcion = input("Si quieres estudiar verbos escribe "+Fore.LIGHTMAGENTA_EX+ "V"+Fore.RESET+" y si quieres añadir un verbo a la lista escribe "+Fore.LIGHTMAGENTA_EX+ "AV"+Fore.RESET+".\nSi quieres estudiar palabras escribe "+Fore.LIGHTMAGENTA_EX+ "W"+Fore.RESET+" y si queires añadir palabras escribe "+Fore.LIGHTMAGENTA_EX+ "AW"+Fore.RESET+".\nSi quieres estudiar phrasal verbs escribe "+Fore.LIGHTMAGENTA_EX+ "PV"+Fore.RESET+" y si quieres añadir alguno a la lista escribe "+Fore.LIGHTMAGENTA_EX+ "APV."+Fore.RESET+"\n").upper()

#si la opción es "A" consultar el verbo a añadir y guardarlo en verbs
if opcion == "AV":
    verb_new = input("Escribe el verbo que quieres añadir con el formato [verboenespañol,verboeningles,verboenpasado]: ").lower()
    with open("C:\\Users\\OSCAR GARAY\\Documents\\página\\python\\study_english\\verbs.csv", "a", encoding="UTF-8") as verbs:
        verbs.write(verb_new+",0")
        verbs.write("\n")       
#si la opción es "V" abrir verbs en lectura
elif opcion == "V":
    with open("C:\\Users\\OSCAR GARAY\\Documents\\página\\python\\study_english\\verbs.csv", "r", encoding="UTF-8") as verbs:
        reader = csv.reader(verbs)
        #convertir el lector de verbs en una lista
        listaverbos = list(reader)
        #contar las filas segun la lista de verbos
        cantidadfilas = len(listaverbos)
        lineas = []
        #preguntar si quiere repasar antes de estudiar para mostrar los verbos menos estudiados
        repasar = str(input("¿Quieres repasar los verbos menos estudiados? si/no: ")).lower().strip()
        if repasar == "si":
            for verbo in listaverbos:
                if int(verbo[3]) < 4:
                    print(Fore.LIGHTYELLOW_EX+f"{verbo[0].capitalize()}"+Fore.RESET+" en ingles es "+Fore.LIGHTYELLOW_EX+f"{verbo[1]}"+Fore.RESET+" y en pasado es "+Fore.LIGHTYELLOW_EX+f"{verbo[2]}"+Fore.RESET)
            print(f"\nAhora continuemos...\n")
        else:
            print("Entonces continuemos a estudiar...")
        #alamacena las palabras acertadas y falladas
        acertadas = 0
        falladas = 0
        #ejecutar mientras la cantidad de filas leidas sea menor que la cantidad de filas total
        while len(lineas) < cantidadfilas: 
            #elegir un numero aleatoria entre 1 y la cantidad de filas total
            lineb = random.randint(1,cantidadfilas)
            #ejecutar si el numero aleatorio no esta en la lista de filas
            if lineb not in lineas:
                #almacenar el numero aleatorio en la lista de filas
                lineas.append(lineb)
                #se obtiene el indice y la linea de la lista de verbos
                for indice,linea in enumerate(listaverbos):
                    #convierte el ultimo valor en entero para contar las veces que se ha repetido la linea
                    repeticiones = int(linea[-1])
                    #verifica si la linea de verbos ya la aprendimos (10 repeticiones)
                    if repeticiones < 10:
                        #si el indice es igual al numero aleatorio - 1 ejecuta las preguntas
                        if indice == lineb - 1:
                            verbini = input(f"{linea[0].capitalize()} en ingles: ").lower()
                            #se continua verificando las respuestas
                            if verbini == linea[1]:
                                acertadas += 1
                                print(Fore.LIGHTGREEN_EX+"\t¡Correcto!"+Fore.RESET)
                                #actualizando las repeticiones de cada verbo y agregandolo al archivo csv
                                listaverbos[indice][-1] = repeticiones + 1
                                actualizar(listaverbos,"verbs")
                            else:
                                falladas += 1
                                print(Fore.LIGHTRED_EX+f"\tIncorrecto"+Fore.RESET+f", {linea[0].capitalize()} en ingles es {linea[1].capitalize()}")
                            verbinp = input(f"{linea[1].capitalize()} en pasado: ").lower()
                            if verbinp == linea[2]:
                                acertadas += 1
                                print(Fore.LIGHTGREEN_EX+"\t¡Correcto!"+Fore.RESET)
                            else:
                                falladas += 1
                                print(Fore.LIGHTRED_EX+f"\tIncorrecto"+Fore.RESET+f", {linea[1].capitalize()} en pasado es {linea[2].capitalize()}")                              
                    else:
                        continue
                else:
                    continue
#si la opción es "W" abrir words para estudiar palabras
elif opcion == "W":
    with open("C:\\Users\\OSCAR GARAY\\Documents\\página\\python\\study_english\\words.csv", "r", encoding="UTF-8") as words:
        reader = csv.reader(words)
        #convertir el lector de verbs en una lista
        listapalabras = list(reader)
        #contar las filas segun la lista de verbos
        cantidadfilas = len(listapalabras)
        lineas = []
        #preguntar si quiere repasar antes de estudiar para mostrar las palabras menos estudiados
        repasar = str(input("¿Quieres repasar las palabras menos estudiados? si/no: ")).lower().strip()
        if repasar == "si":
            for palabra in listapalabras:
                if int(palabra[2]) < 4:
                    print(Fore.LIGHTYELLOW_EX+f"{palabra[0].capitalize()}"+Fore.RESET+" en ingles es "+Fore.LIGHTYELLOW_EX+f"{palabra[1]}"+Fore.RESET)
                    print(f"\nAhora continuemos...\n")
        else:
            print("Entonces continuemos a estudiar...")
        #alamacena las palabras acertadas y falladas
        acertadas = 0
        falladas = 0
        #ejecutar mientras la cantidad de filas leidas sea menor que la cantidad de filas total
        while len(lineas) < cantidadfilas:
            #elegir un numero aleatoria entre 1 y la cantidad de filas total
            lineb = random.randint(1,cantidadfilas)
            #ejecutar si el numero aleatorio no esta en la lista de filas
            if lineb not in lineas:
                #almacenar el numero aleatorio en la lista de filas
                lineas.append(lineb)
                #se obtiene el indice y la linea de la lista de verbos
                for indice,linea in enumerate(listapalabras):
                    #convierte el ultimo valor en entero para contar las veces que se ha repetido la linea
                    repeticiones = int(linea[-1])
                    #verifica si la linea de verbos ya la aprendimos (10 repeticiones)
                    if repeticiones < 10:
                        #si el indice es igual al numero aleatorio - 1 ejecuta las preguntas
                        if indice == lineb - 1:
                            wordini = input(f"{linea[0].capitalize()} en ingles: ").lower()
                            #se continua verificando las respuestas
                            if wordini == linea[1]:
                                acertadas += 1
                                print(Fore.LIGHTGREEN_EX+"\t¡Correcto!"+Fore.RESET)
                                #actualizando las repeticiones de cada verbo y agregandolo al archivo csv
                                listapalabras[indice][-1] = repeticiones + 1
                                actualizar(listapalabras,"words")
                            else:
                                falladas += 1
                                print(Fore.LIGHTRED_EX+f"\tIncorrecto"+Fore.RESET+f", {linea[0].capitalize()} en ingles es {linea[1].capitalize()}")
                    else:
                        continue
elif opcion == "AW":
    word_new = input("Escribe la palabra que quieres añadir con el formato [palabraenespañol,palabraeningles]: ").lower()
    with open("C:\\Users\\OSCAR GARAY\\Documents\\página\\python\\study_english\\words.csv", "a", encoding="UTF-8") as words:
        words.write(word_new+",0")
        words.write("\n")

#devuelve la cantidad de acertadas y falladas
if acertadas > falladas:
    print(Fore.LIGHTGREEN_EX+f"\nHas acertado {acertadas} y has fallado {falladas}"+Fore.RESET)
else:
    print(Fore.LIGHTYELLOW_EX+f"\nHas acertado {acertadas} y has fallado {falladas}"+Fore.RESET)
