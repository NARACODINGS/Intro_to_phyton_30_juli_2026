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