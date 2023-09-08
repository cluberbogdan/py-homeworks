class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    
    def __add__(self, other_country):
        new_name = f'{self.name} {other_country.name}'
        new_population = self.population + other_country.population
        return Country(new_name, new_population)
    

    def __str__(self) -> str:
        return f'{self.population}\n{self.name}'


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina

print(bosnia_herzegovina)