"""
The classes for the game 'The Rotten Heart'
"""


from random import uniform
import time, sys


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

    def link_location(self, c_location: object, side: str) -> None:
        """
        Connects two locations
        To the self.connections adds c_location
        """
        self._connections[side] = c_location

    def get_details(self) -> None:
        """
        Prints the details of the current location
        """
        print(self._name)
        print('—'*15)

        if self._description:
            print(self._description)

        for side in self._connections:
            print(f'На {side} — {self._connections[side]._name}')

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
    def __init__(self, entity_name: str) -> None:
        self._name = entity_name
        self._description = None

    def set_description(self, entity_description: str) -> None:
        """
        Sets the description for entity
        """
        self._description = entity_description

    def describe(self) -> None:
        """
        Prints the name and the description of an entity
        """
        print(f'{self._name} is here')
        print(self._description)

    def talk(self) -> None:
        """
        Prints the conversation
        """
        print(f'[{self._name} says]:', end=' ')
        print(self._conversation)


class Ally(Entity):
    """
    Class that represents an ally
    On creation takes 1 atribute:
    ally_name
    """
    def __init__(self, ally_name: str) -> None:
        super().__init__(ally_name)
        self._conversation = None

    def set_conversation(self, conversation: str) -> None:
        """
        Sets the conversation line for entity
        """
        self._conversation = conversation


class Enemy(Entity):
    """
    Class that represents an enemy
    On creation takes 1 atribute:
    enemy_name
    """
    def __init__(self, entity_name: str, health = 1) -> None:
        super().__init__(entity_name)
        self._weakness = None
        self._health = health
        self._alive = True

    def fight(self, item: str) -> bool:
        """
        The process of battle
        If the item is the same as the weakness
        returns True, else False
        """
        time_for_hit = round(uniform(1, 4), 1)

        print('————— Бій —————\n')
        time.sleep(1)
        print('ГОТУЙСЯ')
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

    def set_weakness(self, object_name: str) -> None:
        """
        Sets the weakness of entity
        """
        self._weakness = object_name

    # def get_defeated(self) -> int:
    #     """
    #     Returns the amount of defeated enemies
    #     """
    #     return Enemy.defeated


class Player:
    """
    Class that represents player
    On creation takes 1 atribute:
    player_name
    """
    def __init__(self, player_name) -> None:
        self._name = player_name
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

    def get_name(self) -> str:
        """
        Returns the name of the player
        """
        return self._name

    def take(self, item: object) -> None:
        """
        Places item into your backpack
        """
        self._backpack.append(item)

    def get_items_in_backpack(self) -> list:
        """
        Returns the list of items in backpack
        """
        return self._backpack

    @property
    def backpack_string(self) -> str:
        """
        The string representation of backpack
        """
        result_string = ''
        for item in self._backpack:
            result_string += item + ', '
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
        print(f'The {self._name} is here', end=' — ')
        print(self._description)
