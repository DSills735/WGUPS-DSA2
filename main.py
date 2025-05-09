# David Sills, Student ID Number: 011355522, WGU


import csv
import datetime
from packages import packages
from truck import truck
from hash_table import hash_table



#read the CSV files

with open("distances.csv") as csvfile:
    distance_csv = csv.reader(csvfile, delimiter=',')
    distance_csv = list(distance_csv)

with open("delivery_addresses.csv") as csvfile:
    delivery_addresses_csv = csv.reader(csvfile)
    delivery_addresses_csv = list(delivery_addresses_csv)


#initialize hash table for the packages
packages_hash_table = hash_table()
#uses the CSV information to read package data and create the parcel object
def parcel_information(file):
    with open(file) as parcel_info:
        parcel_info = csv.reader(parcel_info)
        next(parcel_info)
        for parcel in parcel_info:
            packID = int(parcel[0])
            packAddress = parcel[1]
            packCity = parcel[2]
            packState = parcel[3]
            packZip = parcel[4]
            packDeadline = parcel[5]
            packWeight = parcel[6]
            packNotes = parcel[7]
            packStatus = 'At hub'
            pack_out_for_delivery = None
            pack_time_of_delivery = None

            parcel = packages(packID, packAddress, packCity, packState, packZip, packDeadline, packWeight, packNotes, packStatus, pack_out_for_delivery,pack_time_of_delivery)
            #print(packID, parcel)
            packages_hash_table.table_add(packID, parcel)

            #test below delete or comment before submitting
            #return print(parcel)
parcel_information("package.csv")
#find the distance between curr location and next delivery
def distances(x, y):
    distance = distance_csv[x][y]
    if distance == '':
        distance = distance_csv[y][x]
    return float(distance)

#distance to find next address
def delivery_address(address_to_find):
    for row in delivery_addresses_csv:
        if address_to_find.strip().lower() in row[2].strip().lower():
            return int(row[0])

#Is the hash table populating test code. Current is Yes populating
#for bucket in packages_hash_table.table:
 #   if bucket:
  #      for entry in bucket:
   #         print(f"ID: {entry[0]}, Address: {entry[1].street}")

#load the trucks with the packages and set their time to go out for delivery. I chose to manually load the trucks
truck1 = truck(18, 16, 0.0, [1, 13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 37, 40], 0.0, '4001 South 700 East', datetime.timedelta(hours = 8), datetime.timedelta(hours = 8))
#packages 3, 18, 37, 38 must be on truck2, package 9 cannot be delivered until 1020 at the earliest d/t wrong delivery address
truck2 = truck(18, 16, 0.0, [2, 3, 4, 5, 9, 18, 26, 28, 32, 35, 36, 38], 0.0, '4001 South 700 East', datetime.timedelta(hours = 10, minutes = 20), datetime.timedelta(hours = 10, minutes = 20) )
#A few of these packages cannot leave shop until 905.
truck3 = truck(18, 16, 0.0, [6, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 25, 33, 39], 0.0, '4001 South 700 East', datetime.timedelta(hours = 9, minutes = 5), datetime.timedelta(hours = 9, minutes = 5))
all_trucks = [truck1, truck2, truck3]
#nearest neighbor algorithm for delivery.
def delivery(truck):
    packages_on_truck = []
    distance_travelled = 0.0
    for packageID in truck.packages:
        #print(truck.packages )
        package = packages_hash_table.hash_search(packageID)
        #print(package)
        packages_on_truck.append(package)
    truck.packages.clear()
#initializzes current time to adequately keep track of the truck.
    truck.current_time = truck.departure

    #print(truck.packages)
    while len(packages_on_truck) > 0:
        next_delivery_dist = 10000
        #iterates over packages on truck to ensure delivery of the closest package.
        for package in packages_on_truck:
            #print(truck.address, package)
            next_package = package
            next_package.out_for_delivery = truck.current_time

            if distances(delivery_address(truck.address), delivery_address(package.street)) <= next_delivery_dist:
                next_delivery_dist = distances(delivery_address(truck.address), delivery_address(package.street))
                next_package = package
        if next_package:
            #if next package is true update the variables for comparison
            truck.packages.append(next_package.ID)
            truck.address = package.street
            #print('ID = ' , next_package.ID)
            #calculates time by using the avg truck speed
            truck.current_time += datetime.timedelta(hours=next_delivery_dist / 18)

            next_package.time_of_delivery = truck.current_time
            #print(next_package.time_of_delivery)


            #remove the package and track miles travelled.
            packages_on_truck.remove(next_package)
            distance_travelled += next_delivery_dist


    #finalize milage for truck object
    truck.mileage = distance_travelled
#finalizze times for truck object, so the third can leave ASAP.
truck_1_completed = truck1.current_time
truck_2_completed = truck2.current_time


#begin delivery for 3 trucks
delivery(truck1)

delivery(truck2)
#once a truck is completed, start the third
truck3.departure = min(truck1.departure, truck2.departure)
delivery(truck3)

#Should be ~105.39 Miles travelled. Requirement for this is 140
#('Truck 1:', truck1.mileage)
#print('Truck 2:', truck2.mileage)
#print('Truck 3', truck3.mileage)
#Departure Times for testing
#print('Truck 1 Departure:', truck1.departure)
#print('Truck 2 Departure:', truck2.departure)
#print('Truck 3 Departure:', truck3.departure)
#Completion Times for testing
#print('Truck 1 Complete:', truck1.current_time)
#print('Truck 2 Complete:', truck2.current_time)
#print('Truck 3 Complete:', truck3.current_time)
#print('Total:', truck3.mileage + truck2.mileage + truck1.mileage)

#user interface begin:
class main:
    print('Welcome to WGUPS User Interface, brought to you by David Sills.')
    print('Choose an option below to begin:')
    print('--------------------------------------------------------------------')
    print('1: Track a single package using the ID Number')
    print('2: Track the status of all packages at a given time')
    print('3: Track the total mileage of all delivery apparatus for the day')
    choice = input('4: Quit\n')
    if choice == '1':
        id_to_track = int(input('Enter the ID Number you wish to track: '))
        time = input('Enter the current time(HH:MM): ')
        #time conversion and package status update.
        hour, minute = time.split(':')
        timeinput = datetime.timedelta(hours = int(hour), minutes = int(minute))
        package = packages_hash_table.hash_search(id_to_track)
        package.status_change(timeinput)
        #iterate over the truck to find the ID in a specific truck.
        for i, truck in enumerate(all_trucks, start=1):
            if id_to_track in truck.packages:
                print(f'This package is assigned Truck #{i}, and its status is {package.status}', end = ' ')
                if package.status == 'delivered!':
                    print(f'It was delivered at {package.time_of_delivery}')

    if choice == '2':

        #same time conversion as before
        time = input('Enter the time that you would like to see the status of each package for. (HH:MM): ')
        hour, minute = time.split(':')
        timeinput = datetime.timedelta(hours=int(hour), minutes=int(minute))
#iterate over all packages to show their time and ID.
        for package in range(1, 41):
            package = packages_hash_table.hash_search(package)
            package.status_change(timeinput)
            print('ID:', str(package.ID) + ': ' + package.status, end = ' ')
            if package.status == 'delivered!':
                print(f'It was delivered at {package.time_of_delivery}')
                #print a newline if the package hasnt been delivered
            else:
                print()
#show the total miles.
    if choice == '3':
        print('The total miles travelled by our units today is:', truck1.mileage + truck2.mileage + truck3.mileage)
        #exit the program.
    if choice == '4':
        quit()

    #print('Package with ID: {id_to_track} status: {status}')
    #print('Tracking package %s' % package.status)
#program completed here. Please note I did leave several prints and notes to myself in as well
#I left those as I felt they also satisfied the requirement for C2