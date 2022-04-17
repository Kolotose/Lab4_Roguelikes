"""
The main code of the game 'The Rotten Heart'
"""

import TheRottenHeart_objects as objects
import time
import sys


# Initianting locations
town_hall_entrance = objects.Location("Головний Вхід")
town_hall_entrance.set_description(
"""Південна частина площі ринок.
По обидва боки входу сидять 2 кам'яні леви, які мали б захищати вхід.
Зараз вони також потерпали від цієї дивної \"прокази\"."""
)

fountain_neptune = objects.Location("Фонтан з Нептуном")
fountain_amphitrite = objects.Location("Фонтан з Амфітрітою")
fountain_diana = objects.Location("Фонтан з Діаною")
fountain_adonis = objects.Location("Фонтан з Адонісом")
monument_shevchenko = objects.Location("Пам'ятник Шевченку")
apothecary = objects.Location("Музей Аптека")
town_hall = objects.Location("Ратуша")

# Linking locations
town_hall_entrance.link_location(fountain_neptune, "захід")
town_hall_entrance.link_location(fountain_diana, "схід")
# town_hall_entrance.link_location(town_hall, "північ") # Will be linked later in game

fountain_neptune.link_location(monument_shevchenko, "захід")
fountain_neptune.link_location(fountain_amphitrite, "північ")
fountain_neptune.link_location(town_hall_entrance, "схід")

monument_shevchenko.link_location(fountain_neptune, "схід")

fountain_amphitrite.link_location(fountain_adonis, "схід")
fountain_amphitrite.link_location(fountain_neptune, "південь")

fountain_diana.link_location(town_hall_entrance, "захід")
fountain_diana.link_location(fountain_adonis, "північ")

fountain_adonis.link_location(apothecary, "схід")
fountain_adonis.link_location(fountain_diana, "південь")
fountain_adonis.link_location(fountain_amphitrite, "захід")

apothecary.link_location(fountain_adonis, "захід")

# town_hall.link_location(town_hall_entrance, "південь") # Will be linked later in game

# Initiating items
bandura = objects.Item("Бандура")
duma = objects.Item("Текст Думи")
the_gift = objects.Item("Подарунок Нептуна")
ocean_tear = objects.Item("Океанська Сльоза")
divine_waters = objects.Item("Божествені Води")
anemone = objects.Item("Анемона")
potion = objects.Item("Зілля")
bow_and_arrows = objects.Item("Лук та Стріли")

# Initiating allies
neptune = objects.Ally("Нептун")
diana = objects.Ally("Діана")
amphitrite = objects.Ally("Амфітріта")
adonis = objects.Ally("Адоніс")

# Initiating player
# player_name = input("Введи ім\'я персонажа:\n")
player_name = "[Ім'я]"
player = objects.Player(player_name)

current_location = town_hall_entrance

# Game cycle
while player.is_alive:

    print("\n")
    current_location.get_details()

    inhabitant = current_location.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_location.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["північ", "південь", "захід", "схід"]:
        # Move in the given direction
        current_location = current_location.move(command)
    elif command == "балакати":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "битися":
        pass
    elif command == "взяти":
        if item is not None:
            print(f"Ти поклав [{item.get_name()}] у свій наплічник")
            player.take(item)
            current_location.set_item(None)
        else:
            print("Наразі,предметів немає")
    elif command == "наплічник":
        if player.get_items_in_backpack():
            print(f"Ти маєш [{player.backpack_string}] у своєму наплічнику")
        else:
            print("Твій наплічник порожній")
    elif command == "вихід":
        print('Бувай!')
        sys.exit()
    else:
        print("Неможливо виконати " + command)
