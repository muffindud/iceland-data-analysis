from dataclasses import dataclass, field
from enum import Enum

from pandas import DataFrame


class Category(Enum):
    MACROECONOMICS = "Macroeconomics"
    PRICES_AND_INFLATION = "Prices and Inflation"
    LABOR_MARKET = "Labor Market"
    EDUCATION_AND_HUMAN_CAPITAL = "Education and Human Capital"
    EARNINGS_AND_INEQUALITY = "Earnings and Inequality"


class Frequency(Enum):
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    ANNUAL = "Annual"


@dataclass
class Frame:
    name: str
    file_name: str
    description: str
    eurostat_code: str
    frequency: Frequency
    categories: list[Category]
    data_columns: list[str] = field(default_factory=lambda: ["value", "TIME_PERIOD"])
    useful_column_filter: dict[str, list[str]] = None
    series_id_columns: list[str] = None
    dataframe: DataFrame | None = None
