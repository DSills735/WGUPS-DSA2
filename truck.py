class truck:

    def __init__(self, speed, capacity, load, packages, mileage, address, departure, current_time):
        self.speed = speed
        self.capacity = capacity
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.departure = departure
        self.current_time = current_time


    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.speed, self.capacity,
                            self.load, self.packages, self.mileage, self.address, self.departure, self.current_time)

