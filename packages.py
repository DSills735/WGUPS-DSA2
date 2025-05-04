import datetime
from hash_table import hash_table

#packages class for requirement B
class packages:
    def __init__(self, ID, street, city, state, zip, due, weight, instructions, status,
                 out_for_delivery = None, time_of_delivery = None):
        self.ID = ID
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.due = due
        self.weight = weight
        self.instructions = instructions
        self.status = status
        self.out_for_delivery = out_for_delivery
        self.time_of_delivery = time_of_delivery

    #update the status of packages as needed for the UI

    def status_change(self, time):
        if time < self.out_for_delivery:
            self.status = 'At the hub.'
        elif time > self.out_for_delivery and time < self.time_of_delivery:
            self.status = 'Enroute to delivery address.'
        elif time > self.time_of_delivery:
            self.status = 'Delivered.'

#Package 9 has the incorrect address per instruction.
        #This will correct it when the info arrives at WGUPS at 10:20 AM.
        if self.ID == 9:
            if time > datetime.timedelta(hours = 10, minutes = 20):
                self.street = '410 S State St'
                self.zip = '84111'


    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.street, self.city,
                                                       self.state, self.zip, self.weight, self.instructions, self.status)