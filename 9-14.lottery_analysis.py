from random import choice


MY_TICKET = "15e2"
print(f"My ticket number is {MY_TICKET}")


def lottery():
    possibilities = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
    ]
    first_up = choice(possibilities)
    second_up = choice(possibilities)
    third_up = choice(possibilities)
    forth_up = choice(possibilities)
    return first_up + second_up + third_up + forth_up


plays = 0

while True:
    winner = lottery()
    plays += 1
    if MY_TICKET == winner:
        print(f"It took {plays} turns for you to win")
        break
