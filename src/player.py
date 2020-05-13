# Write a class to hold player information, e.g. what room they are in
# currently.
import os

"""
player.py
Special Room
    1. outside
    2. Foyer
    3. overlook
    4. narrow
    5. treasure
Select the number of the room.

Attributes:
- name
- room
- description
- direction

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


    def move(self, direction):
        next_room =f'{direction}_to'

        try:
            self.room = getmoving(self.room, next_room)
        except:
            print("Sorry you cant move that way, try another way!")
            input("Please press any key to continue...")


player = Player ("Jessie Jefferson", "treasure")

print(player)


