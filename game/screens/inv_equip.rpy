#########################
# Equip Screen
#########################
screen inv_equip():
    # Frame, without a background.
    frame:
        style_prefix "inventory_side_menu"
        style_suffix "frame" # Style: inventory_side_menu_frame

        vbox:
            style_suffix "vbox_equipped"

            if inv_settings.show_equipped_label:
                # Label
                text "Equipped Item:":
                    style_suffix "vbox_equipped_text" # Style: inventory_side_menu_vbox_equipped_text

            if inv_settings.show_equipped_slot:
                # Frame around the Slot.
                frame:
                    style_suffix "vbox_equipped_slot" # Style: inventory_side_menu_vbox_equipped_slot

                    # If there is an Equipped Item, create a marker around it.
                    # Makes more clear how the equipped item is marked in the Inventory slots.
                    # if inventory.equipped:
                    grid 2 2:
                        spacing 10
                        drag:
                            drag_name "chest"
                            align(0.0, 0.0)
                            add "/gui/inventory/equip empty.png" xysize(150, 150)
                            text "Chest" align((0.5, 0.5)) size 40 color "#000"
                        drag:
                            drag_name "hands"
                            align(1.0, 0.0)
                            add "/gui/inventory/equip empty.png" xysize(150, 150)
                            text "Hands" align((0.5, 0.5)) size 40 color "#000"
                        drag:
                            drag_name "legs"
                            align(0.0, 1.0)
                            add "/gui/inventory/equip empty.png" xysize(150, 150)
                            text "Legs" align((0.5, 0.5)) size 40 color "#000"
                        drag:
                            drag_name "feet"
                            align(1.0, 1.0)
                            add "/gui/inventory/equip empty.png" xysize(150, 150)
                            text "Feet" align((0.5, 0.5)) size 40 color "#000"
                
                    # this is the selected equipped image
                    # add inv_settings.slot_equip_empty align (0.5, 0.5)
                    # If there is an Equipped Item, add its Image in the middle.
                    if inventory.equipped:
                        add inventory.equipped_item.item_image:
                            align (0.5, 0.5)
                            xsize 150
                            fit "contain"
                    else:
                        # this is the empty equip image
                        add inv_settings.slot_equip_empty align (0.5, 0.5)