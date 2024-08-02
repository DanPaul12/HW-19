class WeatherForecast:
    def __init__(self):
        self.weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }
        
    def fetch_weather_data(self, city):
        if city in self.weather_data:
            return self.weather_data.get(city, {})
    
WeatherForecast.fetch_weather_data("New York", "New York")