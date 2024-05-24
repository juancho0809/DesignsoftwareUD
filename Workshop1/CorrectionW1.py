
"""
Solution to the first workshop of the University Distrital Francisco José de Caldas

Author: Juan Diego Lozada (correction)

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

class Vehicle:
    """This class is an abstraction of the Vehicle"""
    def __init__(self, engine, chassis:str, model:str, year:int):
        self.engine = engine
        self.chassis = chassis
        self.model = model
        self.year = year
        self.consumption = self.__calculate_gas_consumption()
        
    def __str__(self):
        return f"Nombre: {self.name}    Potencia:{self.potency}"

    def __calculate_gas_consumption(self) -> float:

        """
        This method calculates consumption based on engine values

        Returns:
        - float: The consumption of the vehicle
        """

        consumption = ((1.1 * self.engine.potency  )
                        +(0.2 * self.engine.weight)+
                        (0.3 if self.chassis == "A" else 0.5))
        return consumption

class Car(Vehicle):
    """This class represents a car"""

class Truck(Vehicle):
    """This class represents a truck"""

class Yacht(Vehicle):
    """This class represents a yacht"""

class Motorcycle(Vehicle):
    """This class represents a motorcycle"""


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
            new_obj_vehicle = Car(engine, chassis, model, year)
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
        print(vehicle)
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

