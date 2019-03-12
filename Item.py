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
        self.attack = attack


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