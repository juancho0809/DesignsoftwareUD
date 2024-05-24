from Catalog import Catalog
from Engines import Engine, ElectricEngine, GasEngine
from User import User,Admin,Client
from Vehicles import Car,Helicopter,Motorcycle,Scooter,Yacht,Truck
from ProxyCatalog import Proxy
from Decorator import MonitoringDecorating
from Factories import PoorEngineFactory, HighEngineFactory


if __name__ == "__main__":

    def engine():
        poor_engine_factory = PoorEngineFactory()
        high_engine_factory = HighEngineFactory()

        print("""

        Choose the type of engine:
              1) Low and Gas
              2) Low and Electric
              3) High and Gas
              4) High and Electric
              """)
        option = int(input("Please, choose an option: "))

        if option == 1:
            return poor_engine_factory.create_gas_engine()
        elif option == 2:
            return poor_engine_factory.create_electric_engine()
        elif option == 3:
            return high_engine_factory.create_gas_engine()
        elif option == 4:
            return high_engine_factory.create_electric_engine()
        else:
            return None


    def create_vehicle():
        print("""
        Choose a vehicle to add:
        1) Car
        2) Helicopter
        3) Motorcycle
        4) Scooter
        5) Yacht
        6) Truck          
              """)
        # Create the factories

        vehicle_option = int(input("Please, choose an option: "))
        if vehicle_option == 1:
            chassis = input("Enter the chassis: ")
            price = float(input("Enter the price: "))
            model = input("Enter the model: ")
            year = int(input("Enter the year: "))
            consumption = float(input("Enter the consumption: "))
            trade = input("Enter the trade: ")
            combustible_type = input("Enter the combustible type: ")
            return Car(engine(),chassis,price,model,year,consumption,trade,combustible_type)
            
    def menu():
        print("""
        Welcome to the Login Catalog
            
        1) Register as a client
        2) Register as an admin
        3) Login as a Client
        4) Login as an Admin
        5) Exit      
            """)
    def catalog_menu(user:User):
        print("""
        Welcome to the Catalog
                
        1) See all the vehicles
        2) Add a vehicle
        3) Remove a vehicle
        4) Update a vehicle
        5) Get filter by price
        6) Get filter by age
        7) Get filter by combustion
        8) Get filter by maximum speed
        9) Logout 
        """)

        catalog_option = int(input("Please, choose an option: "))
        catalog = Catalog()
        proxy = Proxy(catalog, user)

        while catalog_option != 9:
            if catalog_option == 1:
                catalog = Catalog()
                vehicles = catalog.get_all_vehicles()
                for vehicle in vehicles:
                    print(vehicle)
            elif catalog_option == 2:
                vehicle = create_vehicle
                proxy.add_vehicle(vehicle)
                if user == Client:
                    catalog_menu(Client)
                    catalog_option = int(input("Please, choose an option: "))


    menu()
    option = 0
    client = Client()
    admin = Admin()
    client= MonitoringDecorating(client)
    admin = MonitoringDecorating(admin)
    while option != 5:


        if option == 1:
            
            print("Enter your username")
            username = input()
            print("Enter your password")
            password = input()
            client.register(username, password)
            print(client.users)
            
        elif option == 2:
            
            print("Enter your username")
            username = input()
            print("Enter your password")
            password = input()
            admin.register(username, password)

        elif option == 3:
            print("Enter your username")
            username = input()
            print("Enter your password")
            password = input()
            client.login(username, password)
            print(client.users) 
            catalog_menu(Client)
                
     
        elif option == 4:
            try:
                admin = MonitoringDecorating(admin)
                print("Enter your username")
                username = input()
                print("Enter your password")
                password = input()
                admin.login(username, password)
                catalog_menu(Admin)
                     
            except:
                print("Try again.")
        else:
            print("Invalid option")
        print("\n\n")
        menu()
        option = int(input("Please, choise an option: "))
    print("Goodbye!")
        
