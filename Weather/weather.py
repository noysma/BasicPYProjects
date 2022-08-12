import requests # (pip install requests)

API_KEY = '' # here put the API key from https://openweathermap.org/api
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Enter a city name: ')
requests_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
data = requests.get(requests_url)

if data.status_code == 200:
    weather_data = data.json()
    weather = weather_data['weather'][0]['description']
    temperature = round(weather_data['main']['temp'] - 273.5, 2)
    feels_like = round(weather_data['main']['feels_like'] - 273.5, 2)
    temp_min = round(weather_data['main']['temp_min'] - 273.5, 2)
    temp_max = round(weather_data['main']['temp_max'] - 273.5, 2)
    country = weather_data['sys']['country']

    print()
    print('We are in {0}, in {1}; the temperature today is: {2}°C.'.format(country, city, temperature))
    print('Today the minimum temperature is {0}°C and the maximum is {1}°C.\nThe perceived temperature is {2}°C'.format(temp_min, temp_max, feels_like))
else:
    print('Something goes wrong')