#####################################################################################
#                    Projeto nº 5: Hangman em python                                #
#                                                                                   #
#                                                                                   #
# Projeto vindo do curso gratuito "12 Beginner Python Projects - Coding Course"     #
#                                                                                   #
#                                                                                   #
#                                                                                   #
#                                                                                   #
# baseado no vídeo:https://www.youtube.com/watch?v=8ext9G7xspg 						#
#                                                                                   #                                                                                  #                                                                                  #                                                                                  3
#####################################################################################

import random
from palavras import dicio
import string

def palaValida(palavra):
    pala = random.choice(palavra)
    while '-' in pala or ' ' in pala:
        pala = random.choice(palavra)
    return pala.upper()

def forca():
    escolha = palaValida(dicio)
    escolhaLetras = set(escolha)
    alfabeto = set(string.ascii_uppercase)
    letrasUsadas = set()

    vidas = 10

    while len(escolhaLetras) > 0 and vidas > 0:
        # ' '.join(['a','b','cd']) ----> " a b cd"
        print("You have ",vidas,'lives left and you have used these letter: ',' '.join(letrasUsadas))

        #what current word is (IE   W - R D)
        word_list = [letra if letra in letrasUsadas else '-' for letra in escolha]
        print('Current word: ', ' '.join(word_list))

        userLetra = input("Guess a Letter: ").upper()
        if userLetra in alfabeto - letrasUsadas:
            letrasUsadas.add(userLetra)
            if userLetra in escolhaLetras:
                escolhaLetras.remove(userLetra)
                print('')
            else:
                vidas -= 1
                print("\nYour letter,",userLetra, 'is not in the word.\n')
        elif userLetra in letrasUsadas:
            print("You already used that word!")
        else: print("Invalid Character!!!")

    if vidas == 0:
        print("You died, sorry. \nThe word was",escolha)
    else: print("CONGRATZ!!!\nYou guess the word ",escolha,"!!")

if __name__ == '__main__':
    forca()