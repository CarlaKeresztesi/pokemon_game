from pokemon_api import get_pokemon
import random

def choose_player_pokemon():
    name = input("Enter a Pokemon name (or press Enter for random): ").lower()
    if name.strip() == "":
        rand_id = random.randint(1, 151)
        return get_pokemon(rand_id)
    return get_pokemon(name)

def choose_cpu_pokemon():
    rand_id = random.randid(1, 151)
    return get_pokemon(rand_id)

def print_pokemon(p, owner):
    print(f"\n--- {owner}'s Pokémon ---")
    print(f"Name:   {p['name']}")
    print(f"Types:  {', '.join(p['types'])}")
    print(f"Attack: {p['attack']}")