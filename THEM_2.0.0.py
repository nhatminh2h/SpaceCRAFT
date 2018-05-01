import sys

PROMPT = "> "
inventory = [""]
# rooms are just dictionaries, with a description and a list of named actions, which point at other rooms
# the 'exit' value indicates a room which ends the game
# the 'name' is used to give each room a unique  in the map
entrance_room = {
'name':'entrance',
'desc': 'You are in a dimly lit cave. To your left there is a winding staircase heading up into the darkness, to your right, a rusty iron gate',
'actions': {'go up': 'tower', 'break the gate': 'main_stairs'},
'exit':False
}

tower_dead_end = {
'name':'tower'  ,
'desc' : 'You emerge from the stairway in the ruins of an old tower. There is nothing here but broken stones and matted vines',
'actions': {'go down': 'entrance'},
'exit':False
}

main_stairs = {
'name':'main_stairs',
'desc':'The gate gives way after a few hard kicks, and clangs loundly down a flight of steps into the darkness. You hear the sound of water from down below.',
'actions': { 'go down':'pitfall', 'light torch':'stairs_torch'},
'exit':False
}

stairs_torch= {
'name':'stairs_torch',
'desc':'your torch sputters to life and reveals a large gap in the stairs about ten feet ahead of you. It might be possible to edge by it to the left side...',
'actions': { 'jump the gap':'pitfall', 'go_up':'entrance', 'edge around':'sneak_by', 'Pick up metal pipe':'inventory.append(metalpipe)'},
'exit':False
}

sneak_by = {
'name':'sneak_by',
'desc':'You carefully step past the gap. A few feet later you are handed a check for $85,000,000 and the keys to a Tesla. Congratulations!',
'actions':{},
'exit':True}

pitfall = {
'name':'pitfall',
'desc':'You fall into a large gap in the stairs that you would have seen if you had only lit a torch. You plummet to a mercifully quick death in the icy water far below.',
'actions':{},
'exit':True
}

# this is shorthand way of making all of the above dictionaries into a dictionary keyed by the 'name' entries
# in a real game you'd want to make sure these all actually existed and that there were no typos!
map = dict ( (item['name'],item) for item in (entrance_room, tower_dead_end, main_stairs, stairs_torch, sneak_by, pitfall))


def game_loop(room, map):
    # room is a dictionary describing an individual room or action
    # map is a dictionary of rooms, keyed by name

    sys.stdout.writelines(room['desc'])

    if room['exit']:
        sys.stdout.writelines('\nThanks for playing!')
        return

    next = None

    while not next:
        sys.stdout.writelines ("\nYou can...")
        for item in room['actions'].keys():
            sys.stdout.writelines("\n\t" + item)

        sys.stdout.writelines("\n>")
        user_input = sys.stdin.readline()
        user_input = user_input.strip().lower() # just take  lower case for simplicity
        if user_input in room['actions']:
            next = room['actions'][user_input]
        else:
            sys.stdout.writelines("'%s' is not a supported option. Please try again\h" % user_input)
    game_loop(map[next], map)

game_loop (entrance_room, map)

start = {
'name':'Air Lock',
'desc': 'Walking out of the airlock',
'actions': {'Corridor 1': 'cor1', 'Back to Expedition Ship': 'expe'},
'exit':False
}

hub = {
'name':'Hub',
'desc': 'Central Hub',
'actions': {'Corridor 1': 'cor1', 'Corridor 2': 'cor2', 'Pick up metal pipe':'inventory.append(metalpipe)'},#try if this works
'item': {'Metal Pipe'},
'exit':False
}

cor1 = {
'name':'Corridor 1',
'desc': 'There are 8 rooms',
'actions': {'Corridor 1': 'cor1', 'Corridor 2': 'cor2', 'Pick up metal pipe':'inventory.append(metalpipe)'},#try if this works
'item': {'Metal Pipe'},
'exit':False
}

expe = {
'name':'Hub',
'desc': 'Central Hub',
'actions': {'Corridor 1': 'cor1', 'Corridor 2': 'cor2', 'Pick up metal pipe':'inventory.append(metalpipe)'},#try if this works
'item': {'Metal Pipe'},
'exit':False
}
additem = {
'name':'additem',
'desc': 'abc have been added to inventory',
'actions': {'Corridor 1': 'cor1', 'Corridor 2': 'cor2', 'Pick up metal pipe':'inventory.append(metalpipe)'},#try if this works
'item': {'Metal Pipe'},
'exit':False
}
