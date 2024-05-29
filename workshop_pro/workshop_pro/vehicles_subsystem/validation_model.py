from workshop_pro.vehicles_subsystem.vehicle import Vehicle
from .vehicle_validation import VehicleValidation
import re

class ValidationModel(VehicleValidation):
    """This class validates the model of the vehicle."""

    def is_invalid(self, vehicle: Vehicle):
        """This method validates the model of the vehicle."""
        if len(vehicle.model) > 30:
            return True
        elif not re.match("^[a-zA-Z0-9]*$", vehicle.model):
            return True
        return False