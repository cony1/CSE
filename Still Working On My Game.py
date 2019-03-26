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
        super(Gun, self).__init__("Bronze Handgun, Attack Damage - 10", 10)


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

class Room(object):
    def __init__(self, name, north, south, east, west=None, description, item):
        self.name = name
        self.north = north
        self.south = east
        self.east = south
        self.west = west
        self.description = description
        self.characters = []
        self.item = item


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


NACHT_DER_UNTOTEN_ROOM_1 = Room("Nacht Der Untoten", 'VERUCKT_ROOM_2', 'SHI_NO_NUMA_ROOM_3', None, None, "You are in a"
                                                                                                         "building, you"
                                                                                                         " see an"
                                                                                                         "envelope")

VERUCKT_ROOM_2 = Room("Veruckt", 'ASCENSION_ROOM_5', 'MIDDLE_OF_A_RIFT_EX_ROOM_1', 'NACHT_DER_UNTOTEN_ROOM_1', None, "")
SHI_NO_NUMA_ROOM_3 = Room("Shi No Numa", None, 'KINO_DER_TOTEN_ROOM_4', None, 'NACHT_DER_UNTOTEN_ROOM_1')
MIDDLE_OF_A_RIFT_EX_ROOM_1 = Room("Middle Of A Rift", None, 'SHANGRILA_ROOM_6', 'SHI_NO_NUMA_ROOM_3', 'VERUCKT_ROOM_2')
KINO_DER_TOTEN_ROOM_4 = Room("Kino Der Toten", None, None, None, 'SHI_NO_NUMA_ROOM_3')
ASCENSION_ROOM_5 = Room("Ascension", 'TRANZIT_ROOM_9', None, 'VERUCKT_ROOM_2', None)
SHANGRILA_ROOM_6 = Room("Shangrila", 'MOON_ROOM_7', 'MIDDLE_OF_A_RIFT_EX_ROOM_1', None, None)
MOON_ROOM_7 = Room("Moon", 'NUKETOWN_ROOM_8', None, 'SHANGRILA_ROOM_6', None)
NUKETOWN_ROOM_8 = Room("Nuketown", 'ORIGINS_ROOM_10', None, None, 'TRANZIT_ROOM_9')
TRANZIT_ROOM_9 = Room("Tranzit", 'ORIGINS_ROOM_10', 'NUKETOWN_ROOM_8', None, None)
ORIGINS_ROOM_10 = Room("Origins", 'MIDDLE_OF_A_RIFT_2_EX_ROOM_2', None, None, None)
MIDDLE_OF_A_RIFT_2_EX_ROOM_2 = Room("Middle Of a Rift 2", None, 'DEAD_OF_THE_NIGHT_ROOM_11', None, 'BLOOD_OF_THE_DEAD_ROOM_12')
DEAD_OF_THE_NIGHT_ROOM_11 = Room("Dead Of The Night", 'VOYAGE_OF_DESPAIR_ROOM_13', None, None, None)
BLOOD_OF_THE_DEAD_ROOM_12 = Room("Blood Of The Dead", 'VOYAGE_OF_DESPAIR_ROOM_13', None, None, None)
VOYAGE_OF_DESPAIR_ROOM_13 = Room("Voyage of Despair", 'IX_ROOM_14', None, None, None)
IX_ROOM_14 = Room("IX", None, 'CLASSIFIED_ROOM_15', None, None)
CLASSIFIED_ROOM_15 = Room("Classified", None, 'HOME_ROOM_16', None, None)
HOME_ROOM_16 = Room("Home", None, None, None, None)


# Armor
chestplate = Armor("Chest Plate", 10)
leggings = Armor("Leggings", 10)
boots = Armor("Boots", 10)


# Weapons
gun = Weapon("Gun", 10)
crossbow = Weapon("Crossbow", 10)
kitchenknife = Weapon("KitchenKnife", 10)
sword = Weapon("Sword", 10)


# Electronic
flashlight = Electronic("Flashlight",)
tv = Electronic("Tv",)
computer = Electronic("Computer",)


# Household
watch = Household("Watch",)
alarmclock = Household("Alarmclock",)
key = Household("Key",)
envelope = Household("Envelope",)


# Consumable
pizza = Consumable("Pizza", 10)

