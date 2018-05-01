
# instead of using an if/then tree, first we store the damage range
# of all the weapons in the game
WEAPONS = {'pipe': (3,3), None:(1,1), 'scapel':(2,6), 'gun':(5,10)}

#and instead of tracking inventory with one variable, have a 'player' who
# has stuff in a dictionary:

player = {'weapon':None, 'health':10}

#to give the player stuff, you add it to his dictionary:

player['weapon'] = 'stick'

# while we're at it, we can treat the monsters the same way:

IT = {name:'thing', 'health':5, 'attack':(3,5)}

# so for any given fight there's a player and an enemy:
# and two possible outcomes for each combatant. You'll want to report
# the damage (which varies) and the result:

def combat (player, enemy):
    player_damage = random.range(*WEAPONS[player['weapon'])
    enemy_damage = random.range(*enemy['attack'])

    player_win = player_damage > enemy['health']
    enemy_win= enemy_damage  > player['health']

    return player_damage, player_win , enemy_damage, enemy_win

# of course, you also want flavor text. So you can set that up as another dictionary.
# you might want to make different dictionaries for different parts of the game
# to give a different flavor to the fights as you did above:

IT_FIGHT = {
player_damage: 'You hit the %s for %i damage',
enemy_damage: '%s hits you for %i damage',
player_win: 'The %s dies!',
enemy_win: 'You die!'
}

def describe_combat(player, enemy, fight_description):
   player_damage, player_win , enemy_damage, enemy_win = combat(player, enemy)

   print fight_description['player_damage'] % (enemy['name'], player_damage)
   print fight_description['enemy_damage'] % (enemy['name'], enemy_damage)

   if player_win:
      print fight_description['player_win'] % enemy['name'])
      return True

   if enemy_win:
      print fight_description['player_win'] % enemy['name'])
      return False

    return None # this means a draw :)


 # with that in place, you can play out a fight like so:


 fight_result = describe_combat(player, IT, IT_FIGHT)
 if fight_result is None:
     # what do you do for draws?
 elif fight_result:
     # you've won.
 else:
     # game over
def cor1():
    print("You are in Corridor 1")
    print("There are 8 rooms")
    print("1 - Decontamination chamber leading to the expedition ship")
    print("2 - Spacesuit closet")
    print("3 - Tools storage")
    print("4 - A locked room that only the captain has access to")
    print("5 - Central Air Ventilation System")
    print("6 - Bio-Chemistry Laboratory")
    print("7 - Medical Bay")
    print("8 - The central Hub")

    cmdlist = ['1', '2', '3', '4','5','6','7','8']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        expe()
    elif cmd == '2':
        closet()
    elif cmd == '3':
        supply()
    elif cmd == '4':
        if 'cap_card' in inventory:
            SECRET()
        else:
            print('Captain''s Storage - LOCKED, ACCESS DENIED')
            time.sleep(2)
            cor1()
    elif cmd == '5':
        cen_AC()
    elif cmd == '6':
        lab_chem()
    elif cmd == '7':
        med_bay()
    elif cmd == '8':
        Hub()

def cor6():
    print("You are in the upper deck")
    print("There are 5 rooms")
    print("1 - Control Room")
    print("2 - Stairs going down")
    print("3 - Lift")
    print("4 - Escape pod 1")
    print("5 - Escape pod 2")

    cmdlist = ['1', '2', '3', '4','5']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        if power == True:
        ctrl_room()
        else:[]
            print('The power is not on, Control Room door is locked')
            time.sleep(2)
            cor6()
    elif cmd == '2':
        cor4()
    elif cmd == '3':
        lift()
    elif cmd == '4':
        esc1()
    elif cmd == '5'
        esc2()

def cor2():
    print("You are in corridor 2")
    print("There are 5 rooms")
    print("1 - Study Room")
    print("2 - Cryogenic Chamber 2")
    print("3 - Cryogenic Chamber 3")
    print("4 - Lift")
    print("5 - Materials Lab")

    cmdlist = ['1', '2', '3', '4','5']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        study_room()
    elif cmd == '2':
        cry2()
    elif cmd == '3':
        cry2()
    elif cmd == '4':
        lift()
    elif cmd == '5'
        lab_mat()

def cor3():
    print("You are in corridor 3")
    print("There are 2 rooms")
    print("1 - Bedroom 2")
    print("2 - Bedroom 3")

    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        bed_2()
    elif cmd == '2':
        bed_3()

def cor4():
    print("You are in corridor 4")
    print("There are 4 rooms")
    print("1 - Stairs going up")
    print("2 - Stairs going down")
    print("3 - Bedroom 1")
    print("4 - Captain's Room")

    cmdlist = ['1', '2', '3', '4']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        cor6()
    elif cmd == '2':
        stair_bot()
    elif cmd == '3':
        bed1()
    elif cmd == '4':
        if 'cap_card' in inventory:
            cap_room()
        else:
            print("Captain's Room, ACCESS DENIED")
            time.sleep(2)
            start()

def cor5():
    print("You are in corridor 5")
    print("There are 4 rooms")
    print("1 - Dining Room")
    print("2 - Kitchen")
    print("3 - Cryogenic Chamber 2")
    print("4 - Experimental Lab")

    cmdlist = ['1', '2', '3', '4']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        dining_room()
    elif cmd == '2':
        kitchen()
    elif cmd == '3':
        cry2()
    elif cmd == '4':
        exlab()
    '''commands'''

def getcmd(cmdlist):
    cmd = input()
    if cmd in cmdlist:
        return cmd
    elif cmd == 'help':
        print('\nTYPE: inventory to view items')
        print('or quit to self-destruct')
        return getcmd(cmdlist)
    elif cmd == 'inventory':
        print('\n inventory contains:\n')
        for item in inventory:
            print('-- %s' % (item))
        return getcmd(cmdlist)
    elif cmd == 'quit':
        exit(0)
    else:
        print('\n error. invalid command-\n')
        return getcmd(cmdlist)
