"""
The classes for the game 'The Rotten Heart'
"""

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
        self._character = None
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
        # To the c_location.connections adds self
        """
        # if side == 'north':
        #     opposite = 'south'
        # elif side == 'south':
        #     opposite = 'north'
        # elif side == 'east':
        #     opposite = 'west'
        # else:
        #     opposite = 'east'

        self._connections[side] = c_location
        # c_location._connections[opposite] = self

    def get_details(self) -> None:
        """
        Prints the details of the current location
        """
        print(self._name)
        print('—'*15)

        if self._description:
            print(self._description)

        for side in self._connections:
            print(f'The {self._connections[side]._name} is {side}')

    def set_character(self, entity: object) -> None:
        """
        Adds entity to the location
        """
        self._character = entity

    def get_character(self) -> object:
        """
        Returns the character in location
        """
        return self._character

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
        # self._conversation = None
        # self._weaknes = None

    def set_description(self, entity_description: str) -> None:
        """
        Sets the description for entity
        """
        self._description = entity_description

    def set_conversation(self, conversation: str) -> None:
        """
        Sets the conversation line for entity
        """
        self._conversation = conversation

    def set_weakness(self, object_name: str) -> None:
        """
        Sets the weakness of entity
        """
        self._weakness = object_name

    def describe(self) -> None:
        """
        Prints the name and the description of an entity
        """
        print(f'{self._name} is here')
        print(self._description)

    # def get_defeated(self) -> int:
    #     """
    #     Returns the amount of defeated enemies
    #     """
    #     return Enemy.defeated

    def talk(self) -> None:
        """
        Prints the conversation
        """
        print(f'[{self._name} says]:', end=' ')
        print(self._conversation)

    # def fight(self, item: str) -> bool:
    #     """
    #     The process of fight
    #     If the item is the same as the weakness
    #     returns True, else False
    #     """
    #     if item == self.weakness:
    #         Enemy.defeated += 1
    #         return True
    #     else:
    #         return False
