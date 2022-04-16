"""
The main code of the game 'The Rotten Heart'
"""

import TheRottenHeart_objects as objects
import time


town_hall_entrance = objects.Location("Головний Вхід")
town_hall_entrance.set_description(
"""Південна частина площі ринок.
По обидва боки входу сидять 2 кам'яні леви, які мали б захищати вхід.
Зараз вони також під ефектом цієї дивної прокази."""
)

fountain_neptune = objects.Location("Фонтан з Нептуном")

fountain_amphitrite = objects.Location("Фонтан з Амфітрітою")

fountain_diana = objects.Location("Фонтан з Діаною")

fountain_adonis = objects.Location("Фонтан з Адонісом")

monument_shevchenko = objects.Location("Пам'ятник Шевченку")

apothecary = objects.Location("Музей Аптека")

town_hall = objects.Location("Ратуша")

town_hall_entrance.link_location(fountain_neptune)
town_hall_entrance.link_location(fountain_diana)
# town_hall_entrance.link_location(town_hall) # Will be linked later in game

fountain_neptune.link_location(town_hall_entrance)
fountain_neptune.link_location(monument_shevchenko)
fountain_neptune.link_location(fountain_amphitrite)

monument_shevchenko.link_location(fountain_neptune)

fountain_amphitrite.link_location(fountain_adonis)
fountain_amphitrite.link_location(fountain_neptune)

fountain_diana.link_location(town_hall_entrance)
fountain_diana.link_location(fountain_adonis)

fountain_adonis.link_location(fountain_amphitrite)
fountain_adonis.link_location(fountain_diana)
fountain_adonis.link_location(apothecary)

# town_hall.link_location(town_hall_entrance) # Will be linked later in game
