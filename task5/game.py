"""
Module with objects for game
"""

class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.connections = {}
        self.character = None
        self.object = None

    def set_description(self, description: None) -> None:
        """
        Sets the description for the room
        """
        self.description = description

    def link_room(self, c_room: object, side: str) -> None:
        """
        Connects two rooms
        To the self.connections adds c_room
        To the c_room.connections adds self
        """
        if side == 'north':
            opposite = 'south'
        elif side == 'south':
            opposite = 'north'
        elif side == 'east':
            opposite = 'west'
        else:
            opposite = 'east'

        self.connections[side] = c_room
        c_room.connections[opposite] = self

    def set_character(self, entity):
        """
        Adds entity to the room
        """
        self.character = entity


class Enemy:
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