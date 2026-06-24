🌍 Country Relocation and Culture Guide

An interactive application where users can search for a country and view details such as capital, currency, languages, population, region, flag, and timezone. The app also generates simple travel, study, or relocation guides using AI, and includes a country comparison feature.

✨ Features

- Search for a country using name

- View details: capital, currency, languages, population, region, flag, timezone

- AI-generated guides: travel, study, relocation tips (powered by Gemini API)

- Country comparison: side-by-side comparison of two countries

- Before you travel checklist: automatically generated based on country info

- Timezone difference calculator

- Error handling: unknown countries, missing API fields, invalid input, failed API requests

- Validation: country names, codes, and timezone formats

🏗️ Architecture

The app is structured into modular classes:

* Country  
Represents a country with attributes like name, capital, population, region, currency, languages, timezone, and flag.

* CountryAPIClient  
Handles API requests to the REST Countries API and validates responses.

* RelocationGuide  
Uses the Gemini API to generate tailored travel, study, or relocation guides.

* CountryComparator  
Compares two countries side-by-side and calculates timezone differences.

🛠️ Tech Stack

* Python (core logic)

* Streamlit or Tkinter (UI)

* Requests (API calls)

* JSON (data parsing)

* Date/Time handling (timezone differences)

* REST Countries API (country data)

* Gemini API (AI-generated guides)

🚀 Installation & Setup

Clone the repository:

bash

git clone https://github.com/your-username/Country_Relocation_and_Culture_Guide.git

cd Country_Relocation_and_Culture_Guide


Install dependencies:

Run the app:

- For Streamlit:

bash
streamlit run app.py
- For Tkinter:

bash
python app.py

📂 Data Storage

* Local JSON files or SQLite database for:

* Saved country profiles

* Comparison results

* Travel checklists

⚠️ Error Handling

* Invalid country names or codes → user-friendly error message

* Missing API fields → gracefully skipped with defaults

* Failed API requests → retry or fallback message

* Timezone validation → strict format checking

🧩 Example Workflow

* User searches for Japan

* App fetches details from REST Countries API

* Gemini API generates a relocation guide (study tips, cultural notes, travel advice)

* User compares Japan vs Germany

* App shows side-by-side comparison and timezone difference

* User saves the guide locally for future reference
