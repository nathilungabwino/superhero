# hero.py

import random
from ability import Ability
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
       
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0

    def attack(self):
        '''Calculate the total damage from all ability attacks.
           return: total_damage:Int
        '''
        # Start our total out at 0
        total_damage = 0
        # Loop through all of our hero's abilities
        for ability in self.abilities:
            # Add the damage of each attack to our running total
            total_damage += ability.attack()
        # Return the total damage
        return total_damage

    def add_ability(self, ability):
        """Add ability to hero's abilities list."""
        self.abilities.append(ability)

    def add_armor(self, armor):
        """Add armor to hero's armors list."""
        self.armors.append(armor)

    def defend(self):
        """Compute total block value from all armors."""
        total_block = sum(armor.block() for armor in self.armors)  # Assuming Armor class has a method 'block'
        return total_block

    def take_damage(self, damage_amt):
        """Reduce hero's health by damage amount after considering armor."""
        net_damage = damage_amt - self.defend()
        if net_damage < 0:  # Can't heal from over-defending
            net_damage = 0

        self.current_health -= net_damage

    def is_alive(self):
        """Return True if hero is alive, False otherwise."""
        return self.current_health > 0
    
    def fight(self, opponent):

    # First, check if at least one hero has abilities. If no heroes have abilities, print "Draw"
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
            return
        # While both heroes are still alive, continue the fight
        while self.is_alive() and opponent.is_alive():
            # Hero attacks opponent
            opponent_damage = self.attack()
            opponent.take_damage(opponent_damage)
            
            # If the opponent is still alive after the attack, they get to counter
            if opponent.is_alive():
                # Opponent attacks hero
                hero_damage = opponent.attack()
                self.take_damage(hero_damage)
            if self.current_health > opponent.current_health:
                self.add_kill(1)
                opponent.add_death(1)
            elif self.current_health < opponent.current_health:
                opponent.add_kill(1)
                self.add_death(1)

        # After the loop, at least one hero has fallen. Determine the winner.
        if self.is_alive():
            print(f"{self.name} won!")
        else:
            print(f"{opponent.name} won!")

    def add_weapon(self, weapon):    
        self.abilities.append(weapon)
         
    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills
        
    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths
    

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    weapon = Weapon("Lasso of Truth", 90)
    hero2.add_weapon(weapon)
    hero1.fight(hero2)