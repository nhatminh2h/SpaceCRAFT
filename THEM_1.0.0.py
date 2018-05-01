inventory = ["torch","something funny"]
power = False
fuel = False
#introduction
print("\nWelcome to Them!")
print("This is a text-based adventure game conducted through texting.")
print("To play the game, text your response to the prompts you are given by this phone number.")
print("Texting 'inventory' tells you what you're carrying.")
print("Text 'help' at any time for game instructions.")
print("text 'quit' to quit the game")
#start of game
def start():
    print("\nWalking out of the airlock")
    print('where do you go?')
    print('1 - Corridor 1')
    print('2 - Back to Expedition Ship')

    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        cor1()
    elif cmd == '2':
        expe()
#corridor1
def cor1():
    print("\nYou are in Corridor 1")
    print("There are 8 rooms")
    print("1 - Airlock leading to the Expedition Ship")
    print("2 - Spacesuit closet")
    print("3 - Tools storage")
    print("4 - A locked room that only the captain has access to")
    print("5 - Central Air Ventilation System")
    print("6 - Bio-Chemistry Laboratory")
    print("7 - Medical Bay")
    print("8 - The Central Hub")

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
            cor1()
    elif cmd == '5':
        cen_AC()
    elif cmd == '6':
        lab_biochem()
    elif cmd == '7':
        med_bay()
    elif cmd == '8':
        hub()
def expe():
    print("\nYou strap in, ready to get the f**k out of here")
    if power == True and fuel == True:
        print("You leave")
        victory()
    else:
        print("The shuttle detaches")
        print("")
        dead()

def cen_AC():
    print("\n Central Air Ventilation Control Room")
    print("\nThere is a vent big enough to crawl through here.")
    print("You can make your way up to the upper deck, where the control room is,")
    print("or down to the storage area.")
    print("1 - Upper Deck")
    print("2 - Storage Area")
    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)
    if cmd == '1':
        print("\nThe vent is pitch black")
        print("Clanking can be heard up ahead")
        print("Investigate ?")
        print("1 - Yes")
        print("2- No")
        cmdlist = ['1','2']
        cmd = getcmd(cmdlist)
        if cmd == '1':
            print("\nThis should lead to the control room")
            print("You keep crawling")
            print("*clanking stops*")
            print("*silence*")
            dead()
        elif cmd == '2':
            print("\nYou are back in the")
    elif cmd == '2':
        print("\nYou arrive at the storage unit")
        storage()
def closet():
    print("\nThere are tools for carrying out minor repairs in this supply closet.")
    print("1 - Corridor 1")
    cmdlist = ['1']
    cmd = getcmd(cmdlist)
    if cmd == '1':
        cor1()
def supply():
    print("\nThere are spacesuits in this supply closet for expeditions like the one you were on. You don't need to wear them on the ship.")
    print("1 - Corridor 1")
    cmdlist = ['1']
    cmd = getcmd(cmdlist)
    if cmd == '1':
        cor1()
def SECRET():
    print("\nThere's a massive f**king hole in the hull of the ship")
    print("---!!!---")
    print("The pressure differential sucks you out into space")
    print("You ded")
    print("RIP Squidward")
    nothing = input()
    exit()
def med_bay():
    print("\nThe medical bay has been trashed but most of the items you’d expect to find are still there.")
    print("Several first aid kits lie on the desk and a scalpel lies on the floor.")
    print("Not very hygienic but it could come in handy for something else later on….")
    print("1 - Pick up scalpel")
    print("2 - Corridor 1")
    cmdlist = ['1','2']
    cmd = getcmd(cmdlist)
    if cmd == '1':
        inventory.append('scalpel')
        items = ['scalpel']
        print('Scalpel added to inventory')
        print('You are still in the medical bay')
        med_bay()
    elif cmd == '2':
        cor1()
#corridor2
def recreational_gym():
    print("\nThe gym")
    #needs fixing
    hub()
#MAIN HUB
def hub(items=['metalpipe']):
    print("\nThe hub is the central part of the main floor of the ship.")
    print("Pieces of metal piping litter one side of the room.")
    print("Damage seems to have been done to the wall and ceiling.")
    print("The furniture is ripped and the wall monitor is smashed on the floor.")
    print("1 - Pick up one of the pipes")
    print("2 - Corridor 1(Expedition Ship)")
    print("3 - Corridor 2")
    print("4 - Corridor 3")
    print("5 - Corridor 4")
    print("6 - Corridor 5")

    cmdlist = ['1', '2', '3', '4','5','6']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        inventory.append('metalpipe')
        items = ['metalpipe']
        print('Metal pipe added to inventory, might come in handy')
        print('You are still in the hub')
        hub()
    if cmd == '2':
        cor1()
    elif cmd == '3':
        cor2()
    elif cmd == '4':
        cor3()
    elif cmd == '5':
        cor4()
    elif cmd == '6':
        cor5()
def cry():
    print("\nOne of the cryogenic chambers where the crew is kept in stasis while the ship travels for centuries further into space.")
    hub()

def lab_biochem():
    print("\nDo you smell it ?")
    print("The smell? A kind of smelly smell, a smelly smell that smells ... smelly")
    print("or maybe that’s just the smell of the fertiliser.")
    print("Microscopes and test tubes lie scattered across the tables.")
    print("On the desk , a container of a mold spample collected on the ship.")
    print("It excreets acid capable of degrading metal.")
    print("1 - Collect acid")
    print("2 - Collect fertiliser")
    print("3 - Smell fertiliser")
    print("4 - Corridor 1")
    cmdlist = ['1', '2', '3','4']
    cmd = getcmd(cmdlist)
    if cmd == '1':
        inventory.append('acid')
        items = ['acid']
        print('Acid added to inventory, might come in handy')
        print('You are still in the biochem lab')
        lab_biochem()
    elif cmd == '2':
        inventory.append('fertiliser')
        items = ['fertiliser']
        print('Fertiliser added to inventory, might come in handy')
        print('You are still in the biochem lab')
        lab_biochem()
    elif cmd == '3':
        print("\nIt smells smelly")
        lab_biochem()
    elif cmd == '4':
        cor1()


def bedcap():
    print("\nThis bedroom belongs to Talha Jamal.")
    print("There is a suspicious amount of tissue beside the bed...")
    print("What’s left of Emil is on the floor grasping an orange he was no doubt hiding in TJ’s room as a part of his latest prank.")
    print("1 - Captain's Bathroom")
    print("2 - Corridor 4")
#hel
def storage():
    print("\nYou enter the storage room of the ship.")
    print("Three rovers and shelves with repair supplies line one side of the large room.")
    print("You can hardly recognise Marco’s corpse but the rotting banana in his hand gives him away.")
    print("He lies next to the life support systems, material supplies and oil reserves.")
    print("A lift is on one side of the room while ladder going up are on the other.")
    print("The door leading to the electrical hub can also be seen.")
    print("1 - Lift")
    print("2 - Ladder up")
    print("3 - Electrical hub")
    print("4 - Fill up oil can")
    cmdlist = ['1', '2', '3', '4']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        if power == True:
            lift()
        else:
            print("The power is off. The emergency power is not enough to operate the lift")
            cor6()
    elif cmd == '2':
        cor4()
    elif cmd == '3':
        elec_hub()
    elif cmd == '4':
        inventory.append('oil')
        items = ['oil']
        print('Oil can added to inventory')
        print('You are still in the storage')
        storage()

def elec_hub():
    print("\nYou enter the electrical hub of the ship.")
    print("You can see the main power supply and the backup generator.")
    print("A lift is on one side of the room while ladder going up are on the other.")
    print("A door leading to the storage room can also be seen.")
    print("1 - Flip master power switch")
    print("2 - Lift")
    print("3 - Ladder up")
    print("4 - Storage room")
    cmdlist = ['1', '2', '3', '4']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        global power
        power == True
        print("The main generator is now ON")
        print("Emergency battery is now OFF")
        elec_hub()
    elif cmd == '2':
        if power == True:
            lift()
        else:
            print("The power is off. The emergency power is not enough to operate the lift")
            cor6()
    elif cmd == '3':
        cor4()
    elif cmd == '4':
        storage()
def kitchen():
    print("\nYou step over Minh's body as you enter the kitchen.")
    print("A clean container and some plates are next to the sink.")
    print("There is some chicken biryani on the counter.")
    print("It seems it was prepared not too long ago. But no one is to be seen.")
    print("1 - Dining room")
    print("2 - Corridor 5")
    print("3 - Pick up container")
    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        dine()
    elif cmd == '2':
        cor5()
    elif cmd == '3':
        inventory.append('box')
        items = ['box']
        print('Container added to inventory')
        print('You are still in the kitchen')
        kitchen()

def dine():
    print("\nYou enter the dining room and see it is connected to the kitchen.")
    print("Broken plates and a pool of tea lie on the floor next to a piece of chocolate cake and Mitra’s blood-soaked body.")
    print("1 - Kitchen")
    print("2 - Corridor 5")
    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        kitchen()
    elif cmd == '2':
        cor5()

def study_room():
    print("\nThere are plenty of books in here")
    cor2()
def bed1():
    print("\nThis bedroom belongs to Minh and Marco. There is only a double bed")
    print("1 - Bathroom 1")
    print("2 - Corridor 4")

    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        bath1()
    elif cmd == '2':
        cor4()

def ctrl_room():
    print("\nYou are now in the control room of the ship.")
    print("The communications panels lie to your left but seem damaged beyond repair.")
    print("The fuel injection and charging controls lie to your right.")
    print("Up ahead of you are the steering controls for the ship,")
    print("and lying on the floor next to a large open vent is your captain, Talha Jamal.")
    print("He looks seriously wounded.")
    print("1 - Examine captain's body")
    print("2 - Approach fuelling and charging controls")
    print("3 - Enter vent")
    print("4 - Balcony")
    cmdlist = ['1', '2', '3', '4']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        print("Captain TJ is dead. You see his keycard and decide to take it.")
        inventory.append('cap_card')
        items = ['cap_card']
        print("Captain's keycard added to inventory")
        ctrl_room()
    elif cmd == '2':
        print("The fuelling controls appear to be working! You refueled the expedition ship.")
        global fuel
        fuel = True
        ctrl_room()
    elif cmd == '3':
        print("You enter the vent and begin to crawl through it when you hear a growl which reverberates throughout the vent.")
        dead()
    elif cmd == '4':
        cor6()

def bath1():
    print("\nYou enter the bathroom. There are some bunny magazines besides the toilet.")
    print("1 - Bedroom 1")

def bathcap():
    print("\nThis is the Captain's bathroom. The toilet is completely blocked.")
    print("1 - Captain's bedroom")
    capbed()

#asgard
def cor6():
    print("\nYou are in the upper deck on a balcony overlooking the hub.")
    print("There are five rooms")
    print("1 - Control Room")
    print("2 - Ladder going down")
    print("3 - Lift")
    print("4 - Escape pod 1")
    print("5 - Escape pod 2")

    cmdlist = ['1', '2', '3', '4','5']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        if power == True:
            ctrl_room()
        else:
            print("Must construct additional Pylons !")
            print('The power is not on, Control Room door is LOCKED')
            cor6()
    elif cmd == '2':
        cor4()
    elif cmd == '3':
        if power == True:
            lift()
        else:
            print("The power is off. The emergency power is not enough to operate the lift")
            cor6()
    elif cmd == '4':
        esc1()
    elif cmd == '5':
        esc2()

def esc1():
    print("\nThe first escape pod seems to be missing. I wonder where it is ?")
    cor6()
def esc2():
    print("The second escape pod is available. There's a trail of blood leading to the hatch door.")
    print("1 - Open the pod")
    print("2 - Return to the upper deck")
    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        esc2_in()
    elif cmd == '2':
        cor6()
def cor2():
    print("\nYou are in corridor 2")
    print("There are 5 rooms")
    print("1 - Study Room")
    print("2 - Cryogenic Chamber 2")
    print("3 - Cryogenic Chamber 3")
    print("4 - Lift")
    print("5 - Materials Lab")
    print("6 - Hub")

    cmdlist = ['1', '2', '3', '4','5','6']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        study_room()
    elif cmd == '2':
        cry()
    elif cmd == '3':
        cry()
    elif cmd == '4':
        if power == True:
            lift()
        else:
            print("The power is off. The emergency power is not enough to operate the lift")
            cor6()
    elif cmd == '5':
        lab_mat()
    elif cmd == '6':
        hub()
#corridor3
def cor3():
    print("\nYou are in corridor 3")
    print("There are 4 rooms")
    print("1 - Bedroom 2")
    print("2 - Bedroom 3")
    print("3 - Bedroom 4")
    print("4 - Hub")

    cmdlist = ['1', '2', '3', '4']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        bed2()
    elif cmd == '2':
        bed3()
    elif cmd == '3':
        bed4()
    elif cmd == '4':
        hub()
def bed2():
    print("\nThere are two beds. One belonging to Emil and the other belonging to Louis.")
    print("On Louis' bed there is a note asking for help...")
    print("1 - Bathroom 2")
    print("2 - Corridor 3")
    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        bath2()
    elif cmd == '2':
        cor4()
def bath2():
    print("\nYou enter the bathroom. The stench is unbearable. You should probably leave.")
    print("1 - Bedroom 2")
    bed2()
def bed3():
    print("\nThere are two beds. One belonging to Mitra and the other belonging to Kirthana.")
    print("There's a book titled 'Eragon' on one of the beds.")
    print("1 - Bathroom 3")
    print("2 - Corridor 3")
    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        bath3()
    elif cmd == '2':
        cor4()
def bath3():
    print("\nYou enter the bathroom. This one is actually pretty clean.")
    if 'spoiler1' not in inventory:
        print("There's a scrunched up note in the toilet bowl")
        print("Someone was trying to flush it away")
    print("1 - Bedroom 3")
    if 'spoiler1' not in inventory:
        print("2 - Pick up the note")
    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        bed3()
    elif cmd == '2':
        inventory.append('spoiler1')
        items = ['spoiler1']
        print("\nThe note reads")
        print("Vision dies in Avengers Infinity War")
        print("Note#1 added to inventory")
        bath3()

def bed4():
    print("\nThis bedroom belongs to you and your companion.")
    print("You can hardly see the floor; it’s just as you left it.")
    print("The new lithium-ion battery you asked for to fix your lamp is still on your bedside table.")
    print("1 - Bathroom 4")
    print("2 - Corridor 3")
    print("3 - Pick up battery")
    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        print("\nTheres nothing in the bathroom")
        bed4()
    if cmd == '2':
        cor3()
    elif cmd == '3':
        #add battery to inventory
        bed4()

def bath4():
    print("\nYou enter the bathroom. The bin is full, it was your companion’s turn to empty it.")
    print("1 - Bedroom 4")
    bed4()
#corridor4
def cor4():
    print("\nYou are in corridor 4")
    print("There are 5 rooms")
    print("1 - Ladder going up")
    print("2 - Ladder going down")
    print("3 - Bedroom 1")
    print("4 - Captain's Room")
    print("5 - Hub")

    cmdlist = ['1', '2', '3', '4', '5']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        cor6()
    elif cmd == '2':
        ladder_bot()
    elif cmd == '3':
        bed1()
    elif cmd == '4':
        if 'cap_card' in inventory:
            cap_room()
        else:
            print("Captain's Room, ACCESS DENIED")
            start()
    elif cmd == '5':
        hub()
#corridor5
def cor5():
    print("\nYou are in corridor 5")
    print("There are 5 rooms")
    print("1 - Dining Room")
    print("2 - Kitchen")
    print("3 - Cryogenic Chamber 2")
    print("4 - Experimental Lab")
    print("5 - Hub")

    cmdlist = ['1', '2', '3', '4', '5']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        dining_room()
    elif cmd == '2':
        kitchen()
    elif cmd == '3':
        cry()
    elif cmd == '4':
        exlab()
    elif cmd == '5':
        hub()
#Lift
def lift():
    print("\nYou arrive at the lift")
    print("Which floor?")
    print("1 - Upper Floor")
    print("2 - Main Area")
    print("3 - Lower Floor")
    cmdlist = ['1', '2','3']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        cor6()
    elif cmd == '2':
        cor2()
    elif cmd == '3':
        ladder_bot()
def ladder_bot():
    print("\nTo the left is the storage room and to the right is the electrical hub")
    print("1 - Electrical hub")
    print("2 - Storage room")
    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)
    if cmd == '1':
        elec_hub()
    elif cmd == '2':
        storage()
#interaction
def getcmd(cmdlist):
    cmd = input()
    if cmd in cmdlist:
        return cmd
    elif cmd == 'help':
        print('\nTYPE: inventory to view items')
        print('or quit to suicide')
        return getcmd(cmdlist)
    elif cmd == 'inventory':
        print('\n inventory contains:\n')
        for item in inventory:
            print('-- %s' % (item))
        return getcmd(cmdlist)
    elif cmd == 'quit':
        print("Goodbye cruel world")
        exit(0)
    else:
        print('\n error. invalid command-\n')
        return getcmd(cmdlist)
#endgame
def dead():
    print("\n*darkness*\n")
    print("\nYou died.\n")

def victory():
    print("\nYou've done it! You survived and managed to make your way off the ship! It's smooth sailing from here on out... hopefully.")
    nothing = input()
    exit()
start()
