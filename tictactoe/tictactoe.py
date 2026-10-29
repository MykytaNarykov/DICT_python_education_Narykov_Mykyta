
cells = list("         ")
current_player = "X"

def print_grid():
    print("---------")
    print(f"| {cells[0]} {cells[1]} {cells[2]} |")
    print(f"| {cells[3]} {cells[4]} {cells[5]} |")
    print(f"| {cells[6]} {cells[7]} {cells[8]} |")
    print("---------")

def check_winner():
    wins = [
        cells[0:3], cells[3:6], cells[6:9],
        [cells[0], cells[3], cells[6]], [cells[1], cells[4], cells[7]], [cells[2], cells[5], cells[8]],
        [cells[0], cells[4], cells[8]], [cells[2], cells[4], cells[6]]
    ]

    if ['X', 'X', 'X'] in wins:
        return "X wins"
    elif ['O', 'O', 'O'] in wins:
        return "O wins"
    elif ' ' not in cells:
        return "Draw"
    return None

print_grid()

while True:
    coords = input("Enter the coordinates: ").split()

    if len(coords) != 2 or not coords[0].isdigit() or not coords[1].isdigit():
        print("You should enter numbers!")
        continue

    row, col = int(coords[0]), int(coords[1])

    if not (1 <= row <= 3 and 1 <= col <= 3):
        print("Coordinates should be from 1 to 3!")
        continue

    index = (row - 1) * 3 + (col - 1)

    if cells[index] != ' ':
        print("This cell is occupied! Choose another one!")
        continue

    cells[index] = current_player
    print_grid()

    result = check_winner()
    if result:
        print(result)
        break

    current_player = "O" if current_player == "X" else "X"