init python:
    class Inventory:
        def __init__(self):
            self.items = []
            self.max_items_per_slot = 99

        def add_item(self, item, quantity=1):
            remaining_quantity = quantity

            while remaining_quantity > 0:
                # Check if there is an existing slot with available space
                for inv_item in self.items:
                    if inv_item.name == item.name and inv_item.quantity < self.max_items_per_slot:
                        available_quantity = min(remaining_quantity, self.max_items_per_slot - inv_item.quantity)
                        inv_item.quantity += available_quantity
                        remaining_quantity -= available_quantity
                        break
                else:
                    # If no existing slot is found, create a new slot for the remaining quantity
                    available_quantity = min(remaining_quantity, self.max_items_per_slot)
                    new_item = Item(name=item.name, quantity=available_quantity)
                    self.items.append(new_item)
                    remaining_quantity -= available_quantity

        def remove_item(self, item, quantity=1):
            remaining_quantity = quantity

            for inv_item in self.items:
                if inv_item.name == item.name:
                    if remaining_quantity >= inv_item.quantity:
                        # Remove the entire slot if the quantity to remove is greater or equal to the slot's quantity
                        remaining_quantity -= inv_item.quantity
                        self.items.remove(inv_item)
                    else:
                        # Decrease the slot's quantity if the quantity to remove is less than the slot's quantity
                        inv_item.quantity -= remaining_quantity
                        remaining_quantity = 0

                    if remaining_quantity == 0:
                        break


    class Item:
        def __init__(self, name, quantity=1, info=""):
            self.name = name
            self.quantity = quantity
            self.info = info
