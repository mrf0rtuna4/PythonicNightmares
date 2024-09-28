from nightmares.modules.commands import registry

class Property:
    def __init__(self):
        self.name = "property"

class Cogs:
    def __init__(self):
        self.description = "Я - шестеренка (da-da), делающая шестеренки!"

@registry.register("lol", aliases=["laugh", "fun"], help_text="Возвращает Help.")
def lol_command():
    property_instance = Property()
    cogs_instance = Cogs()
    funny_object = {
        "property": property_instance,
        "cogs": cogs_instance
    }
    
    print(f"Вот ваш объект: {{'property': {property_instance}, 'cogs': {cogs_instance}}}")
    print("Попытка извлечь значения:")
    print(f"property.name: {property_instance.name}")
    print(f"cogs.description: {cogs_instance.description}")