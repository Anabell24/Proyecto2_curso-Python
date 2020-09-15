import sys
import os
import random
import time 

def historia():
    os.system('cls')
    ima0="____________________________________________________________________\n",
    ima1="\\__                        *------------*                        __/\n",
    ima2="   \\____________________________________________________________/\n",
    ima3="____  ________________________________________________________  ____\n",
    ima4=" .  \\ \\      _________________________    _____________      / / . . \n",
    ima5="     \\ \\    |////////////////////     |  | ❂ ✉ ☠ ⌛     |    / /\n",
    ima6="   *  \\ \\   |///////////¡PELIGRO!     |  | oo oo oo oo |   / / .  *\n",
    ima7="   .   \\ \\  |///////////////////////  |  |_____________|  / /\n",
    ima8="        \\ \\     ____________________________________     / /  .   *\n",
    ima9="   *     \\ \\   | ▄▄▄  ▄▄▄  ▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄▄▄     |   / /      .\n",
    ima10=" .       .\\ \\  |____________________________________|  / / *   .\n",
    ima11="___________\\ \\________________________________________/ /___________\n",
    ima12="__________    ________________________________________    __________ \n",
    ima13="         /   / ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄ \\   \\\n",
    ima14="       /    /__________________________________________\\    \\      \n",
    ima15="     /________________________________________________________\\\n",
    ima16="    | oooooooooo  ◄ ► ▲ ▼                     (_)   (_)   (_)  |\n",
    ima17="    |___________________.     / __O__ \\    .___________________|\n",
    ima18="    | |  |  T  |  |  T  |    (_/  O  \\_)   | ▐   ▐       ◘ ◘ ◙ |\n",
    ima19="    | T  |  |  |  |  |  |      -------     | ▐ ▐ ▐ ▐ ▐   ◘ ◘ ◙ |   \n",
    ima20="____| |  T  |  T  T  |  |__________________|___________________|____\n",
    ima21="    |__________________________________________________________|\n"
    intro="¡Hoy no es tu día, viajero espacial! "
    intro1="La nave ha sido impactada por basura espacial. "
    intro2="¡Oh, no! ¡Se escapa el oxígeno! "
    intro3="Pronto morirás... \n"
    intro4="*Sonido de trasmisión entrarte* \n"
    intro5="Has detectado una señal. "
    intro6="Hay una estación espacial cerca, bueno quizás no tienes "
    intro7="tan mala suerte.\n "
    intro8="******************************************************* \n"
    iman1= "      .  ✴         .         .                 ___________\n",
    iman2="             .            .         .      *  _|           |_   *\n",
    iman3="     .               /\\       *             _|   O        _  |_   .\n",
    iman4=".                  /   \\           ..      |     _   o   | |   |\n",
    iman5=" .         *     /    / /\\         __      |   /  |_     |_|   |  .\n",
    iman6="       .       /    / /   \\      /  |    . |  |_    |   _      |\n",
    iman7=".            /    / /    /  .  /   /       |_   |_ /   |_|    _|   .\n",
    iman8="            \\   / /    /     /   /           |_             _|     \n",
    iman9="             \\/ /    / \\   /   /      *        |___________|       *\n",
    iman10="   *           \\   /    \\/   /  *         .       *              .   \n",
    iman11="                \\/  .  /   /     /\\  .     .    ✴           \n",
    iman12="          .          /   / \\   /   \\     .              .     .\n",
    iman13="     ✴             /   /    \\/    / /\\      .                     .\n",
    iman14="            .    /   /     /    / /   \\           .   *\n",
    iman15="  .        .   /   /  .  /    / /    /  .           .     .       .\n",
    iman16="      .    .  |__/      \\   / /    /        *\n",
    iman17="                         \\/ /    /     .      *        *       .\n",
    iman18=" .         ..         .    \\   /  .          .         .     .   .\n",
    iman19="  .             *           \\/     .    .           .      *        .\n",
    iman20="\n",
    intro9='"Bienvido a la Estación Once" \n'
    intro10="Al parecer está abandonada, solo está la IA de la estación. "
    intro11="Es un lugar algo creepy. \n"
    intro12='"Entra sin miedo Viajero espacial, aquí estás seguro." \n '
    intro13="****************************************************** \n"
    imang1= "                                    ______________________________\n",
    imang2="   __________________________      |                              |\n",
    imang3="  /                        / |     |  o o o o o o    |  |  |  |   |\n",
    imang4=" /________________________/  |     |   _   _   _     |  |  |  T   |\n",
    imang5="|   ___________________   |  |     |  | | | | | |    T  |  |  |   |\n",
    imang6="|  |                   |  |  |     |  | | | | | |    |  |  T  |   |\n",
    imang7="|  |                   |  |  |     |  |_| |_| |_|    |  T  |  |   |\n",
    imang8="|  | NO PODRÁS ESCAPAR |  |  |     |                              |  \n",
    imang9="|  |                   |  |  |     |   ---------     (.)   (.)    |\n",
    imang10="|  |___________________|  | // |___|   ---------                  |\n",
    imang11="|_________________________|//  |   |______________________________|\n",
    imang12=" /       _ |  | _          /   |-┐\n",
    imang13="/_______|________|________/   /   |\n",
    imang14="|    o           | --- |  | _/    |\n",
    imang15="|    o           |_____|  | /|     |\n",
    imang16="|_________________________|/ |     | \n",
    imang17="          ___________________|     |\n",
    imang18="   _______|                        |\n",
    imang19="  /__/__/ |     ___________________|_____\n",
    imang20=" /_____/ /     /__/__/__/__/__/__/__/__//|\n",
    imang21="|______|/     /_/__/__/__/__/__/__/__/ / /\n",
    imang22="             /__/__/__/__/__/__/__/__// /\n",
    imang23="            |_________________________|/\n",
    imang24="\n",
    intro14="*Sonido de puertas que se cierra* \n"
    intro15='"Muahahahaah! Muahahahah! ¡Te engañé!"\n'
    intro16="¡Santa Galaxia! Que mala suerte tienes\n "
    intro17='"ES HORA DE JUGAR, SI PIERDES MORIRÁS"\n'
    
    
    for character in ima0:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)  
    for character in ima1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima11:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima12:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima13:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima14:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima15:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima16:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima17:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima18:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima19:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima20:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in ima21:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)    
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)  
    for character in intro1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman11:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman12:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman13:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman14:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman15:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman16:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman17:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman18:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman19:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in iman20:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro11:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro12:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro13:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang11:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang12:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang13:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang14:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang15:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang16:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang17:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang18:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang19:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in imang20:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)    
    for character in imang21:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05) 
    for character in imang22:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05) 
    for character in imang23:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05) 
    for character in imang24:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05) 
    for character in intro14:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro15:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro16:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro17:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    
    print("Presiona enter para continuar")
    option = input("> ")
    if option.lower()=="\n":
        return

def opciones_menu_principal():
    option = input("> ")
    if option.lower() == "jugar":
        historia()
        print('***********************************************')
        print("*                Instrucciones                *")
        print('***********************************************')
        print("Para moverse ingrese los valores de columna y fila")
        print("como xy, pegado y sin espacios.")
        print("Para responder las preguntas que te haga la malvada IA")
        print("solo ingrese el número del inciso que crea que sea")
        print("la correcta.")
        print("Para ir al menú escriba menu.")
        print("Suerte y que Atenea te ayude.")
        print('***********************************************\n')
        setup_game()
    elif option.lower() == "ayuda":
        menu_ayuda()
    elif option.lower() == "salir":
        sys.exit()
    while option.lower() not in ['jugar', 'ayuda', 'salir']:
        print("Error. Selecciona las opciones disponibles (-jugar -ayuda -salir).")
        option = input("> ")
        if option.lower() == "jugar":
            setup_game()
        elif option.lower() == "ayuda":
            menu_ayuda()
        elif option.lower() == "salir":
            sys.exit()


def title_screen():
    os.system('cls')
    print('***********************************************')
    print('*        ¡Bienvenido Viajero Espacial!        *')
    print('***********************************************')
    print('                   > Jugar                     ')
    print('                   > Ayuda                     ')
    print('                   > Salir                     ')
    print("***********************************************")
    print("*            La aventura nos espera           *")
    print("***********************************************")
    opciones_menu_principal()


def menu_ayuda():
    print('***********************************************')
    print('*                    Ayuda                    *')
    print('***********************************************')
    print('***********************************************')
    print("*                Instrucciones                *")
    print('***********************************************')
    print("Para moverse ingrese los valores de columna y fila")
    print("como xy, pegado y sin espacios.")
    print("Para responder las preguntas que  haga la malvada IA")
    print("solo ingrese el número del inciso que crea que sea")
    print("la correcta.")
    print("Para ir al menú escriba menu.")
    print("Suerte y que Atenea te ayude.")
    print('***********************************************\n')
    opciones_menu_principal()

def menu():
    os.system('cls')
    print('***********************************************')
    print('                   > Jugar                     ')
    print('                   > Ayuda                     ')
    print('                   > Salir                     ')
    print("***********************************************")
    opciones_menu_principal()
    
def juego():
    retry= True
    while (retry== True):
        question=""
        answer=""
        fake_answer1=""
        fake_answer2=""
        fake_answer3=""

        diccionario={"¿Cuáles son las dos lunas de marte?\n a-Fobos y Deimos  b-Io y Europa\n c-Deimos y Luna   d-Pluton y Caronte":"a",
                     "¿Qué planeta se le denomina planeta rojo?\n a-Jupiter b-marte\n c-venus   d-tierra":"b",
                     "¿Cuál es el sexto planeta de nuestro sistema solar?\n a-Neptuno b-Urano\n c-Saturno d-Jupiter":"c",
                     "¿Cuánto tarda Marte en dar una vuelta alrededor del sol?\n a-87 años          b-224 años\n c-779,96 años      d-365,25 años":"c",
                     "¿Qué planeta del sistema solar se ha encontrado agua?\n a-Jupiter b-Mercurio\n c-Venus   d-Marte":"d",
                     "¿En que año fue lanzada la estacion espacial internacional (ISS)?\n a-1971 b-1982\n c-1973 d-1998":"d",
                     "¿Cuánto tarda la ISS en completar una vuelta alrededor de la tierra?\n a-5 dias     b-24 horas\n c-8 meses    d-92 min/1.5 dias":"d",
                     "¿Qué animal fue el primero en ir al espacio?\n a-Perra Laika          b-Mono ardilla Gordo\n c-Mono Alberto II      d-Perro Dezik":"a",
                     "¿En que fecha llega el hombre a la Luna?\n a-30 de julio de 1969    b-20 de julio de 1969\n c-Nunca llego a la Luna  d-10 de marzo de 1960":"b",
                     "¿En que mision Apolo llego el hombre a la Luna?\n a-11 b-15\n c-17 d-7":"a",
                     "¿Quien Fue el primer hombre en pisar la Luna?\n a-Edwin E. Aldrin Jr. b-Michael Collins\n c-Neil A. Armstrong   d-Nunca llegaron ":"c",
                     "¿Dónde aterrizo el modulo Eagle cuando llego a la Luna?\n a-Crater Kepler           b-Mare Nubium\n c-Mare Tranquilidad       d-Mare Imbrium":"c",
                     "El nombre griego que recibe la Luna es:\n a-Iah       b-Ninnin\n c-Selene    d-Coya Raymi ":"c",
                     "¿Cuántas Unidades Astronomicas(UA) hay entre la Tierra y el sol?\n a-1            b-5,20336301\n c-9,53707032   d-0,38709893 ":"a",
                     "¿Quién es la primera mujer en el espacio?\n a-Judith Resnik  b-Peggy Whitson\n c-Sally Rid      d-Valentina Tereshkova":"d",
                     "¿Cuál es el principal telescopio en el espacio?\n a-Observatorio de rayos X Chandra      b-Telescopio espacial Hubble\n c-Observatorio de Rayos Gamma Compton  d-elescopio espacial Spitzer":"b", 
                     "¿Cuántos anillos tiene Jupiter?\n a-3   b-15\n c-40  d-8":"a",
                     "¿Qué planetas del sistema solar, tienen anillos?\n a-Mercurio,Jupiter, Saturno,Tierra b-Urano, Marte, Venus, Saturno\n c-Ninguno tiene anillos            d-Jupiter,Saturno, Urano, Neptuno":"d",
                     "¿Qué planeta es el que tiene mas lunas en el sistema solar?'\n a-Neptuno  b-Saturno\n c-Mercurio d-Jupiter":"b",
                     "¿Cuánto es el periodo de orbita del cometa Halley?\n a-2537 años  b-6.8 años\n c-76 años    d-6.6 años":"c",
                     "¿Qué planeta es conocido como el escudo contra cometas y asteroides, de la tierra?\n a-Neptuno  b-Saturno\n c-Mercurio d-Jupiter":"d",
                     "¿Qué es lo que se encuentra entre Marte y Jupiter?\n a-Cinturon de asteroides  b-Nada\n c-Pluton                  d-Tierra":"a",
                     "¿Qué cinturon es mas grande?\n a-Cinturon de Kuiper b-Cinturon de asteroides\n         c-nube de Oort ":"a",
                     "¿Qué cuerpo celeste, se observa a simple vista y parece que tiene cola?\n a-No existe nada igual  b-Cometa\n c-Meteorito             d-Pluton":"b",}
        
        question = random.choice(list(diccionario.keys()))
        answer = diccionario[question]
        fake_answer1=answer
        fake_answer2=answer
        fake_answer3=answer
        
        while(fake_answer1==answer):
            fake_answer1=random.choice(list(diccionario.values()))

        while(fake_answer2==answer):
            fake_answer2=random.choice(list(diccionario.values()))

        while(fake_answer3==answer):
            fake_answer3=random.choice(list(diccionario.values()))

        answerslist= [answer,fake_answer1,fake_answer2,fake_answer3]
        selected_diccionario={}

        print("Pregunta: " + question)
        for i in range(0,len(answerslist)):
            element= random.choice(answerslist)
            print(str(i+1) + ")" +element)
            selected_diccionario[str(i+1)]=element
            answerslist.remove(element)


        print("Ingrese la respuesta que considera correcta, asqueroso humano:"'\n')
        user_answer_index=input("> ")
        user_answer= selected_diccionario[user_answer_index]

        if user_answer in diccionario.values():
            if (diccionario[question]== user_answer):
                print("Correcto")
            else:
                print("Incorrecto")
                print("Has muerto viajero espacial")

        print("¿Quieres volver a jugarte la vida? Escribe: SI o NO"'\n')
        val = input("> ")
        if val=="SI" or val=="si" or val=="Si":
            juego()
        elif val=="NO" or val=="no" or val=="No":
            mover()
        else:
            print("NO HAS SEGUIDO MIS INTRUCCIONES. MUERE \n")
            print("\n")
            menu()
            
def impmap(val):
    print("Mapa de la Estación Once \n")
    print("|01|02|03|04|05|06|07|")
    print("======================")
    print("| 0| 0| 0| 0| 0| 0| 0| 1")
    print("|  |  |  |  | 0| 1| 0| 2")
    print("| 0| 0| 0|  | 0|  | 0| 3")
    print("| 0| 1| 0|  |  |  | 0| 4")
    print("| 0|  |  |  | 0|  | 0| 5")
    print("| 0| 0| 0| 0| 0| 0| 0| 6")
    print("======================\n")
    print("Usted está en ", val)

    
def mover():
    print("Mapa de la Estación Once \n")
    print("|01|02|03|04|05|06|07|")
    print("======================")
    print("| 0| 0| 0| 0| 0| 0| 0| 1")
    print("|  |  |  |  | 0| 1| 0| 2")
    print("| 0| 0| 0|  | 0|  | 0| 3")
    print("| 0| 1| 0|  |  |  | 0| 4")
    print("| 0|  |  |  | 0|  | 0| 5")
    print("| 0| 0| 0| 0| 0| 0| 0| 6")
    print("======================\n")
    print("Escriba posición: ")
    val = input("> ")
    if val=="11"or val=="21"or val=="31"or val=="41"or val=="51"or val=="61"or val=="71":
        impmap(val)
        print("Es una pared \n")
        mover()
    elif val=="52"or val=="72"or val=="13"or val=="23"or val=="33"or val=="33"or val=="53":
        impmap(val)
        print("Es una pared \n")
        mover()
    elif val=="73"or val=="14"or val=="34"or val=="74"or val=="15"or val=="55"or val=="75":
        impmap(val)
        print("Es una pared \n") 
        mover()
    elif val=="16"or val=="26"or val=="36"or val=="46"or val=="56"or val=="66"or val=="76":
        impmap(val)
        print("Es una pared \n") 
        mover()
    elif val=="12"or val=="22"or val=="32"or val=="42"or val=="43"or val=="63"or val=="44":
        impmap(val)
        print("Está en un pasillo \n")
        mover()
    elif val=="54"or val=="64"or val=="25"or val=="35"or val=="45"or val=="65":
        impmap(val)
        print("Está en un pasillo \n")
        mover()
    elif val=="62":
        juego()
    elif val=="24":
        juego()
    elif val=="menu" or val=="MENU" or val=="Menu":
        menu()
    else:
        print("La posición no existe \n")
        mover()             
            
def setup_game():
    mover()
title_screen()