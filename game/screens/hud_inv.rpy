default player_hp_max = 100
default player_mp_max = 100
default player_hp = 100
default player_mp = player_mp_max

default maxHP = player_hp_max
default maxMP = player_mp_max
default ymaximum = 5

###########################################
# Player HUD
###########################################
screen hud_inv():
    use hud_gold()
    use hud_bars()
    
    # open player inventory + drag items
    drag:
        align(0, 1.0)
        drag_raise False
        draggable False
        droppable True
        dropped add_item
        imagebutton:
            auto "/gui/hud/bag %s.png"
            action [Play("sound", "/audio/hud/inv open.ogg"),ToggleScreen("hud_inv"), Show("inv_player")]
            at transform:
                xysize(150, 150)