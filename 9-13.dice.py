from random import randint


class Die:
    """A simple attempt to model a dice."""

    def __init__(self, sides=6):
        """Initialize the battery's attributes."""
        self.sides = sides

    def roll_die(self):
        rolled_die = randint(1, self.sides)
        print(f"The number in the dice in {rolled_die}")


print("6 sides")
six_sided = Die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()

print("10 sides")
ten_sided = Die(10)
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()

print("20 sides")
twenty_sided = Die(20)
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
