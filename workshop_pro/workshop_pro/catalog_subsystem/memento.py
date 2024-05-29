class Memento:
    def __init__(self, name,state):
        self._name = name
        self._state = state

    def get_state(self):
        return self._state