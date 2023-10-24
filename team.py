import random

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes '''
        self.name = name
        self.heroes = list()
        
    def remove_hero(self, name):
        ''' Remove hero from heroes list. If Hero isn't found return 0. '''
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0
            
    def view_all_heroes(self):
        ''' Prints out all heroes to the console. '''
        for hero in self.heroes:
            print(hero.name)
            
    def add_hero(self, hero):
        ''' Add Hero object to self.heroes. '''
        self.heroes.append(hero)

    
    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            # Avoid division by zero for heroes that haven't died
            if hero.deaths == 0:
                kd = hero.kills
            else:
                kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health
            
    def attack(self, other_team):
        ''' Battle each team against each other.'''
        living_heroes = [hero for hero in self.heroes if hero.current_health > 0]
        living_opponents = [hero for hero in other_team.heroes if hero.current_health > 0]

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            selected_hero = random.choice(living_heroes)
            selected_opponent = random.choice(living_opponents)

            # Have the selected heroes fight each other
            selected_hero.fight(selected_opponent)

            # Update lists of living heroes and opponents based on the fight results
            living_heroes = [hero for hero in self.heroes if hero.current_health > 0]
            living_opponents = [hero for hero in other_team.heroes if hero.current_health > 0]
