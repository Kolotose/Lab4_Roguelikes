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