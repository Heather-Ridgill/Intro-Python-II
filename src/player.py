# Write a class to hold player information, e.g. what room they are in
# currently.

"""
player.py
My Condo
    1. Kitchen
    2. Foyer
    3. Living Room
    4. Bedroom
Select the number of the room.

Attributes:
- name
- room

Optional extra attributes"
- time 
- activity

"""
class Player:

    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return(f'My name is {self.name}')


player = Player ("Jessie Jefferson", "Kitchen")

print(player)


