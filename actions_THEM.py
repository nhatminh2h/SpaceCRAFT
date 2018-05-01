def ded():
    print("You died")
 
def prompt_4():

    cmdlist = ['1', '2', '3', '4']
	cmd = getcmd(cmdlist)

    if cmd == '1':
        closet(inventory)
	elif cmd == '2':
		supply(inventory)
	elif cmd == '3':
		cargo_hold(inventory)
	elif cmd == '4':
		if 'cap_card' in inventory:
            SECRET(inventory)
		else:
			print('Captain Storage LOCKED, ACCESS DENIED')
            time.sleep(2)
            start(inventory)
def prompt_3():
    cmdlist = ['1', '2', '3']
    cmd =
def prompt_2():

def getcmd(cmdlist):
	cmd = input('\nCTRL866:> ')
	if cmd in cmdlist:
		return cmd
	elif cmd == 'help':
		print('\nTYPE: inventory to view items')
		print('or quit to self-destruct')
		return getcmd(cmdlist)
	elif cmd == 'inventory':
		print('\ninventory contains:\n')
		for item in inventory:
			print('-- %s' % (item))
		return getcmd(cmdlist)
	elif cmd == 'secret':
		print('\n........')
		time.sleep(1)
		print('\n[--Paradroid -- published by Hewson 1985--]')
		time.sleep(1)
		print('\n[--written by Andrew Braybrook for Commodore 64 computer--]')
		time.sleep(1)
		print('\n[--play this game or die--]')
		time.sleep(1)
		print('\n........\n')
		return getcmd(cmdlist)
	elif cmd == 'quit':
		print('\n----------')
		time.sleep(1)
		print('\nI cant take this anymore')
		time.sleep(1)
		print('...')
		time.sleep(1)
		print('\n...')
		time.sleep(1)
		print('Darkness.\n')
		exit(0)
	else:
		print('\n Nothing happens.\n')
		return getcmd(cmdlist)
def combat()
