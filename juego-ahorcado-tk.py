
from ast import Delete
from gc import disable
from operator import length_hint
from sys import intern
import tkinter as tk
import random
from typing import Literal

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

palabra_secreta = generar_palabra_secreta()
intentos = 7
letras_adivinadas = []
juego_terminado = False
numeroDeLetras = len(palabra_secreta)
progreso_actual = mostrar_progreso


    # print("Bienvenido al juego del Ahorcado con nombres de videojuego")
    # print(f"el nombre de videojuego que debes adivinar tiene {numeroDeLetras} letras")
    # print(f"tenes {intentos} intentos para descubrir la palabra")
    # print(mostrar_progreso(palabra_secreta, letras_adivinadas))
    
def juego_iniciado():
        global  palabra_secreta
        global  letras_adivinadas
        global  numeroDeLetras
        global  intentos
        global  juego_terminado
        letra_ingresada = str(letra.get()).lower()
        if len(letra_ingresada) != 1 or not letra_ingresada.isalpha:
                instruccion.config(text="Ingrese una sola letra")
        elif letra_ingresada in letras_adivinadas:
            instruccion.config(text="ya utilizaste esa letra")
        else:
            letras_adivinadas.append(letra_ingresada)
            
            if letra_ingresada in palabra_secreta:
                instruccion.config(text=f"muy bien haz acertado la letra {letra_ingresada} está presente en el nombre")
            else:
                intentos -= 1
                instruccion.config(text=f"lo siento la letra {letra_ingresada} no está presente")
                instruccion.config(text=f"te que dan {intentos} intentos")
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        progreso_palabra.config(text=progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            instruccion.config(text=f"Felicitaciones haz ganado, el videojuego se llamaba {palabra_secreta}")
            ingresar.config(state="disabled")
        if intentos == 0:
            instruccion.config(text=f"haz perdido, el videojuego era {palabra_secreta}")
            ingresar.config(state="disabled")
        letra.delete(0, tk.END)

def nuevo_titulo():
    global  palabra_secreta
    global  letras_adivinadas
    global  numeroDeLetras
    global  intentos
    global  juego_terminado
    generar_palabra_secreta()
    palabra_secreta = generar_palabra_secreta()
    intentos = 7
    letras_adivinadas = []
    juego_terminado = False
    numeroDeLetras = len(palabra_secreta)
    progreso_actual = mostrar_progreso
    ingresar.config(state="normal")
    instruccion.config(text="Ingrese una letra")
    progreso_palabra.config(text=progreso_actual(palabra_secreta, letras_adivinadas))


#Configuracion de ventana
ventana = tk.Tk()
ventana.title("Ahorcado con videojuegos")
ventana.geometry("800x400")

#Mostrar Avance
progreso_palabra = tk.Label(ventana, font=('Arial', 18), text=progreso_actual(palabra_secreta, letras_adivinadas))
progreso_palabra.pack()

#ingreso de letra
instruccion = tk.Label(ventana, font=('Arial', 18), text="ingresar una letra")
instruccion.pack()
letra = tk.Entry(ventana, font=('Arial', 18), bd=20, insertwidth=1, width=4, borderwidth=4)
letra.pack()
ingresar = tk.Button(ventana, text="Ingresar Letra", font=('Arial', 12), padx=20, pady=20, command=juego_iniciado)
ingresar.pack()
nuevo_juego = tk.Button(ventana, text="Nuevo Juego", font=('Arial', 12), padx=20, pady=20, command=nuevo_titulo)
nuevo_juego.pack()


ventana.mainloop()



    
