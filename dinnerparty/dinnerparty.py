import random

num_friends = int(input("Enter the number of friends joining (including you):\n"))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    friends_dict = {}

    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        name = input()
        friends_dict[name] = 0

    total_amount = float(input("\nEnter the total amount:\n"))

    lucky_answer = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if lucky_answer == "Yes":
        lucky_name = random.choice(list(friends_dict.keys()))
        print(f"\n{lucky_name} is the lucky one!")

        if num_friends > 1:
            split_amount = round(total_amount / (num_friends - 1), 2)
        else:
            split_amount = 0  # Якщо людина одна, ділити ні на кого

        for friend in friends_dict:
            if friend == lucky_name:
                friends_dict[friend] = 0
            else:
                friends_dict[friend] = split_amount

    else:
        print("\nNo one is going to be lucky")

        split_amount = round(total_amount / num_friends, 2)

        for friend in friends_dict:
            friends_dict[friend] = split_amount

    print(friends_dict)
