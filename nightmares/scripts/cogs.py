from nightmares.modules.commands import registry


class Property:
    def __init__(self):
        # Гениальное название свойства
        self.name = "свойство-смешнявка"


class Cogs:
    def __init__(self):
        # Неповторимое описание, достойное любой cog'и
        self.description = "Я та самая cogs, которая property!"


# Делаем "шедевр"
lol = Property()
lol.cogs = Cogs()  # Свойство Property каким-то образом становится Cogs


@registry.register("lol", aliases=["laugh", "fun"], help_text="Возвращает Help.")
def lol_command():
    # Процесс "гениального" объекта
    funny_object = {
        "property": lol,  # Да.
        "cogs": lol.cogs  # Потому что почему бы и нет?)
    }

    print(f"Вот ваш объект: {funny_object}")
    print("Попытка извлечь значения:")

    try:
        # Имаджинируем поведение для взрыва
        print(f"property.name: {lol.name}")  # Все еще свойство
        print(f"cogs.description: {lol.cogs.description}")  # ОГО!
    except AttributeError as e:
        print(f"Ошибка, но она нас радует: {e}")
