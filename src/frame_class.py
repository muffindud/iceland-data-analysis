from dataclasses import dataclass
from enum import Enum


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
