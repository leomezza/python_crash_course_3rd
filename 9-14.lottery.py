from random import choice

lottery = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e"]
first_up = choice(lottery)
second_up = choice(lottery)
third_up = choice(lottery)
forth_up = choice(lottery)

winner = first_up + second_up + third_up + forth_up

print(f"The person with the ticket {winner} wins a prize")
