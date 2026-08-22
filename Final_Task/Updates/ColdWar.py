# ==========================================
# COLD WAR ARMORY
# NATO vs WARSAW PACT
# ==========================================

# ---------- CLASS ----------

class Weapon:
    def __init__(self, name, year_design, caliber, firing_mode,
                 damage, accuracy, range, rate_of_fire,
                 magazine_capacity, reload_time, recoil,
                 weight, description):

        self.name = name
        self.year_design = year_design
        self.caliber = caliber
        self.firing_mode = firing_mode

        self.damage = damage

        self.accuracy = accuracy
        self.range = range
        self.rate_of_fire = rate_of_fire
        self.magazine_capacity = magazine_capacity
        self.reload_time = reload_time
        self.recoil = recoil
        self.weight = weight
        self.description = description

    def show_info(self):
        print("\n=== WEAPON INFORMATION ===")

        print("Name:", self.name)
        print("Year of Design:", self.year_design)
        print("Caliber:", self.caliber)
        print("Firing Mode:", self.firing_mode)

        print("Damage:", self.damage)
        print("Accuracy:", self.accuracy)
        print("Range:", self.range)
        print("Rate of Fire:", self.rate_of_fire)
        print("Magazine Capacity:", self.magazine_capacity)
        print("Reload Time:", self.reload_time, "seconds")
        print("Recoil:", self.recoil)
        print("Weight:", self.weight, "kg")

        print("Description:", self.description)

    def compare(self, other_weapon):
        print("\n=== WEAPON COMPARISON ===")

        print(f"\n{self.name} vs {other_weapon.name}")

        print("\nDamage:")
        print(self.name + ":", self.damage)
        print(other_weapon.name + ":", other_weapon.damage)

        print("\nAccuracy:")
        print(self.name + ":", self.accuracy)
        print(other_weapon.name + ":", other_weapon.accuracy)

        print("\nRange:")
        print(self.name + ":", self.range)
        print(other_weapon.name + ":", other_weapon.range)

        print("\nRate of Fire:")
        print(self.name + ":", self.rate_of_fire)
        print(other_weapon.name + ":", other_weapon.rate_of_fire)

        print("\nMagazine Capacity:")
        print(self.name + ":", self.magazine_capacity)
        print(other_weapon.name + ":", other_weapon.magazine_capacity)

        print("\nReload Time:")
        print(self.name + ":", self.reload_time)
        print(other_weapon.name + ":", other_weapon.reload_time)

        print("\nRecoil:")
        print(self.name + ":", self.recoil)
        print(other_weapon.name + ":", other_weapon.recoil)

        print("\nWeight:")
        print(self.name + ":", self.weight)
        print(other_weapon.name + ":", other_weapon.weight)

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
    
    # TODO:
    # Display weapons belonging to the
    # selected faction and class

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
                continue

            else:
                print("\nInvalid choice.")

        elif choice == "3":
            comparison_menu(weapons, faction, selected_weapon)

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