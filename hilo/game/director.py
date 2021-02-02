import sys
from game.dealer import Dealer

class Director:
    '''
    The director class will start the game, allows the user to play again,
    and it gets the choice of the user.
    '''

    def __init__(self):
        self.keep_playing = True
        self.dealer = Dealer()
        self.score = 300      
        self.choice = ''

    def start_game(self):
        self.dealer.draw_card()
        while self.keep_playing:
            self.choice = self.get_choice()
            self.next_card()
            self.points(self.choice)
            self.play_again()
    
    def next_card(self):
        self.dealer.draw_card()
        print(f"Next card was: {self.dealer.get_last_card()}")

    def points(self, choice):
        if choice == 'h' or choice == 'H' or choice == 'l' or choice == 'L':
            self.score += self.dealer.determine_points(choice)
        else:
            self.score -= self.dealer.determine_points(choice)
        
        print(f"The score is {self.score}")

                
         
    def play_again(self):
        if self.score > 0:
            play_again = input("Do you want to play again? [y/n]: ")
            if play_again == "y":
                self.keep_playing = True
                print()
            else:
                print('Sad to see you go!')
                self.keep_playing = False
        else:
            print('Sad to see you go!')
            self.keep_playing = False
      
    def get_choice(self):
        self.dealer.draw_card()
        print(f'The card is {self.dealer.get_last_card()}')
        condition = True
        while(condition):
            choice = input("Higher or Lower [h/l]: ")
            if choice == 'h' or choice == 'H' or choice == 'L' or choice == 'l':
                condition = False
                return choice
            else:
                print("Please choose an h/H or an l/L")