

import random

# Generar Palabra Secreta
def generar_palabra_secreta():
    palabra = ["grand theft auto", "earthwormjim", "mario kart", "league of legend", "mario bros", "the legend of zelda", "double dragon", "castlevania", "red dead redemption", "god of war", "batman arkham knight", "donkey kong"]
    numeroDePalabras = len(palabra)
    palabraElegida = random.randint(0, numeroDePalabras-1)
    return palabra[palabraElegida]

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ""
    for letra in palabra_secreta:
        if letra in palabra_secreta:
            if letra in letras_adivinadas:
                adivinado += letra
            elif letra == " ":
                adivinado += " "
            else:
                adivinado += "_"

    return adivinado

def juego_ahorcado():
    palabra_secreta = generar_palabra_secreta()
    intentos = 7
    letras_adivinadas = []
    juego_terminado = False
    numeroDeLetras = len(palabra_secreta)

    print("Bienvenido al juego del Ahorcado con nombres de videojuego")
    print(f"el nombre de videojuego que debes adivinar tiene {numeroDeLetras} letras")
    print(f"tenes {intentos} intentos para descubrir la palabra")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas))
    
    while not juego_terminado:
        letra_ingresada = input("ingrese una letra: ").lower()
        if len(letra_ingresada) != 1 or not letra_ingresada.isalpha:
                print("Ingrese una sola letra")
        elif letra_ingresada in letras_adivinadas:
            print("ya utilizaste esa letra")
        else:
            letras_adivinadas.append(letra_ingresada)
            
            if letra_ingresada in palabra_secreta:
                print(f"muy bien haz acertado la letra {letra_ingresada} está presente en el nombre")
            else:
                intentos -= 1
                print(f"lo siento la letra {letra_ingresada} no está presente")
                print(f"te que dan {intentos} intentos")
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"Felicitaciones haz ganado, el videojuego se llamaba {palabra_secreta}")
        if intentos == 0:
            print(f"haz perdido, el videojuego era {palabra_secreta}") 
            break

        



juego_ahorcado()
    


