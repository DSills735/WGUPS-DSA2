class truck:

    def __init__(self, speed, capacity, load, packages, mileage, address, departure):
        self.speed = speed
        self.capacity = capacity
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.departure = departure


    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.speed, self.capacity,
                                               self.load, self.packages, self.mileage, self.address, self.departure)

    #def truck(self, speed, capacity, load, packages, mileage, address, departure):