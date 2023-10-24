from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        '''Instantiate properties: team_one and team_two.'''
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")

    def create_ability(self):
        '''Prompt for Ability information and return an Ability instance.'''
        name = input("What is the ability name?  ")
        max_damage = int(input("What is the max damage of the ability?  "))
        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt for Weapon information and return a Weapon instance.'''
        name = input("What is the weapon name?  ")
        max_damage = int(input("What is the max damage of the weapon?  "))
        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt for Armor information and return an Armor instance.'''
        name = input("What is the name of the armor?  ")
        defense = int(input("What is the defensive strength of the armor?  "))
        return Armor(name, defense)

    def create_hero(self):
        '''Prompt for Hero information, add abilities, weapons, armor and return a Hero instance.'''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
                print(f"{hero_name} now has the ability: {ability.name}")
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
                print(f"{hero_name} now wields the weapon: {weapon.name}")
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
                print(f"{hero_name} now wears the armor: {armor.name}")

        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one.'''
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
            print(f"{hero.name} has been added to {self.team_one.name}")

    def build_team_two(self):
        '''Prompt the user to build team_two.'''
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
            print(f"{hero.name} has been added to {self.team_two.name}")

    def team_battle(self):
        '''Have team_one and team_two fight each other.'''
        print("Battle begins between Team One and Team Two!")
        self.team_one.attack(self.team_two)
        self.team_two.attack(self.team_one)
        print("The battle has ended!")

    def show_stats(self):
        '''Print team statistics to the terminal.'''
        print("\nTeam One statistics: ")
        self.team_one.stats()
        print("\nTeam Two statistics: ")
        self.team_two.stats()

        team_one_kills = sum([hero.kills for hero in self.team_one.heroes])
        team_one_deaths = sum([hero.deaths for hero in self.team_one.heroes])
        team_two_kills = sum([hero.kills for hero in self.team_two.heroes])
        team_two_deaths = sum([hero.deaths for hero in self.team_two.heroes])

        if team_one_deaths == 0: team_one_deaths = 1  # To prevent division by zero
        if team_two_deaths == 0: team_two_deaths = 1  # To prevent division by zero

        print(f"\n{self.team_one.name} average K/D was: {team_one_kills/team_one_deaths}")
        print(f"{self.team_two.name} average K/D was: {team_two_kills/team_two_deaths}")

        for hero in self.team_one.heroes:
            if hero.is_alive():
                print(f"Survived from {self.team_one.name}: {hero.name}")
        for hero in self.team_two.heroes:
            if hero.is_alive():
                print(f"Survived from {self.team_two.name}: {hero.name}")

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()