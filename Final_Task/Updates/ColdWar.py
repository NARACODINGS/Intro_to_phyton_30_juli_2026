# ==========================================
# COLD WAR ARMORY
# NATO vs WARSAW PACT
# ==========================================


# ---------- CLASS ----------

import random

from Weapon import Weapon

# ---------- DISPLAY FUNCTIONS ----------

def load_weapons():
    file = open("weapons.txt", "r")

    loaded_weapons = {
        "NATO": {
            "Assault": [],
            "Support": [],
            "Recon": []
        },

        "Warsaw Pact": {
            "Assault": [],
            "Support": [],
            "Recon": []
        }
    }

    for line in file:
        data = line.strip().split("|")

        weapon = Weapon(
            data[2],
            int(data[3]),
            data[4],
            data[5],
            int(data[6]),
            int(data[7]),
            int(data[8]),
            int(data[9]),
            int(data[10]),
            float(data[11]),
            int(data[12]),
            float(data[13]),
            data[14]
)

        faction = data[0]
        weapon_class = data[1]

        loaded_weapons[faction][weapon_class].append(weapon)

    file.close()

    return loaded_weapons

def show_factions():
    print("\n=== CHOOSE FACTION ===")
    print("1. NATO")
    print("2. Warsaw Pact")

    choice = input("Choose your faction: ")

    if choice == "1":
        return "NATO"
    elif choice == "2":
        return "Warsaw Pact"
    else:
        print("Invalid choice.")
        return show_factions()

def show_classes():
    print("\n=== CHOOSE CLASS ===")
    print("1. Assault")
    print("2. Support")
    print("3. Recon")

    choice = input("Choose your class: ")

    if choice == "1":
        return "Assault"
    elif choice == "2":
        return "Support"
    elif choice == "3":
        return "Recon"
    else:
        print("Invalid choice.")
        return show_classes()


def show_weapons(weapons, faction, weapon_class):
    print("\n=== AVAILABLE WEAPONS ===")
    
    selected_weapons = weapons[faction][weapon_class]

    for weapon in selected_weapons:
        print("-", weapon.name)

def choose_weapon(weapons, faction, weapon_class):
    selected_weapons = weapons[faction][weapon_class]

    print("\n=== CHOOSE WEAPON ===")

    for number, weapon in enumerate(selected_weapons, start=1):
        print(f"{number}. {weapon.name}")
    
    choice = input("Choose a weapon: ")

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= len(selected_weapons):
            return selected_weapons[choice - 1]
        
    print("Invalid choice")
    return choose_weapon(weapons, faction, weapon_class)

def show_weapon_info(weapon):
    weapon.show_info()

def armory_menu(weapons, faction, weapons_class, selected_weapon):

    while True:

        print("\n=== ARMORY ===")
        print("1. Done")
        print("2. Reset")
        print("3. Compare Weapon")
        print("4. Faction Quiz")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\n=== YOUR SELECTION ===")
            print("Nation:", faction)
            print("Class:", weapons_class)
            print("Weapon:", selected_weapon.name)

            print("\nArmory selection complete.")
            return "done"

        elif choice == "2":
            print("\nAre you sure you want to reset?")
            confirm = input("Yes / No: ")

            if confirm.lower() == "yes":
                print("\nResetting armory...")
                return "reset"

            elif confirm.lower() == "no":
                show_weapon_info(selected_weapon)
                continue

            else:
                print("\nInvalid choice.")

        elif choice == "3":
            comparison_menu(weapons, faction, selected_weapon)

        elif choice == "4":
            quiz_faction(weapons)

        else:
            print("\nInvalid choice.")

def get_faction_weapons(weapons, faction):
    faction_weapons = []

    for weapon_class in weapons[faction]:
        faction_weapons.extend(weapons[faction][weapon_class])

    return faction_weapons

def choose_comparison_weapon(weapons, faction, excluded_weapon):
    faction_weapons = get_faction_weapons(weapons, faction)

    print("\n=== CHOOSE WEAPON TO COMPARE ===")

    number = 1

    for weapon in faction_weapons:
        if weapon != excluded_weapon:
            print(f"{number}. {weapon.name}")
            number += 1

    choice = input("Choose a weapon: ")

    if choice.isdigit():
        choice = int(choice)

        available_weapons = []

        for weapon in faction_weapons:
            if weapon != excluded_weapon:
                available_weapons.append(weapon)

        if 1 <= choice <= len(available_weapons):
            return available_weapons[choice - 1]

    print("Invalid choice.")
    return None

def comparison_menu(weapons, faction, selected_weapon):

    while True:

        print("\n=== COMPARISON MENU ===")
        print("Selected weapon:", selected_weapon.name)

        other_weapon = choose_comparison_weapon(
            weapons,
            faction,
            selected_weapon
        )

        if other_weapon is not None:
            selected_weapon.compare(other_weapon)
            return

        print("\nInvalid choice. Returning to comparison menu.")

def quiz_faction(weapons):

    score = 0
    questions = 5

    print("\n=== FACTION QUIZ ===")

    all_weapons = []

    for faction in weapons:
        for weapon_class in weapons[faction]:
            for weapon in weapons[faction][weapon_class]:
                all_weapons.append((weapon, faction))

    for question_number in range(1, questions + 1):

        selected_weapon, correct_faction = random.choice(all_weapons)

        print("\nQuestion", question_number, "of", questions)

        print("\nWeapon:", selected_weapon.name)
        print("Year of Design:", selected_weapon.year_design)
        print("Caliber:", selected_weapon.caliber)
        print("Firing Mode:", selected_weapon.firing_mode)

        print("\nWhich faction does this weapon belong to?")
        print("1. NATO")
        print("2. Warsaw Pact")

        choice = input("Your answer: ")

        if choice == "1":
            answer = "NATO"
        elif choice == "2":
            answer = "Warsaw Pact"
        else:
            print("\nInvalid choice.")
            continue

        if answer == correct_faction:
            print("\nCorrect!")
            score += 1
        else:
            print("\nIncorrect.")
            print("The correct answer was:", correct_faction)

        print("Score:", score)

    print("\n=== QUIZ COMPLETE ===")
    print("Final Score:", score, "/", questions)
# ---------- MAIN PROGRAM ----------

def main():

    weapons = load_weapons()

    while True:

        print("================================")
        print("       COLD WAR ARMORY")
        print("       NATO vs WARSAW PACT")
        print("================================")

        # 1. Choose faction
        faction = show_factions()

        print("You selected:", faction)

        # 2. Choose class
        weapons_class = show_classes()

        print("You selected class:", weapons_class)

        # 3. Display weapons
        show_weapons(weapons, faction, weapons_class)

        # 4. Choose weapon
        selected_weapon = choose_weapon(weapons, faction, weapons_class)

        print("You selected weapon:", selected_weapon.name)

        # 5. Display weapon information
        show_weapon_info(selected_weapon)

        # 6. Armory menu
        result = armory_menu(
            weapons,
            faction,
            weapons_class,
            selected_weapon
        )

        if result == "done":
            break

        elif result == "reset":
            print("\nReturning to faction selection...")
            continue

# ---------- START PROGRAM ----------

main()