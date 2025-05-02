# David Sills, Student ID Number: 011355522, WGU

import csv
import datetime
from packages import packages
from truck import truck
from hash_table import hash_table

#read the two CSV files
with open("package.csv") as csvfile:
    package_csv = csv.reader(csvfile, delimiter=',')
    package_csv = list(package_csv)

with open("distances.csv") as csvfile:
    distance_csv = csv.reader(csvfile, delimiter=',')
    distance_csv = list(distance_csv)

    with open("delivery_addresses.csv") as csvfile:
        delivery_addresses_csv = csv.reader(csvfile, delimiter=',')
        delivery_addresses_csv = list(delivery_addresses_csv)

packages_hash_table = hash_table()
#uses the CSV information to read package data and create the parcel object
def parcel_information(filename):
    with open(filename) as parcel_info:
        parcel_info = csv.reader(parcel_info)
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
            print(parcel)
#find the distance to the nearest delivery
def distances(x, y):
    distance = distance_csv[x][y]
    if distance == '':
        distance = distance_csv[y][x]
    return float(distance)

#
def delivery_address(addresses):
    for address in addresses:
        if addresses in address[2]:
            return int(address[0])

#why isnt this working? need to figure out my issue with the csv files before going further
#parcel_information('package_csv')


#class main: