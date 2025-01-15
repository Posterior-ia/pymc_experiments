import logging
from pathlib import Path
from typing import Optional
import pandas as pd
import requests

class DataImporter:
    """Class to handle data importing for statistical analysis.
    
    This class manages downloading and importing data files for different
    statistical bayesian analysis. The data is obtained from the online 
    page of the book "Bayesian Data Analysis" by Andrew Gelman, available 
    at https://raw.githubusercontent.com/
    
    Attributes:
        data_name (str): Name of the dataset to import
        data (Optional[pd.DataFrame]): Loaded data as pandas DataFrame
    """
    
    def __init__(self, data_name: str):
        self.data_name = data_name
        self.data: Optional[pd.DataFrame] = None
        self._setup_logging()

    def _setup_logging(self) -> None:
        """Configure logging for the class."""
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def download_data_football(self) -> None:
        """Download football data from the source URL.
        
        Raises:
            requests.RequestException: If download fails
        """
        url = "https://raw.githubusercontent.com/example/football.txt"
        response = requests.get(url)
        
        if response.ok:
            data_dir = Path("data")
            data_dir.mkdir(exist_ok=True)
            
            with open(data_dir / "football.txt", "w") as file:
                file.write(response.text)
            self.logger.info("Football data downloaded successfully")
        else:
            self.logger.error(f"Failed to retrieve data: {response.status_code}")
            raise requests.RequestException(f"Download failed with status {response.status_code}")

    def import_data(self) -> pd.DataFrame:
        """Import data based on the specified data name.
        
        Returns:
            pd.DataFrame: Loaded dataset
            
        Raises:
            ValueError: If data_name is not supported
        """
        if self.data_name != 'football':
            raise ValueError(f"Unsupported data type: {self.data_name}")
            
        data_file = Path("data") / "football.txt"
        if not data_file.exists():
            self.download_data_football()
            
        self.data = pd.read_csv(data_file, sep=r'\s+', skiprows=7)
        return self.data


if __name__ == "__main__":
    try:
        data_importer = DataImporter('football')
        df = data_importer.import_data()
        print(df.head())
    except Exception as e:
        logging.error(f"Error importing data: {e}")