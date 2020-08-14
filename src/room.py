# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def item_string(self):
        if len(self.items) == 0:
            print("\n No Item available \n")
        else:
            print(f" \nItems on the ground: => {', '.join([item.name for item in self.items])} <=\n")
