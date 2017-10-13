import argparse
import codecs
import json
import sys
from json import JSONDecodeError
from math import radians, sin, cos, asin, sqrt
from operator import attrgetter


class Bar:
    def __init__(self, bar_name, seats, coordinates):
        self.name = bar_name
        self.seats = seats
        self.coordinates = coordinates
        self.distance = ()

    def __str__(self):
        return 'bar named {}, has {} seats and located in {} km'.format(
            self.name, self.seats, "%.3f" % self.distance)

    def get_distance(self, longitude, latitude):
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


def is_file_valid(filepath):
    try:
        json_object = load_data(filepath)
    except ValueError :
        msg = "%s is not a valid JSON file" % filepath
        raise argparse.ArgumentTypeError(msg)
    except FileNotFoundError:
        msg = "%s is not found" % filepath
        raise argparse.ArgumentTypeError(msg)
    return json_object


def resolve_args(argv):
    parser = argparse.ArgumentParser(description='Find some bars.')
    parser.add_argument('filename', type=is_file_valid,
                        help='JSON file with info about bars', )
    parser.add_argument('longitude', type=float,
                        help='longitude of current GPS coordinates')
    parser.add_argument('latitude', type=float,
                        help='latitude of current GPS coordinates')
    return parser.parse_args()


def main(args):
    bars = parse_bars(args.filename)
    closest_bar = get_closest_bar(bars, args.longitude, args.latitude)
    smallest_bar = get_smallest_bar(bars)
    biggest_bar = get_biggest_bar(bars)
    print("Biggest {}".format(biggest_bar))
    print("Smallest {}".format(smallest_bar))
    print("Nearest {}".format(closest_bar))


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
    return max(bars, key=attrgetter('seats'))


def get_smallest_bar(bars):
    return min(bars, key=attrgetter('seats'))


def get_closest_bar(bars, longitude, latitude):
    for bar in bars:
        bar.distance = bar.get_distance(longitude, latitude)
    return min(bars, key=attrgetter("distance"))


if __name__ == '__main__':
    args = resolve_args(sys.argv)
    main(args)
