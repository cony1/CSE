class Item(object):
    def __init__(self, name):
        self.name = name


class Armor(Item):
    def __init__(self, name, protection,):
        super(Armor, self).__init__(name)
        self.protection = protection


class ChestPlate1(Armor):
    def __init__(self):
        super(ChestPlate1, self).__init__("Bronze Chest Plate, Protection-10", 10)


class Leggings1 (Armor):
    def __init__(self):
        super(Leggings1, self).__init__("Bronze Leggings, Protection - 10", 10)


class Boots1 (Armor):
    def __init__(self):
        super(Boots1, self).__init__("Bronze Boots, Protection - 10", 10)


class Weapon(Item):
    def __init__(self, name, attack):
        super(Weapon, self).__init__(name)
        self.attack = attackwq


class Gun1 (Weapon):
    def __init__(self):
        super(Gun1, self).__init__("Bronze Handgun, Attack Damage - 10", 10)


class Crossbow1 (Weapon):
    def __init__(self):
        super(Crossbow1, self).__init__("Bronze Crossbow, Attack Damage - 10", 10)


class KitchenKnife1 (Weapon):
    def __init__(self):
        super(KitchenKnife1, self).__init__("Bronze Kitchen Knife, Attack Damage- 10", 10)


class Sword1 (Weapon):
    def __init__(self):
        super(Sword1, self).__init__("Bronze Sword, Attack Damage - 10", 10)


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

class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=""):
        self.name = name
        self.north = north
        self.south = east
        self.east = south
        self.west = west
        self.description = description
        self.characters = []


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room so see if a room exists in the direction

        :param direction: The direction the you want to move
        :return:
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]
