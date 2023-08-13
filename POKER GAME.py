import random

class Card:
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Card.SUITS for value in Card.VALUES]
        random.shuffle(self.cards)

    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]

def evaluate_hand(hand):
    values = [card.value for card in hand]
    value_counts = {value: values.count(value) for value in values}
    sorted_counts = sorted(value_counts.values(), reverse=True)

    # Check for simple cases: 4-of-a-kind, 3-of-a-kind, 2-pair, 1-pair
    if 4 in sorted_counts:
        return "Four of a Kind", values
    elif 3 in sorted_counts and 2 in sorted_counts:
        return "Full House", values
    elif 3 in sorted_counts:
        return "Three of a Kind", values
    elif sorted_counts.count(2) == 2:
        return "Two Pairs", values
    elif 2 in sorted_counts:
        return "One Pair", values
    else:
        return "High Card", values

def main():
    deck = Deck()
    player_hand = deck.deal(5)
    computer_hand = deck.deal(5)

    print("Your hand:", ', '.join(str(card) for card in player_hand))
    print("Computer's hand:", ', '.join(str(card) for card in computer_hand))

    player_evaluation, player_values = evaluate_hand(player_hand)
    computer_evaluation, computer_values = evaluate_hand(computer_hand)

    print("\nYour hand is:", player_evaluation)
    print("Computer's hand is:", computer_evaluation)

    # Compare hands
    hand_ranks = ["High Card", "One Pair", "Two Pairs", "Three of a Kind", "Full House", "Four of a Kind"]
    if hand_ranks.index(player_evaluation) > hand_ranks.index(computer_evaluation):
        print("\nYou win!")
    elif hand_ranks.index(player_evaluation) < hand_ranks.index(computer_evaluation):
        print("\nComputer wins!")
    else:
        # Compare card values for tie-breaker
        player_values.sort(key=lambda v: (Card.VALUES.index(v), v), reverse=True)
        computer_values.sort(key=lambda v: (Card.VALUES.index(v), v), reverse=True)
        if player_values > computer_values:
            print("\nYou win!")
        else:
            print("\nComputer wins!")

if __name__ == "__main__":
    main()