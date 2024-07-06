screen inv_buttons():
    frame:
        style_prefix "inventory_buttons"
        style_suffix "frame"
        # A horizontal box. This one contains:
        hbox:
            style_suffix "equip_box" # Style: inventory_side_menu_vbox_interaction_equip_box
            # DISCARD BTN
            if inv_settings.show_throw_away_button:
                # The Throw Away button.
                textbutton "Discard":

                    style_suffix "discard_textbutton" # Style: inventory_side_menu_vbox_interaction_discard_textbutton

                    # Can be clicked if an item is Selected.
                    sensitive inventory.selected
                    action Function(inventory.discard)

            # EQUIP BTN
            if inv_settings.show_equip_button:
                # Checks whether the player can Unequip an item.
                # This means that NOT ONLY does an item have to be equipped,
                # that same item also has to in a selected slot.

                # The Unequip button (If Equip is hidden)
                if inventory.can_unequip():
                    textbutton "Unequip":
                        style_suffix "unequip_textbutton" # Style: inventory_side_menu_vbox_interaction_unequip_textbutton
                        action Function(inventory.unequip)

                # The Equip button (If Unequip is hidden)
                # If you can't Unequip stuff, automatically show the Equip button.
                else:
                    textbutton "Equip": 
                        style_suffix "equip_textbutton"
                        # .can_equip() decides whether you can actually click the button.
                        # Depends on whether an Equippable is Selected.
                        sensitive inventory.can_equip()
                        action Function(inventory.equip)

            # USE BTN
            if inv_settings.show_use_button:
                # Either way, the Use button is shown.
                textbutton "Use":
                    style_suffix "use_textbutton" # Style: inventory_side_menu_vbox_interaction_use_textbutton
                    
                    # .can_use() decides whether you can click this button,
                    # and this one depends on the Item being Usable. 
                    sensitive inventory.can_use()
                    action Function(inventory.use)
            textbutton "Add Armor":
                style_suffix "use_textbutton"
                action Function(inventory.add, leather_novice) # rarity = random)
