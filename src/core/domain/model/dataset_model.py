from dataclasses import dataclass
import pandas as pd

@dataclass
class DatasetModel:
    """
    Domain model representing a loaded dataset.
    """
    data: pd.DataFrame
