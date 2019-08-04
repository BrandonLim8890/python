'''
Author: Brandon Lim
Project: distance-between-two-cities.py
Description: Calculates the distance between two cities through user input
'''

from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def runner():
    print('Enter the first city: ')
    first_city = input()
    print(f'First city is {first_city}')
    print('Enter the second city: ')
    second_city = input()
    print(f'Second city is {second_city}')
    print(f'Enter the unit of measurement')
    units = input()

    first_loc = coordFinder(first_city)
    second_loc = coordFinder(second_city)

    print(f'Distance between {first_city} and {second_city} is {distanceCalc(first_loc, second_loc, units)}')


def coordFinder(address):
    geolocator = Nominatim(user_agent="distance-between-two-cities")
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude)


def distanceCalc(loc_one, loc_two, unit):
    unit = unit.lower()
    
    if unit == 'km' or unit == 'kilometers':
        return str(round(geodesic(loc_one, loc_two).kilometers)) + 'km'    
    elif unit == 'miles':
        return str(round(geodesic(loc_one, loc_two).miles)) + 'miles'
    elif unit == 'feet' or unit == 'ft':
        return str(round(geodesic(loc_one, loc_two).feet)) + 'ft'
    elif unit == 'meters' or unit == 'm':
        return str(round(geodesic(loc_one, loc_two).meters)) + 'm'
    else:
        print('Invalid Units. Exiting program')


runner()