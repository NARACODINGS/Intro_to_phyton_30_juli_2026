# ==========================================
# COLD WAR ARMORY
# NATO vs WARSAW PACT
# ==========================================


# ---------- WEAPON DATA ----------

weapons = {
    "NATO": {
        "Assault": [
            {
                "name": "M16A1",
                "year_design": 1957,
                "caliber": "5.56x45mm",
                "firing_mode": "Semi / Burst",
                "damage": 72,
                "accuracy": 88,
                "range": 80,
                "rate_of_fire": 75,
                "magazine_capacity": 20,
                "reload_time": 2.4,
                "recoil": 35,
                "weight": 3.6,
                "description": "A lightweight service rifle designed for medium-range infantry combat."
            },
            {
                "name": "FN FAL",
                "year_design": 1947,
                "caliber": "7.62x51mm",
                "firing_mode": "Semi / Automatic",
                "damage": 82,
                "accuracy": 84,
                "range": 85,
                "rate_of_fire": 70,
                "magazine_capacity": 20,
                "reload_time": 2.6,
                "recoil": 45,
                "weight": 4.3,
                "description": "A powerful battle rifle designed for reliable medium-to-long-range combat."
            } 
        ],
        "Support": [
            {
                "name": "M60",
                "year_design": 1945,
                "caliber": "7.62x51mm",
                "firing_mode": "Automatic",
                "damage": 85,
                "accuracy": 78,
                "range": 85,
                "rate_of_fire": 72,
                "magazine_capacity": 100,
                "reload_time": 5.5,
                "recoil": 60,
                "weight": 10.5,
                "description": "A general-purpose machine gun designed to provide sustained fire support."
            },
            {
                "name": "Bren",
                "year_design": 1935,
                "caliber": ".303 British",
                "firing_mode": "Automatic",
                "damage": 78,
                "accuracy": 82,
                "range": 80,
                "rate_of_fire": 68,
                "magazine_capacity": 30,
                "reload_time": 3.2,
                "recoil": 50,
                "weight": 10.1,
                "description": "A magazine-fed light machine gun known for its accuracy and reliability."
            }
        ],
        "Recon": [
            {
                "name": "M1 Carbine",
                "year_design": 1941,
                "caliber": ".30 Carbine",
                "firing_mode": "Semi-Automatic",
                "damage": 65,
                "accuracy": 78,
                "range": 65,
                "rate_of_fire": 70,
                "magazine_capacity": 15,
                "reload_time": 2.3,
                "recoil": 25,
                "weight": 2.5,
                "description": "A lightweight semi-automatic carbine that offers good mobility and manageable recoil."
            },
            {
                "name": "Lee-Enfield",
                "year_design": 1895,
                "caliber": ".303 British",
                "firing_mode": "Bolt-Action",
                "damage": 90,
                "accuracy": 92,
                "range": 90,
                "rate_of_fire": 35,
                "magazine_capacity": 10,
                "reload_time": 3.0,
                "recoil": 55,
                "weight": 4.2,
                "description": "A bolt-action rifle known for strong long-range performance and a reliable magazine system."
            }
        ]
    },

    "Warsaw Pact": {
        "Assault": [
            {
                "name": "AK-47",
                "year_design": 1947,
                "caliber": "7.62×39mm",
                "firing_mode": "Semi / Automatic",
                "damage": 80,
                "accuracy": 76,
                "range": 72,
                "rate_of_fire": 75,
                "magazine_capacity": 30,
                "reload_time": 2.5,
                "recoil": 45,
                "weight": 3.8,
                "description": "A rugged assault rifle designed for reliable performance in a wide range of conditions."
            },
            {
                "name": "AKM",
                "year_design": 1959,
                "caliber": "7.62×39mm",
                "firing_mode": "Semi / Automatic",
                "damage": 78,
                "accuracy": 78,
                "range": 73,
                "rate_of_fire": 75,
                "magazine_capacity": 30,
                "reload_time": 2.4,
                "recoil": 43,
                "weight": 3.1,
                "description": "A lighter modernization of the AK platform, balancing durability, mobility, and firepower."
            }
        ],
        "Support": [
            {
                "name": "RPK",
                "year_design": 1958,
                "caliber": "7.62×39mm",
                "firing_mode": "Semi / Automatic",
                "damage": 76,
                "accuracy": 78,
                "range": 75,
                "rate_of_fire": 70,
                "magazine_capacity": 30,
                "reload_time": 2.5,
                "recoil": 45,
                "weight": 5.0,
                "description": "A light machine gun based on the AK platform, designed to provide mobile squad-level fire support."
            },
            {
                "name": "PK",
                "year_design": 1961,
                "caliber": "7.62×54mmR",
                "firing_mode": "Automatic",
                "damage": 86,
                "accuracy": 80,
                "range": 88,
                "rate_of_fire": 72,
                "magazine_capacity": 100,
                "reload_time": 5.2,
                "recoil": 58,
                "weight": 8.4,
                "description": "A general-purpose machine gun designed to provide sustained fire support over medium and long distances."
            }
        ],
        "Recon": [
            {
                "name": "Mosin-Nagant",
                "year_design": 1891,
                "caliber": "7.62×54mmR",
                "firing_mode": "Bolt-Action",
                "damage": 92,
                "accuracy": 90,
                "range": 92,
                "rate_of_fire": 30,
                "magazine_capacity": 5,
                "reload_time": 3.5,
                "recoil": 60,
                "weight": 4.0,
                "description": "A bolt-action rifle valued for its strong long-range performance and simple design."
            },
            {
                "name": "SVD",
                "year_design": 1958,
                "caliber": "7.62×54mmR",
                "firing_mode": "Semi-Automatic",
                "damage": 88,
                "accuracy": 94,
                "range": 95,
                "rate_of_fire": 55,
                "magazine_capacity": 10,
                "reload_time": 2.8,
                "recoil": 48,
                "weight": 4.3,
                "description": "A designated marksman rifle designed to provide accurate fire at extended ranges."
            }
        ]
    }
}


# ---------- DISPLAY FUNCTIONS ----------

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
        return None

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
        return None


def show_weapons(faction, weapon_class):
    print("\n=== AVAILABLE WEAPONS ===")

    # TODO:
    # Display weapons belonging to the
    # selected faction and class

    selected_weapons = weapons[faction][weapon_class]

    for weapon in selected_weapons:
        print("-", weapon["name"])

def choose_weapon(faction, weapon_class):
    selected_weapons = weapons[faction][weapon_class]

    print("\n=== CHOOSE WEAPON ===")

    for number, weapon in enumerate(selected_weapons, start=1):
        print(f"{number}. {weapon["name"]}")
    
    choice = input("Choose a weapon: ")

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= len(selected_weapons):
            return selected_weapons[choice - 1]
    print("Invalid choice")
    return None

def show_weapon_info(weapon):
    print("\n=== WEAPON INFORMATIOM ===")

    print("Name:", weapon["name"])
    print("Year of Design:", weapon["year_design"])
    print("Caliber:", weapon["caliber"])
    print("Firing Mode:", weapon["firing_mode"])

    print("Damage:", weapon["damage"])
    print("Accuracy:", weapon["accuracy"])
    print("Range:", weapon["range"])
    print("Rate of Fire:", weapon["rate_of_fire"])
    print("Magazine Capacity", weapon["magazine_capacity"])
    print("Reload Time:", weapon["reload_time"], "seconds")
    print("Recoil", weapon["recoil"])
    print("Weight:", weapon["weight"], "kg")

    print("Description:", weapon["description"])

def armory_menu(faction, weapons_class, selected_weapon):
    print("\n=== ARMORY ===")
    print("1. Done")
    print("2. Reset")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\n=== YOUR SELECTION ===")
        print("Nation:", faction)
        print("Class:", weapons_class)
        print("Weapon:", selected_weapon["name"])

        print("\nArmory selection complete.")
        return "done"

    elif choice == "2":
        print("\nAre you sure you want to reset?")
        confirm = input("Yes / No: ")

        if confirm.lower() == "yes":
            print("\nResetting armory...")
            return "reset"

        elif confirm.lower() == "no":
            print("\nReturning to armory menu...")
            return armory_menu(faction, weapons_class, selected_weapon)

        else:
            print("\nInvalid choice.")
            return armory_menu(faction, weapons_class, selected_weapon)

    else:
        print("\nInvalid choice.")
        return armory_menu(faction, weapons_class, selected_weapon)

# ---------- MAIN PROGRAM ----------

def main():

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
        show_weapons(faction, weapons_class)

        # 4. Choose weapon
        selected_weapon = choose_weapon(faction, weapons_class)

        print("You selected weapon:", selected_weapon["name"])

        # 5. Display weapon information
        show_weapon_info(selected_weapon)

        # 6. Armory menu
        result = armory_menu(faction, weapons_class, selected_weapon)

        if result == "done":
            break

        elif result == "reset":
            print("\nReturning to faction selection...")
            continue

# ---------- START PROGRAM ----------

main()