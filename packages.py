import datetime
from hash_table import hash_table

#packages class for requirement B
class packages:
    def __init__(self, ID, street, city, state, zipcode, due, weight, instructions, status, out_for_delivery, time_of_delivery):
        self.ID = ID
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.due = due
        self.weight = weight
        self.instructions = instructions
        self.status = status
        self.out_for_delivery = None
        self.time_of_delivery = None

    #update the status of packages as needed for the UI

    def status_change(self, time):

        if time < self.out_for_delivery or self.out_for_delivery == None:
            self.status = 'at the hub.'
        elif self.out_for_delivery < time < self.time_of_delivery:
            self.status = 'enroute to delivery address. Will be delivered soon!'
        elif time > self.time_of_delivery:
            self.status = 'delivered!'
        # Package 9 has the incorrect address per instruction.
        # This will correct it when the info arrives at WGUPS at 10:20 AM.
        if self.ID == 9:
            if time > datetime.timedelta(hours=10, minutes=20):
                self.street = '410 S State St'
                self.zipcode = '84111'
        if self.ID in [6, 25, 28, 35] and time < datetime.timedelta(hours = 9, minutes = 5):
            self.status = 'Package delayed. Will arrive at 9:05 AM.'


    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.street, self.city,
                                                       self.state, self.zipcode, self.weight, self.instructions, self.status)