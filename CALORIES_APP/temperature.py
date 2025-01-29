from selectorlib import Extractor
import requests

class Temperature:
    """
    A scraper that uses a yaml file to read the xpath of a value it needs to extract
    from the timeanddate.com/weather/url
    """
    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        """Builds the url string adding country and city"""
        url = self.base_url + self.country + "/" + self.city
        return url

    def _scrape(self):
        """Extracts a value as instructed by the yml file and returns a dictionary """
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):
        """Cleans the output of _scrape"""

        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace("°C", "").strip())

if __name__ == "__main__":
    temperature = Temperature(city='paris', country='france')
    print(temperature.get())