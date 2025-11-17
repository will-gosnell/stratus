"""
Now let's practice functions with parameters and return values!

Parameters are like ingredients in a recipe - you can change them to get different results.
Return values are like the finished dish - the function gives you back something useful.

The examples below show functions that take inputs and give back outputs.
"""


def create_weather_message(city):
    message = "Weather report for " + city + " is coming up!"
    return message


# Call the function and store the result
report = create_weather_message("Austin")
# print(report)


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# Call the function and use the result
temp_celsius = convert_to_celsius(75)
# print("75°F equals", temp_celsius, "°C")

"""
Notice how parameters make functions flexible - the same function can work with
different inputs. Return values let you get results back to use in other places.

Time to practice with your own weather parameter functions!
"""

# Create a function called 'weather_greeting' that takes a weather condition parameter
# and print a greeting message about that weather
def weather_greeting(condition):
    print("the weather today is", condition, "!")



# Test your function with "sunny" and print the result
# weather_greeting("rainy")

# Create a function called 'calculate_wind_chill' that takes temperature and wind speed
# and returns a simple wind chill estimate (temp - wind_speed for simplicity)
def calculate_wind_chill(temperature, wind_speed):
    wind_chill = (temperature - wind_speed)
    return wind_chill


# Test your function with temperature 30 and wind speed 15
print(calculate_wind_chill(30, 15))


# Create a function called 'create_forecast' that takes city, temperature, and condition
# and returns a complete weather forecast sentence
def create_forecast(city, temperature, condition):
    forecast= ("Today's weather in " + city   + " is " + temperature + " and "+ condition)
    return forecast
# Test your function with your local weather information
print(create_forecast("Houston", "80", "overcast"))



# Create a function called 'convert_to_fahrenheit' that takes celsius and returns fahrenheit
# Formula: (celsius * 9/5) + 32

# Test it by converting 25 degrees Celsius to Fahrenheit

# Create a function called 'calculate_rainfall_average' that takes two rainfall amounts
# and returns the average rainfall

# Test it with rainfall amounts like 2.5 and 1.8 inches
# print(convert_to_celsius(80))



def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

temp_celsius = convert_to_celsius(75)
# print(temp_celsius)
