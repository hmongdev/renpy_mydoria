# rarity chances
# 50% common:           rarity <= 50
# 25% uncommon:         51 < rarity < 75
# 13% rare:             76 < rarity < 89 
# 9% mythic:           90 < rarity < 98
# 3% legendary:         98 < rarity < 100

# armor bonus
# common = 1-3
# uncommon = 4-9
# rare = 10-24
# mythic = 25-37
# legendary = 49-99

# will be reused for armors, weapons, etc.

init -880 python:
    # Class Definition
    class Armor(Item):

        # Class Attributes
        equippable = True
        stackable = True
        usable = False
        consumed_on_use = False
        consumed_on_unequip = False

        # Initializer Method
        def __init__(self, name, kind, desc):
            self.name = name
            self.kind = kind
            self.description = desc
            self.rarity = None
            self.image = ""
            
            # Assign rarity based on a random number
            rarity_roll = renpy.random.randint(1, 100)
            if rarity_roll <= 50:  
                self.rarity = "common"      # 50% chance for common
            elif 51 <= rarity_roll <= 75:   # 25% chance for uncommon
                self.rarity = "uncommon"
            elif 76 <= rarity_roll <= 89:   # 13% chance for rare
                self.rarity = "rare"
            elif 90 <= rarity_roll <= 98:   # 9% chance for mythic
                self.rarity = "mythic"
            else:  
                self.rarity = "legendary"   # 3% chance for legendary
            
            rarity = self.rarity
            # Images for the Item and Card
            self.item_image = f"/images/armor/{name}.png"
            self.card_image = f"/images/armor/{name}.png"
            self.bg = f'/gui/inventory/item {self.rarity}.png'

        
default leather_novice = Armor(
    "Novice Leather",
    "Armor",
    "Perfect for adventurers who need to be quick and nimble.",
)

default leather_veteran = Armor(
    "Veteran Leather",
    "Armor",
    "Perfect for skilled adventurers.",
)

default leather_master = Armor(
    "Master Leather",
    "Armor",
    "Only the masters can wear this.",
)