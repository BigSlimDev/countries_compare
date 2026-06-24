import os
from collections.abc import Mapping
from enum import Enum
from google import genai
from google.genai import types

# This class handles the API error calls
class GeminiAPIError(Exception):
    """Raised when the Gemini API call fails."""

class GuideType(str, Enum):
    TRAVEL = "travel"
    STUDY = "study"
    RELOCATION = "relocation"

class RelocationGuide:
    """Generate a relocation guide for a given country using the Gemini API"""
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY", "")
        if not self.api_key:
            raise GeminiAPIError(
                "Gemini API key not set. "
                "Pass api_key= or set the GEMINI_API_KEY environment variable."
            )
        self.client = genai.Client(api_key=self.api_key)

    def _field(self, country, *names, default="N/A"):
        if isinstance(country, Mapping):
            for name in names:
                value = country.get(name)
                if value is not None:
                    return value
            return default

        for name in names:
            value = getattr(country, name, None)
            if value is not None:
                return value
        return default

    def _build_country_context(self, country) -> str:
        """Format country facts into a compact context block for Gemini."""
        country_name = self._field(country, "name", default=str(country) if isinstance(country, str) else "Unknown")
        official_name = self._field(country, "official_name", "official", default=country_name)
        capital = self._field(country, "capital_display", "capital")
        region = self._field(country, "region")
        subregion = self._field(country, "subregion")
        population = self._field(country, "population_display", "population")
        area = self._field(country, "area_display", "area")
        languages = self._field(country, "language_display", "languages")
        currencies = self._field(country, "currency_display", "currency")
        timezones = self._field(country, "timezone_display", "timezone")
        driving_side = self._field(country, "driving_side")
        calling_codes = self._field(country, "calling_codes", "calling_code", default=[])
        if isinstance(calling_codes, str):
            calling_codes = [calling_codes]
        calling_codes_str = ", ".join(calling_codes) if calling_codes else "N/A"
        tlds = self._field(country, "tlds", default=[])
        tlds_str = ", ".join(tlds) if tlds else "N/A"
        borders = self._field(country, "borders", default=[])
        borders_str = ", ".join(borders) if borders else "none / island nation"
        continent = self._field(country, "continent")

        return f"""
Country Profile:
- Common name    : {country_name}
- Official name  : {official_name}
- Capital        : {capital}
- Region         : {region} / {subregion}
- Population     : {population}
- Area           : {area}
- Languages      : {languages}
- Currencies     : {currencies}
- Timezones      : {timezones}
- Driving side   : {driving_side}
- Calling code(s): {calling_codes_str}
- Internet TLD(s): {tlds_str}
- Borders        : {borders_str}
- Continent      : {continent}
""".strip()
    def _build_prompt(self, country, guide_type) -> str:
        """Construct the full prompt for Gemini."""
        ctx = self._build_country_context(country)
        country_name = self._field(country, "name", default=str(country) if isinstance(country, str) else "Unknown")

        guide_type_value = guide_type.lower() if isinstance(guide_type, str) else guide_type.value
        if guide_type_value == GuideType.TRAVEL.value:
            task = (
                "Write a short and simple and engaging **travel guide** for someone planning a holiday "
                f"to {country_name}. Cover: best times to visit, top attractions, local food, "
                "transport tips, cultural etiquette, visa/entry notes, and safety tips. "
                "Use a friendly, inspiring tone."
            )
        elif guide_type_value == GuideType.STUDY.value:
            task = (
                f"Write a short and simple **study abroad guide** for a student considering {country_name}. "
                "Cover: education system overview, top universities, student visa requirements, "
                "cost of living, language considerations, cultural adjustment tips, and scholarship "
                "opportunities. Use an informative, supportive tone."
            )
        else:  # RELOCATION
            task = (
                f"Write a short and Simple **relocation guide** for someone planning to move to "
                f"{country_name}. Cover: visa/residency pathways, cost of living, housing market, "
                "job market and work permits, healthcare system, education for children, cultural "
                "integration tips, banking and finance, and practical first steps after arrival. "
                "Use a helpful, practical tone."
            )

        return (
            f"You are an expert travel and relocation consultant with deep knowledge of every "
            f"country in the world.\n\n"
            f"Here is factual data about the country:\n{ctx}\n\n"
            f"Task: {task}\n\n"
            f"Structure your response with clear markdown headings (##) and bullet points where "
            f"appropriate. Keep the total length under 800 words. Be accurate and constructive."
        )
    def call_gemini(self, prompt) -> str:
        """Call the Gemini API with the constructed prompt."""
        try:
            response = self.client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(thinking_level="low")
                ),
            )
            return response.text
        except Exception as e:
            raise GeminiAPIError(f"Gemini API call failed: {e}")
