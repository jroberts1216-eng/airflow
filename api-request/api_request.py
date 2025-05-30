import requests

api_key = '82c8f6eb50dcc044b4dd1ec199f6cfc0'
api_url = f'http://api.weatherstack.com/current?access_key={api_key}&query=New York'

def fetch_data():
    print('Fetching data from Weatherstack.com . . .')
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print('API response received')
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        raise

def mock_fetch_data():
    return {
        'request': {
            'type': 'City',
            'query': 'New York, United States of America',
            'language': 'en',
            'unit': 'm'
        },
        'location': {
            'name': 'New York',
            'country': 'United States of America',
            'region': 'New York',
            'lat': '40.714',
            'lon': '-74.006',
            'timezone_id': 'America/New_York',
            'localtime': '2025-05-29 20:25',
            'localtime_epoch': 1748550300,
            'utc_offset': '-4.0'
        },
        'current': {
            'observation_time': '12:25 AM',
            'temperature': 18,
            'weather_code': 119,
            'weather_icons': [
                'https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0003_white_cloud.png'
            ],
            'weather_descriptions': ['Cloudy '],
            'astro': {
                'sunrise': '05:29 AM',
                'sunset': '08:19 PM',
                'moonrise': '07:29 AM',
                'moonset': '11:36 PM',
                'moon_phase': 'Waxing Crescent',
                'moon_illumination': 5
            },
            'air_quality': {
                'co': '534.65',
                'no2': '123.21',
                'o3': '28',
                'so2': '16.095',
                'pm2_5': '49.025',
                'pm10': '49.21',
                'us-epa-index': '3',
                'gb-defra-index': '3'
            },
            'wind_speed': 13,
            'wind_degree': 264,
            'wind_dir': 'W',
            'pressure': 1014,
            'precip': 0,
            'humidity': 81,
            'cloudcover': 0,
            'feelslike': 18,
            'uv_index': 0,
            'visibility': 16,
            'is_day': 'no'
        }
    }

# Toggle here between real API or mock
if __name__ == "__main__":
    use_mock = True  # Set to False to use the live API

    if use_mock:
        data = mock_fetch_data()
        print("Using mock data:")
    else:
        data = fetch_data()
        print("Using live API data:")

    print(data)