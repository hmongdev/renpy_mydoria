default armor_list = ['iron l', 'iron m', 'iron h']

init python:
    def add_item(player_inventory, dragged_item):
        global inventory
        item_name = dragged_item[0].drag_name  # Access the drag_name attribute directly
        print(f"{item_name} has been added to your inventory")

        # adds item to inventory
        inventory.add(item_name)
        
        # removes drag from screen
        dragged_item[0].set_child(Null())

    def say_hello(dragged_item, dropped_on):
        item_name = dragged_item[0].drag_name
        print(f"{item_name} is the dragged item")

screen env_items():
    for armor in armor_list:
        drag:
            align(0.5, 0.5)
            drag_name armor
            # dragged say_hello
            drag_raise True
            add f"/images/armor/{armor}.png" xysize(200,200)  # Use the current armor name
