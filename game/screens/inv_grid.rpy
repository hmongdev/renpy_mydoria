# Inventory Grid
screen inv_grid():
    grid inventory.width inventory.height:
        style_suffix "slots_grid"

        # Slot
        for index, item in enumerate( inventory.get_page_items() ):
            button:
                style_suffix "slot"
                # TODO: diff bg based on the item
                background item.bg

                # selected slot image
                if inventory.is_selected(item):
                    add inv_settings.slot_full_selected align (0.5, 0.5)

                # Checks whether given item is currently selected.
                selected inventory.is_selected(item)

                # Selects an Item.
                action Function(inventory.select, item)
                
                # Image of the Item inside the Slot
                add item.item_image:
                    align (0.5, 0.5)
                    xsize 120
                    fit "contain"
                
                # # Item Stack Count
                $ item_count = inventory.get_item_count(item)
                if item_count < 1:
                    $ item_count = ""
                else:
                    text "{size=30}x{/size}" + str(item_count):
                        style_suffix "slot_text"
                    
        # .get_empty_cells() fetches the number of cells that have
        # been left empty on a non-full page and fills them with empty space.
        #
        # This is necessary because Ren'Py requires grids to have all cells filled.
        for x in range( inventory.get_empty_cells() ):
            # One Empty Slot.
            # Also has a background to function as a frame around the "item".
            button:
                style_suffix "slot_empty" # Style: inventory_slot_empty                    
                # Unselects the selected item.
                action Function( inventory.unselect )

#########################
# Inventory Card
#########################
screen inv_card():
    vbox:
        align 0.55, .5
        frame:
            style_prefix "inventory_card"
            style_suffix "frame"

            # equip, use, discard buttons
            frame:
                style_suffix 'frame_image'
                if inventory.selected_item:
                    add inventory.selected_item.card_image:
                        xsize 480
                        fit "contain"
        
            # Item Name, Kind, Description
            if inv_settings.show_description:
                # Name
                text ( inventory.selected.name if inventory.selected else "Select an item..." ):
                    style_suffix "name" # Style: inventory_side_menu_name

                # Kind
                text ( inventory.selected.kind if inventory.selected else "???" ):
                    style_suffix "kind"
                # text (inventory.selected.name + inventory.selected.rarity if inventory.selected.kind = "Armor")

                frame:
                    style_suffix "frame_description"
                    # Description.
                    text ( inventory.selected.description if inventory.selected else "To read its description." ):
                        style_suffix "description" # Style: inventory_side_menu_description
        use inv_buttons()

#########################
# Equip Screen
#########################
    use inv_equip()