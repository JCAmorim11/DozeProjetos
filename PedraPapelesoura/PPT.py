#####################################################################################
#                    Projeto nº 4: Rock,Paper and Scissors em python                #
#                                                                                   #
#                                                                                   #
# Projeto vindo do curso gratuito "12 Beginner Python Projects - Coding Course"     #
#                                                                                   #
#                                                                                   #
#                                                                                   #
#                                                                                   #
# baseado no vídeo:https://www.youtube.com/watch?v=8ext9G7xspg                      #                                                                                   #                                                                                  #                                                                                  #                                                                                  3
#####################################################################################

import random
def play():
    user = input("What's your choice?\n'R' for rock, 'P' for paper, 'S' for scissors\n").upper()
    computer = random.choice(['R','P','S'])
    if user == computer:
        return 'It\'s a tie'
    if is_win(user, computer):

        return 'You Won!!!!!'
    return 'You Lost! :('

def is_win(player, opponent):
    if(player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') \
        or (player == 'P' and opponent == 'R'):
        return True

print(play())