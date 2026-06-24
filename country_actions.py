import os
import tkinter as tk
from tkinter import messagebox

from Rest_API_Module import CountryAPIClient
from compare import CountryComparator
from Gemini_Guide import RelocationGuide
from local_storage import LocalStorage
from Country_Model import Country
from checklist import checkList
from local_storage import Localsave

# Handles all the functions of our GUI
class CountryAppController:
    def __init__(
        self,
        country_entry: tk.Entry,
        purpose_entry: tk.Entry,
        country1_entry: tk.Entry,
        country2_entry: tk.Entry,
        output: tk.Text,
    ):
        self.country_entry = country_entry
        self.purpose_entry = purpose_entry
        self.country1_entry = country1_entry
        self.country2_entry = country2_entry
        self.output = output
        self.client = CountryAPIClient()
        self.storage = LocalStorage()
        self.comparator = CountryComparator()
        self.store = Localsave()
        self.guide_api_key = "GEMINI_API_KEY"

    def _country_from_api_result(self, result: dict) -> Country:
        languages = result.get("languages", "")
        if isinstance(languages, str):
            languages = [lang.strip() for lang in languages.split(",") if lang.strip()]

        population = result.get("population", 0)
        try:
            population = int(population)
        except (ValueError, TypeError):
            population = 0

        return Country(
            name=result.get("name", "Unknown"),
            capital=result.get("capital", "Unknown"),
            currency=result.get("currency", "Unknown"),
            languages=languages,
            population=population,
            region=result.get("region", "Unknown"),
            flag = result.get("flag", "Unknown"),
            timezone=result.get("timezone", "Unknown"),
        )

    def search_country(self):
        country_name = self.country_entry.get().strip()
        if not country_name:
            messagebox.showwarning("Input required", "Enter a country name.")
            return

        try:
            result = self.client.get_country(country_name)
            profile_text = (
                f"Country profile for {country_name}:\n\n"
                f"Country: {result['name']}\n"
                f"Capital: {result['capital']}\n"
                f"Currency: {result['currency']}\n"
                f"Languages: {result['languages']}\n"
                f"Population: {result['population']}\n"
                f"Region: {result['region']}\n"
                f"Flag: {result.get('flag', 'Unknown')}\n"
                f"Timezone: {result['timezone']}\n\n"
                "----------\n"
            )
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, profile_text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def check_list(self):
        country_name = self.country_entry.get().strip()
        if not country_name:
            messagebox.showwarning(
                "Input required", "Enter a country name before generating a checklist.")
            return

        try:
            api_key = "GEMINI_API_KEY"
            result = self.client.get_country(country_name)
            country = self._country_from_api_result(result)
            checklist_generator = checkList(api_key)
            checklist = checklist_generator.generate_checklist(country)
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, checklist)
            messagebox.showinfo("Checklist generated", "Checklist generated successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def view_saved(self):
            saved_countries = self.storage.load_all()

            if not saved_countries:
                messagebox.showinfo(
                    "No saved countries",
                    "No countries have been saved."
                )
                return

            try:
                saved_countries_text = ""

                for country_name, country_data in saved_countries.items():

                    saved_countries_text += (
                        f"Country: {country_data.get('name', country_name)}\n"
                        f"Capital: {country_data.get('capital', 'Unknown')}\n"
                        f"Currency: {country_data.get('currency', 'Unknown')}\n"
                        f"Languages: {country_data.get('languages', 'Unknown')}\n"
                        f"Population: {country_data.get('population', 'Unknown')}\n"
                        f"Region: {country_data.get('region', 'Unknown')}\n"
                        f"Flag: {country_data.get('flag', 'Unknown')}\n"
                        f"Timezone: {country_data.get('timezone', 'Unknown')}\n"
                        "\n\n"
                    )

                self.output.delete("1.0", tk.END)
                self.output.insert(tk.END, saved_countries_text)

                messagebox.showinfo(
                    "Saved Countries",
                    "Opened saved countries successfully."
                )

            except Exception as e:
                messagebox.showerror("Error", str(e))



    def save_favorite_country(self):
        country_name = self.country_entry.get().strip()
        if not country_name:
            messagebox.showwarning("Input required", "Enter a country name before saving.")
            return

        try:
            result = self.client.get_country(country_name)
            self.storage.save(country_name, result)
            messagebox.showinfo(
                "Saved",
                f"Country profile for {country_name} saved successfully."
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generate_guide(self):
        country_name = self.country_entry.get().strip()
        guide_type = self.purpose_entry.get().strip().lower()
        if guide_type not in {"study", "travel", "relocation"}:
            messagebox.showwarning(
                "Invalid purpose",
                "Please enter one of: study, travel, relocation."
            )
            return
        if not country_name:
            messagebox.showwarning("Input required", "Enter a country name to generate a guide.")
            return

        if not self.guide_api_key:
            messagebox.showerror(
                "Gemini API key missing",
                "Set GEMINI_API_KEY in your environment to generate guides."
            )
            return

        try:
            result = self.client.get_country(country_name)
            country = self._country_from_api_result(result)
            guide_generator = RelocationGuide(api_key=self.guide_api_key)
            prompt = guide_generator._build_prompt(country, guide_type)
            guide_text = guide_generator.call_gemini(prompt)

            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, guide_text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_guide(self):
        guide_type = self.purpose_entry.get().strip().lower()

        if not guide_type:
            messagebox.showwarning("Input required", "Enter a guide type to save.")
            return

        if not self.guide_api_key:
            messagebox.showerror(
                "Gemini API key missing",
                "Set GEMINI_API_KEY in your environment."
            )
            return

        guide_text = self.output.get("1.0", tk.END).strip()

        if not guide_text:
            messagebox.showwarning("Error", "No guide to save.")
            return

        try:
            self.store.save(guide_type, guide_text)

            messagebox.showinfo(
                "Guide saved",
                "Guide saved successfully."
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def view_saved_guide(self):
            saved_guides = self.store.load_all()
            if not saved_guides:
                messagebox.showinfo(
                    "No saved guides",
                    "No guides have been saved."
                )
                return
            try:
                saved_guides_text = str(saved_guides)

                self.output.delete("1.0", tk.END)
                self.output.insert(tk.END, saved_guides_text)

                messagebox.showinfo(
                    "Saved Guides",
                    "Opened saved guides successfully."
                )
            except Exception as e:
                    messagebox.showerror("Error", str(e))                                    


    def compare_countries(self):
        first_name = self.country1_entry.get().strip()
        second_name = self.country2_entry.get().strip()

        if not first_name or not second_name:
            messagebox.showwarning(
                "Input required",
                "Enter two countries to compare."
            )
            return

        if first_name.lower() == second_name.lower():
            messagebox.showwarning(
                "Invalid input",
                "Please select two different countries."
            )
            return

        try:
            first_data = self.client.get_country(first_name)
            second_data = self.client.get_country(second_name)
            country1 = self._country_from_api_result(first_data)
            country2 = self._country_from_api_result(second_data)

            result = self.comparator.compare(country1, country2)
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
