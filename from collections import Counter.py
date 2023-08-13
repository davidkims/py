from collections import Counter

def find_incomplete_player(participants, finishers):
    return list(Counter(participants) - Counter(finishers))[0]

if __name__ == "__main__":
    participants = ["leo", "kiki", "eden"]
    finishers = ["eden", "kiki"]

    print(find_incomplete_player(participants, finishers))