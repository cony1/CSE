class Room(object):
    def __init__(self, name, north=None, east=None, south=None, west=None, description=""):
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


# Option 2 - Set all at once, modify controller
R19A = Room("Mr. Viebe's Room", 'parking_lot')
parking_lot = Room("Parking Lot", None, R19A)

player = Player(R19A)

playing = True
directions = ['north', 'east', 'south', 'west']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")


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
