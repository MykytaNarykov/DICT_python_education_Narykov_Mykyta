import random

player1 = "John"
player2 = "Jack" # Jack теперь бот

while True:
    pencils_str = input("How many pencils would you like to use:\n")
    if not pencils_str.isdigit():
        print("The number of pencils should be numeric")
        continue
    pencils = int(pencils_str)
    if pencils == 0:
        print("The number of pencils should be positive")
        continue
    break

while True:
    current_player = input(f"Who will be the first ({player1}, {player2}):\n")
    if current_player not in [player1, player2]:
        print(f"Choose between '{player1}' and '{player2}'")
        continue
    break

while pencils > 0:
    print("|" * pencils)
    print(f"{current_player}'s turn!")

    if current_player == player1:
        while True:
            taken_str = input()
            if taken_str not in ['1', '2', '3']:
                print("Possible values: '1', '2' or '3'")
                continue
            taken = int(taken_str)
            if taken > pencils:
                print("Too many pencils were taken")
                continue
            break

    else:
        if pencils == 1:
            taken = 1
        elif pencils % 4 == 0:
            taken = 3
        elif pencils % 4 == 3:
            taken = 2
        elif pencils % 4 == 2:
            taken = 1
        else:
            possible_moves = [i for i in [1, 2, 3] if i <= pencils]
            taken = random.choice(possible_moves)

        print(taken)

    pencils -= taken

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

print(f"{current_player} won!")