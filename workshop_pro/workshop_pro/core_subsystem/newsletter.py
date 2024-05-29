class Newsletter:

    def __init__(self):
        self.subscribers = []

    def subscribe(self,subscriber):
        """This method subscribes a subscriber to the newsletter."""
        
        self.subscribers.append(subscriber)
        

    def unsubscribe(self, subscriber):
        """This method unsubscribes a subscriber from the newsletter."""
        
        self.subscribers.remove(subscriber)

    def send_newsletter(self, message):
        """This method sends a newsletter to all subscribers."""
        for subscriber in self.subscribers:
            subscriber.update(message)
            

