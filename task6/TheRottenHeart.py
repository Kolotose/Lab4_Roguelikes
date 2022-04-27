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
    print()
    if ally == neptune:
        if ally.get_reputation() == 0:
            print("[Нептун]: Іди геть!")
            ally.increace_reputation()

        elif ally.get_reputation() == 1:
            if bandura in player.get_items_in_backpack() and\
               duma in player.get_items_in_backpack():
                print("*Ти граєш на бандурі, проговорюючи речитативом нещодавно знайдену думу*")
                print("[Нептун]: Чудово граєш. Мущу визнати, ти трохи підняв мій натрій.")
                print("В такому випадку, якщо ти вже тут. Віднеси цей пакунок моїй коханій Амфітріті.")
                print()

                ally.increace_reputation()
                prize = ally.take_item()
                player.take(prize)
            else:
                print("[Нептун]: Я тобі ще раз повторюю! Іди геть!")

        elif ally.get_reputation() == 2:
            if ocean_tear in player.get_items_in_backpack():
                print("[Нептун]: Вона отримала мій подарунок? Це її сльоза? Неймовірно!")
                print("Дуже дякую за твою роботу. Впевнений, Океанські Води тобі знадобляться.")

                ally.increace_reputation()
                player.use_item(ocean_tear)
                prize = ally.take_item()
                player.take(prize)

        else:
            print("[Нептун]: Наступного разу, подарую їй намисто з цієї сльози.")

    elif ally == amphitrite:
        if ally.get_reputation() == 0:
            print("[Амфітріта]: Який чудовий день! Чи не так, сонечку?\n")

        if the_gift in player.get_items_in_backpack():
            print("[Амфітріта]: Це від мого чоловіка? Ох... Коли ж він мене полишить у спокої.")
            print("Якби ж я тоді не погодилася, й залишилася там... Горе мені, бути навіки з ним...")

            ally.increace_reputation()
            player.use_item(the_gift)
            prize = ally.take_item()
            player.take(prize)

        elif ally.get_reputation() == 1:
            print("[Амфітріта]: Не хвилюйся. Ти тут ні до чого. Дарма він тебе вплутав.")

    elif ally == adonis:
        if ally.get_reputation() == 0:
            print("[Адоніс]: Яка краса! Але треба відновити сили. На підтримку цього саду їх йде багато.\n")

        if divine_waters in player.get_items_in_backpack() and\
            ally.get_reputation() == 0:
            print("[Адоніс]: Божествені Води? Величезна подяка! Мені вистачить лише частини з цього.")
            print("*Він оприскує себе Водами, залишаючи близько половини вмісту. В ту ж мить, на його тілі")
            print("виростає квітка анемони, яку він зриває, і віддає тобі.")
            print("[Адоніс]: Тримай. Це в додачу до подяки. Не залишу ж я тебе з порожніми руками.")

            ally.increace_reputation()
            prize = ally.take_item()
            player.take(prize)

        elif ally.get_reputation() == 1:
            print("[Адоніс]: Як тобі мій сад? Краса...")

    elif ally == asclepius:
        if ally.get_reputation() == 0:
            print("[Асклепій]: Нам треба знищити цю заразу. Доню, що в тебе?")
            print("[Гігея]: Нічого. Нам не вистачає інгредієнтів.\n")

        if anemone in player.get_items_in_backpack() and\
           flask in player.get_items_in_backpack():
            print("[Гігея]: Анемона й Божествені води! Саме те що треба! Люд врятований!")
            print("[Асклепій]: Не кажи гоп. Благаю. Треба ще знайти когось, хто переможе Гнійне Серце...")

            ally.increace_reputation()
            player.use_item(flask)
            player.use_item(divine_waters)
            player.use_item(anemone)
            prize = ally.take_item()
            player.take(prize)

            print("\n*Під кінець процесу варки Зілля, із сусідньої кімнати виривається міцелій і починає трощити усе, що є на полицях*")
            print("[Гігея]: Тримай зілля і тікай! Ти наша остання надія! БАТЬКУ!")
            print("*Ти вибігаєш із будівлі. Гігея гучно грюкає дверима за твоєю спиною. В наступний момент, всі вікна вкриваються цим жахливим грибком.*")

    elif ally == diana:
        if ally.get_reputation() == 0:
            print("[Діана]: О! Смертна душа! Перевіримо що ти можеш!")
            print("Я викликаю тебе на поєдинок! І ти не маєш права відмовити.")
            print("Почнемо, коли будеш готовий.\n")

            input("[Щоб продовжити натисни Enter]")
            duel_win = ally.fight()
            ally.increace_reputation()
            if duel_win:
                print("[Діана]: Хоча я й не билася у повну силу, але ти був неслабким опонентом. Так тримати!")

                ally.increace_reputation()
                prize = ally.take_item()
                player.take(prize)

            else:
                print("[Діана]: Не впадай у відчай. Приходь іще раз. Стояти тут весь день все одно нудно.")

        elif ally.get_reputation() == 1:
            print("[Діана]: Хочеш реванш? Чудно!\n")
            input("[Щоб продовжити натисни Enter]\n")


            duel_win = ally.fight()
            if duel_win:
                print("[Діана]: Хоча я й не билася у повну силу, але ти був неслабким опонентом. Так тримати!")

                ally.increace_reputation()
                prize = ally.take_item()
                player.take(prize)

            else:
                print("[Діана]: Не впадай у відчай. Приходь іще раз. Стояти тут весь день все одно нудно.")

        else: #reputation == 2
            print("[Діана]: Цей лук точно у надійних руках.")

def print_win():
    """
    Prints the winning message of the game
    """
    print('\n')
    print("Гнійне Серце вбите! Воно з глухим але гучним грюкітом падає на підлогу. Уся гниль починає зсихатися.")
    print("Протягом наступних кількох хвилин ти гордо й зачаровано спостерігаєш за тим, як ця зараза стрімко")
    print("перетворюється в купи пилу та попелу. До тебе ззаду підійшла золота пані, та вручає тобі кошичок з купою карамельних")
    print("півників. Ти з кам'яним лицем дивишся на неї, але вирішуєш що краще нічого не казати й просто подякувати.")
    print("Це грандіозна перемога!")


# Initiating items
bandura = objects.Item("Бандура")
bandura.set_description("зроблена з незвичайно липи. На ній не вистарчає деяких струн, але грати все ще можна.")
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
flask.set_description("колба з надколотою шийкою. Може знадобитися для якогось варива.")
potion = objects.Item("Зілля")
potion.set_description("")
bow_and_arrows = objects.Item("Лук та Стріли")
bow_and_arrows.set_description("")


# Initiating allies
neptune = objects.Ally("Нептун")
neptune.set_description("Бог морів та океанів. Він очевидно чимось стривожений.")
neptune.add_item(the_gift)
neptune.add_item(divine_waters)

diana = objects.SpecialAlly("Діана")
diana.set_description(
"""Вічноцнотлива богиня полювання. Інколи цілить зі свого лука
по пухлинах грибка, але багато веселощів це не приносить."""
)
diana.add_item(bow_and_arrows)

amphitrite = objects.Ally("Амфітріта")
amphitrite.set_description("Морська богиня, дружина Нептуна. Попри небажаний шлюб, вона не виглядає нещасною.")
amphitrite.add_item(ocean_tear)

adonis = objects.Ally("Адоніс")
adonis.set_description("Неймовірної краси парубок, що є напіврослиною. Хіба не кабан убив його?")
adonis.add_item(anemone)

asclepius = objects.Ally("Асклепій та Гігея")
asclepius.set_description(
"""Батько й донька, які завдяки своїм медичним знанням були богами здоро'я та медицини.
Вони єдині, крім пані з парасолькою, хто виглядає стурбованим що до розрісшогося грибка."""
)
asclepius.add_item(potion)


# Initiation enemies
ancestors = objects.Enemy("Незабуті Предки")
ancestors.set_description(
"""Тіні минулого, які різко озлобилилися на народ.
Ймовірно, джерело цього жаху є спільним із грибком на дверях Ратуші."""
)
ancestors.add_item(duma)

fungus = objects.Enemy("Багряний Грибок")
fungus.set_description("Гидка маса, вкрита темними пухлинами й від якою тягнуться тонкі капілярчики міцелію.")
fungus.set_weakness(potion)

the_heart = objects.Enemy("Гнійне Серце")
the_heart.set_description(
"""Джерело цього жаху, що звисає з вершини ратуші на бридкій подобі
кровоносних судин. Так просто до нього не підійти."""
)
the_heart.set_weakness(bow_and_arrows)


# Initianting locations
town_hall_entrance = objects.Location("Головний Вхід")
town_hall_entrance.set_description(
"""Південна частина площі Ринок.
Ти зараз навпроти ратуші. По обидва боки входу сидять 2 кам'яні леви, які мали
б захищати його. Зараз вони також потерпають від цієї дивної \"прокази\".
На колії, що проходить крізь площу, стоїть золота пані з парасолькою."""
)
town_hall_entrance.set_entity(fungus)

fountain_neptune = objects.Location("Фонтан з Нептуном")
fountain_neptune.set_description(
"""Південно-західна частина площі Ринок.
Тут стоїть фонтан Нептуна, з вірним дельфіном біля ніг — створінням,
яке й допомогло вмовити Амфітріту вийти заміж за бога морів та океанів.
Темний міцелій грибка тріщинами обвивав один з бортів фонтану."""
)
fountain_neptune.set_entity(neptune)

fountain_amphitrite = objects.Location("Фонтан з Амфітрітою")
fountain_amphitrite.set_description(
"""Північно-західна частина площі Ринок.
Тут стоїть фонтан Амфітріти. Коли Нептун захотів одружитися на богині,
вона, бажаючи зберегти свою цноту, втекла у Атлаські гори.
В цій частині площі, грибок практично не розрісся."""
)
fountain_amphitrite.set_entity(amphitrite)

fountain_diana = objects.Location("Фонтан з Діаною")
fountain_diana.set_description(
"""Південно-східна частина площі Ринок.
Тут стоїть фонтан Діани. А по обидва боки від неї — дві мисливські собаки.
Де-інде видно темні калюжі, що були залишені луснутими пухлинами грибка."""
)
fountain_diana.set_entity(diana)

fountain_adonis = objects.Location("Фонтан з Адонісом")
fountain_adonis.set_description(
"""Північно-східна частина площі Ринок.
Тут стоїть фонтан Адоніса. Біля нього сидить собака, й лежить мертвий
насланий Персефоною кабан, якого він усе-таки зміг перемогти.
У цій частині площі грибок має достатньо дивний вигляд: чим ближче він до
Адоніса, тим більше на ньому дивних квітів, які віддалено нагадують троянди"""
)
fountain_adonis.set_entity(adonis)

monument_shevchenko = objects.Location("Пам'ятник Шевченку")
monument_shevchenko.set_description(
"""Ти вийшов на проспект Свободи.
Тут простягається головна алея Львова, на якій в даличині видно театр опери та балету.
Зараз тут надзвичайно тихо, що контрастує з тим, як тут зазвичай.
Прямо перед тобою височіє \"Хвиля національного відродження\", праворуч
від якої стоїть Шевченко. Навколо хвилі, витає шторм із тіней."""
)
monument_shevchenko.set_item(bandura)
monument_shevchenko.set_entity(ancestors)

apothecary = objects.Location("Аптека «Під Чорним Орлом»")
apothecary.set_description(
"""На розі площі ринок ти увійшов у аптеку.
У світлій залі попід стін стоять шафи з величезною кількістю різних пляшечок та посудин.
Під стелею зображені чотири медальйони, кожен з яких символізує праелементи всесвіту:
Вогонь, Вода, Земля та Повітря. З дальніх зал тягнеться дивний сирий сморід. 
Звідти ж повзуть чорні тріщини міцелію. В одному з кутів головної кімнати стоять терези
чаші яких тримають Асклепій та Гігея."""
)
apothecary.set_item(flask)
apothecary.set_entity(asclepius)

town_hall = objects.Location("Ратуша")
town_hall.set_description(
"""Серце міста. Центр усіх подій. Ядро усього жаху.
Усюди чорний міцелій, товщина якого інколи більша ніж обхват людської руки.
Він пульсує від протікаючої всередині рідини. Чути віддалене тікання механічного
годинника, на яке накладається глухе биття серця, що звисає по центру зали."""
)
town_hall.set_entity(the_heart)


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

# Starting Game
print(
"""Вийшовши з трамваю на площі Ринок ти помічаєш дві дещо дивні речі: 
якийсь сирий терпкий дивний запах, що стоїть на площі, і те, що у практично найгучнішому місці Львова
не видно ані душі, окрім золотої пані, яка з жахом дивиться на ратушу. Лише тоді ти бачиш у чому справа.
Уся ратуша вкрита багряно-чорним грибком, що пульсує і переливається. Ти підходиш до пані, щоби запитатися,
що сталося, але вона тебе випереджає.
[Золота Пані]: Боже! Як добре, що Ви приїхали! Розумієте, тут невеличка... Кого я обманюю..? Тут проблема
неймовірних масштабів! Величезна кількість людей постраждали через цей дивний грибок. Я дуже сподіваюся,
що Ви зможете її вирішити. Правда? 
*Ти безнадійно киваєш головою*
[Золота Пані]: Дуже Вам дякую! Ви увійдете в міські легенди!
З цими словами вона повертається назад до ратуші, в ту саму позицію, що і раніше, перед діалогом.
Більше вона не скаже і слова."""
)

# Game cycle
while player.is_alive():
    # The ending of the game:
    if the_heart.get_alive() == False:
        print_win()
        break

    # Linking town hall after fungus death
    if fungus.get_alive() == False and\
       "північ" not in town_hall_entrance.get_connections().keys():
        town_hall_entrance.link_location(town_hall, "північ")
        town_hall.link_location(town_hall_entrance, "південь")

    # Closing apothecary, when the potion is ready
    if potion in player.get_items_in_backpack() and\
       "захід" in apothecary.get_connections().keys():
        current_location = fountain_adonis
        apothecary.unlink_location("захід")
        fountain_adonis.unlink_location("схід")

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
                    print(f"\nТи використовуєш [{entity.get_weakness().get_name()}] для битви")
                if entity.fight() == True:
                    # What happens if you win?
                    print("Ти перемагаєш " + entity.get_name())
                    prize = entity.take_item()
                    if prize != None:
                        print(f"З {entity.get_name()} випав предмет [{prize.get_name()}]")
                        player.take(prize)
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
