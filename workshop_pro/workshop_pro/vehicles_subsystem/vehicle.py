"""
This file has an abstrac class called Vehicle as reference
for all the vehicles to have in the application.

Author: Carlos Sierra <cavirguezs@udistrital.edu.co>
"""

from abc import ABC

from ..engines_subsystem import Engine


class Vehicle(ABC):
    """
    This represents the behavior of any vehicle into the application.

    Methods:
        is_in_year -> bool: This method returns if the vehicle is in the range of years.
        is_in_speed -> bool: This method returns if the vehicle is in the range of speeds.
        is_in_price -> bool: This method returns if the vehicle is in the range of prices.
        is_chassis -> bool: This method returns if the vehicle has the same chassis.
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self, chassis: str, price: float, engine: Engine, model: str, year: int
    ):
        self.chassis = chassis
        self.price = price
        self.engine = engine
        self.model = model
        self.year = year

    def is_in_year(self, min_year: int, max_year: int):
        """This method returns if the vehicle is in the range of years."""
        return self.year >= min_year and self.year <= max_year

    def is_in_speed(self, min_speed: int, max_speed: int):
        """This method returns if the vehicle is in the range of speeds."""
        return self.engine.is_in_speed(min_speed, max_speed)

    def is_in_price(self, min_price: float = 0, max_price: float = float("inf")):
        """This method returns if the vehicle is in the range of prices."""
        return self.price >= min_price and self.price <= max_price

    def is_chassis(self, chassis: str):
        """This method returns if the vehicle has the same chassis."""
        return self.chassis == chassis

    def __str__(self):
        return f"Model: {self.model}\n\
                Year: {self.year}\n\
                Chassis: {self.chassis}\n\
                Price: {self.price}\n\
                Engine: {str(self.engine)}"
