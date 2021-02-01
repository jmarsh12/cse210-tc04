import sys
from game.dealer import Dealer

class Director:
    '''
    
    '''

    def __init__(self):
                

    def points(self):
        # TODO compute points/track points
        pass

    def play_again(self):
        # TODO ask to play again, determine if the player can play again
        play_again = input("Do you want to play again? y/n")
        if play_again == "y"
            get_choice()
        else:
            exit()
      

    def get_choice(self):
        print('The card is {card}')
        choice = input("Higher or Lower [h/l]")
        if choice == 'h' or choice == 'H':
            return choice
        # TODO get user input 
        # TODO figure out how to connect if the user's number is higher or lower than the card value
        pass
    pass

    
    # start_game
    # points
    # play_again
    # get_choice