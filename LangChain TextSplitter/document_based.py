from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text="""
import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            return {
                "City": data["name"],
                "Temperature (°C)": data["main"]["temp"],
                "Weather": data["weather"][0]["description"],
                "Humidity (%)": data["main"]["humidity"],
                "Wind Speed (m/s)": data["wind"]["speed"]
            }
        else:
            return {"Error": data.get("message", "Unknown error")}
    except Exception as e:
        return {"Error": str(e)}

def display_weather(weather_data):
    if "Error" in weather_data:
        print("Error:", weather_data["Error"])
    else:
        print("\nCurrent Weather:")
        for key, value in weather_data.items():
            print(f"{key}: {value}")

def main():
    print("Simple Weather App")
    city = input("Enter city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")
    weather = get_weather(city, api_key)
    display_weather(weather)

if __name__ == "__main__":
    main()


"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=500,
    chunk_overlap=0

)

docs=splitter.split_text(text)
print(docs[1])