# Beard Masters service module
# Contains product and service classes for managing beard care products and grooming services

from datetime import datetime

class BeardProduct:
    # Represents a beard care product available for sale.
    # Handles product details and price validation.
    def __init__(self, name, price, description):
        # Initialize a new beard product.
        # Args:
        #     name (str): Name of the product
        #     price (float/int): Price of the product
        #     description (str): Product description
        self.name = name
        self.price = price
        self.description = description
        self._validate_price()

    def _validate_price(self):
        # Validates that the product price is a positive number.
        # Raises:
        #     ValueError: If price is negative or not a number
        if not isinstance(self.price, (int, float)) or self.price < 0:
            raise ValueError("Price must be a positive number")

    def __str__(self):
        # Returns a string representation of the product with name and price.
        return f"{self.name} - ${self.price:.2f}"

class GroomingService:
    # Represents a standard grooming service offered by Beard Masters.
    # Includes basic service attributes and pricing.
    def __init__(self, name, price, description):
        # Initialize a new grooming service.
        # Args:
        #     name (str): Name of the service
        #     price (float/int): Price of the service
        #     description (str): Service description
        self.name = name
        self.price = price
        self.description = description
        self.duration = 30  # minutes - default duration for standard service

    def get_total(self):
        # Calculates and returns the total price for the service.
        # Returns:
        #     float: Total price of the service
        return self.price

class LuxuryGroomingService(GroomingService):
    # Represents a premium grooming service that extends the standard service.
    # Includes additional luxury features like hot towel and facial treatment.
    def __init__(self, name, price, description):
        # Initialize a new luxury grooming service.
        # Args:
        #     name (str): Name of the luxury service
        #     price (float/int): Price of the luxury service
        #     description (str): Luxury service description
        super().__init__(name, price, description)
        self.duration = 60  # minutes - extended duration for luxury service
        self.includes_hot_towel = True  # Additional luxury feature
        self.includes_facial = True      # Additional luxury feature
