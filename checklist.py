from google import genai
from google.genai import types

class GeminiApiError(Exception):
    """Raised when the Gemini API call fails."""

class checkList:
    """This generates a list of things the person would need for the trip"""
    def __init__(self, api_key):
        self.api_key = api_key
        if not api_key:
            raise GeminiApiError(
                "Gemini API key not set. "
                "Pass api_key= or set the GEMINI_API_KEY environment variable."
            )
        self.client = genai.Client(api_key=self.api_key)

    def generate_checklist(self, country):
        """uses the Gemini API to generate a Travel list for the client"""
        prompt = (f"Generate a checklist of essential items and preparations for someone relocating to {country}. ")
        try:
            response = self.client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(thinking_level="low")
                ),
            )
        except Exception as e:
            raise GeminiApiError(f"Error generating checklist for {country}: {e}")
        return response.text.strip()
    
if __name__ == "__main__":
    api_key = "GEMINI_API_KEY"
    checklist_generator = checkList(api_key)
    country = "Japan"
    checklist = checklist_generator.generate_checklist(country)
    print(f"Checklist for {country}:")
    print(checklist)
