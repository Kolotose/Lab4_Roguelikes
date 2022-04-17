"""
Module with objects for game
"""


class Room:
    def __init__(self, room_name: str) -> None:
        self.name = room_name
        self.description = None
        self.connections = {}
        self.character = None
        self.item = None

    def set_description(self, description: None) -> None:
        """
        Sets the description for the room
        """
        self.description = description

    def link_room(self, c_room: object, side: str) -> None:
        """
        Connects two rooms
        To the self.connections adds c_room
        # To the c_room.connections adds self
        """
        # if side == 'north':
        #     opposite = 'south'
        # elif side == 'south':
        #     opposite = 'north'
        # elif side == 'east':
        #     opposite = 'west'
        # else:
        #     opposite = 'east'

        self.connections[side] = c_room
        # c_room.connections[opposite] = self

    def get_details(self) -> None:
        """
        Prints the details of the current room
        """
        print(self.name)
        print('—'*15)

        if self.description:
            print(self.description)

        for side in self.connections:
            print(f'The {self.connections[side].name} is {side}')

    def set_character(self, entity: object) -> None:
        """
        Adds entity to the room
        """
        self.character = entity

    def get_character(self) -> object:
        """
        Returns the character in room
        """
        return self.character

    def set_item(self, item: object) -> None:
        """
        Sets the item of the room
        """
        self.item = item

    def get_item(self) -> object:
        """
        Returns the item of the room
        """
        return self.item

    def move(self, side: str) -> object:
        """
        Returns the room that is connected on dte side
        """
        try:
            return self.connections[side]
        except KeyError:
            return self


class Enemy:
    defeated = 0

    def __init__(self, enemy_name: str, description: str) -> None:
        self.name = enemy_name
        self.description = description
        self.conversation = None
        self.weaknes = None

    def set_conversation(self, conversation: str) -> None:
        """
        Sets the conversation line for entity
        """
        self.conversation = conversation

    def set_weakness(self, object_name: str) -> None:
        """
        Sets the weakness of entity
        """
        self.weakness = object_name

    def describe(self) -> None:
        """
        Prints the name and the description of an entity
        """
        print(f'{self.name} is here')
        print(self.description)

    def get_defeated(self) -> int:
        """
        Returns the amount of defeated enemies
        """
        return Enemy.defeated

    def talk(self) -> None:
        """
        Prints the conversation
        """
        print(f'[{self.name} says]:', end=' ')
        print(self.conversation)

    def fight(self, item: str) -> bool:
        """
        The process of fight
        If the item is the same as the weakness
        returns True, else False
        """
        if item == self.weakness:
            Enemy.defeated += 1
            return True
        else:
            return False


class Item:
    def __init__(self, item_name: str) -> None:
        self.name = item_name
        self.description = None

    def set_description(self, item_description: str) -> None:
        """
        Sets the description for the item
        """
        self.description = item_description

    def get_name(self) -> str:
        """
        Returns the name of the item
        """
        return self.name

    def describe(self) -> print:
        """
        Prints the description of the item
        """
        print(f'The {self.name} is here', end=' — ')
        print(self.description)
