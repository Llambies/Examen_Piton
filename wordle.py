from cgitb import text
from operator import contains, le
import random as r


def choose_secret(nombreArchivo):
    """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
    """
    palabros=[]
    texto = ""
    with open(nombreArchivo, mode="rt", encoding="utf-8") as f:
      texto = f.read()
      if(len(texto)<1):
        raise ValueError("Fichero vacío")

      palabras = texto.split("\n")
      for p in palabras:
          palabros.append(p)

    numero = r.randint(0,len(palabros))
    print(palabros)
    return palabros[numero]



    
def compare_words(secret,word):
    """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    if(len(secret)!=len(word)):
      raise ValueError("No tienen el mismo tamaño")

    same_position = []
    same_letter = []

    for i in range(len(word)):
      if(word[i]==secret[i]):
        same_position.append(i)
      elif(contains(secret,word[i])):
        same_letter.append(i)

    return same_position,same_letter

def print_word(word,same_position,same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    transformed = ""
    for i in range(len(word)):
      if(contains(same_position,i)):
        transformed+=word[i].upper()
      elif(contains(same_letter,i)):
        transformed+=word[i].lower()
      else:
        transformed+="-"
    return transformed
        

    
def choose_secret_advanced(nombreArchivo):
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """
    accentos = ["á","é","í","ó","ú"]
    palabros=[]
    with open(nombreArchivo, mode="rt", encoding="utf-8") as f:
      for linea in f:
          palabras = linea.split(" ")
          for p in palabras:
              if "\n" in p:
                p = p[0:(len(p)-1)]
                valida = True
                for letra in p:
                  if(contains(accentos,letra)):
                    valida = False
                if(len(p)==5):
                  if(valida):
                    if not (contains(palabros,p)):
                      palabros.append(p)
          
    if(len(palabros)<15):
      raise ValueError("No hay suficientes palabras") 
    palabras = palabros[0:15]
    numero = r.randint(0,len(palabras))
    return palabras[numero]
 
def check_valid_word(selected):
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """
    word = input("Introduce una palabra :")

    while( not contains(selected,word)):  
      word = input("Palabra no válida, introduce otra palabra :")

    return word




if __name__ == "__main__":
    try:
      #secret=choose_secret("palabras_reduced.txt")
      secret=choose_secret_advanced("palabras_extended.txt")
    except Exception as exc:
      print(exc)
      exit()


    lista_palabras = ['metro', 'sigla', 'mergo', 'mafia', 'chica', 'tozar', 'risco', 'merca', 'almea', 'suero', 'nidio', 'visco', 'guaro', 'hampo', 'toque']
    
    
    print("Palabra a adivinar: "+secret) #Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = check_valid_word(lista_palabras)
        same_position, same_letter = compare_words(secret,word)
        resultado=print_word(word,same_position,same_letter)
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   
    
