"""
Beard Masters service module
Contains product and service classes
"""

from datetime import datetime

class BeardProduct:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        self._validate_price()

    def _validate_price(self):
        if not isinstance(self.price, (int, float)) or self.price < 0:
            raise ValueError("Price must be a positive number")

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class GroomingService:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        self.duration = 30  # minutes

    def get_total(self):
        return self.price

class LuxuryGroomingService(GroomingService):
    def __init__(self, name, price, description):
        super().__init__(name, price, description)
        self.duration = 60
        self.includes_hot_towel = True
        self.includes_facial = True