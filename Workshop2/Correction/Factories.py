


from abc import ABC

from Engines import ElectricEngine, GasEngine

class abstractEngineFactory(ABC):
    """
    This is a class abstracy factory to create engines with a factory
    """
    def create_electric_engine(self) -> ElectricEngine:
        """
        This method create an electric engine

        Returns:
        ElectricEngine
        """
    def create_gas_engine(self) -> GasEngine:
        """
        This method create a gas engine
        """
    

class HighEngineFactory(abstractEngineFactory):
    """
    THis class is a concreate factory to create expensive versiones of engines
    """

    def create_electric_engine(self) -> ElectricEngine:
        return ElectricEngine(
            torque=100,
            maximun_speed=400,
            dimmension="200x200x200",
            power=200,
            stability="high",
            weight=243.3
        )
    def create_gas_engine(self) -> GasEngine:
        return GasEngine(
            torque=200,
            maximun_speed=600,
            dimmension="200x240x200",
            power=188,
            stability="high",
            weight=225.1           
        )

class PoorEngineFactory(abstractEngineFactory):
    """
    This class is a concrete factory to create cheap versions of engines
    """

    def create_electric_engine(self) -> ElectricEngine:
       return ElectricEngine(
           torque=60,
           maximun_speed=100,
           dimmension="100x30x30",
           power=50,
           stability="Low",
           weight=54.4
       )
    def create_gas_engine(self) -> GasEngine:
        """
        dddddddddddddddddddddd
        """
        
        return GasEngine(
           torque=60,
           maximun_speed=100,
           dimmension="140x30x30",
           power=50,
           stability="Low",
           weight=54.4
        )