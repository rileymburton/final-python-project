import random

#start screen
def start_screen():
	print("Welcome to GAME!")
	start_screen_loop = 1
	while start_screen_loop == 1:
		play = input("1. Play\n2. Exit\n")
		if play == "2":
			start_screen_loop = 0
			raise SystemExit
		elif play != "2" and play != "1":
			print("Please select Play or Exit")
		elif play == "1":
			start_screen_loop = 0

#pick class
def choose_class():
	class_choose_loop = 1
	while class_choose_loop == 1:
		chosen_class = input("\nPlease select a class:\n1. Knight\n2. Wizard\n")
		if chosen_class == "1":
			print("\nThe Knight:\nHealth: 750\nDamage: 25")
			x = 1
			while x == 1:
				confirm_class_knight = input("Are you sure you would like to be the Knight? (Y/N): ")
				if confirm_class_knight == "y":
					return("knight")
				elif confirm_class_knight == "n":
					x = 0
				else:
					print("Please select Yes or No")
		if chosen_class == "2":
			print("\nThe Wizard:\nHealth: 350\nDamage: 55 ")
			y = 1
			while y == 1:
				confirm_class_wizard = input("Are you sure you would like to be the Wizard? (Y/N): ")
				if confirm_class_wizard == "y":
					return("wizard")
				elif confirm_class_wizard == "n":
					y = 0
				else:
					print("Please select Yes or No")

#bag
bag = []
def use_bag_item(bag_item):
	if bag_item == "Health Potion":
		hp = HealthPotion()
		print("\nDescription: {}".format(hp.desc))
		confirm = input("\nAre you sure you want to use {} (Y/N)?: ".format(bag_item))
		if confirm == "y":
			hp.use()
			print("\nHealth restored! Your health: {}".format(Player.hp))
	elif bag_item == "Damage Potion":
		dp = DamagePotion()
		print("\nDescription: {}".format(dp.desc))
		confirm = input("\nAre you sure you want to use {} (Y/N)?: ".format(bag_item))
		if confirm == "y":
			dp.use()
			print("\nDamage increased by 20! Your damage: {}".format(Player.dmg))
	elif bag_item == "Vitality Potion":
		vp = VitalityPotion()
		print("\nDescription: {}".format(vp.desc))
		confirm = input("\nAre you sure you want to use {} (Y/N)?: ".format(bag_item))
		if confirm == "y":
			vp.use()
			print("\nMaximum health increased by 50! Your maximum health: {}".format(Player.max_hp))

	bag.remove(bag_item)

def find_item(item):
	pick_up = input('\nYou found "{}"! Would you like to pick it up? (Y/N): '.format(item))
	if pick_up == "y":
		bag.insert(0, item)
		bag_check = input("\nWould you like to view your bag? (Y/N): ")
		if bag_check == "y":
			print("\nBag:")
			print("Gold: {}\n".format(Player.gold))
			b = 0
			while b < len(bag):
				print("{}. {}".format(b + 1, bag[b]))
				b += 1
	else:
		print("\nItem discarded")

#battle
def battle(enemy_name, enemy_health, enemy_dmg, next_savepoint, reward):
	battle_loop = 1
	while battle_loop == 1:
		print("You encountered a {}!\n".format(enemy_name))
		print("Your Health: {}".format(Player.hp))
		print("{} Health: {}".format(enemy_name, enemy_health))
		
		x = 1
		while x == 1:
			battle_option = input("Would you like to (A)ttack or (R)un: ")
			if battle_option == "a":
				dmg = round(random.uniform(Player.dmg * .8, Player.dmg * 1.2), 0)
				print("\nYou did {} damage!".format(dmg))
				enemy_health -= dmg
				print("Your Health: {}".format(Player.hp))
				print("Enemy Health: {}\n".format(enemy_health))
				if enemy_health <= 0:
					x = 0
					battle_loop = 0
					print("\nCongratulations, you defeated {}!".format(enemy_name))
					Player.save_point = next_savepoint
					print("You looted {} gold!".format(reward))
					Player.gold += reward
					return True
				else:
					enemy_dmg = round(random.uniform(enemy_dmg * .8, enemy_dmg * 1.2), 0)
					print("\nMonster did {} damage to you!".format(enemy_dmg))
					Player.hp -= enemy_dmg
					print("Your Health: {}".format(Player.hp))
					print("Enemy Health: {}\n".format(enemy_health))
					if Player.hp <= 0:
						x = 0
						battle_loop = 0
						print("You died!\n")
						input("Resetting to last save point...\n")
					
			elif battle_option == "r":
				print("\nYou ran away!")
				x = 0
				battle_loop = 0
				Player.save_point = next_savepoint
				return False
			else:
				print("Please select (A)ttack, or (R)un")

#puzzle level
def puzzle():
	print("You encountered a puzzle! Get it correct, and you will be rewarded greatly, get it wrong, and you will lose 50% of your current health.")
	do_puzzle = input("Would you like to participate? (Y/N):")
	if do_puzzle = "y":
		puzzle_choice = random.randint(1, 3)
		if puzzle_choice == 1:
			answer_1 = "umbrella"
			response_1 = input("What goes up as the rain comes down?: ")
			if response_1 == answer_1:
				return True
			else:
				return False
		if puzzle_choice == 2:
			answer_2 == "short"
			response_2 = input("What 5 letter word becomes shorter when you add two letters to it?: ")
			if response_2 == answer_2:
				return True
			else:
				return False
		if puzzle_choice == 3:
			answer_3 = "e"
			response_3 = input("What is the beginning of eternity, but the end of time and space?: ")
			if response_3 == answer_3:
				return True
			else:
				return False
		
#main game loop
def game_loop():
	loop = 1
	while loop == 1:
		option = input("\nWould you like to (C)ontinue or go to (B)ag?: ")
		print("\n")
		if option == "b":
			print("\nBag: ")
			print("Gold {}\n".format(Player.gold))
			if not bag:
				print("Bag is empty!")
			else:
				b = 0
				while b < len(bag):
					print("{}. {}".format(b + 1, bag[b]))
					b += 1
				bag_item_choice = int(input("\nWhich item do you want to use? (Press 0 to exit): "))
				if bag_item_choice == 0:
					return
				elif bag_item_choice > len(bag):
					print("Invalid bag item")
				else:
					bag_item_choice = bag[bag_item_choice - 1]
					use_bag_item(bag_item_choice)
		elif option != "c":
			print("Please select (C)ontinue or (B)ag")
		else:
			loop = 0

# -=[PLAYER]-= #
class Player:
	max_hp = 0
	hp = 0
	dmg = 0
	cl = ""
	gold = 0
	save_point = "pt1"

# -=[ENEMIES]=- #
class Bandit:
	name = "Bandit"
	hp = 100
	dmg = 10

class BanditLeader:
	name = "Bandit Leader"
	hp = 250
	dmg = 50

class Wolf:
	name = "Hungry Wolf"
	hp = 350
	dmg = 50

# -=[ITEMS]=- #
class HealthPotion:
	desc = "Restores you to full health"
	def use(self):
		Player.hp = Player.max_hp

class DamagePotion:
	desc = "Permanently increases damage by 20"
	def use(self):
		Player.dmg += 20

class VitalityPotion:
	desc = "Permanently increases maximum health by 50"
	def use(self):
		Player.max_hp += 50
		
start_screen()

Player.cl = choose_class()
if Player.cl == "knight":
	Player.hp = 750
	Player.max_hp = 750
	Player.dmg = 25
elif Player.cl == "wizard":
	Player.hp = 350
	Player.max_hp = 350
	Player.dmg = 55

##############
# STORY PT 1 #
##############
print("\nstory pt 1\n")
input()
while Player.save_point == "pt1":
	if battle(Bandit.name, Bandit.hp, Bandit.dmg, "pt2", 100):
		find_item("Health Potion")
game_loop()

##############
# STORY PT 2 #
##############
print("\nstory pt 2\n")
input()
while Player.save_point == "pt2":
	if battle(BanditLeader.name, BanditLeader.hp, BanditLeader.dmg, "pt3", 250):
		find_item("Damage Potion")
game_loop()

##############
# STORY PT 3 #
##############
print("\nstory pt 3\n")
input()
while Player.save_point == "pt3":
	if battle(Wolf.name, Wolf.hp, Wolf.dmg, "pt4", 150):
		find_item("Vitality Potion")
game_loop()

##############
# STORY PT 4 #
##############
print("\nstory pt 3\n") #puzzle
input()
if puzzle():
	Player.gold += 250
else:
	Player.hp -= Player.hp * .5