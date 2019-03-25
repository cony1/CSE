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
        self.attack = attackwq


class Gun (Weapon):
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
    def __init__(self, name, light):
        super(Electronic, self).__init__(name)
        self.light = light


class Flashlight (Electronic):
    def __init__(self):
        super(Flashlight, self).__init__("Flashlight",)


class Tv (Electronic):
    def __init__(self):
        super(Tv, self).__init__("Tv",)


class Computer (Electronic):
    def __init__(self):
        super(Computer, self).__init__("Computer",)


class Household (Item):
    def __init__(self, name):
        super(Household, self).__init__(name)


class Watch (Household):
    def __init__(self):
        super(Watch, self).name__init__("Watch",)


class AlarmClock (Household):
    def __init__(self):
        super(AlarmClock, self).__init__("Alarm Clock",)


class Key (Household):
    def __init__(self):
        super(Key, self).__init__("Key",)


class Envelope (Household):
    def __init__(self):
        super(Envelope, self).__init__("Envelope",)


class Consumable (Item):
    def __init__(self, name):
        super(Consumable, self).__init__(name)


class Pizza (Consumable):
    def __init__(self):
        super(Pizza, self).__init__("Pizza")


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


# Items