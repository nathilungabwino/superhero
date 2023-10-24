import pytest
from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team
from arena import Arena
import random
import io
import sys

# Helper Functions


def capture_console_output(function_body):
    # _io.StringIO object
    string_io = io.StringIO()
    sys.stdout = string_io
    function_body()
    sys.stdout = sys.__stdout__
    return string_io.getvalue()


def create_armor():
    armors = [
        "Calculator",
        "Laser Shield",
        "Invisibility",
        "SFPD Strike Force",
        "Social Workers",
        "Face Paint",
        "Damaskus Shield",
        "Bamboo Wall",
        "Forced Projection",
        "Thick Fog",
        "Wall of Will",
        "Wall of Walls",
        "Obamacare",
        "Thick Goo"]
    name = armors[random.randint(0, len(armors) - 1)]
    power = random.randint(23, 700000)
    return Armor(name, power)


def create_weapon():
    weapons = [
        "Antimatter Gun",
        "Star Cannon",
        "Black Hole Ram Jet",
        "Laser Sword",
        "Laser Cannon",
        "Ion Accellerated Disc Drive",
        "Superhuman Strength",
        "Blinding Lights",
        "Ferociousness",
        "Speed of Hermes",
        "Lightning Bolts"]
    name = weapons[random.randint(0, len(weapons) - 1)]
    power = random.randint(27, 700000)
    return Weapon(name, power)


def create_ability():
    abilities = [
        "Alien Attack",
        "Science",
        "Star Power",
        "Immortality",
        "Grandmas Cookies",
        "Blinding Strength",
        "Cute Kittens",
        "Team Morale",
        "Luck",
        "Obsequious Destruction",
        "The Kraken",
        "The Fire of A Million Suns",
        "Team Spirit",
        "Canada"]
    name = abilities[random.randint(0, len(abilities) - 1)]
    power = random.randint(45, 700000)
    return Ability(name, power)


def create_hero(weapons=False, armors=False, health=False):

    heroes = [
        "Athena",
        "Jodie Foster",
        "Christina Aguilera",
        "Gamora",
        "Supergirl",
        "Wonder Woman",
        "Batgirl",
        "Carmen Sandiego",
        "Okoye",
        "America Chavez",
        "Cat Woman",
        "White Canary",
        "Nakia",
        "Mera",
        "Iris West",
        "Quake",
        "Wasp",
        "Storm",
        "Black Widow",
        "San Luis Obispo",
        "Ted Kennedy",
        "San Francisco",
        "Bananas"]
    name = heroes[random.randint(0, len(heroes) - 1)]
    if health:
        power = health
    else:
        power = random.randint(3, 700000)
    hero = Hero(name, power)
    if weapons and armors:
        for weapon in weapons:
            hero.add_ability(weapon)
        for armor in armors:
            hero.add_armor(armor)
    if armors and not weapons:
        for armor in armors:
            hero.add_armor(armor)

    return hero


def create_team(heroes=[]):
    teams = [
        "Orchids",
        "Red",
        "Blue",
        "Cheese Steaks",
        "Warriors",
        "49ers",
        "Marvel",
        "DC",
        "Rat Pack",
        "The Little Red Riding Hoods",
        "Team One",
        "Generic Team",
        "X-men",
        "Team Two",
        "Golden Champions",
        "Vegan Protectors",
        "The Cardinals",
        "Winky Bears",
        "Steelsmiths",
        "Boilermakers",
        "Nincompoops"]
    name = teams[random.randint(0, len(teams) - 1)]
    team = Team(name)
    if len(heroes) > 0:
        for member in heroes:
            team.add_hero(member)

    return team


def create_set():
    armor_pieces = random.randint(1, 300)
    weapon_pieces = random.randint(1, 300)
    ability_ct = random.randint(1, 300)
    armors = []
    abilities = []
    for _ in range(0, armor_pieces):
        armors.append(create_armor())
    for _ in range(0, weapon_pieces):
        abilities.append(create_weapon())
    for _ in range(0, ability_ct):
        abilities.append(create_ability())

    hero_set = {'weapons': abilities, 'armors': armors}
    return hero_set


# Test Armor
def test_armor():
    armor = Armor("The Ring", 200)
    for _ in range(0, 500):
        defense = armor.block()
        assert (defense <= 200 and defense >= 0)


# Test Hero


def test_hero_initialize_health():
    jodie = Hero("Jodie Foster")
    assert jodie.current_health == 100

def test_hero_default_starting_health():
    jodie = Hero("Jodie Foster")
    assert jodie.starting_health == 100


def test_hero_defense():
    jodie = Hero("Jodie Foster")
    gauntlets = Armor("Gauntlets", 30)
    jodie.add_armor(gauntlets)
    defense = jodie.defend()
    assert defense >= 0 and defense <= 30


def test_dead_hero_defense():
    hero = Hero("Vlaad", 0)
    defense_amount = 30000
    garlic = Armor("Garlic", defense_amount)
    hero.add_ability(garlic)
    assert hero.defend() == 0


def test_hero_equip_armor():
    jodie = Hero("Jodie Foster")
    gauntlets = Armor("Gauntlets", 30)
    jodie.add_armor(gauntlets)
    assert len(jodie.armors) == 1
    assert jodie.armors[0].name == "Gauntlets"


def test_hero_defend_multi_armor():
    jodie = Hero("Jodie Foster")
    gauntlet_defense = 4000
    science_defense = 9000
    gauntlets = Armor("Gauntlets", gauntlet_defense)
    science = Armor("Science", science_defense)
    jodie.add_armor(gauntlets)
    jodie.add_armor(science)
    defend = jodie.defend()
    assert defend <= 13000 and defend >= 0


def test_hero_attack():
    flash = Hero("The Flash")
    assert flash.attack() == 0
    pesto = Ability("Pesto Sauce", 8000)
    flash.add_ability(pesto)
    attack = flash.attack()
    assert attack <= 8000 and attack >= 0


# Test Team


def test_team_attack():
    team_one = Team("One")
    jodie = Hero("Jodie Foster")
    aliens = Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_two = Team("Two")
    athena = Hero("Athena")
    socks = Armor("Socks", 10)
    athena.add_armor(socks)
    team_two.add_hero(athena)
    assert team_two.heroes[0].current_health == 100

    team_one.attack(team_two)

    assert team_two.heroes[0].current_health <= 0


def test_team_attack_kills():
    team_one = Team("One")
    jodie = Hero("Jodie Foster")
    aliens = Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_two = Team("Two")
    athena = Hero("Athena")
    socks = Armor("Socks", 10)
    athena.add_armor(socks)
    team_two.add_hero(athena)
    assert team_one.heroes[0].kills == 0
    team_one.attack(team_two)
    assert team_one.heroes[0].kills == 1


def test_team_attack_deaths():
    team_one = Team("One")
    jodie = Hero("Jodie Foster")
    aliens = Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_two = Team("Two")
    athena = Hero("Athena")
    socks = Armor("Socks", 10)
    athena.add_armor(socks)
    team_two.add_hero(athena)
    assert team_two.heroes[0].deaths == 0
    team_one.attack(team_two)
    assert team_two.heroes[0].deaths == 1


def test_revive_heroes():
    heroes = []
    for _ in range(0, 20):
        heroes.append(create_hero(health=60))

    team_one = Team("One")
    for hero in heroes:
        team_one.add_hero(hero)
    
    for hero in heroes:
        hero.take_damage(15)

    for hero in team_one.heroes:
        assert hero.current_health == 45
    team_one.revive_heroes()
    for hero in team_one.heroes:
        assert hero.current_health == 60