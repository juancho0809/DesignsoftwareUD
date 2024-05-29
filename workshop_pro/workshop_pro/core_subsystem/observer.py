from abc import abstractmethod

class Observer:
    """This class represents the behavior of an observer into the application."""

    @abstractmethod
    def update(self, message: str):
        """This method updates the observer with a message."""
        pass