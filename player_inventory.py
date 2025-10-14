import random

def display_map(position, treasures):
    for y in range(4, -1, -1):
        for x in range(5):
            if (x, y) == position:
                print("P", end=" ")
            elif (x, y) in treasures:
                print(".", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

print("Hello! Welcome to the Treasure Hunt Game")
print("TREASURE HUNT")

player = {
    "name": "Noshin",
    "coins": 0,
    "inventory": set()
}

position = (2, 2)
health = 100

treasures = {(random.randint(0, 4), random.randint(0, 4)) for _ in range(3)}
print(f"\nHello {player['name']}! You are starting at {position}. Let's find the treasures!\n")
display_map(position, treasures)

while True:
    print(f"Current position: {position} | Health: {health}")
    move = input("Move (w, s, a, d or q): ").lower()

    if move == "q":
        print("Thanks for playing!")
        break

    x, y = position

    if move == "w" and y < 4:
        y += 1
        health -= 5
    elif move == "s" and y > 0:
        y -= 1
        health -= 5
    elif move == "a" and x > 0:
        x -= 1
        health -= 5
    elif move == "d" and x < 4:
        x += 1
        health -= 5
    else:
        print("Invalid move or edge of the map!")
        continue

    position = (x, y)
    display_map(position, treasures)

    if health <= 0:
        print("You have no life left. Game over!")
        break

    if position in treasures:
        print("You found a treasure!")
        player["inventory"].add("Treasure")
        health += 2
        player["coins"] += 10
        treasures.remove(position)
    else:
        print("No treasure here.")

    if not treasures:
        print("Congratulations! You found all treasures!")
        print(f"Earned coins: {player['coins']}")
        break
