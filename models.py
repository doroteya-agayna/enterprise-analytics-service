from dataclasses import dataclass
from datetime import date

@dataclass
class RevenueRecord:
    record_date: date
    customer: str
    revenue: float