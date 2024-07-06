init -890 python:
    class Item():

        "Base class for all the items."
        
        # This is the base class for Items, 
        # so it's neither usable nor equippable.
        usable = False
        equippable = False

        # Taken from inv_settings, default of whether
        # usable items get removed from the Inventory when used.
        consumed_on_use = inv_settings.consumed_on_use

        # Taken from inv_settings, default of whether
        # usable items get removed from the Inventory when used.
        consumed_on_unequip = inv_settings.consumed_on_unequip

        # Initialization. Arguments:
        #
        # name - String, name of the item.
        #
        # desc - Description of the item.
        #
        # image - Image of the Item. Can be a file,
        # a displayable, or the default None, which then
        # creates a Text Displayable from the name argument.
        #
        # stackable - True if the Item can stack, False if not.
        # If not given, default of None refers to inv_settings.defaultStack.
        # Only regular Items and Usable Items can be stackable, 
        # Equippable Items cannot.
        #
        # stack_size - How big this Item's stack can be.
        # Never brought up if stackable is False.
        #
        # What happens upon the definition.
        def __init__(self, name, desc, item_image = None, card_image = None): #stackable = None, stack_size = 1

            # Name of the Item.
            self.name = name

            # Description of the Item.
            self.description = desc
            
            # Images for the Item and Card
            if item_image:
                self.item_image = item_image
                
            if card_image:
                self.card_image = card_image
            
            if not item_image or not item_card:
                self.item_image = Text(name, size = 20)
                self.card_image = Text(name, size = 20)

            # Stackability
            if stackable != None:
                self.stackable = stackable
            # Default from inv_settings if not given.
            else:
                self.stackable = inv_settings.stackable
            
            # Max number of items in the stack.
            # if stack_size != None:
            #     self.stack_size = stack_size
            # # Default from inv_settings if not given.
            # else:
            #     self.stack_size = inv_settings.stack_size

            # Check for things that aren't allowed.
            self.check()

        # Checks for things that aren't allowed. Items:
        # - Cannot be both stackable and equippable.
        def check(self):
            if self.stackable and self.equippable:
                raise Exception("Item Check failed: Equippable Items cannot be stackable - {} is.".format(self))

        ############################
        ## Checks
        ############################

        # Used by the Inventory screen, whether Item can be Equipped.
        def is_equippable(self):

            return self.equippable

        # Used by the Inventory screen, whether Item can be Used.
        def is_usable(self):

            return self.usable

        ############################
        ## These do nothing by default, and are to be overwritten
        ## when you create your own usable and equippable Items.
        ############################
        
        # What happens when the Item is used.
        def used(self, Inventory):
            return None 

        # What happens when the Item is Equipped.
        def equipped(self, Inventory):
            return None 

        # What happens when the Item is Unequipped.
        def unequipped(self, Inventory):
            return None

        # What happens when the Item is Discarded.
        def discarded(self, Inventory):
            renpy.play("/audio/hud/discard.ogg")
            return None