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


class FiveCards:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)


class Player(object):
    def __init__(self, name, starting_stack):
        self.name = name
        self.starting_stack = starting_stack
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)


def play_game():
    player_name = input("Enter Your Name: ")
    if not player_name:
        print("Name shouldnt be empty.")
        return

    player_stack = int(input("Enter Your Stack: "))
    if player_stack < 1:
        print("Enter normal stack please")
        return

    player1 = Player(name=player_name, starting_stack=player_stack)
    player2 = Player(name="Player 2", starting_stack=player_stack)

    players = [player1, player2]

    def start_turn():
        print("new round has started")
        deck = FullDeck()
        deck.shuffle()

        comCards = FiveCards()

        for _ in range(2):
            card1 = deck.pop()
            card2 = deck.pop()
            player1.receive_card(card1)
            player2.receive_card(card2)

        for _ in range(3):
            flop_card = deck.pop()
            comCards.add_card(flop_card)

    def end_turn():
        print("Turn ended")

    start_turn()
    end_turn()


def quit_game():
    print("Game quit.")


def main():
    print("main executed")
    play_game()
    quit_game()


if __name__ == "__main__":
    main()
