
# Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## Acknowledgements

 - [Awesome Weather API](http://api.openweathermap.org/data/2.5/weather)
 
 - [GitHub Copilot](https://github.com/features/copilot)


# Fastest Coder Hackathon

Weather Forecasting Tool - Create a command line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.

# Description



# API Usage:

- GitHub Copilot can assist with API usage by suggesting the base URL for making the API request, in this case, the OpenWeatherMap API endpoint.
Copilot can provide hints for constructing the query parameters required by the API, such as the city, country, state, and API key.
It can also suggest using the requests.get() method to send the API request and retrieve the weather data.

# Data Parsing:

- Copilot can assist with data parsing by suggesting the usage of json.loads() to convert the JSON response from the API into a Python dictionary.
It can help with extracting the relevant weather information from the parsed data, such as the city name, temperature, wind speed, and weather description.

# Error Handling:

- Copilot can suggest error handling code using try-except blocks to handle potential errors during the API request and response handling process.

It can provide suggestions for handling HTTP errors, such as 404 or 500 status codes, using the requests.exceptions.HTTPError exception.
Copilot can also assist with handling request exceptions, such as network connectivity issues or timeouts, using the requests.exceptions.RequestException exception.
Additionally, it can help with handling errors related to parsing the JSON response, such as json.JSONDecodeError or missing key errors, using the json_err variable.

## API Reference

#### Get all items

```http
  base_url = 'http://api.openweathermap.org/data/2.5/weather'
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

Just enter the city and you will get all the weather Updates.


## Authors

- [@VishweshSalampuria](https://github.com/Salampuriavv) [Leader]
- [@AyushiRaghuwanshi](https://github.com/ayushi84461)
- [@AtharvaWerulkar](https://github.com/Atharva-Werulkar)
- [@AishwaryGathe](https://github.com/AishwaryGathe)


## Deployment

To deploy this project run

```bash
    python main.py
```


## Feedback

If you have any feedback, please reach out to us at aishwarygathe@gmail.com

