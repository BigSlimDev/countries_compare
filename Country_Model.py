from dataclasses import dataclass
from typing import List


@dataclass
class Country:
    name: str
    capital: str
    currency: str
    languages: List[str]
    population: int
    region: str
    flag: str
    timezone: str

    @classmethod
    def from_api_data(cls, data):
        """
        Create a Country object from REST Countries API data.
        """

        name = data.get("name", {}).get("common", "Unknown")

        capital = (
            data.get("capital", ["Unknown"])[0]
            if data.get("capital")
            else "Unknown"
        )

        currencies = data.get("currencies", {})
        currency = (
            list(currencies.keys())[0]
            if currencies
            else "Unknown"
        )

        languages = list(data.get("languages", {}).values())

        population = data.get("population", 0)

        region = data.get("region", "Unknown")

        flag = data.get("flag", "Unknown")

        timezone = (
            data.get("timezones", ["Unknown"])[0]
            if data.get("timezones")
            else "Unknown"
        )

        country = cls(
            name=name,
            capital=capital,
            currency=currency,
            languages=languages,
            population=population,
            region=region,
            flag = flag,
            timezone=timezone
        )

        country.validate()

        return country

    def validate(self):
        """
        Validate country data received from API.
        """

        if not self.name:
            raise ValueError("Country name missing.")

        if self.population < 0:
            raise ValueError("Invalid population.")

        if not isinstance(self.languages, list):
            raise ValueError("Languages must be a list.")

        return True


    def validate_country_search(self, country_name):
        """
        Validate search input before API request.
        """

        country_name = country_name.strip()

        if not country_name:
            raise ValueError("Country name cannot be empty.")

        if len(country_name) < 2:
            raise ValueError("Country name is too short.")

        return True


    def validate_country_comparison(self, country1, country2):
        """
        Ensure different countries are selected.
        """

        if country1.name.lower() == country2.name.lower():
            raise ValueError(
                "Please select two different countries."
            )

        return True


    def calculate_timezone_difference(country1, country2):
        """
        Calculate timezone difference using UTC offsets.
        """

        try:
            tz1 = country1.timezone
            tz2 = country2.timezone

            offset1 = int(tz1[3:6])
            offset2 = int(tz2[3:6])

            return offset2 - offset1

        except (ValueError, TypeError):
            return None