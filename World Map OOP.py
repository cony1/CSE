class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west

class PLayer(object):
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


# Option 1 - Define as we go
R19A = Room("Mr. Wiebe's Room", parking_lot)
parking_lot = Room("Parking LOt", None, R19A)

R19A.north = Room("Parking Lot", None, R19A)

# Option 2 - Set all at once, modify controller
R19A = Room("Mr. Viebe's Room", 'parking_lot')
parking_lot = Room("Parking Lot", None, R19A)

player = PLayer(R19A)

playing = True
directions = ['north', 'south', 'east', 'west']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")





ROOM_1 = Room("Nacht Der Untoten", "Veruckt")
ROOM_2 = Room("Veruckt", "Ascension", "Middle Of A Rift", "Nacht Der Untoten")
ROOM_3 = Room("Shi No Numa", "Nacht Der Untoten",)
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