from random import randint
player = {'weapon':'None', 'health':10, 'healthmax':10}
WEAPONS = {'pipe': (3,3), 'None':(1,1), 'scapel':(2,6), 'gun':(10,15)}
alien = {'name':'thing', 'health':15, 'healthmax':15, 'attack':(3,5)}
crew = {'name':'crew', 'health':7, 'healthmax':10, 'weapon':'None'}
#combat system
def combat (player, enemy):
    while player['health'] > 0 and enemy['health'] >0:
        player_damage = randint(WEAPONS[player['weapon']])
        enemy_damage = randint(enemy['attack'])
        player['health'] .__sub__(self,enemy_damage)
        enemy['health'].__sub__(self,player_damage)
        #description
        print('You deal ' + player_damage + '. The enemy has : ' +enemy + ['health'] + '/' + enemy['healthmax'])
        print('You receive ' + enemy_damage + '. You have : ' + player['health'] + '/' + player['healthmax'])
    if player['health'] >0 and enemy['health'] <=0:#test if it reads enemy health from global or local
        return True
    else:
        return False
#fight
fight_result = combat(player, alien)
if fight_result is True:
    print("won")
else:
    print("lose")
