# Write a class to hold player information, e.g. what room they are in
# currently.


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

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room


    def __str__(self):
        return(f'My name is {self.name}')


    def move(self, direction):
        print(direction, "input")
        next_room =f'{direction}_to'

        try:
            self.current_room = getattr(self.current_room, next_room)
            
        except:
            print("Sorry you cant move that way, try another way!")
            # input("Please press any key to continue...")


player = Player ("Dr. Abigail Chase", "outside")

print(player)


