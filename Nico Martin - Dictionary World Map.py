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
            'NORTH': 'Ascension',
            'SOUTH': 'Nacht Der Untoten',
        }
    },
}

# Controller
playing = True
current_node = world_map['R19A']
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
        exept KeyError:
        print("I can't go that way")
    else:
        print("Command Not Found")

