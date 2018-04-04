'''from weather import Weather, Unit
weather = Weather(unit=Unit.CELSIUS)

# Lookup WOEID via http://weather.yahoo.com.

lookup = weather.lookup(560743)

condition = lookup.condition()
print(condition.text())

# Lookup via location name.

location = weather.lookup_by_location('Bengaluru')
condition = location.condition()
print(condition.text())

#Get weather forecasts for the upcoming days.

forecasts = location.forecast()
for forecast in forecasts:
    print(forecast.text())
    print(forecast.date())
    print(forecast.high())
    print(forecast.low())'''

import pyowm

owm = pyowm.OWM('662855d7e546e5700e2cafcd000019a2')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

city = input("Please enter the city name: ")

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place(city) # C: What format should the city name be?
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
print(w.get_wind())                 # {'speed': 4.6, 'deg': 330}
print(w.get_humidity())             # 87
print(w.get_temperature('celsius')) # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# Issues: 
# What do lines 1 - 24 do?
# Hard coding API keys (line 28) is extremely dangerous; Extract sensitive information such as these from env variables
# No error handling or input sanitization done (line 33). Code will fail at the slightest touch
# Print statement at line 37 prints an object. Was there a reason for that?

# This was the problem statement:
# => Write a program that takes in the name of a city as input and outputs the weather data of the city for the current week.

# What this code does:
# This code prints some weather data but doesn't specify what date, time or even where
# Code also prints weather data for Rio De Janeiro? Why?
# Most of the guidelines have not been followed

# Changes to be made:
# => Get input from user
# => Sanitize the input
# => Verify the validity of the city name
# => Obtain weather data for the current week (Mon, Tue, Wed, Thurs, Fri, Sat, Sun)
# => Ensure you catch errors and proceed with appropirate actions
#
# Please follow the guidelines for the code:
# > Ensure JSON format as the output wherever possible
#
# > Keep the program as small as possible
#
# > code should be modular. Make functions
#
# > Ensure variable names are as meaningful as they can be. Avoid comments for explanations. The code should explain itself
#
# > Comment only when necessary

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
