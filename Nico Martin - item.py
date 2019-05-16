class Item(object):
    def __init__(self, name):
        self.name = name


class Armor(Item):
    def __init__(self, name, protection,):
        super(Armor, self).__init__(name)
        self.protection = protection


class ChestPlate(Armor):
    def __init__(self):
        super(ChestPlate, self).__init__("Bronze Chest Plate, Protection-10", 10)


class Leggings (Armor):
    def __init__(self):
        super(Leggings, self).__init__("Bronze Leggings, Protection - 10", 10)


class Boots (Armor):
    def __init__(self):
        super(Boots, self).__init__("Bronze Boots, Protection - 10", 10)


class Weapon(Item):
    def __init__(self, name, attack):
        super(Weapon, self).__init__(name)
        self.attack = attack


class Gun1 (Weapon):
    def __init__(self):
        super(Gun1, self).__init__("Bronze Handgun, Attack Damage - 10", 10)


class Crossbow (Weapon):
    def __init__(self):
        super(Crossbow, self).__init__("Bronze Crossbow, Attack Damage - 10", 10)


class KitchenKnife (Weapon):
    def __init__(self):
        super(KitchenKnife, self).__init__("Bronze Kitchen Knife, Attack Damage- 10", 10)


class Sword (Weapon):
    def __init__(self):
        super(Sword, self).__init__("Bronze Sword, Attack Damage - 10", 10)


class Electronic (Item):
    def __init__(self, name, battery):
        super(Electronic, self).__init__(name)
        self.battery = battery


class Flashlight (Electronic):
    def __init__(self):
        super(Flashlight, self).__init__("Flashlight", 50)


class Tv (Electronic):
    def __init__(self):
        super(Tv, self).__init__("Tv", 100)


class Computer (Electronic):
    def __init__(self):
        super(Computer, self).__init__("Computer", 30)


class Household (Item):
    def __init__(self, name, usage):
        super(Household, self).__init__(name)
        self.usage = usage


class Watch (Household):
    def __init__(self):
        super(Watch, self).__init__("Watch", 3)


class AlarmClock (Household):
    def __init__(self):
        super(AlarmClock, self).__init__("Alarm Clock", 5)


class Key (Household):
    def __init__(self):
        super(Key, self).__init__("Key", 5)


class Envelope (Household):
    def __init__(self):
        super(Envelope, self).__init__("Envelope", 1)


class Consumable (Item):
    def __init__(self, name, health):
        super(Consumable, self).__init__(name)
        self.health = health


class Pizza (Consumable):
    def __init__(self):
        super(Pizza, self).__init__("Pizza", 25)


class Character(object):
    def __init__(self, name, health: int, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor.protechion > damage:
            print("You survived the attack!")
        else:
            self.health -= damage - self.armor.protection
            if self.health <= 0:
                print("%s has died" % self.name)
                self.health = 0
        print("%d has %d heal left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s  for %d damage" % (self.name, target.name, self.weapon. damage))

    def death(self):
        if self.health >= 0:
            print("You have died!")

