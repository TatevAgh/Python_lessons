# *Create a class for representing a smartphone with related attributes
# (private, public, protected) and behavior, create objects and use them

class Smartphone:
    def __init__(self, model, camera, storage, color, serial_number, password):
        self.model = model
        self.camera = camera
        self.storage = storage
        self.color = color
        self.serial_number = serial_number
        self.__password = password

    def print_password(self, not_robot):
        if not_robot == self.color:
            print('Your phone\'s password is:', self.__password)
        else:
            print('Your answer is wrong !!!')

    def stolen_phone(self):
        if self.serial_number:
            self.__password = int(input('write a new password: '))

    def available_storage(self):
        used_storage = int(input('Write used storage: '))
        self.available_storage = self.storage - used_storage
        print('Your smartphone\'s availble storage is:', self.available_storage)


class Iphone(Smartphone):
    def __init__(self, model, camera, storage, color, serial_number, password, software_version):
        Smartphone.__init__(self, model, camera, storage, color, serial_number, password)
        self.software_version = software_version

    def update_software(self):
        if self.software_version < 16:
            return self.software_version + 0.01


my_iphone11 = Iphone('11', 15, 128, 'Purple', 451025446, 5241, 14.23)
s_20 = Smartphone('S 20', 13, 256, 'White', 7876976, 8888)
my_iphone11.print_password(input('If you are not a robot then write the correct answer. \n Your iphone\'s color: ').lower())
my_iphone11.available_storage()
print('Your Iphone updated ios version is:  ', my_iphone11.update_software())
s_20.stolen_phone()



