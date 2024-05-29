from .vehicle import Vehicle
from .vehicle_validation import VehicleValidation

class ValidationChassis(VehicleValidation):
    
    """This class validates the chassis of the vehicle."""

    def is_invalid(self, vehicle: Vehicle):
        """This method validates the chassis of the vehicle."""
        if not vehicle.chassis == "A" or vehicle.chassis == "B":           
            return True
        return False