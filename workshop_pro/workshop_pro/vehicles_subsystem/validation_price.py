from .vehicle_validation import VehicleValidation
from .vehicle import Vehicle

class ValidationPrice(VehicleValidation):
    """This class validates the price of the vehicle."""

    def is_invalid(self, vehicle: Vehicle):
        """This method validates the price of the vehicle."""
        if vehicle.price < 20000000 or vehicle.price > 500000000:
            return True
        return False