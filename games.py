import time
from random import randint

player = {'name': 'John', 'health': 20, 'attack': 15, 'attack_min': 5, 'attack_max': 20, 'heal': 10}
monster = {'name': 'Smith', 'health': 100, 'attack': 15, 'attack_min': 5, 'attack_max': 20}
game_running = True
def monsterAttack():
    print("You've been attacked by", monster['name'])
    monster_attack = randint(monster['attack_min'],monster['attack_max'])
    player['health'] = player['health'] - monster_attack
    time.sleep(1)
    print("Your health is now: ", player['health'])
    time.sleep(1)
def playerAttack():
    player_attack = randint(player['attack_min'],player['attack_max'])
    print("You've attacked the monster!")
    monster['health'] = monster['health'] - player_attack
    time.sleep(1)
    print("The monster's health is: ", monster['health']) 
    time.sleep(1)
def checkPlayer():
    if player['health'] <= 0:
        monster_won = True
        print('Monster has won!')
        time.sleep(1)
        print('Start a new round?')
        print('Enter Yes or No')
        select = input()
        if select == "No":
            game_running = False


        

while game_running == True:
    new_round = True
    monster['health'] = 100
    player['health'] = 100
    while new_round == True:
        player_won = False
        monster_won = False
        print('---' * 7)
        print ('Choose an option:')
        print ('1 - Attack')
        print ('2 - Heal')
        print ('3 - Exit Game')
        print ('4 - Change player name')
        player_choice = input()
        if player_choice == '1':
            #Attack
            playerAttack()
            #Check if monster ded
            if monster['health'] <= 0:
                player_won = True
                print('Player has won!')
                time.sleep(1)
                print('Start a new round?')
                print('Enter Yes or No')
                select = input()
                if select == "No":
                    game_running = False
            else:
                monsterAttack()
                checkPlayer()


        elif player_choice == '2':
            print("You've healed yourself.")
            player['health'] = player['health'] + player['heal']
            print("Your health is: ", player['health'])
            time.sleep(1)
            monsterAttack()
            checkPlayer()

        elif player_choice == '3':
            new_round = False
            game_running = False
        elif player_choice == '4':
            print("Enter new Player Name:")
            new_name = input()
            player['name'] = new_name
            print("Name has changed to: '" + player['name'] + "'")
            time.sleep(1.5)
            print("Starting new round....")
            time.sleep(1.5)
        else:
            print("Invalid input")

        if player_won == True or monster_won == True:
            new_round = False

