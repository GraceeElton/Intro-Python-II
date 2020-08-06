from room import Room
from player import Player
from item import Item

# Declare all the rooms with thier items

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", Item("Sword", "you know")),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item("Spear", "long thing with pointy end")),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item("CrossBow", "not worth it - go for the gun")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item("Gun", "good choice - but do you have bullets?")),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item("Gold", "lots of it")),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])


def try_direction(player, direction):
    # check the player's current location and see if there is
    # a room in the specified direction
    # if there is, move them there to that room
    # otherwise, a print message saying "we can't go there" and
    # not move the player
    attribute = direction + '_to'
    # python has a handy method called hasattr
    # which allows us to check if a class has an attribute
    if hasattr(player.location, attribute):
        # this is a valid direction
        # use getattr to fetch the value associated with the attribute
        # update our player's location with the fetched room
        player.location = getattr(player.location, attribute)
    else:
        print('\n')
        print("There is nothing in that direction!")


while True:
    # * Prints the current description  and location(the textwrap module might be useful here).
    print('\n')
    print(player.location)

    command = input("\nCommand: ").strip().lower().split()
    print(command[0])
# if the first letter is get and the last word is item name
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#

# If the user enters "q", quit the game.
    command2 = command[0]
    first_word = command2[0]
    if first_word == 'q':
        break
    elif first_word == 'n':
        # move to the north
        try_direction(player, first_word)
    elif first_word == 's':
        # move to the south
        try_direction(player, first_word)
    elif first_word == 'w':
        # move to the west
        try_direction(player, first_word)
    elif first_word == 'e':
        # move to the east
        try_direction(player, first_word)
    else:
        print(f"That is not a correct direction")
