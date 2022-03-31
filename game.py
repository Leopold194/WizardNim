import random

class Game:

    def __init__(self, nb = 12):

        self.batons = [1 for _ in range(nb)]

    def player_turn(self, nb):
        
        for _ in range(nb):
            self.batons.pop()

        if len(self.batons) == 0:
            return 0 #Le joueur a perdu
        else:
            return 1 #Le jeu continue

    def computer_turn(self):

        if len(self.batons) - 1 == 9 or len(self.batons) - 1 == 5 or len(self.batons) - 1 == 1:
            nb = 1
        elif len(self.batons) - 2 == 9 or len(self.batons) - 2 == 5 or len(self.batons) - 2 == 1:
            nb = 2
        elif len(self.batons) - 3 == 9 or len(self.batons) - 3 == 5 or len(self.batons) - 3 == 1:
            nb = 3
        else:
            max = len(self.batons) if len(self.batons) <= 3 else 3
            nb = random.randint(1,max)
        
        for _ in range(nb):
            self.batons.pop()

        if len(self.batons) == 0:
            return 0 #La machine a perdu
        else:
            return nb #On renvoie le nombre d'allumette utilisé par la machine

    def remaining(self):
        
        return len(self.batons)