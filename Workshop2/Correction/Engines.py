#pylint: disable = too-many-arguments
"""
This file make a bullshit
Remember install pip install black
Black Formatter
pip install pyliny
Pyliny
This file has some classes related to the implementation of an Abstract Factory Pattern Design
"""

class Engine:
    """
    This class represetns an abstraction og a engine for any vehicle
    """

    def __init__(
        self,
        torque: int,
        maximun_speed: int,
        dimmension: str,
        power: int,
        stability: str,
        weight: float,
    ):
        
        self.torque = torque
        self.maximun_speed = maximun_speed
        self.dimmension = dimmension
        self.power = power
        self.stability = stability
        self.weight = weight


        
class GasEngine(Engine):
    """
    This class represents
    """
   
class ElectricEngine(Engine):
    """
    This class represents
    
    """