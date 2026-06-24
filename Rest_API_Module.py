# Import requests library to make API calls (HTTP requests)
import requests

# Import json to read/write data in JSON format
import json

# Import os to work with files (check if file exists, etc.)
import os


# Class responsible for fetching country data from REST Countries API
class CountryAPIClient:
    def __init__(self):
        pass

    # Base URL for the API (endpoint for searching countries by name)
    BASE_URL = "https://api.restcountries.com/countries/v5?q="

    # Method to get country details using country name
    def get_country(self, country_name):

        # Check if input is empty or just spaces
        if not country_name or not country_name.strip():
            # raises an error if invalid
            raise ValueError("Invalid country name.") 

        try:
            # Create full API URL by adding the country name
            url = f"{self.BASE_URL}{country_name.strip().lower()}"

            # Send GET request to the API
            response = requests.get(url, headers={'Authorization': 'KEY'}, timeout=5)

            # Raise error if response status is not 200 (success)
            response.raise_for_status()

            # Convert API response to Python dictionary
            data = response.json()

            # Get the first result (API returns a list)
            country = data['data']['objects'][0]

            country_info = {
                "name": country["names"]["common"],
                "capital": country["capitals"][0]["name"],
                "population": country["population"],
                "region": country["region"],
                "currency": country["currencies"][0]["name"],
                "languages": ", ".join(
                        lang["name"] for lang in country["languages"]
                                    ),
                "flag": country["flag"]["url_png"],
                "timezone": ", ".join(country["timezones"]),
                
                    }
            return country_info

        # If country is not found (404 error)
        except requests.exceptions.HTTPError:
            raise ValueError("Country not found.")

        # If network fails (no internet, timeout, etc.)
        except requests.exceptions.RequestException:
            raise ConnectionError("API request failed.")


# Import the LocalStorage class from the separate module
from local_storage import LocalStorage


# This block runs only when file is executed directly (not imported)
if __name__ == "__main__":

    # Create API client object
    api = CountryAPIClient()

    # Create storage object
    storage = LocalStorage()

    try:
        # Fetch country data from API
        country = api.get_country("Canada")

        # Print fetched data
        print(country)

        # Save country data locally
        storage.save("Canada", country)

        # Load saved data
        saved = storage.load("Canada")

        # Print loaded data
        print("Loaded:", saved)

    # Catch and print any errors
    except Exception as e:
        print(e)
