# David Sills, Student ID Number: 011355522, WGU

import csv
import datetime
from packages import packages
from truck import truck
from hash_table import hash_table



#read the three CSV files
with open("package.csv") as csvfile:
    package_csv = csv.reader(csvfile)
    package_csv = list(package_csv)

with open("distances.csv") as csvfile:
    distance_csv = csv.reader(csvfile)
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
            packID = parcel[0]
            packAddress = parcel[1]
            packCity = parcel[2]
            packState = parcel[3]
            packZip = parcel[4]
            packDeadline = parcel[5]
            packWeight = parcel[6]
            packNotes = parcel[7]
            packStatus = 'At hub'

            parcel = packages(packID, packAddress, packCity, packState, packZip, packDeadline, packWeight, packNotes, packStatus)
            packages_hash_table.table_add(packID, parcel)

            #test below delete or comment before submitting
            #return print(parcel)

#find the distance between curr location and next delivery
def distances(x, y):
    distance = distance_csv[x][y]
    if distance == '':
        distance = distance_csv[y][x]
    return float(distance)

#distance to find next address
def delivery_address(address_to_find):
    for row in delivery_addresses_csv:
        if address_to_find == row[2]:
            return int(row[0])


parcel_information("package.csv")

#load the trucks with the packages and set their time to go out for delivery. I chose to manually load the trucks
#packages loaded: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40 ALL LOADED

truck1 = truck(18, 16, 0.0, [1, 13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 37, 40], 0.0, '4001 South 700 East', datetime.timedelta(hours = 8))
#packages 3, 18, 37, 38 must be on truck2, package 9 cannot be delivered until 1020 at the earliest d/t wrong delivery address
truck2 = truck(18, 16, 0.0, [2, 3, 4, 5, 9, 18, 26, 28, 32, 35, 36, 38], 0.0, '4001 South 700 East', datetime.timedelta(hours = 10, minutes = 20))
#A few of these packages cannot leave shop until 905.
truck3 = truck(18, 16, 0.0, [6, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 25, 33, 39], 0.0, '4001 South 700 East', datetime.timedelta(hours = 9, minutes = 5))


def delivery(truck):
    packages_on_truck = []
    distance_travelled = 0.0

    for packageID in truck.packages:
        package = packages_hash_table.hash_search(packageID)
        packages_on_truck.append(package)
    truck.packages.clear()

    while len(packages_on_truck) > 0:

        next_delivery_dist = 10000
        next_package = None
        for package in packages_on_truck:
            if distances(delivery_address(truck.address), delivery_address(package.address)) <= next_delivery_dist:
                next_delivery_dist = distances(delivery_address(truck.address), delivery_address(package.address))
                next_package = package

        truck.packages.append(next_package.ID)
        distance_travelled += next_delivery_dist
        truck.time += datetime.timedelta(hours=next_address / 18)
        packages_on_truck.remove(next_package)
        truck.address = next_package.address
        next_package.delivery = truck.time
        next_package.departure = truck.time



delivery(truck1)
delivery(truck2)

truck3.departure = min(truck1.time, truck2.time)
delivery(truck3)

print(truck1.mileage)
print(truck2.mileage)
print(truck3.mileage)


#class main