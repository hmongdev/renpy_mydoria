python:
    class LeatherLight(Item):
        equippable = True

        def equipped(self, Inventory):
            
            return renpy.notify("Leather Light has been equipped.")