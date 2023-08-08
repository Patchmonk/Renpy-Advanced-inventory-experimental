# name of the character.
define e = Character("Eileen")
    
  
# Global currency
default gold = 1000
label start:
    show Forest
    # To set up the initial state of the inventory we have to create an instance of the inventory class
    $ inventory = Inventory()
    show screen HUD
    # To use the instance of the functions, you first need to create an instance of the Game_Time class. 
    # You can do this by calling the Game_Time() constructor, and passing in the current hour, day, month, and year. 
    # $ game_time = GameTime(year=2023, month=1, weekday=5, day=3, hour=12)

    # Add some initial items to the inventory
    $ map = Item(name="map", quantity=5)
    $ apple = Item(name="apple", quantity=3)
    $ inventory.add_item(map, 10)
    $ inventory.add_item(apple,5)

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