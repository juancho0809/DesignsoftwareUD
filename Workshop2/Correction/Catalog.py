"""
This file contains a Catalog class and an entry point 

Author: Juan Diego Lozada
"""

from typing import List
from Vehicles import Vehicle

class Catalog:

    def __init__(self) -> None:
        self.vehicles = List[Vehicle]

    def __new__(cls):
        if not hasattr(cls,"instance"):
            cls.instance = super(Catalog,cls).__new__(cls)
            cls.instance.vehicles = []
        return cls.instance
    
    def get_all_vehicles(self):
        return self.vehicles
    
    def get_price_by_range(self, min_price: float, max_price:float) -> List[Vehicle]:
        return [ vehicle for vehicle in self.vehicles if min_price<= vehicle.price <= max_price]
    
    def add_vehicle(self,vehicle: Vehicle):
        self.vehicles.append(vehicle)