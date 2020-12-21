# *Create a class for representing a smartphone with related attributes
# (private, public, protected) and behavior, create objects and use them

class Smartphone:
    def __init__(self, model, camera, storage, color, serial_number, password):
        self.model = model
        self.camera = camera
        self.storage = storage
        self.color = color
        self.serial_number = serial_number
        self.password = password



class Iphone(Smartphone):
    def __init__(self, model, camera, storage, color, serial_number, password, software_version):
        Smartphone.__init__(self, model, camera, storage, color, serial_number, password)
        self.software_version = software_version




