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
        # TODO pick a random card between 1 and 13, returns that card value
        # TODO have a for loop to loop between cards (for i in range(1, 14))
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
        # TODO pass draw_card value into determine points, return number of points (if and else statement)
        # TODO get_last_card, is_last_card_higher, is_last_card_lower
        # TODO if correct, add 100 points, if incorrect lose 75 points