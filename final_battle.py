# Import the functions we need from setup.py
# choose_player_pokemon() will let the player pick a Pokémon
# choose_cpu_pokemon() will pick a Pokémon for the CPU
# print_pokemon() will display the Pokémon's name and stats
from setup import choose_player_pokemon, choose_cpu_pokemon, print_pokemon


# Define the main function that runs the battle
def main():
    # Print the title of the game
    print("=== Simple Pokémon Battle ===\n")

    # Get the player's Pokémon by calling the choose_player_pokemon function
    player = choose_player_pokemon()

    # Get the CPU's Pokémon by calling the choose_cpu_pokemon function
    cpu = choose_cpu_pokemon()

    # Print the details of the player's Pokémon
    print_pokemon(player, "Player")

    # Print the details of the CPU's Pokémon
    print_pokemon(cpu, "CPU")

    # Print a header for the battle outcome
    print("\n--- Battle Result ---")

    # Compare the attack stats of the player's and CPU's Pokémon
    if player["attack"] > cpu["attack"]:
        # Player has a higher attack, so player wins
        print("Player wins! Congratulations!")
    elif cpu["attack"] > player["attack"]:
        # CPU has a higher attack, so CPU wins
        print("CPU wins! Better luck next time.")
    else:
        # Both have the same attack, so it's a tie
        print("It's a tie! Well matched.")


# Standard Python check to make sure main() runs only when this file is executed directly
if __name__ == "__main__":
    main()

