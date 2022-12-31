import requests
import inquirer

lat = ''
long = ''
counter = 0
totalRain = 0

question = [
  inquirer.List('city',
                message="What city do you want to check?",
                choices=['San Francisco', 'Las Vegas', 'Denver', 'St. Louis', 'Nashville', 'New York', 'Boston'],
            )
]

answer = inquirer.prompt(question)
print(answer["city"])

match answer["city"]:
    case "San Francisco":
        lat = '37.77'
        long = '-122.42'
    case "Las Vegas":
        lat = '36.17'
        long = '-115.14'
    case "Denver":
        lat = '39.74'
        long = '-104.98'
    case "St. Louis":
        lat = '38.63'
        long = '-90.20'
    case "Nashville":
        lat = '36.17'
        long = '-86.78'
    case "New York":
        lat = '40.71'
        long = '-74.01'
    case "Boston":
        lat = '42.36'
        long = '-71.06'

response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + lat + '&longitude=' + long + '&hourly=temperature_2m,precipitation,rain&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch')
jason = response.json()

jason_string = str(jason['current_weather']['temperature'])
print(jason_string + " degrees currently")
hourlyRain = jason['hourly']['rain']

while counter < 24:
    totalRain += hourlyRain[counter]
    counter+=1

print('Total rain expected over 24 hours: ' + str(totalRain) + ' inches')
