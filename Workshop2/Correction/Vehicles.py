from Engines import Engine


class Vehicle:
    """
    This class represents an abstraction of a vehicle
    """

    def __init__(
        self,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
    ):
        self.engine = engine
        self.chassis = chassis
        self.price = price
        self.model = model
        self.year = year
        self.consumption = consumption
    #pylint: disable = too-many-arguments
    def __str__(self) -> str:
        return f"Vehicle: {self.model}"


class Helicopter(Vehicle):
    """
    dsadadasdasdsad
    """


class Motorcycle(Vehicle):
    """
    sdddddddddddd
    """


class Scooter(Vehicle):
    """
    dddddddddddd
    """


class Car(Vehicle):
    """
    This is a concrete implementation of a car
    """

    def __init__(
        self,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
        transmission: str,
        trade: str,
        combustible_type: str,
    ):
        super().__init__(engine, chassis, price, model, year, consumption)
        self.transmission = transmission
        self.trade = trade
        self.combustible_type = combustible_type


class Truck(Vehicle):
    """
    This is a concreate implementation of a truck
    """

    def calculate_gas_consumption(self):
        """
        Calculate the gas consumption based on engines values
        """
        consumption = (
            (1.1 * self.engine.power)
            + (0.2 * self.engine.weight)
            + (0.3 if self.chassis == "A" else 0.5)
        )
        return consumption


class Yacht(Vehicle):
    """
    This is a concreate implementation of a yacht
    """
    def __init__(
        self,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
        length: int,
        weight: float,
        trade: str,
    ):
        super().__init__(engine, chassis, price, model, year, consumption)
        self.lenght = length
        self.weight = weight
        self.trade = trade
