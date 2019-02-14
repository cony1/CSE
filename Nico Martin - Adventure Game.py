world_map = {
    'ROOM_1': {
        'NAME': "Nacht Der Untoten",
        'DESCRIPTION': "You are in a room that is very small, some windows have barriers."
                       "In the distance you see two weird looking portals one heading North, and the other heading East",
        'PATHS': {
            'NORTH': "ROOM_2",
            'EAST': "ROOM_3",
        }
    },
    'ROOM_2': {
        'NAME': "Veruckt",
        'DESCRIPTION': "You are in a building with screams coming out of every corner of the room"
                       "There are three weird looking portals"
                       "One is heading North, and the other is heading South"
                       "There is one that you have a weird felling about.",
        'PATHS': {
            'NORTH': "Ascension",
            'EAST': "Middle Of A Rift",
            'SOUTH': 'Nacht Der Untoten',
        }
    },
    'ROOM_3': {
        'NAME': "Shi No Numa",
        'DESCRIPTION': "You are in a swamp with screams coming out of every corner of the room"
                       "There are two weird looking portals"
                       "One is heading West, and the other is heading East.",
        'PATHS': {
            'WEST': "Nacht Der Untoten",
            'EAST': "Kino Der Toten",
        }
    },
    'EX_ROOM_1': {
        'NAME': "Middle Of A Rift",
        'DESCRIPTION': "You are felling very sick"
                       "There are weird lights from every corner of the room"
                       "You see tree ways to escape"
                       "One way is heading West, another way is East, and the other way is South."
                       "You hear moneys and drums coming from the East",
        'PATHS': {
            'WEST': "Verruckt",
            'EAST': "Shangrila",
            'SOUTH': "Shi No Numa",
        }
    },
    'ROOM_4': {
        'NAME': "Kino Der Toten",
        'DESCRIPTION': "You are in a theater... you hear music and screams everywhere"
                       "There is only one weird portal"
                       "It is heading West",
        'PATHS': {
            'WEST': "Shi No Numa",
        }
    },
    'ROOM_5': {
        'NAME': "Ascension",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'North': "Transit",
            'SOUTH': "Verruckt",
        }
    },
    'ROOM_6': {
        'NAME': "Shangrila",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "Moon",
            'EAST': "Middle Of A Rift",
        }
    },
    'ROOM_7': {
        'NAME': "Moon",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "Nuketown",
            'SOUTH': "Shangrila",
        }
    },
    'ROOM_8': {
        'NAME': "Nuketown",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "Origins",
            'WEST': "Tranzit",
        }
    },
    'ROOM_9': {
        'NAME': "Tranzit",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "Origins",
            'EAST': "Nuketown",
        }
    },
    'ROOM_10': {
        'NAME': "Origins",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "Middle Of a Rift 2",
        }
    },
    'EX_ROOM_2': {
        'NAME': "Middle Of A Rift 2",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'EAST': "Dead Of The Night",
            'WEST': "Blood OF THe Dead",
        }
    },
    'ROOM_11': {
        'NAME': "Dead Of The Night",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "Voyage Of Despair",
        }
    },
    'ROOM_12': {
        'NAME': "Blood OF The Dead",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "Voyage OF Despair",
        }
    },
    'ROOM_13': {
        'NAME': "Voyage Of Despair",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "IX",
        }
    },
    'ROOM_14': {
        'NAME': "IX",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'EAST': "Classified",
        }
    },
    'ROOM_15': {
        'NAME': "Classified",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'EAST': "Classified",
        }
    },











}

# Controller
playing = True
current_node = world_map['ROOM_1']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
        except AttributeError:
            pass
    else:
        print("Command Not Found")

