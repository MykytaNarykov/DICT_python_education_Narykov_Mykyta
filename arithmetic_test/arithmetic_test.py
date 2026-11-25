import random

while True:
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")

    level = input()

    if level in ["1", "2"]:
        break

    print("Incorrect format.")

mark = 0

for i in range(5):
    if level == "1":
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        operation = random.choice(["+", "-", "*"])

        print(f"{a} {operation} {b}")

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        else:
            result = a * b

    else:
        a = random.randint(11, 29)
        print(a)
        result = a ** 2

    while True:
        try:
            answer = int(input())
            break
        except ValueError:
            print("Incorrect format.")

    if answer == result:
        print("Right!")
        mark += 1
    else:
        print("Wrong!")

print(f"Your mark is {mark}/5.")
print("Would you like to save your result to the file?")
print("Enter yes or no.")

save = input().lower()

if save in ["yes", "y"]:
    print("What is your name?")
    name = input()

    if level == "1":
        description = "simple operations with numbers 2-9"
    else:
        description = "integral squares of 11-29"

    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(
            f"{name}: {mark}/5 in level {level} ({description}).\n"
        )

    print('The results are saved in "results.txt".')