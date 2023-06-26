import requests
import json
import sys
import re
from datetime import date, datetime

def get_weather(city):
    api_key = 'ADD_API_KEY'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = json.loads(response.text)
        return weather_data
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Request exception occurred: {err}')
    except (json.JSONDecodeError, KeyError) as json_err:
        print(f'Error parsing JSON data: {json_err}')
    
    return None

def display_weather(weather_data):
    if weather_data is not None:
        city_name = weather_data['name']
        temperature_celsius = weather_data['main']['temp']        
        temperature_fahrenheit = (temperature_celsius * 9/5) + 32
        temperature_fahrenheit = round(temperature_fahrenheit, 3)
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        clouds = weather_data['clouds']['all']  
        sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise']).strftime("%I:%M:%S %p")
        sunset = datetime.fromtimestamp(weather_data['sys']['sunset']).strftime("%I:%M:%S %p")
        description = weather_data['weather'][0]['description']        
        today = date.today()

        print(f'Current weather in {city_name}:')
        print("Today's date:", today)
        print(f'Temperature: {temperature_celsius}°C / {temperature_fahrenheit}°F')        
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed} m/s')
        print(f'Clouds: {clouds}%')
        print(f'Sunrise: {sunrise}')
        print(f'Sunset: {sunset}')
        print(f'Description: {description}')
    else:
        print('Failed to fetch weather data.')

def validate_city_name(city_name):
    if not re.match("^[A-Za-z\s]+$", city_name):
        print('Invalid city name. Please provide a valid city name.')
        return False
    return True

def main():
    city_name = input("Enter the city name: ")
    if not validate_city_name(city_name):
        return
    
    weather_data = get_weather(city_name)
    if weather_data is not None:
        display_weather(weather_data)
    else:
        print('Weather data not available.')

if __name__ == '__main__':
    main()
