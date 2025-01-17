import logging
import os
from pathlib import Path
from typing import Optional
import pandas as pd
import requests

class DataImporter:
    """Class to handle data importing for statistical analysis.
    
    This class manages downloading and importing data files for different
    statistical bayesian analysis. The data is obtained from the online 
    page of the book "Bayesian Data Analysis" by Andrew Gelman, available 
    at http://www.stat.columbia.edu/~gelman/book/data/
    
    Attributes:
        data_name (str): Name of the dataset to import
        data (Optional[pd.DataFrame]): Loaded data as pandas DataFrame
        data_description (Optional[str]): Description of the loaded data
    """
    
    def __init__(self, data_name: str):
        self.data_name = data_name
        # Get the directory where the script is located
        self.script_dir = Path(__file__).parent
        # Get project root (2 levels up from script)
        self.project_root = self.script_dir.parent.parent
        # Define data directory relative to project root
        self.data_dir = self.project_root / "data"
        self.data: Optional[pd.DataFrame] = None
        self.data_description: Optional[str] = None
        self._setup_logging()
        self.import_data()

    def _setup_logging(self) -> None:
        """Configure logging for the class."""
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def download_data_football(self) -> None:
        """Download football data from the source URL.
        
        Raises:
            requests.RequestException: If download fails
        """
        url = "http://www.stat.columbia.edu/~gelman/book/data/football.asc"
        response = requests.get(url)
        
        if response.ok:
            # Create data directory if it doesn't exist
            self.data_dir.mkdir(exist_ok=True)
            
            with open(self.data_dir / "football.txt", "w") as file:
                file.write(response.text)
            self.logger.info(f"Football data downloaded successfully to {self.data_dir}")
        else:
            self.logger.error(f"Failed to retrieve data: {response.status_code}")
            raise requests.RequestException(f"Download failed with status {response.status_code}")
        
    def process_football_data(self) -> pd.DataFrame:
        """Process raw football data file into a pandas DataFrame.
        
        Args:
            file_path (Path): Path to the raw data file.
            
        Returns:
            pd.DataFrame: Processed data as a pandas DataFrame.
        """
        data_file = self.data_dir / "football.txt"
        if not data_file.exists():
            self.download_data_football()
            
        df = pd.read_csv(data_file, sep=r'\s+', skiprows=7)

        years = [1981] + list(range(1983, 1987)) + list(range(1988, 1993))
        # Create a list to store the assigned years
        assigned_years = []
        # Initialize the year index
        year_index = 0
        # Iterate over the rows of the DataFrame
        for i in range(len(df)):
            if i > 0 and df.loc[i, 'week'] == 1 and df.loc[i-1, 'week'] != 1:
                year_index += 1
            assigned_years.append(years[year_index])

        # Assign the list of years to the DataFrame
        df['year'] = assigned_years

        # Filter the data to include only the 1981, 1983, and 1984 seasons
        self.data = df[df['year'].isin([1981, 1983, 1984])]

    def description_football_data(self) -> str:
        """Return a description of the football data."""
        description = """
        The football data contains information about the results of American football games 
        across multiple seasons. Each row represents a game and includes the following columns:
        
        - home: Indicates whether the favorite team played at home (1 for yes, 0 for no).
        - favorite: Score of the favorite team in the game.
        - underdog: Score of the underdog team in the game.
        - spread: Expected point difference (betting line) between the favorite and underdog.
        - favorite.name: Code for the team that is the favorite.
        - underdog.name: Code for the underdog team.
        - week: Week number in the season when the game was played.
        
        The analysis in Chapter 1 focuses on the data from the 1981, 1983, and 1984 seasons.

        Important notes:
            - Each season consists of 224 games, and data from different seasons are concatenated.
            - Chapter 1 analysis focuses on data from the 1981, 1983, and 1984 seasons.
            - The dataset is useful for analyses such as evaluating betting line accuracy,
                modeling outcomes based on home field advantage and spread, and exploring 
                historical patterns in team performance.
        """
        self.data_description = description

    def import_data(self) -> None:
        """Import data and description based on the specified data name.
        
        Returns:
            pd.DataFrame: Loaded dataset
            
        Raises:
            ValueError: If data_name is not supported
        """
        if self.data_name != 'football':
            raise ValueError(f"Unsupported data type: {self.data_name}")
            
        elif self.data_name == 'football':
            self.process_football_data()
            self.description_football_data()

if __name__ == "__main__":
    try:
        data_importer = DataImporter('football')
        df = data_importer.data
        print(df.head())
    except Exception as e:
        logging.error(f"Error importing data: {e}")