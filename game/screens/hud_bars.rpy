###########################################
# Bars Screen
###########################################
screen hud_bars():
    vbox:
        align(0.065, 0.02)
        hbox:
            bar:
                value AnimatedValue(player_hp, player_hp_max, delay=0.5)
                left_bar "/gui/hud/health full.png" # full
                right_bar "/gui/hud/health empty.png" # empty
                maximum(maxHP, ymaximum) # this controls the width of the health bar
                # thumb None
                # thumb_shadow None
                # thumb_offset 30
            text "[player_hp]/[player_hp_max]" size 25 yalign(0.5) xpos(-1.15)
        hbox:
            bar:
                value AnimatedValue(player_mp, player_mp_max, delay=0.5)
                left_bar "/gui/hud/mana full.png" # full
                right_bar "/gui/hud/health empty.png" # empty
                maximum(maxMP, ymaximum) # this controls the width of the health bar
                # thumb None
                # thumb_shadow None
                # thumb_offset 30
            text "[player_mp]/[player_mp_max]" size 25 yalign(0.5) xpos(-1.15)