import codecs
import json
from math import radians, sin, cos, asin, sqrt

import sys


class Bar:
    def __init__(self, name, seats, coordinates):
        self.name = name
        self.seats = seats
        self.coordinates = coordinates

    def __str__(self):
        return 'bar named {}, has {} seats and located in {} km'.format(
            self.name, self.seats, "%.3f" % self.distance)

    def get_distance(self, longitude, latitude):
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians,
                                     [longitude, latitude, self.coordinates[0],
                                      self.coordinates[1]])
        delta_longitude = lon2 - lon1
        delta_latitude = lat2 - lat1
        # haversine formula
        var_a = sin(delta_latitude / 2) ** 2 + cos(lat1) * cos(lat2) * sin(
            delta_longitude / 2) ** 2
        var_c = 2 * asin(sqrt(var_a))
        earth_radius = 6367
        return var_c * earth_radius


def load_data(filepath):
    with codecs.open(filepath, 'r', encoding='utf-8',
                     errors='ignore') as opened_file:
        return json.loads(opened_file.read())


def parse_bars(json_data):
    bars = []
    for entry in json_data['features']:
        bar = Bar(entry['properties']['Attributes']['Name'],
                  entry['properties']['Attributes']['SeatsCount'],
                  entry['geometry']['coordinates'])
        bars.append(bar)
    return bars


def get_biggest_bar(bars):
    biggest = None
    max_seats = 0
    for bar in bars:
        if bar.seats > max_seats:
            biggest = bar
            max_seats = bar.seats
    return biggest


def get_smallest_bar(bars):
    smallest = None
    min_seats = 10000
    for bar in bars:
        if bar.seats < min_seats:
            smallest = bar
            min_seats = bar.seats
    return smallest


def get_closest_bar(bars, longitude, latitude):
    closest_bar = None
    min_distance = 20000
    for bar in bars:
        distance = bar.get_distance(longitude, latitude)
        bar.distance = distance
        if distance < min_distance:
            closest_bar = bar
            min_distance = distance
    return closest_bar


if __name__ == '__main__':
    data = load_data(sys.argv[1])
    bars = parse_bars(data)
    closest_bar = get_closest_bar(bars, int(sys.argv[2]), int(sys.argv[3]))
    smallest_bar = get_smallest_bar(bars)
    biggest_bar = get_biggest_bar(bars)
    print("Biggest {}".format(biggest_bar))
    print("Smallest {}".format(smallest_bar))
    print("Nearest {}".format(closest_bar))