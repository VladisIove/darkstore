from typing import List
from dataclasses import dataclass


@dataclass
class YearToDate:
    candles: dict

    def __call__(self, position_amount: float):
        price_on_first_day_at_the_year = self.candles.get("c", [0])[0]
        return float(price_on_first_day_at_the_year) - float(position_amount)

    def min(self, amounts: List[float]) -> float:
        return min(self(amount) for amount in amounts)

    def max(self, amounts: List[float]) -> float:
        return max(self(amount) for amount in amounts)
