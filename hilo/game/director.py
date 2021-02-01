import sys
from game.dealer import Dealer

class Director:
    '''
    The director class will start the game, allows the user to play again,
    and it gets the choice of the user.
    '''

    def __init__(self):
        self.points = 0        

    def points(self, choice):
        # TODO compute points/track points
        if choice == 'h' or choice == 'H':
            self.points += 100
        else:
            self.points -= 75
        

    def play_again(self):
        # TODO ask to play again, determine if the player can play again
        play_again = input("Do you want to play again? y/n")
        if play_again == "y":
            get_choice()
        else:
            exit()
      

    def get_choice(self):
        print('The card is {card}')
        condition = True
        while(condition):
            choice = input("Higher or Lower [h/l]")
            if choice == 'h' or choice == 'H' or choice == 'L' or choice == 'l':
                condition = False
                return choice
            else:
                print("Please choose an h/H or an l/L")
        # TODO get user input 
        # TODO figure out how to connect if the user's number is higher or lower than the card value
        pass
    pass

    
    # start_game
    # points
    # play_again
    # get_choice