from CellPhone import CellPhone

#instantiate a new cell phone - fyi, took some liberties here, didn't think it made sense for all cell phones to have the same number
tessas_phone = CellPhone('Pixel', '555-555-5555')
print('Tessas Phone Number: ' + tessas_phone.phone_number)

#bonus (not in instructions) add contacts to cell phone
# tessas_phone.create_contact()
# tessas_phone.create_contact()

#Print the cell phone's contacts to the terminal
print('Contacts: ')
print(tessas_phone.contacts)

#Send two new messages to the phone through the receive text message method'
tessas_phone.receive_text()
tessas_phone.receive_text()

#Print the cell phone's messages to the terminal
print(tessas_phone.messages)

#Call the create text message method to create a new message
tessas_phone.send_text()

#Toggle the cell phones ringer to vibrate
print('Vibrate Currently On? ' + str(tessas_phone.vibrate_on))
tessas_phone.toggle_vibrate()

#Print the cell phone's current ringer/vibrate setting to the terminal
print('Vibrate Currently On? ' + str(tessas_phone.vibrate_on))