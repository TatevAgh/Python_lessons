# *Create a class for representing a ticket with some attributes
# (from location, to location, transport type, duration in minutes, arrival time, passenger)
# and behavior (set from/to, change transport type, increase duration by some number, set passenger),
# create several tickets and perform operations on them



class Ticket:
    def __init__(self, from_location, to_location, transport_type, duration, arrival_time, passenger):
        self.from_location = from_location
        self.to_location = to_location
        self.transport_type = transport_type
        self.duration = duration
        self.arrival_time = arrival_time
        self.passenger = passenger

    def setting_loc_from(self, new_loc):
        self.from_location = new_loc
        return self.from_location

    def setting_loc_to(self, new_to):
        self.to_location = new_to
        return self.to_location

    def changing_tr_type(self, new_transport):
        self.transport_type = new_transport
        return self.transport_type

    def increase_duration(self):
        num = int(input('write a number for increase duration: '))
        self.duration = self.duration * num
        return self.duration

    def setting_passanger(self, new_passanger):
        self.passenger = new_passanger
        return self.passenger

ticket_for_adult = Ticket('Amsterdam', 'Berlin', 'Train',  2, '15:30', 'Hylke Tomson')
ticket_for_children = Ticket('Paris', 'Moscow', 'Plane', 8, '02:45', 'Sasha Novikova')

print('Ticket for adults passanger is: ', ticket_for_adult.passenger)
print('Ticket for child passanger is: ', ticket_for_children.passenger)
print('Adults tickets New location from is', ticket_for_adult.setting_loc_from(input('Write new from location: ')))
print('Children tickets New location to is', ticket_for_children.setting_loc_to(input('Write new to location: ')))
print('Children tickets new transport type is', ticket_for_children.changing_tr_type(input('Write new transport type: ')))
print('Adults tickets increased duration time is: ', ticket_for_children.increase_duration())
print('New passenger for children ticket is :', ticket_for_children.setting_passanger(input('Write new passengers name: ')))