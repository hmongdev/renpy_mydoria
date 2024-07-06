init -880 python:
    class Food(Item):
        equippable = False
        stackable = True
        usable = True
        consumed_on_use = True
        bg = '/gui/inventory/slot food.png'
        kind = "Food"

        def __init__(self, name, desc, item_image = None, card_image = None):
            self.name = name
            self.description = desc

            # Images for the Item and Card
            self.item_image = item_image
            self.card_image = card_image
            # self.count = renpy.random.randint(1, 7)

            self.check()

        def check(self):
            if self.stackable and self.equippable:
                raise Exception("Item Check failed: Equippable Items cannot be stackable - {} is.".format(self))

        ############################
        ## Checks
        ############################

        # Checks whether Item can be Equipped.
        def is_equippable(self):
            return self.equippable # False

        # Checks whether Item can be Used.
        def is_usable(self):
            return self.usable # True

        ############################
        ## Functions
        ############################

        # What happens when the Item is eaten.
        def used(self, Inventory):
            global player_hp
            global player_hp_max

            if player_hp >= player_hp_max:
                renpy.notify("You are full.")
            else:
                health_gained = renpy.random.randint(3, 7)
                player_hp = min(player_hp_max, player_hp + health_gained)
                renpy.play("/audio/food/eat food.ogg")
                renpy.notify(f"+{health_gained} health.")
        
default apple = Food(
    "Honeydrip Apples",
    "\"Legends say the seeds of this honeydrip were planted by Herona herself -- goddess of fertility and nature. Its juices are said to drip like honey and have rare healing properties.\"\n\n-Garibald, farmer of Honeydrip Orchards",
    "/images/food/apple item.png",
    "/images/food/apple card.png",
)

default chicken = Food (
    "Roasted Junglefowl",
    "Junglefowl, often mistaken for chickens, roam freely across the plains and savannas of Mydoria. You can find them hiding in shrubs, tall grass, or scurrying into bushes when approached. They make a delectable meal.",
    "/images/food/chicken item.png",
    "/images/food/chicken card.png",
)

        