#####################################################################################
#                    Projeto nº 2: Guess the Number em python                       #
#                    Projeto nº 3: Computer Guess the Number em python              #
#                                                                                   #
# Projeto vindo do curso gratuito "12 Beginner Python Projects - Coding Course"     #
#                                                                                   #
#                                                                                   #
#                                                                                   #
#                                                                                   #
# baseado no vídeo:https://www.youtube.com/watch?v=8ext9G7xspg                      #                                                                                   #                                                                                  #                                                                                  #                                                                                  3
#####################################################################################

import random

def adivinhacao(x):
    randomNumero = random.randint(1,x)
    guess = 0
    while guess != randomNumero:
        guess = int(input(f'Advinhe o número (Is between 1 and {x}): '))
        print(guess)
        if guess < randomNumero:
            print('Foi mal, você vai ter que adivinhar de novo (T_T).\nValor MUITO BAIXO')
        elif guess >randomNumero:
            print('Eita desculpa, você vai ter que adivinhar de novo (T_T).\nValor MUITO ALTO')
        print()
    print(f'YAY PARABAINS.（*＾＾*)\nVocê adivinhou o número {randomNumero} corretamente!!!')

def pc_adivinhacao(x):
    low = 1
    high = x
    feedback=''
    while feedback != 'c':
        if low !=high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Está {guess} muito alto (H), muito baixo (L),ou está correto (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'YAY! *Voz robotica* Eu consegui adivinhar o número, {guess}, corretamente!! *Voz robotica* ')

pc_adivinhacao(1000)