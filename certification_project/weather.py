import argparse
import requests

def get_weather(api_key, city_id):
    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        print(f"Error: {data['message']}")
        return

    weather = data['main']
    wind = data['wind']
    clouds = data['clouds']
    sys = data['sys']

    print(f"Temperature: {weather['temp']}°C")
    print(f"Temperature (min): {weather['temp_min']}°C")
    print(f"Temperature (max): {weather['temp_max']}°C")
    print(f"Pressure: {weather['pressure']} hPa")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {wind['speed']} m/s")
    print(f"Cloudiness: {clouds['all']}%")
    print(f"Sunrise: {sys['sunrise']}")
    print(f"Sunset: {sys['sunset']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the weather parameters of a location.")
    parser.add_argument('api_key', type=str, help="Your OpenWeatherMap API key.")
    parser.add_argument('city_id', type=int, help="The city ID.")
    
    args = parser.parse_args()
    get_weather(args.api_key, args.city_id)




'''

Usage
Google Search Script:

1 python googlesearch.py "openai"
python googlesearch.py "openai" --num_results 5

2 Location Script:
python location.py "New York, USA"

3 Weather Script:
python weather.py YOUR_API_KEY CITY_ID

Replace YOUR_API_KEY with your actual OpenWeatherMap API key and CITY_ID with the city ID of the location you want to get the weather for. You can find city IDs on the OpenWeatherMap website.



'''
