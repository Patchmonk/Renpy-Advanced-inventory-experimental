screen inventoryScreen():
    modal True
    frame style style["inventory_frame"]:
        imagebutton style style["close_btn"]:
            idle "close"
            hover "close_hover"
            action Hide("inventoryScreen")
        # You can change background of the inventory grid if you want, here is an example code below commented.    
        # add "images/forest.png"   size(1130,700)
        vbox:
            text "Inventory" xpos 5 ypos -5

            # Calculate the maximum number of slots based on the maximum items per slot
            $ max_items_per_slot = inventory.max_items_per_slot
            $ num_slots = max(28, int(sum(item.quantity for item in inventory.items) / max_items_per_slot) + 1) # You can increase the slot here

            # Use vpgrid for flexible grid layout with scrollbars
            if num_slots > 28:
                vpgrid cols 7 spacing 5 draggable True mousewheel True scrollbars "vertical":
                    xpos 5 ypos 5
                    for slot in range(num_slots):  
                        frame:
                            maximum(155, 155)
                            background Image("images/inventory/inventory_gui/slot_bg.png") xalign 0.5 yalign 0.5

                            # Check if the slot should display an item
                            if slot < len(inventory.items):
                                $ item = inventory.items[slot]
                                add Image("images/inventory/" + item.name + ".png", xalign=0.5, yalign=0.5)

                                # Get the item name
                                $ item_name = item.name.replace('_', ' ')

                                # Get the item quantity
                                $ item_quantity = item.quantity

                                # Display the item name
                                #text item_name style style["inv_item"]

                                # Display the item quantity
                                text str(item_quantity) style style["item_quantity"]
            else:
                vpgrid cols 7 spacing 5 draggable False mousewheel False:
                    xpos 5 ypos 5
                    for slot in range(num_slots):  
                        frame:
                            maximum(155, 155)
                            background Image("images/inventory/inventory_gui/slot_bg.png") xalign 0.5 yalign 0.5

                            # Check if the slot should display an item
                            if slot < len(inventory.items):
                                $ item = inventory.items[slot]
                                add Image("images/inventory/" + item.name + ".png", xalign=0.5, yalign=0.5)

                                # Get the item name
                                $ item_name = item.name.replace('_', ' ')

                                # Get the item quantity
                                $ item_quantity = item.quantity

                                # Display the item name
                                # text item_name style style["inv_item"]

                                # Display the item quantity
                                text str(item_quantity) style style["item_quantity"]





image close:
    "images/inventory/inventory_gui/close.png"
    size(30,30) 

# backpack icon     
image close_hover:
    "images/inventory/inventory_gui/close_hover.png"
    size(30,30) 
 