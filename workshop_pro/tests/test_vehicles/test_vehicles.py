from workshop_pro.engines_subsystem.engines import Engine,ElectricEngine
from workshop_pro.vehicles_subsystem import Vehicle
from workshop_pro.vehicles_subsystem.validation_chassis import ValidationChassis
from workshop_pro.vehicles_subsystem.validation_model import ValidationModel
from workshop_pro.vehicles_subsystem.validation_price import ValidationPrice
from workshop_pro.vehicles_subsystem.validation_year import ValidationYear
import unittest

class TestVehicles(unittest.TestCase):

    """This class tests the validation of the vehicle."""

    @classmethod

    def setUpClass(cls):
        cls.vehicle1 = {
            "model": "Mazda",
            "year": 2020,
            "price": 30000000,
            "chassis": "A",          
        }
        cls.vehicle2 = {
            "model": "fsfdsdsc+++++423dndskldsvnkfdjasx",
            "year": 1890,
            "price": 20000000000,
            "chassis": "D",          
        }

    def test_validation_vehicle_year(self):
        """This method tests the validation of the year of the vehicle."""
        engine_test = Engine(100, 200, "100x100x100", 150, "medium", 100.5)
        vehicle = Vehicle(
            self.vehicle1["chassis"],
            self.vehicle1["price"],
            engine_test,
            self.vehicle1["model"],
            self.vehicle1["year"],
        )
        validation = ValidationYear()
        self.assertFalse(validation.is_invalid(vehicle))
        vehicle.year = self.vehicle2["year"]
        self.assertTrue(validation.is_invalid(vehicle))

    def test_validation_vehicle_chassis(self):
        """This method tests the validation of the chassis of the vehicle."""
        engine_test = Engine(100, 200, "100x100x100", 150, "medium", 100.5)
        vehicle = Vehicle(
            self.vehicle1["chassis"],
            self.vehicle1["price"],
            engine_test,
            self.vehicle1["model"],
            self.vehicle1["year"],
        )
        validation = ValidationChassis()
        self.assertFalse(validation.is_invalid(vehicle))
        vehicle.chassis = self.vehicle2["chassis"]
        self.assertTrue(validation.is_invalid(vehicle))

    def test_validation_vehicle_model(self):
        """This method tests the validation of the model of the vehicle."""
        engine_test = Engine(100, 200, "100x100x100", 150, "medium", 100.5)
        vehicle = Vehicle(
            self.vehicle1["chassis"],
            self.vehicle1["price"],
            engine_test,
            self.vehicle1["model"],
            self.vehicle1["year"],
        )
        validation = ValidationModel()
        self.assertFalse(validation.is_invalid(vehicle))
        vehicle.model = self.vehicle2["model"]
        self.assertTrue(validation.is_invalid(vehicle))

    def test_validation_vehicle_price(self):
        """This method tests the validation of the price of the vehicle."""
        engine_test = Engine(100, 200, "100x100x100", 150, "medium", 100.5)
        vehicle = Vehicle(
            self.vehicle1["chassis"],
            self.vehicle1["price"],
            engine_test,
            self.vehicle1["model"],
            self.vehicle1["year"],
        )
        validation = ValidationPrice()
        self.assertFalse(validation.is_invalid(vehicle))
        vehicle.price = self.vehicle2["price"]
        self.assertTrue(validation.is_invalid(vehicle))
