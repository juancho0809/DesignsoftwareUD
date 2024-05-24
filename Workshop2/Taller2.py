from abc import ABC
"""
Solution to the second workshop of the University Distrital Francisco José de Caldas

Author: Juan Diego Lozada

"""

class Engine:
    """This class represetns the behaviour of the engine of the car"""

    def __init__(self, name:str, type_engine:str , potency:int , weight:float ):
        self.name = name
        self.type_ = type_engine
        self.potency = potency
        self.weight = weight

    def __str__(self):
        return f"Nombre: {self.name}    Potencia:{self.potency}"


#Abstract factory to create engine low and high gama

class FactoryEngine(ABC):
    """This class represents the behaviour of the engine of the furniture"""

    def create_engine(self) -> Engine:
        pass

class FactoryEngineHigh(FactoryEngine):
    """This class represents the behaviour of the engine of the furniture"""

    def create_engine(self) -> Engine:
        return Engine("High", "Gasoline", 200, 100)

class FactoryEngineLow(FactoryEngine):
    """This class represents the behaviour of the engine of the furniture"""

    def create_engine(self) -> Engine:
        return Engine("Low", "Gasoline", 150, 80)
    

class LowFurniture(FactoryEngine):
    def create_engine(self) -> Engine:
        return FactoryEngineLow()

class HighFurniture(FactoryEngine):
    def create_engine(self) -> Engine:
        return FactoryEngineHigh()




class Vehicle:
    """This class is an abstraction of the Vehicle"""
    def __init__(self, engine, chassis:str, model:str, year:int):
        self.engine = engine
        self.chassis = chassis
        self.model = model
        self.year = year
        
    
    def get_engine(self) -> Engine:
        """
        This method returns the engine of the vehicle.

        Returns:
        - Engine: engine of the vehicle
        """
        return self.__engine

    def get_year(self) -> int:
        """
        This method returns the year of the vehicle.

        Returns:
        - int: year of the vehicle
        """
        return self.__year
        
    def __str__(self):
        return f"Nombre: {self.name}    Potencia:{self.potency}"


class FactoryVehicleType(ABC):
    """This class represents the behaviour of the engine of the furniture"""

    def create_vehicletype(self) -> Vehicle:
        pass

class GasVehicleType(Vehicle):
    def type_vehicle(self) -> Vehicle:
        return "Gasoline"

class ElectricVehicleType(Vehicle):
    def type_vehicle(self) -> Vehicle:
        return "Electric"

class GasVehicleType(FactoryVehicleType):
    re






class Car(Vehicle):
    """This class represents a car"""
    def __init__(self, engine, chassis: str, model: str, year: int, transmision:str, trade:str,combustible_type:str):
        super().__init__(engine, chassis, model, year,)
        self.transmision = transmision
        self.trade = trade
        self.combustible_type = combustible_type



class Truck(Vehicle):
    """This class represents a truck"""
    def __init__(self, engine, chassis: str, model: str, year: int, max_weight:int,trade:str):
        super().__init__(engine, chassis, model, year)
        self.max_weight = max_weight
        self.trade = trade
        self.__consumption = self.__calculate_gas_consupmtion()

    def __calculate_gas_consumption(self) -> float:


        consumption = ((1.1 * self.engine.potency  )
                        +(0.2 * self.engine.weight)+
                        (0.3 if self.chassis == "A" else 0.5))
        return consumption

class Yacht(Vehicle):
    """This class represents a yacht"""
    def __init__(self, engine, chassis: str, model: str, year: int,length:int,weight_yacht:float,trade:str):
        super().__init__(engine, chassis, model, year)
        self.length = length
        self.weight_yacht = weight_yacht
        self.trade = trade


class Motorcycle(Vehicle):
    """This class represents a motorcycle"""


class Helicopter(Vehicle):
    """This class represents a helicopter"""
    def __init__(self, engine, chassis: str, model: str, year: int, weight_helicopter:float, tripulation_max:int):
        super().__init__(engine, chassis, model, year)
        self.weight_helicopter = weight_helicopter
        self.tripulation_max = tripulation_max

class Scooter(Vehicle):
    """This class represents a scooter"""
    def __init__(self, engine, chassis: str, model: str, year: int, color:str, type_wheels:str):
        super().__init__(engine, chassis, model, year)
        self.color = color
        self.type_wheels = type_wheels



MESSAGE = """

    Welcome to the vehicle workshop
    Options:
    1. Create a car
    2. Create a truck
    3. Create a yacht
    4. Create a motorcycle
    5. Create an engine
    6. Show Engine
    7. Show Vehicle
    8. Search Vehicle by year
    9. Search Vehicle by potency
    10. Exit
    """

engines = {}
vehicles = [] 

def create_engine():
    """This function creates an engine and returns it
        Parameters: None
    """
    name = input("Please enter the name of the engine: ")
    type_engine = input("Please enter the type of the engine: ")
    potency = int(input("Please enter the potency of the engine: "))
    weight = float(input("Please enter the weight of the engine: "))
    
    new_obj_engine = Engine(name, type_engine, potency, weight)
    engines[name] = new_obj_engine

def create_vehicle(type_vehicle:str):
    """This function creates a vehicle and returns it
        Parameters: type_vehicle: str
    """
    chassis = input("Write the chassis of the vehicle: ")
    if chassis not in ["A", "B"]:
        raise ValueError("Invalid chassis")
        
    model = input("Write the model of the vehicle: ")
    year = int(input("Write the year of the vehicle: "))


    if year < 2010:
        raise ValueError("Invalid year")
    engine_name = input("Write the name of the motor for the vehicle")
    try:
        engine = engines[engine_name] 
        if type_vehicle == "car":
            transmision = input("Write the transmision of the vehicle: ")
            trade = input("Write the trade of the vehicle: ")
            combustible_type = input("Write the combustible type of the vehicle: ")
            new_obj_vehicle = Car(engine, chassis, model, year, transmision, trade, combustible_type)
        elif type_vehicle == "truck":
            new_obj_vehicle = Truck(engine, chassis, model, year)
        elif type_vehicle == "yacht":
            new_obj_vehicle = Yacht(engine, chassis, model, year)
        elif type_vehicle == "motorcycle":
            new_obj_vehicle = Motorcycle(engine, chassis, model, year)             
        vehicles.append(new_obj_vehicle)
    except Exception as e:
        print(f"Error: {e}")    

def search_vehicle_by_year(year:int) -> list:
    """This function searches a vehicle by year
        Parameters: year: int
    """
    return [vehicle for vehicle in vehicles if vehicle.year == year]

def search_vehicle_by_potency(potency:int):
    """This function searches a vehicle by potency
        Parameters: potency: int
    """
    return [vehicle for vehicle in vehicles if vehicle.engine.potency == potency]

print(MESSAGE)
option = int(input("Please select an option: "))
while option != 10:
    if option == 1:
        create_vehicle("car")
    elif option == 2:
        create_vehicle("truck")
    elif option == 3:
        create_vehicle("yacht")
    elif option == 4:
        create_vehicle("motorcycle")
    elif option == 5:
        create_engine()
    elif option == 6:
        for name, values in engines.items():
            print(f"{name} ) {str(values)}")
    elif option == 7:
        print(Vehicle)
    elif option == 8:
        year = int(input("Please enter the year: "))
        search_vehicle_by_year(year)
    elif option == 9:
        potency = float(input("Please enter the potency: "))
        search_vehicle_by_potency(potency)
    else:
        print("Invalid option")
    print(MESSAGE)  
    option = int(input("Please select an option: "))

