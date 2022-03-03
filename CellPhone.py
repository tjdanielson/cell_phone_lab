
class CellPhone:
    
    def __init__(self, model, phone_number):
        self.model = model,
        self.phone_number = phone_number
        self.contacts = ['Mom', 'Dad', 'Dan', 'Katie', 'Emily']
        self.messages = []
        self.vibrate_on = True

    def create_contact(self):
        new_contact = input('Enter your contact name ')
        self.contacts.append(new_contact)
    
    def receive_text(self):
        message_received = input('Enter text to send a message to the Cell Phone ')
        self.messages.append(message_received)
        print('New Text Received: ' + message_received)

    def toggle_vibrate(self):
        if self.vibrate_on == True:
            self.vibrate_on = False
        else:
            self.vibrate_on = True

    def send_text(self):
        print('Contacts: ')
        for i in self.contacts:
            print(i)
        contact = input('Choose an above contact to send a message to')
        message_sent = input('Enter text to send a message from the Cell Phone ')
        print(f'Message to {contact} sent. Message: {message_sent}')



