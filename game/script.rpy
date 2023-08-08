# name of the character.
define e = Character("Eileen")
    
  
# Global currency
default gold = 1000
label start:
    show Forest
    # To set up the initial state of the inventory we have to create an instance of the inventory class
    $ inventory = Inventory()
    show screen HUD

    # Add some initial items to the inventory
    $ map = Item(name="map", quantity=1)
    $ apple = Item(name="apple", quantity=1)
    $ fish = Item(name="fish", quantity=1)
    $ compass = Item(name="compass", quantity=1)
    $ log = Item(name="log", quantity=1)  
    $ mana_ram = Item(name="Mana_ram", quantity=1) 
   

    $ inventory.add_item(map, 99)
    $ inventory.add_item(apple,99)
    $ inventory.add_item(apple,99)
    $ inventory.add_item(compass, 99)
    $ inventory.add_item(log, 99)
    $ inventory.add_item(mana_ram, 99)
    $ inventory.add_item(fish, 99)

    $ inventory.add_item(map, 99)
    $ inventory.add_item(apple,99)
    $ inventory.add_item(apple,99)
    $ inventory.add_item(compass, 99)
    $ inventory.add_item(log, 99)
    $ inventory.add_item(mana_ram, 99)
    $ inventory.add_item(fish, 99)


    $ inventory.add_item(map, 99)
    $ inventory.add_item(apple,99)
    $ inventory.add_item(apple,99)
    $ inventory.add_item(compass, 99)
    $ inventory.add_item(log, 99)
    $ inventory.add_item(mana_ram, 99)
    $ inventory.add_item(fish, 99)


    $ inventory.add_item(map, 99)
    $ inventory.add_item(apple,99)
    $ inventory.add_item(apple,99)
    $ inventory.add_item(compass, 99)
    $ inventory.add_item(log, 99)
    $ inventory.add_item(mana_ram, 99)
    $ inventory.add_item(fish, 99)
 

    

    # Show the background image
    # $ game_time.advance_time(5)
   
    show forest
    
    # These display lines of dialogue.
    e "You've created a new Ren'Py game."
    e "Once you add a story, pictures, and music, you can release it to the world!"
    # This ends the game.
    $ inventory.remove_item(apple, 4)
    e "One item Removed."
    "Now you can chack the inventory"
  
    return
    
label Event1:
    "this is Event One"
 
return
 
label Event2:
    "this is Event two Block"
 
return