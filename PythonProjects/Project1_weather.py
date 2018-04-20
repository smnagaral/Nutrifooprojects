from weather import Weather, Unit

import pyowm
import os

def setApi():
	os.environ["API"] = '662855d7e546e5700e2cafcd000019a2'

def getApi():
	setApi()
	return os.environ.get('API')	

def inputCityName():
	return input("Please enter the city name: ")


def cityValidate(city):
	# Search for current weather in London (Great Britain)
	try:
	    cityData = owm.weather_at_place(city) 
	except :
	    print ("The name of the city is not valid\n")
	    city = inputCityName()
	    cityData = cityValidate(city)
	return cityData

def getWeatherData(observation):
	weatherData = observation.get_weather()
	return weatherData

def printWeatherData(weatherData):
	windData = weatherData.get_wind()
	temperatureData = weatherData.get_temperature('celsius')
	print("****Current Weather Report****")
	print("Wind Speed: 		    {}".format(windData['speed']))
	print("Wind Degree: 		    {}".format(windData['deg']))# {'speed': 4.6, 'deg': 330}
	print("Humidity: 		    "+str(weatherData.get_humidity()))
	print("Normal Temperature:	    {}".format(temperatureData['temp']))# {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
	print("Minimum Temperature:	    {}".format(temperatureData['temp_max']))
	print("Maximum Temperature:	    {}\n\n".format(temperatureData['temp_min']))

def weekForecast(city):
	weather = Weather(unit=Unit.CELSIUS)

	# Lookup via location name.

	location = weather.lookup_by_location(city)
	print("*****One Week Weather Report****")
	forecasts = location.forecast
	for forecast in forecasts:
		print("Date :		                {}".format(forecast.date))
		print("Weather Report: 		{}".format(forecast.text))
		print("Maximum Temperature:	        {}".format(forecast.high))
		print("Minimum Temperature:            {}\n".format(forecast.low))

owm = pyowm.OWM(getApi())  # You MUST provide a valid API key

city = inputCityName()

observation = cityValidate(city)

printData = getWeatherData(observation)

printWeatherData(printData)   

weekForecast(city)