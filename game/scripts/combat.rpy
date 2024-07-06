default enemy_hp = 10

label combat:
    while player_hp > 0:

        # player turn

        menu:
            "Attack":
                $ enemy_hp -= 2
                if enemy_hp <= 0:
                    "You win combat!"
                    jump start
            "Flee":
                "You run away"
                return
        
        # enemy turn
        $ player_hp -= 2
        "The enemy makes an attack, reducing you to [player_hp]"

    "You died..."