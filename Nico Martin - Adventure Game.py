world_map = {
    'ROOM 1': {
        'NAME': "Nacht Der Untoten",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "Veruckt",
            'EAST': "Shi No Numa",
        }
    },
    'ROOM 2': {
        'NAME': "Veruckt",
        'DESCRIPTION': "There are a couple cars parked here",
        'PATHS': {
            'NORTH': "Ascension",
            'EAST': "Middle Of A Rift",
            'SOUTH': 'Nacht Der Untoten',
        }
    },
    'ROOM 3': {
        'NAME': "Shi No Numa",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'WEST': "Nacht Der Untoten",
            'EAST': "Kino Der Toten",
        }
    },
    'EX ROOM 1': {
        'NAME': "Middle Of A Rift",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'WEST': "Verruckt",
            'EAST': "Shangrila",
            'SOUTH': "Shi No Numa",
        }
    },
    'ROOM 4': {
        'NAME': "Kino Der Toten",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'WEST': "Shi No Numa",
        }
    },
    'ROOM 5': {
        'NAME': "Ascension",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'North': "Transit",
            'SOUTH': "Verruckt",
        }
    },
    'ROOM 6': {
        'NAME': "Shangrila",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "Moon",
            'EAST': "Middle Of A Rift",
        }
    },
    'ROOM 7': {
        'NAME': "Moon",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "Nuketown",
            'SOUTH': "Shangrila",
        }
    },
    'ROOM 8': {
        'NAME': "Nuketown",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "Origins",
            'WEST': "Tranzit",
        }
    },
    'ROOM 9': {
        'NAME': "Tranzit",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "Origins",
            'EAST': "Nuketown",
        }
    },
    'ROOM 10': {
        'NAME': "Origins",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }
    },

}

# Controller
playing = True
current_node = world_map['ROOM 1']
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

