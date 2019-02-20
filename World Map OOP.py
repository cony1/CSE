class Room(object):
    def __init__(self, name, north=None, south=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west


# Option 1 - Define as we go
R19A = Room("Mr. Wiebe's Room", parking_lot)
parking_lot = Room("Parking LOt", None, R19A)

R19A.north = Room("Parking Lot", None, R19A)

# Option 2 - Set all at once, modify controller
R19A = Room("Mr. Viebe's Room", 'parking_lot')
parking_lot = Room("Parking Lot", None, R19A)


Room_1 = Room("Nacht Der Untoten", "Veruckt")
Room_2 = Room("Veruckt")