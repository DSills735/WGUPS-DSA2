import datetime
from hash_table import hash_table

#packages class for requirement B
class packages:
    def __init__(self, ID, street, city, state, zip, due, weight, instructions, status,
                 out_for_delivery, time_of_delivery):
        self.packages = packages
        self.ID = ID
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.due = due
        self.weight = weight
        self.instructions = instructions
        self.status = status
        self.out_for_delivery = None
        self.time_of_delivery = None

    #update the status of packages as needed for the UI

    def status_change(self, time):
        if time < self.out_for_delivery:
            status = 'At the hub.'
        elif time > self.out_for_delivery and time < self.time_of_delivery:
            status = 'Enroute to delivery address.'
        elif time > self.time_of_delivery:
            status = 'Delivered.'

#Package 9 has the incorrect address per instruction.
        #This will correct it when the info arrives at WGUPS at 10:20 AM.
        if self.ID == 9:
            if time > datetime.timedelta(hours = 10, minutes = 20):
                self.street = '410 S State St'
                self.zip = '84111'


