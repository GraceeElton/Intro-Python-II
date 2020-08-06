# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
from typing import List


class Room:
    def __init__(self, name, description, item=[]):
        self.name = name
        self.description = description
        self.item = item

    def __str__(self):
        return f'Name: {self.name}, Description: {self.description}, Item: {self.item}'

    # def print_items(self):
    #     for id, i in enumerate(self.items):
    #         print(f"{id}: {i}")
    #     print()
