import random

class Dealer:
    '''
    The dealer class will deal a card between 1 and 13, and it will compute the
    points from the user's input.
    '''

    def __init__(self):
        self.card = []
        self.num_draw = 0
    
    def draw_card(self):
        result = random.randint(1, 13)
        self.card.append(result)
        self.num_draw += 1
    
    def get_last_card(self):
        
        return self.card[self.num_draw - 1]
        
    def determine_points(self, choice):
        points_scored = 0
        if ((choice == 'h' or choice == 'H') and self.card[self.num_draw - 1] > self.card[self.num_draw - 2]) or ((choice == 'l' or choice == 'L') and self.card[self.num_draw - 1] < self.card[self.num_draw - 2]):
            points_scored = 100
        else:
            points_scored = -75
        return points_scored