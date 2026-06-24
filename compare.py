
class CountryComparator:

    def compare(self, country1, country2):
        comparison_text = (
            f"{country1.name} vs {country2.name}\n"
            f"Capital: {country1.capital} vs {country2.capital}\n"
            f"Currency: {country1.currency} vs {country2.currency}\n"
            f"Languages: {', '.join(country1.languages)} vs {', '.join(country2.languages)}\n"
            f"Population: {country1.population} vs {country2.population}\n"
            f"Region: {country1.region} vs {country2.region}\n"
            f"Flag: {country1.flag} vs {country2.flag}\n"
            f"Timezone: {country1.timezone} vs {country2.timezone}\n"
        )

        with open("comparison_results.txt", "a") as file:
            file.write(comparison_text + "\n")

        return comparison_text

