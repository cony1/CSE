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


class ChestPlate2 (Armor):
    def __init__(self):
        super(ChestPlate2, self).__init__("Iron Chest Plate, Protection - 40", 40)


class Leggings1 (Armor):
    def __init__(self):
        super(Leggings1, self).__init__("Bronze Leggings, Protection - 10", 10)


class Leggings2 (Armor):
    def __init__(self):
        super(Leggings2, self).__init__("Iron Leggings, Protection - 40", 40)


class Boots1 (Armor):
    def __init__(self):
        super(Boots1, self).__init__("Bronze Boots, Protection - 10", 10)


class Boots2 (Armor):
    def __init__(self):
        super(Boots2, self).__init__("Iron Boots, Protection - 40", 40)


class Weapon(Item):
    def __init__(self, name, attack):
        super(Weapon, self).__init__(name)
        self.attack = attack


class Gun1 (Weapon):
    def __init__(self):
        super(Gun1, self).__init__("Bronze Handgun, Attack Damage - 10", 10)


class Gun2 (Weapon):
    def __init__(self):
        super(Gun2, self).__init__("Iron Handgun, Attack Damage - 40", 40)


class Crossbow1 (Weapon):
    def __init__(self):
        super(Crossbow1, self).__init__("Bronze Crossbow, Attack Damage - 10", 10)


class Crossbow2 (Weapon):
    def __init__(self):
        super(Crossbow2, self).__init__("Iron Crossbow", 40)

class