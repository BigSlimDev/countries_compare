# country
class Countries:
    def __init__(self,name, capital, currency, language, population, rigion, time_zone):
        self.name = name
        self.capital = capital
        self.currency = currency
        self.language = language
        self.population =population
        self.rigion = rigion
        self.time_zone = time_zone
    
    def country_info(self):
        print("\nCountry Profile\n")
        print(f"Name: {self.name}")
        print(f"Capital: {self.capital}")
        print(f"Currency: {self.currency}")
        print(f"Language: {self.language}")
        print(f"Population: {self.population}")
        print(f"Timezone: {self.time_zone}")

    def save_profile(self):
        with open("country_profiles.txt", "a") as file:
            file.write(
                f"{self.name}, {self.capital}, "
                f"{self.currency},{self.language},"
                f"{self.population},"
                f"{self.time_zone}\n")
         


# compare country

class CountryComparator:

    def compare(self, country1, country2):

        print(f"\n{country1.name} vs {country2.name}")
        print(f"Capital: {country1.capital} vs {country2.capital}")
        print(f"Currency: {country1.currency} vs {country2.currency}")
        print(f"Language: {country1.language} vs {country2.language}")
        print(f"Population: {country1.population} vs {country2.population}")
        print(f"Time_zone: {country1.time_zone} vs {country2.time_zone}")

        with open("comparison_results.txt", "a") as file:
            file.write(f"\n{country1.name} vs {country2.name}\n")
            file.write(f"Capital: {country1.capital} vs {country2.capital}\n")
            file.write(f"Currency: {country1.currency} vs {country2.currency}\n")
            file.write(f"Language: {country1.language} vs {country2.language}")
            file.write(f"Population: {country1.population} vs {country2.population}")
            file.write(f"Time_Zone: {country1.time_zone} vs {country2.time_zone}")





nigeria = Countries(
    "Nigeria", "Abuja", "Naira",
    "English", 223000000,
    "Africa", "UTC+01:00"
)

canada = Countries(
    "Canada", "Ottawa", "Canadian Dollar",
    "English/French", 40000000,
    "North America", "UTC-05:00"
)

nigeria.country_info()
nigeria.save_profile()

canada.country_info()
canada.save_profile()

compare = CountryComparator()
compare.compare(nigeria, canada)