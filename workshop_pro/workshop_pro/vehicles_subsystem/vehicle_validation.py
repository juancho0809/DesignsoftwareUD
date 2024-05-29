
from .vehicle import Vehicle

class VehicleValidation: 
    """This class represents the behavior of a vehicle validation into the application."""

    def __init__(self, next_filter=None):
        self.next_filter = next_filter

    def process(self,vehicle:Vehicle):
        """ This method process the vehicle to validate it."""
        if self.is_invalid(vehicle):
            print("Invalid vehicle")
        elif self.next_filter:
            self.next_filter.process(vehicle)
        elif self.next_filter:
            self.next_filter.process(vehicle)
        elif self.next_filter:
            self.next_filter.process(vehicle)
        else:
            print("Vehicle is valid")

    def is_invalid(self, vehicle: Vehicle):
        """This method returns if the vehicle is invalid."""
        print(f"Validating vehicle {vehicle}")
        return False