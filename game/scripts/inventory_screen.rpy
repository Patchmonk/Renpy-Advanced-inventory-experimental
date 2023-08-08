screen inventoryScreen():
    modal True
    frame style style["inventory_frame"]:
        imagebutton style style["close_btn"]:
            idle "close"
           
            action Hide("inventoryScreen")
        # add "images/forest.png"   size(1130,700)
        vbox:
            text "Inventory" xpos 5 ypos -5

            # Calculate the maximum number of slots based on the maximum items per slot
            $ max_items_per_slot = inventory.max_items_per_slot
            $ num_slots = max(28, int(sum(item.quantity for item in inventory.items) / max_items_per_slot) + 1) # You can increase the slot here

            # Use vpgrid for flexible grid layout with scrollbars
            vpgrid cols 7 spacing 5 draggable True mousewheel True scrollbars "vertical":
                xpos 5 ypos 5
                for i in range(num_slots):  
                    frame:
                        maximum(155, 155)
                        background Image("images/inventory/inventory_gui/slot_bg.png") xalign 0.5 yalign 0.5

                        # Check if the slot should display an item
                        if i < len(inventory.items):
                            $ item = inventory.items[i]
                            add Image("images/inventory/" + item.name + ".png", xalign=0.5, yalign=0.5)
                            $ inv_item_name = item.name.replace('_', ' ')
                            # $ inv_item_text = f"{inv_item_name} x{item.quantity}"
                            $ inv_item_text = f"x{item.quantity}"

                            text inv_item_text style style["inv_item"]


image close:
    "images/inventory/inventory_gui/close.png"
    size(30,30) 

# backpack icon     
image close_hover:
    "images/inventory/inventory_gui/close_hover.png"
    size(30,30) 
 