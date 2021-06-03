#####################################################################################
#                    Projeto nº 6: Tic-Tac-Toe em python                            #
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

class Player:
    def __init__(self,letter):
        self.letter = letter

    def get_move(self,game):
        pass


class RandomComputerPlayer(Player):
    def __init__ (self,letter):
        super().__init__(letter)