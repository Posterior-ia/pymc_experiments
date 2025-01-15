import requests
import pandas as pd
import io

class DataImporter:
    def __init__(self, data_name):
        self.data_name = data_name
        self.base_url = 'http://www.stat.columbia.edu/~gelman/book/data'

    def get_data_football(self):
        url = f'{self.base_url}/football.asc'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
            with open('data/football.txt', 'w') as file:
                file.write(data)
        else:
            print(f'Failed to retrieve data: {response.status_code}')

    def import_data(self):
        if self.data_name == 'football':
            self.get_data_football()
        else:
            print(f'No import function defined for data: {self.data_name}')

if __name__ == "__main__":
    data_importer = DataImporter('football')
    data_importer.get_data_football()