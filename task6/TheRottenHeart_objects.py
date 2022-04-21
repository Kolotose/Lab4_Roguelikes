"""
The classes for the game 'The Rotten Heart'
"""


from random import uniform
import time, sys
from typing import List, Dict


class Location:
    """
    The class that represents the location
    On creation takes 1 attribute:
    location name
    """
    def __init__(self, location_name: str) -> None:
        self._name = location_name
        self._description = None
        self._connections = {}
        self._entity = None
        self._item = None

    def set_description(self, description: str) -> None:
        """
        Sets the description for the location
        """
        self._description = description

    def link_location(self, location: object, side: str) -> None:
        """
        Connects two locations
        To the self.connections adds location
        """
        self._connections[side] = location

    def get_connections(self) -> dict:
        """
        Returns the connections of the lication
        """
        return self._connections

    def unlink_location(self, side: str) -> None:
        """
        Unlinks the location on the given side
        Removes the key=side
        """
        del self._connections[side]

    def get_details(self) -> None:
        """
        Prints the details of the current location
        """
        print(self._name)
        print('—'*20)

        if self._description:
            print(self._description + '\n')

        for side in self._connections:
            print(f'На {side} — {self._connections[side]._name}')
        print()

    def set_entity(self, entity: object) -> None:
        """
        Adds entity to the location
        """
        self._entity = entity

    def get_entity(self) -> object:
        """
        Returns the character in location
        """
        return self._entity

    def set_item(self, item: object) -> None:
        """
        Sets the item of the location
        """
        self._item = item

    def remove_item(self):
        """
        Removes first item from the items list
        """
        self._item = None

    def get_item(self) -> object:
        """
        Returns the item of the location
        """
        return self._item

    def move(self, side: str) -> object:
        """
        Returns the location that is connected on dte side
        """
        try:
            return self._connections[side]
        except KeyError:
            print("Тобі туди не треба!")
            return self


class Entity:
    """
    Class that represents an entity
    On creation takes 1 atribute:
    entity_name
    """
    # Entity.defeated = 0
    def __init__(self, entity_name: str, entity_type = None) -> None:
        self._name = entity_name
        self._description = None
        self._type = entity_type
        self._items = []

    def get_name(self) -> str:
        """
        Returns the name of the entity
        """
        return self._name

    def set_description(self, entity_description: str, version = 0) -> None:
        """
        Sets the description for entity
        """
        self._description = entity_description

    def describe(self) -> None:
        """
        Prints the name and the description of an entity
        """
        print(f'Тут є {self._type} {self._name}')
        print(self._description)

    def add_item(self, item: object) -> None:
        """
        Adds item to the ally inventory
        """
        self._items.append(item)

    def take_item(self) -> object:
        """
        Pops first item from ._items list
        """
        return self._items.pop(0)


class Ally(Entity):
    """
    Class that represents an ally
    On creation takes 1 atribute:
    ally_name
    """
    def __init__(self, ally_name: str) -> None:
        super().__init__(ally_name, 'союзник')
        self._conversation = None
        self._reputation = 0

    def set_conversations(self, conversations: dict) -> None:
        """
        Sets the conversation line for entity
        """
        self._conversation = conversations

    # def talk(self, player) -> None:
    #     """
    #     Prints the conversation
    #     """
    #     print(f'[{self._name}]:', end=' ')
    #     print(self._conversation)

    def get_reputation(self) -> int:
        """
        Returns the reputation of player in
        this character
        """
        return self._reputation

    def increace_reputation(self) -> None:
        """
        Increaces the reptation of player in
        this character
        """
        self._reputation += 1


class Enemy(Entity):
    """
    Class that represents an enemy
    On creation takes 1 atribute:
    enemy_name
    """
    def __init__(self, entity_name: str) -> None:
        super().__init__(entity_name, 'ворог')
        self._weakness = None
        self._alive = True

    def fight(self) -> bool:
        """
        The process of battle
        If the item is the same as the weakness
        returns True, else False
        """
        time_for_hit = round(uniform(1, 4), 1)

        print('————— Бій —————')
        time.sleep(1)
        print('ГОТУЙСЯ', end='\n\n')
        time.sleep(time_for_hit)

        # Time challenge
        print('0===[=========>', end='')
        start_time = time.time()
        input() #player presses 'enter'
        end_time = time.time()

        difference_time = end_time - start_time

        if difference_time <= 0.4:
            sys.stdout.write("\033[F")
            print('ˉ - 0===[=========>', end='\r')
            time.sleep(0.05)
            print('_ ˉ - 0===[=========>', end='\r')
            time.sleep(0.05)
            print('- _ ˉ - 0===[=========>')
            time.sleep(1)
            print('* успіх *')
            return True

        else:
            sys.stdout.write("\033[F")
            print('0===[=/ /======>', end='\r')
            time.sleep(0.05)
            print('0===[=/   /======>', end='\r')
            time.sleep(0.05)
            print('0===[=/     /======>')
            time.sleep(1)
            print('* провал *')
            return False

    def set_weakness(self, item: object) -> None:
        """
        Sets the weakness of entity
        """
        self._weakness = item

    def get_weakness(self) -> str:
        """
        Returns the weakness of the enemy
        """
        return self._weakness

    def get_alive(self) -> bool:
        """
        Returns if the enemy is alive
        """
        return self._alive


class SpecialAlly(Ally):
    def __init__(self, ally_name: str) -> None:
        super().__init__(ally_name)

    def fight(self) -> bool:
        """
        The process of battle
        If the item is the same as the weakness
        returns True, else False
        """
        time_for_hit = round(uniform(1, 4), 1)

        print('————— Бій —————')
        time.sleep(1)
        print('ГОТУЙСЯ', end='\n\n')
        time.sleep(time_for_hit)

        # Time challenge
        print('0===[=========>', end='')
        start_time = time.time()
        input() #player presses 'enter'
        end_time = time.time()

        difference_time = end_time - start_time

        if difference_time <= 0.4:
            sys.stdout.write("\033[F")
            print('ˉ - 0===[=========>', end='\r')
            time.sleep(0.05)
            print('_ ˉ - 0===[=========>', end='\r')
            time.sleep(0.05)
            print('- _ ˉ - 0===[=========>')
            time.sleep(1)
            print('* успіх *')
            return True

        else:
            sys.stdout.write("\033[F")
            print('0===[=/ /======>', end='\r')
            time.sleep(0.05)
            print('0===[=/   /======>', end='\r')
            time.sleep(0.05)
            print('0===[=/     /======>')
            time.sleep(1)
            print('* провал *')
            return False


class Player:
    """
    Class that represents player

    has following attributes:
    backpack: list — backpack with items
    alive: bool — the indicator of characters aliveness
    reputation — used to progress through the story
    during dialogues
    """
    def __init__(self) -> None:
        self._backpack = []
        self._alive = True

    def death(self) -> None:
        """
        Makes character dead
        """
        self._alive = False

    def is_alive(self) -> None:
        """
        Returns the live state of character
        """
        return self._alive

    def take(self, item) -> None:
        """
        Places item into your backpack
        """
        self._backpack.append(item)

    def get_items_in_backpack(self) -> list:
        """
        Returns the list of items in backpack
        """
        return self._backpack

    def use_item(self, item: object) -> None:
        """
        Uses (removes) item in backpack
        """
        self._backpack.remove(item)

    def backpack_string(self) -> str:
        """
        The string representation of backpack
        """
        result_string = ''
        for item in self._backpack:
            result_string += item._name + ', '
        return result_string.strip(', ')


class Item:
    """
    Class that represents an item
    On creation takes 1 atribute:
    item_name
    """
    def __init__(self, item_name: str) -> None:
        self._name = item_name
        self._description = None

    def set_description(self, item_description: str) -> None:
        """
        Sets the description for the item
        """
        self._description = item_description

    def get_name(self) -> str:
        """
        Returns the name of the item
        """
        return self._name

    def describe(self) -> print:
        """
        Prints the description of the item
        """
        print(f'Тут є предмет [{self._name}]', end=' — ')
        print(self._description)
