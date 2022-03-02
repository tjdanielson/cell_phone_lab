
class CellPhone:
    
    def __init__(self, model):
        self.model = model,
        self.phone_number = '555-555-5555'
        self.contacts = []
        self.messages = []
        self.vibrate_on = True
    
    def receive_text(self, message):
        message = input('Enter text to send a message to the Cell Phone')
        self.messages.append(message)
        print('New Text Received: ' + message)

    def toggle_vibrate(self):
        pass

    def send_text(self):
        pass


