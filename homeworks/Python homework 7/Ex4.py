# *Create a collection of hotel rooms (room number, state (booked or not), type (econom, business, lux)),
# calculate how many rooms are booked (create a function), calculate how many numbers of different types by
# default lux numbers are free (create a function), generate a collection of econom numbers, print results

hotel_rooms = {300: ['Not Booked', 'econom'], 301: ['Not Booked', 'business'], 302: ['Not Booked', 'business'], 303: ['Booked', 'lux'], 304: ['Booked', 'econom'],
               305: ['Not Booked', 'econom'], 306: ['Booked', 'econom'], 307: ['Booked', 'lux'], 308: ['Not Booked', 'lux'], 309: ['Not Booked', 'business']}

def booked_rooms(rooms):
    count = 0
    for room in rooms.values():
        if 'Booked' in room:
            count += 1
    return count

def free_rooms_by_type(rooms, type):
    count = 0
    for room in rooms.values():
        if room[0] == 'Not Booked' and room[1] == type:
            count += 1
    return count

def genereting_econom_rooms(rooms):
    econom_rooms = []
    for room in rooms.items():
        if room[1][1] == 'econom':
            econom_rooms.append(room)
    return econom_rooms

print(genereting_econom_rooms(hotel_rooms), 'thle collection of econom rooms')
print(free_rooms_by_type(hotel_rooms, 'lux'), 'count of free rooms with Lux type')
print(free_rooms_by_type(hotel_rooms, 'business'), 'count of free rooms with business type')
print(free_rooms_by_type(hotel_rooms, 'econom'), 'count of free rooms with econom type')
print(booked_rooms(hotel_rooms), 'rooms are booked in Hotel')
