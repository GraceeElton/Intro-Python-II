class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'Name: {self.name}, Description: {self.description}'

    def pick_up(self):
        print(f"You have picked up the {self.name}")

    def drop_it(self):
        print(f"You have dropped the {self.name}")
