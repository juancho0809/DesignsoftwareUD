from datetime import datetime
from User import User

class MonitoringDecorating(User):
    def __init__(self, user: User):
        super().__init__()
        self.wrapped = user

    def login(self, username, password):
        self.__monitor_start()
        self.wrapped.login(username, password)
        self.__monitor_end()

    def register(self, username, password):
        self.__monitor_start()
        self.wrapped.register(username, password)
        self.__monitor_end()

    def logout(self, username):
        self.__monitor_start()
        self.wrapped.logout(username)
        self.__monitor_end()

    def __monitor_start(self):
        """This method logs the start of the monitoring."""
        print(f"== Monitoring started at: {datetime.now()}")

    def __monitor_end(self):
        """This method logs the end of the monitoring."""
        print(f"== Monitoring ended at: {datetime.now()}\n")