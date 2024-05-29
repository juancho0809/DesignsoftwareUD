from .memento import Memento

class Originator:
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description

    def create_memento(self):
        return Memento(self._name, self._description)

    def restore(self, memento: Memento):
        self._name = memento.name
        self._description = memento.description

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def __str__(self):
        return f"Originator: {self._name}, {self._description}"