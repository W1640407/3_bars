import sys
from unittest import TestCase

import bars
from bars import Bar


class TestBarFunctions(TestCase):
    def test_get_distance_zero(self):
        bar = Bar("name", 10, [10.1, 10.1])
        distance = bar.get_distance(10.1, 10.1)
        self.assertEqual(0, distance, 'Distance should be 0')

    def test_get_distance_algorithm(self):
        bar = Bar("name", 10, [37.635709999610896, 55.805575000158512])
        distance = bar.get_distance(0, 0)
        self.assertAlmostEqual(7064, distance, delta=1)

    def test_args_resolver(self):
        sys.argv[1:] = ['test.json', '1.1', '1.1']
        try:
            args_resolved = bars.resolve_args(sys.argv)
        except:
            self.fail('resolve_args() raised exception unexpectedly')

    def test_get_biggest_bar(self):
        bars_list = [Bar('small', 20, [0, 0])]
        big_bar = Bar('big', 50, [0, 0])
        bars_list.append(big_bar)
        biggest_bar = bars.get_biggest_bar(bars_list)
        self.assertEqual(big_bar, biggest_bar)

    def test_get_smallest_bar(self):
        bars_list = [Bar('big', 50, [0, 0])]
        small_bar = Bar('small', 20, [0, 0])
        bars_list.append(small_bar)
        smallest_bar = bars.get_smallest_bar(bars_list)
        self.assertEqual(small_bar, smallest_bar)

    def test_get_smallest_bar(self):
        bars_list = [Bar('farther', 50, [0, 0])]
        nearer_bar = Bar('nearer', 20, [10, 10])
        bars_list.append(nearer_bar)
        nearest_bar = bars.get_closest_bar(bars_list, 11, 11)
        self.assertEqual(nearer_bar, nearest_bar)
