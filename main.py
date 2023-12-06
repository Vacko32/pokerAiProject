import random

class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class FullDeck(list):
    def __init__(self):
        super().__init__()
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = list(range(1, 14))
        [self.append(Card(value, suit)) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self)

    def print_shuffled_deck(self):
        for card in self:
            print(f"{card.value} of {card.suit}")

class Player(object):
    def __init__(self, name, starting_stack):
        self.name = name
        self.starting_stack = starting_stack
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)

def main():
    print("main executed")

def play_game():
    player_name = input("Enter Your Name: ")
    if not player_name:
        print("Name shouldnt be empty.")
        return

    player_stack = int(input("Enter Your Stack: "))
    if player_stack < 1:
        print("Enter normal stack please")
        return

    deck = FullDeck()
    deck.shuffle()


    player1 = Player(name=player_name, starting_stack=player_stack)
    player2 = Player(name="Player 2", starting_stack=player_stack)


    for _ in range(2):
        card1 = deck.pop()
        card2 = deck.pop()
        player1.receive_card(card1)
        player2.receive_card(card2)


    print(f"{player1.name}'s hand:")
    for card in player1.hand:
        print(f"{card.value} of {card.suit}")

    print(f"{player2.name}'s hand:")
    for card in player2.hand:
        print(f"{card.value} of {card.suit}")

def quit_game():
    print("Game quit.")

def print_shuffled_deck():
    deck = FullDeck()
    deck.shuffle()
    deck.print_shuffled_deck()

if __name__ == "__main__":

    main()
    play_game()
    quit_game()
