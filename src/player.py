# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def add_item(self, item):
        self.inventory.append(item)
        item.on_take()
        return self.inventory

    def remove_item(self, indx):
        item = self.inventory.pop(indx)
        item.on_drop()
        return self.inventory

    def pickup_item(self, name):
        item = self.current_room.remove_item(name)

        if item: 
            return self.add_item(item)
        else:
            return False

    def drop_item(self, name):
        item = None
        item_index = None

        for indx, itm in enumerate(self.inventory):
            if itm.name.lower() == name:
                item = itm
                item_index = indx
                break
        if item: 
            self.current_room.add_item(name)
            return self.remove_item(item_index)
        else:
            return False

    def inventory_string(self):
        return "\n".join(str(item) for item in self.inventory)