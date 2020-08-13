# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items

        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def add_items(self, items):
        self.items.extend(items)
        return self.items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        item = None
        item_index = None

        for indx, itm in enumerate(self.items):
            if itm.name.lower() == name:
                item = itm
                item_index = indx
                break
            if item:
                return self.items.pop(item_index)
            else: 
                return False

    def __item_string__(self):
        return "\n".join(str(item) for item in self.items)

    def __str__(self):
        return f"\n{self.name} \n{self.description} \n{self.__item_string__}"