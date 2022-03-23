import os
from pyowm.owm import OWM

# Get environment variables
owm_api_key = os.getenv('OWM_API_KEY')
owm_city = os.environ.get('OWM_CITY')



# Stop if environment variables are defined
if owm_api_key is None:
    print("OWM_API_KEY needs to be exported !")
    exit()
if owm_city is None:
    print("OWM_CITY needs to be exported !")
    exit()

owm = OWM(owm_api_key)
mgr = owm.weather_manager()
observation = mgr.weather_at_place(owm_city)
w = observation.weather


city = owm_city
weather_description = w.detailed_status
temperature = w.temperature('fahrenheit')['temp']
humidity = w.humidity

print(f'city="{city}", description="{weather_description}", temp="{temperature}", humidity="{humidity}"')