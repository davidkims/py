import time
import random

class Horse:
    def __init__(self, name):
        self.name = name
        self.distance_covered = 0

    def run(self):
        self.distance_covered += random.randint(1, 5)

    def display(self):
        print(self.name + ': ' + '-' * self.distance_covered + '>')

def race(horses):
    finish_line = 50
    while not any(h.distance_covered >= finish_line for h in horses):
        for horse in horses:
            horse.run()
            horse.display()
            time.sleep(0.1)
        time.sleep(1)
        print("\n" * 50)  # simple way to "clear" the console

    winners = [h.name for h in horses if h.distance_covered >= finish_line]
    return winners

def main():
    balance = 1000
    while balance > 0:
        print(f"Current balance: ${balance}")
        horses = [Horse("Horse1"), Horse("Horse2"), Horse("Horse3"), Horse("Horse4")]
        for idx, horse in enumerate(horses, 1):
            print(f"{idx}. {horse.name}")

        bet_horse = int(input("Choose a horse to bet on by entering its number (1-4): ")) - 1
        bet_amount = int(input(f"How much would you like to bet? (1-${balance}): "))

        if bet_amount > balance or bet_amount <= 0:
            print("Invalid bet amount.")
            continue

        balance -= bet_amount

        print(f"You bet ${bet_amount} on {horses[bet_horse].name}.\n")

        print("Starting the race!\n")
        time.sleep(2)

        winners = race(horses)

        if horses[bet_horse].name in winners:
            print(f"Congratulations! {horses[bet_horse].name} won!")
            balance += bet_amount * 2
        else:
            print(f"Sorry, {horses[bet_horse].name} didn't win this time. Better luck next time!")

    print("You are out of money. Thanks for playing!")

if __name__ == "__main__":
    main()