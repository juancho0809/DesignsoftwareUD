from .vehicle import Vehicle
from .vehicle_validation import VehicleValidation

class ValidationYear(VehicleValidation):
    """This class validates the year of the vehicle."""

    def is_invalid(self, vehicle: Vehicle):
        """This method validates the year of the vehicle."""
        if vehicle.year < 1990 or vehicle.year > 2022:
            return True
        return False