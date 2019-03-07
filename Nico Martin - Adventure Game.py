world_map = {
    'NACHT_DER_UNTOTEN_ROOM_1': {
        'NAME': "Nacht Der Untoten",
        'DESCRIPTION': "------------------------\n"
                       " 🕷[Nacht Der Untoten}🕷 \n"
                       "   ------------------   \n"
                       "                        \n"
                       "         ✉              \n"
                       "                         \n"
                       "                🚶‍        \n"
                       "------------------------\n",
        'PATHS': {
            'NORTH': "VERUCKT_ROOM_2",
            'EAST': "SHI_NO_NUMA_ROOM_3",
        }
    },
    'VERUCKT_ROOM_2': {
        'NAME': "Veruckt",
        'DESCRIPTION': "You are in a building with screams coming out of every corner of the room"
                       "There are three weird looking portals"
                       "One is heading North, and the other is heading South"
                       "There is one that you have a weird felling about.",
        'PATHS': {
            'NORTH': "ASCENSION_ROOM_5",
            'EAST': "MIDDLE_OF_A_RIFT_EX_ROOM_1",
            'SOUTH': 'NACHT_DER_UNTOTEN_ROOM_1',
        }
    },
    'SHI_NO_NUMA_ROOM_3': {
        'NAME': "Shi No Numa",
        'DESCRIPTION': "You are in a swamp with screams coming out of every corner of the room"
                       "There are two weird looking portals"
                       "One is heading West, and the other is heading East.",
            'PATHS': {
                'EAST': "KINO_DER_TOTEN_ROOM_4",
                'WEST': "NACHT_DER_UNTOTEN_ROOM_1",
            }
    },
    'MIDDLE_OF_A_RIFT_EX_ROOM_1': {
        'NAME': "Middle Of A Rift",
        'DESCRIPTION': "You are felling very sick"
                       "There are weird lights from every corner of the room"
                       "You see tree ways to escape"
                       "One way is heading West, another way is East, and the other way is South."
                       "You hear moneys and drums coming from the East",
        'PATHS': {
            'EAST': "SHANGRILA_ROOM_6",
            'SOUTH': "SHI_NO_NUMA_ROOM_3",
            'WEST': "VERUCKT_ROOM_2",
        }
    },
    'KINO_DER_TOTEN_ROOM_4': {
        'NAME': "Kino Der Toten",
        'DESCRIPTION': "You are in a theater... you hear music and screams everywhere"
                       "There is only one weird portal"
                       "It is heading West",
        'PATHS': {
            'WEST': "SHI_NO_NUMA_ROOM_3",
        }
    },
    'ASCENSION_ROOM_5': {
        'NAME': "Ascension",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'North': "TRANZIT_ROOM_9",
            'SOUTH': "VERUCKT_ROOM_2",
        }
    },
    'SHANGRILA_ROOM_6': {
        'NAME': "Shangrila",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "MOON_ROOM_7",
            'EAST': "MIDDLE_OF_A_RIFT_EX_ROOM_1",
        }
    },
    'MOON_ROOM_7': {
        'NAME': "Moon",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "NUKETOWN_ROOM_8",
            'SOUTH': "SHANGRILA_ROOM_6",
        }
    },
    'NUKETOWN_ROOM_8': {
        'NAME': "Nuketown",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "ORIGINS_ROOM_10",
            'WEST': "TRANZIT_ROOM_9",
        }
    },
    'TRANZIT_ROOM_9': {
        'NAME': "Tranzit",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "ORIGINS_ROOM_10",
            'EAST': "NUKETOWN_ROOM_8",
        }
    },
    'ORIGINS_ROOM_10': {
        'NAME': "Origins",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "MIDDLE_OF_A_RIFT_2_EX_ROOM_2",
        }
    },
    'MIDDLE_OF_A_RIFT_2_EX_ROOM_2': {
        'NAME': "Middle Of A Rift 2",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'EAST': "DEAD_OF_THE_NIGHT_ROOM_11",
            'WEST': "BLOOD_OF_THE_DEAD_ROOM_12",
        }
    },
    'DEAD_OF_THE_NIGHT_ROOM_11': {
        'NAME': "Dead Of The Night",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "VOYAGE_OF_DESPAIR_ROOM_13",
        }
    },
    'BLOOD_OF_THE_DEAD_ROOM_12': {
        'NAME': "Blood OF The Dead",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "VOYAGE_OF_DESPAIR_ROOM_13",
        }
    },
    'VOYAGE_OF_DESPAIR_ROOM_13': {
        'NAME': "Voyage Of Despair",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'NORTH': "IX_ROOM_14",
        }
    },
    'IX_ROOM_14': {
        'NAME': "IX",
        'DESCRIPTION': ""
                       "",
        'PATHS': {
            'EAST': "CLASSIFIED_ROOM_15",
        }
    },
    'CLASSIFIED_ROOM_15': {
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
current_node = world_map['NACHT_DER_UNTOTEN_ROOM_1']
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST', 'UP', 'DOWN']

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

