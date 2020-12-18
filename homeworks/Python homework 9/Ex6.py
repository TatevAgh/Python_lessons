# *Create a class for representing building with some attributes and behavior,
# create a classes for representing hotel building with specific attributes and behavior,
# create objects and use them

class Building:
    def __init__(self, count_floor, count_elevator, rooms, parking_place):
        self.count_floor = count_floor
        self.count_elevator = count_elevator
        self.rooms = rooms
        self.parking_place = parking_place

    def show_info(self):
        print('Count of floors is:', self.count_elevator)
        print('Count of elevator is:', self.count_elevator)
        print('Showing rooms:', list(map(lambda room: room, self.rooms)))
        print('Parking places count:', self.parking_place)


class Opera_Hotel(Building):
    def __init__(self, count_floor, count_elevator, rooms, parking_place, staff, swimming_pool):
        Building.__init__(self, count_floor, count_elevator, rooms, parking_place)
        self.staff = staff
        self.swimming_pool = swimming_pool

    def free_rooms(self):
        self.free_rooms = []
        for room in self.rooms.items():
            if room[1][0] == 'Not Booked':
                self.free_rooms.append(room[0])
        return self.free_rooms

    def increase_elevator(self):
        self.count_elevator *= 2
        return self.count_elevator

class Marriot_hotel(Building):
    def __init__(self, count_floor, count_elevator, rooms, parking_place, staff, swimming_pool):
        Building.__init__(self, count_floor, count_elevator, rooms, parking_place)
        self.staff = staff
        self.swimming_pool = swimming_pool

    def showing_info(self):
        Building.show_info()
        print('Swimming pools:', self.swimming_pool)

    def employees_first_smb(self):
        for name in self.staff.items():
            if name[0][0].lower() == 'a':
                print('Employee name starts with A:', name[0])


hotel_rooms = {300: ['Not Booked', 'econom'], 301: ['Not Booked', 'business'], 302: ['Not Booked', 'business'],
                       303: ['Booked', 'lux'], 304: ['Booked', 'econom'],
                       305: ['Not Booked', 'econom'], 306: ['Booked', 'econom'], 307: ['Booked', 'lux'],
                       308: ['Not Booked', 'lux'], 309: ['Not Booked', 'business']}

hotel_staff = {'Abid Jak': 'Manager', 'John Bailley': 'Accountant', 'Ace Smith': 'Administartor', 'John Jamal': 'Engineer',
             'Jack Smith': 'Security agent', 'Jamaal Smith': 'CEO'}
swimming_pool_types =  ['Outdoor pool', 'Indoor pool']
opera = Opera_Hotel(16, 3, hotel_rooms, 15, hotel_staff,swimming_pool_types[1])
marriot = Marriot_hotel(16, 3, hotel_rooms, 15, hotel_staff,swimming_pool_types[0])
opera.show_info()
marriot.show_info()
print(opera.free_rooms())
print(opera.increase_elevator())
marriot.employees_first_smb()
