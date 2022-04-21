"""
The main code of the game 'The Rotten Heart'
"""


import TheRottenHeart_objects as objects
import sys


commands_help = """[що?, шо?, поможіт] — всі команди
[північ, південь, захід, схід] — переміщення
[говорити, поговорити, побалакати] — поговорити зі статуєю
[битися, бій, битва] — битва з ворогом
[взяти] — взяти предмет в інвентар
[наплічник, інвентар] — переглянути предмети в наплічнику
[вихід, вийти] — вийти з гри"""


def talk(ally: objects.Ally, player: objects.Player):
    """
    ALL OF THE DIALOGUES with every character are
    in this function, because i really didn`t come up
    with the better way to do the thing i want to do
    """
    print(ally.get_name(), ally.get_reputation())
    if ally == neptune:
        if ally.get_reputation() == 0:
            print("[Нептун]: Іди геть! Я в поганому настрої.")
            ally.increace_reputation()

        elif ally.get_reputation() == 1:
            if bandura in player.get_items_in_backpack() and\
               duma in player.get_items_in_backpack():
                print("*Ти граєш на бандурі, проговорюючи речитативом нещодавно знайдену думу*")
                print("[Нептун]:")
                print("replica")

                ally.increace_reputation()
                prize = ally.take_item()
                player.take(prize)
            else:
                print("[Нептун]: Я тобі ще раз повторюю! Іди геть!")

        elif ally.get_reputation() == 2:
            if ocean_tear in player.get_items_in_backpack():
                print("[Нептун]:")

                ally.increace_reputation()
                player.use_item(ocean_tear)
                prize = ally.take_item()
                player.take(prize)

        else:
            print("[Нептун]: Наступного разу, подарую їй намисто з цієї сльози.")

    elif ally == amphitrite:
        if ally.get_reputation() == 0:
            print("[Амфітріта]:")

        if the_gift in player.get_items_in_backpack():
            print("Амфітріта]:")

            ally.increace_reputation()
            player.use_item(the_gift)
            prize = ally.take_item()
            player.take(prize)

        if ally.get_reputation() == 1:
            print("[Амфітріта]:")

    elif ally == adonis:
        if ally.get_reputation() == 0:
            print("[Адоніс]:")

        if divine_waters in player.get_items_in_backpack():
            print("[Адоніс]:")

            ally.increace_reputation()
            player.use_item(divine_waters)
            prize = ally.take_item()
            player.take(prize)

    elif ally == asclepius:
        if ally.get_reputation() == 0:
            print("[Асклепій]:")
            print("[Гігея]:")

        if anemone in player.get_items_in_backpack() and\
           flask in player.get_items_in_backpack():
            print("[Асклепій]:")
            print("[Гігея]:")

            ally.increace_reputation()
            player.use_item(anemone)
            player.use_item(flask)
            prize = ally.take_item()
            player.take(prize)

    elif ally == diana:
        pass


# Initiating items
bandura = objects.Item("Бандура")
bandura.set_description("")
duma = objects.Item("Текст Думи")
duma.set_description("")
the_gift = objects.Item("Подарунок Нептуна")
the_gift.set_description("")
ocean_tear = objects.Item("Океанська Сльоза")
ocean_tear.set_description("")
divine_waters = objects.Item("Божествені Води")
divine_waters.set_description("")
anemone = objects.Item("Анемона")
anemone.set_description("")
flask = objects.Item("Скляна Колба")
flask.set_description("")
potion = objects.Item("Зілля")
potion.set_description("")
bow_and_arrows = objects.Item("Лук та Стріли")
bow_and_arrows.set_description("")


# Initiating allies
neptune = objects.Ally("Нептун")
neptune.set_description("")
neptune.add_item(the_gift)
neptune.add_item(divine_waters)

diana = objects.SpecialAlly("Діана")
diana.set_description("")
diana.add_item(bow_and_arrows)

amphitrite = objects.Ally("Амфітріта")
amphitrite.set_description("")
amphitrite.add_item(ocean_tear)

adonis = objects.Ally("Адоніс")
adonis.set_description("")
adonis.add_item(anemone)

asclepius = objects.Ally("Асклепій та Гігея")
asclepius.set_description("")
asclepius.add_item(potion)


# Initiation enemies
ancestors = objects.Enemy("Незабуті Предки")
ancestors.set_description("")
ancestors.add_item(duma)

fungus = objects.Enemy("Багряний Грибок")
fungus.set_description("")
fungus.set_weakness(potion)

the_heart = objects.Enemy("Гнійне Серце")
the_heart.set_description("")
the_heart.set_weakness(bow_and_arrows)


# Initianting locations
town_hall_entrance = objects.Location("Головний Вхід")
town_hall_entrance.set_description(
"""Південна частина площі ринок.
По обидва боки входу сидять 2 кам'яні леви, які мали б захищати вхід.
Зараз вони також потерпають від цієї дивної \"прокази\"."""
)
town_hall_entrance.set_entity(fungus)

fountain_neptune = objects.Location("Фонтан з Нептуном")
fountain_neptune.set_description("")
fountain_neptune.set_entity(neptune)

fountain_amphitrite = objects.Location("Фонтан з Амфітрітою")
fountain_amphitrite.set_description("")
fountain_amphitrite.set_entity(amphitrite)

fountain_diana = objects.Location("Фонтан з Діаною")
fountain_diana.set_description("")
fountain_diana.set_entity(diana)

fountain_adonis = objects.Location("Фонтан з Адонісом")
fountain_adonis.set_description("")
fountain_adonis.set_entity(adonis)

monument_shevchenko = objects.Location("Пам'ятник Шевченку")
monument_shevchenko.set_description("")
monument_shevchenko.set_item(bandura)
monument_shevchenko.set_entity(ancestors)

apothecary = objects.Location("Аптека «Під Чорним Орлом»")
apothecary.set_description("")
apothecary.set_item(flask)
apothecary.set_entity(asclepius)

town_hall = objects.Location("Ратуша")
town_hall.set_description("")


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

# Initiating player
player = objects.Player()
current_location = town_hall_entrance

# Game cycle
while player.is_alive():
    # Linking town hall after fungus death
    if town_hall._connections == {} and \
        fungus.get_alive() == False:
        town_hall_entrance.link_location(town_hall, "північ")
        town_hall.link_location(town_hall_entrance, "південь")

    # C*losing apothecary, when the potion is ready
    if potion in player.get_items_in_backpack() and\
       current_location != apothecary:
        apothecary.unlink_location("Захід")
        fountain_adonis.unlink_location("Схід")

    print("\n")
    current_location.get_details()

    entity = current_location.get_entity()
    if entity is not None:
        entity.describe()

    item = current_location.get_item()
    if item != None:
        item.describe()

    print()
    command = input("> ")

    if command in ["північ", "південь", "захід", "схід"]:
        # Move in the given direction
        current_location = current_location.move(command)

    elif command == "поговорити" or\
         command == "побалакати" or\
         command == "говорити":
        # Talk to the entity - check whether there is one!
        if entity is not None and\
           isinstance(entity, objects.Ally):
            talk(entity, player)

    elif command == "битися" or\
         command == "бій" or\
         command == "битва":
        if entity is not None and\
           isinstance(entity, objects.Enemy):
            # Fight with the entity, if there is one
            if entity.get_weakness() == None or\
               entity.get_weakness() in player.get_items_in_backpack():
                if entity.get_weakness() != None:
                    print(f"Ти використовуєш [{entity.get_weakness()}] для битви")
                if entity.fight() == True:
                    # What happens if you win?
                    print("Ти переміг " + entity.get_name())
                    prize = entity.take_item()
                    if prize != None:
                        player.take(prize)
                        print(f"З {entity.get_name()} випав предмет [{prize.get_name()}]")
                    current_location.set_entity(None)

                else:
                    # What happens if you lose?
                    print("Ти був надто повільним і програв бій. Твій труп приєднається до гниючої купи інших.")
                    print("А тим часом, ратуша чекатиме нового випадкового \"героя\".")
                    print("Але, наразі це кінець")
                    player.death()
            else:
                print(f'У тебе немає [{entity.get_weakness().get_name()}]')
        else:
            print("Тут ні з ким битися")

    elif command == "взяти":
        if item is not None:
            player.take(item)
            current_location.remove_item()
        else:
            print("Наразі, предметів немає")

    elif command == "наплічник" or\
         command == "інвентар":
        if player.get_items_in_backpack():
            print(f"Ти маєш [{player.backpack_string()}] у своєму наплічнику")
        else:
            print("Твій наплічник порожній")

    elif command == "вихід" or\
         command == "вийти":
        print('Бувай!')
        sys.exit()

    elif command.lower() == "шо?" or\
         command.lower() == "що?" or\
         command.lower() == "поможіт":
        print(commands_help)

    else:
        print("Неможливо виконати " + command)
