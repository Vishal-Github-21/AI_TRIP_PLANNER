# AI Trip Planner

A modular, agentic workflow-based trip planning assistant powered by Python. This project leverages multiple APIs (Google Places, OpenWeather, ExchangeRate, Tavily) to provide travel recommendations, weather, currency conversion, and more.

---

## Features
- Search for attractions, restaurants, activities, and transportation in any city
- Get real-time weather information
- Currency conversion and expense calculation
- Modular agent/tool-based architecture
- Fallback to alternative APIs if primary fails

---

## Project Structure
```
AI_TRIP_PLANNER/
  agents/                # Agentic workflow logic
  config/                # Configuration files
  exception/             # Custom exception handling
  logger/                # Logging utilities
  main.py                # Main entry point
  streamlit_app.py       # Streamlit web app
  tools/                 # Tool wrappers for APIs
  utils/                 # Utility functions (API wrappers, helpers)
  requirements.txt       # Python dependencies
  README.md              # This file
```

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd AI_TRIP_PLANNER
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the project root with the following content:
     ```
     GPLACES_API_KEY=your_google_places_api_key
     OPENWEATHER_API_KEY=your_openweathermap_api_key
     EXCHANGERATE_API_KEY=your_exchangerate_api_key
     TAVILY_API_KEY=your_tavily_api_key
     ```
   - Replace each value with your actual API keys.

5. **Run the app:**
   ```bash
   python main.py
   # or for the Streamlit app
   streamlit run streamlit_app.py
   ```

---

## Checking Your API Keys

You can use the following script to verify that your API keys are working:

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def check_google_places_api():
    api_key = os.getenv("GPLACES_API_KEY")
    if not api_key:
        print("❌ Google Places API key not found.")
        return
    endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": "48.8584,2.2945",
        "radius": 500,
        "type": "restaurant",
        "key": api_key
    }
    resp = requests.get(endpoint, params=params).json()
    if "results" in resp:
        print("✅ Google Places API key is working.")
    else:
        print("❌ Google Places API key is NOT working:", resp)

def check_openweather_api():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("❌ OpenWeatherMap API key not found.")
        return
    endpoint = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "London",
        "appid": api_key
    }
    resp = requests.get(endpoint, params=params).json()
    if resp.get("cod") == 200:
        print("✅ OpenWeatherMap API key is working.")
    else:
        print("❌ OpenWeatherMap API key is NOT working:", resp)

def check_exchangerate_api():
    api_key = os.getenv("EXCHANGERATE_API_KEY")
    if not api_key:
        print("❌ ExchangeRate-API key not found.")
        return
    endpoint = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    resp = requests.get(endpoint).json()
    if resp.get("result") == "success":
        print("✅ ExchangeRate-API key is working.")
    else:
        print("❌ ExchangeRate-API key is NOT working:", resp)

def check_tavily_api():
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        print("❌ Tavily API key not found.")
        return
    endpoint = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {api_key}"}
    params = {"query": "test"}
    resp = requests.get(endpoint, headers=headers, params=params)
    if resp.status_code == 200:
        print("✅ Tavily API key is working.")
    else:
        print("❌ Tavily API key is NOT working:", resp.text)

if __name__ == "__main__":
    check_google_places_api()
    check_openweather_api()
    check_exchangerate_api()
    check_tavily_api()
```

---

## Troubleshooting Connection Errors

- **Connection error:**
  - Check your internet connection.
  - Try running the API check script above.
  - If you're on a restricted network, try a different network or hotspot.
  - Check for typos in your API endpoint URLs.
  - Check the API provider's status page.
  - If using a VPN or proxy, try disabling it.

- **API key not working:**
  - Make sure your key is correct and enabled for the right API.
  - Check for extra spaces or quotes in your `.env` file.
  - Make sure your `.env` file is in the project root and loaded before running the app.

---

## License
MIT