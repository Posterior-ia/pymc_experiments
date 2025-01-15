import requests
import pandas as pd
import os

class DataImporter:
    def __init__(self, data_name):
        self.data_name = data_name
        self.base_url = 'http://www.stat.columbia.edu/~gelman/book/data'

    def download_data_football(self):
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
            # download data if it doesn't exist
            if not os.path.exists('data/football.txt'):
                self.download_data_football()
            # read data
            self.data = pd.read_csv('data/football.txt', sep=r'\s+', skiprows=7)

if __name__ == "__main__":
    data_importer = DataImporter('football')
    data_importer.import_data()
    print(data_importer.data.head())