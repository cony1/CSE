class Item(object):
    def __init__(self, name):
        self.name = name

class Armor(Item):
    def __init__(self, name, protection, durability):
        super(Armor, self).__init__(name)
        self.protection = protection


class ChestPlate1(Armor):
    def __init__(self):
        super(ChestPlate1, self).__init__("Wood Chest Plate, Protection-10", 10)



class ChestPlate2 (Armor):
    def __init__(self):
        super(ChestPlate2, self).__init__("Iron Chest Plate, Protection-40", 40)



class ChestPlate3 (Armor):
    def __init__(self):
        super(ChestPlate3, self).__init__("Gold Chest Plate, Protection-60", 60)



class Leggings1 (Armor):
    def __init__(self):
        super(Leggings1,self).__init__("Wood Leggings, Protection-10", 10)



class Leggings2 (Armor):
    def __init__(self):
        super(Leggings2, self).__init__("Iron Leggings, Protection-40," 40)



class Leggings3 (Armor):
    def __init__(self):
        super(Leggings3, self).__init__("Gold Leggings, Protection-60", 60)



class Boots1 (Armor):
    def __init__(self):
        super(Leggings1, self).__init__("Wood Boots, Protection-10", 10)


        