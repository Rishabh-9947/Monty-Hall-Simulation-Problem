import random

def simulate_monty_hall(switch_doors):
    # Set up the doors (0: goat, 1: car)
    doors = [0, 0, 1]
    random.shuffle(doors)

    # Contestant's initial choice
    choice = random.randint(0, 2)

    # Host opens a door with a goat
    open_door = next(i for i in range(3) if i != choice and doors[i] == 0)

    # Contestant decides whether to switch
    if switch_doors:
        choice = next(i for i in range(3) if i != choice and i != open_door)

    # Return whether the contestant won the car
    return doors[choice] == 1

# Example usage
def main():
    stick_wins = sum(not simulate_monty_hall(switch_doors=True) for _ in range(10000))
    switch_wins = sum(simulate_monty_hall(switch_doors=True) for _ in range(10000))
    print(f"Sticking wins: {stick_wins}")
    print(f"Switching wins: {switch_wins}")

if __name__ == "__main__":
    main()
