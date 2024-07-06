init -750 python:

    # Because Inventory is created with the help of
    # the "default" statement, we can't interact with it during the init phase.

    # Because of that, we'll prepare this function to insert all
    # the example items, and add it to a callback so it gets automatically
    # ran when the game starts.

    def add_inv_examples():

        # Usables = Food
        inventory.add(apple, count = renpy.random.randint(1, 7))
        inventory.add(chicken, count = renpy.random.randint(1, 7))
        
        # Equippables = Armor
        # inventory.add(leather_novice, count = 5) # rarity = random
        # inventory.add(leather_veteran, count = 2)

    def reset_inventory():
        inventory.clear()
        add_inv_examples()

    if add_inv_examples not in config.start_callbacks:
        config.start_callbacks.append(reset_inventory)