class WeatherForecast:
    def __init__(self):
        self.weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }
        
    def fetch_weather_data(self, city):
        return self.weather_data.get(city, {})
    
    def parse_weather_data(data):
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
    
    def get_detailed_forecast(city):
        data = WeatherForecast.fetch_weather_data(city)
        return WeatherForecast.parse_weather_data(data)
   
    def display_weather(city):
    # Function to display the basic weather forecast for a city
        data = WeatherForecast.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = WeatherForecast.parse_weather_data(data)
            print(weather_report)
    
def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = WeatherForecast.get_detailed_forecast(city)
        else:
            forecast = WeatherForecast.display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()