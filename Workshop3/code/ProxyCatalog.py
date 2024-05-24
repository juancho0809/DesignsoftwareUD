from typing import List
from Vehicles import Vehicle
from Catalog import Catalog, CatalogInterface
from User import User,Admin

class Proxy(CatalogInterface):
    def __init__(self, catalog: Catalog, user: User):
        self.catalog = catalog 
        self.user = user 

    def get_all_vehicles(self) -> List[Vehicle]:
        
        return self.catalog.get_all_vehicles()

    def get_price_by_range(self, min_price: float, max_price: float) -> List[Vehicle]:
        
        return self.catalog.get_price_by_range(min_price, max_price)

    def add_vehicle(self, vehicle: Vehicle):
        if self.user !=  Admin:
            print("You do not have permission to add vehicles")
        else:
            self.catalog.add_vehicle(vehicle)
        

    def delete_vehicle(self, vehicle: Vehicle):
        if isinstance(self.user, Admin):
            self.catalog.delete_vehicle(vehicle)
        else:
            print("You do not have permission to delete vehicles")

    def update_vehicle(self, vehicle: Vehicle):
        
        pass

    def filter_by_age():
        pass

    def filter_by_combustion():
        pass

    def filter_by_maximum_speed():
        pass