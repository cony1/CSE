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


ROOM_1 = Room("Nacht Der Untoten", "Veruckt")
ROOM_2 = Room("Veruckt")
ROOM_3 = Room("")
EX_ROOM_1 = Room("")
ROOM_4 = Room("")
ROOM_5 = Room("")
ROOM_6 = Room("")
ROOM_7 = Room("")
ROOM_8 = Room("")
ROOM_9 = Room("")
ROOM_10 = Room("")
EX_ROOM_2 = Room("")
ROOM_11 = Room("")
ROOM_12 = Room("")
ROOM_13 = Room("")
ROOM_14 = Room("")
ROOM_15 = Room("")