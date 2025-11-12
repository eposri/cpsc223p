import unittest
import json
from flights import Flights

class TestFlightClass(unittest.TestCase):

    def setUp(self):
        self.filename = "test_flights.json"
        self.f = Flights(self.filename)
        self.f.data = []
        self.f.save_data()

    def tearDown(self):
        self.f.data = []
        self.f.save_data()

    def test_add_flight_valid(self):
        print("\n*** Test: Adding a valid flight ***")
        result = self.f.add_flight("LAX", "ORD", "123", "1000", "1400", "N")
        self.assertTrue(result, "add_flight should return True for valid input")
        self.assertEqual(len(self.f.data), 1, "Flight should be added to data")

    def test_add_flight_invalid_departure_time(self):
        print("\n*** Test: Adding a flight with invalid departure time ***")
        result = self.f.add_flight("LAX", "ORD", "123", "10:00", "1400", "N")
        self.assertFalse(result, "add_flight should return False for invalid departure time")
        self.assertEqual(len(self.f.data), 0, "Flight should not be added")

    def test_add_flight_invalid_arrival_time(self):
        print("\n*** Test: Adding a flight with invalid arrival time ***")
        result = self.f.add_flight("LAX", "ORD", "123", "1000", "14:00", "N")
        self.assertFalse(result, "add_flight should return False for invalid arrival time")
        self.assertEqual(len(self.f.data), 0, "Flight should not be added")

    def test_get_flights_empty(self):
        print("\n*** Test: Getting flights when no flights are added ***")
        flights = self.f.get_flights()
        self.assertEqual(len(flights), 0, "get_flights should return an empty list")

    def test_get_flights_single(self):
        print("\n*** Test: Getting flights with one flight added ***")
        self.f.add_flight("LAX", "ORD", "123", "1000", "1400", "N")
        flights = self.f.get_flights()
        self.assertEqual(len(flights), 1, "get_flights should return one flight")
        expected_flight = {
            "origin": "LAX",
            "destination": "ORD",
            "flight_number": "123",
            "departure": "10:00am",
            "arrival": "2:00pm",
            "duration": "4:00"
        }
        actual_flight = flights[0]
        self.assertEqual(actual_flight, expected_flight, "Flight details should match")

    def test_get_flights_multiple(self):
        print("\n*** Test: Getting flights with multiple flights added ***")
        self.f.add_flight("LAX", "ORD", "123", "1000", "1400", "N")
        self.f.add_flight("ORD", "JFK", "456", "1530", "1800", "N")
        self.f.add_flight("JFK", "LHR", "789", "2200", "0600", "Y")
        flights = self.f.get_flights()
        self.assertEqual(len(flights), 3, "get_flights should return all flights")

    def test_get_flights_time_formatting(self):
        print("\n*** Test: Checking time formatting in get_flights ***")
        self.f.add_flight("LAX", "ORD", "123", "0900", "1730", "N")
        self.f.add_flight("ORD", "JFK", "456", "2359", "0001", "Y")
        flights = self.f.get_flights()
        self.assertEqual(flights[0]["departure"], "9:00am", "Departure time should be formatted correctly")
        self.assertEqual(flights[0]["arrival"], "5:30pm", "Arrival time should be formatted correctly")
        self.assertEqual(flights[1]["departure"], "11:59pm", "Departure time should be formatted correctly")
        self.assertEqual(flights[1]["arrival"], "+12:01am", "Arrival time should be formatted correctly for next day")
        self.assertEqual(flights[0]["duration"], "8:30", "Duration should be calculated correctly")
        self.assertEqual(flights[1]["duration"], "0:02", "Duration should be calculated correctly for short flights")

if __name__ == '__main__':
    unittest.main(verbosity=2) #  verbosity=2 for more detailed output