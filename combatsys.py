from random import randint
import time
player = {'weapon':'metalpipe', 'health':100, 'healthmax':100}
WEAPONS = {'metalpipe': (50,65), 'None':(10,10), 'scapel':(40,80), 'gun':(100,150), 'claws':(30,40), 'jaws':(50,70),'paws':(30,30)}
alien_elec = {'name':'The thing', 'health':150, 'healthmax':150, 'weapon':'claws'}
alien_esc = {'name':'The thing', 'health':150, 'healthmax':150, 'weapon':'jaws'}
alien_ran = {'name':'The thing', 'health':150, 'healthmax':150, 'weapon':'paws'}
crew = {'name':'Andy', 'health':70, 'healthmax':100, 'weapon':'None'}
#combat system
def combat (player, enemy, order):
    time.sleep(0.75)
    while player['health'] > 0 and enemy['health'] >0:
        player_damage = randint(WEAPONS[player['weapon']][0],WEAPONS[player['weapon']][1])
        enemy_damage = randint(WEAPONS[enemy['weapon']][0],WEAPONS[enemy['weapon']][1])
        #1 means player attack first
        if order == 1:
            enemy['health'] = enemy['health'] - player_damage
            if enemy['health'] > 0:
                player['health'] = player['health']- enemy_damage
                print('>You RECEIVE ' + str(enemy_damage) + ' dmg. You have : ' + str(player['health']) + '/' + str(player['healthmax'])+' HP')
                time.sleep(2)
            else:
                print(">You narrowly dodged an attack and returned a blow")
            print('>You DEAL ' + str(player_damage) + ' dmg. '+str(enemy['name'])+ ' has : ' + str(enemy['health']) + '/' + str(enemy['healthmax'])+' HP')
        #2 means enemy attack first
        elif order == 2:
            player['health'] = player['health']- enemy_damage
            if player['health'] > 0:
                enemy['health'] = enemy['health'] - player_damage
                print('>You DEAL ' + str(player_damage) + ' dmg. '+str(enemy['name'])+ ' has : ' + str(enemy['health']) + '/' + str(enemy['healthmax'])+' HP')
                time.sleep(1)
            else:
                print(">The attack stuns you\n>Your ears ringing. Vision whiteout.")
                time.sleep(3)
            print('>You RECEIVE ' + str(enemy_damage) + ' dmg. You have : ' + str(player['health']) + '/' + str(player['healthmax'])+' HP')
        time.sleep(2)
    if player['health'] >0 and enemy['health'] <=0:
        return True
    else:
        return False
#fight
def fight(player, enemy, order):
    fight_result = combat(player, enemy, order)
    if fight_result is True:
        print(str(enemy['name']) +" collapses")
        print("won")
    else:
        print("Your body relaxes")
        print("lose")
fight(player, alien_elec, 2)
