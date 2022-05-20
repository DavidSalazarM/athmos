import struct
import websocket
import _thread
import time
import rel
import json
import sys
import sympy
import time
import datetime as dt
import sys

SAMPLE_MAX_TIME_SECS = 60


class RandomValuesStats:
    def __init__(self):
        self.set_default_values()

    def __str__(self):
        return """
        maximum value: {}
        minimum value: {}
        first value: {}
        last value: {}
        number of prime numbers: {}
        number of even numbers: {}
        number of odd numbers: {}
        """.format(self.max_number,
                   self.min_number,
                   self.first_number,
                   self.last_number,
                   self.number_of_prime_numbers,
                   self.number_of_even_numbers,
                   self.number_of_odd_numbers)

    def update_max_if_greater(self, num):
        if isinstance(num, int):
            if (num > self.max_number):
                self.max_number = num

        else:
            raise Exception("That was no valid number.")

    def update_min_if_lower(self, num):
        if isinstance(num, int):
            if (num < self.min_number):
                self.min_number = num
        else:
            raise Exception("That was no valid number.")

    def set_first(self, num):
        if isinstance(num, int):
            if (self.first_number is None):
                self.first_number = num
        else:
            raise Exception("That was no valid number.")

    def update_odd_or_even_counter(self, num):
        if isinstance(num, int):
            if num % 2 == 0:
                self.number_of_even_numbers = self.number_of_even_numbers + 1

            else:
                self.number_of_odd_numbers = self.number_of_odd_numbers + 1
        else:
            raise Exception("That was no valid number.")

    def update_prime_counter(self, num):
        if isinstance(num, int):
            if sympy.isprime(num):
                self.number_of_prime_numbers = self.number_of_prime_numbers + 1
        else:
            raise Exception("That was no valid number.")

    def set_last(self, num):
        if isinstance(num, int):
            self.last_number = num
        else:
            raise Exception("That was no valid number.")

    def take_sample(self, b_value):
        self.update_max_if_greater(b_value)
        self.update_min_if_lower(b_value)
        self.set_first(b_value)
        self.set_last(b_value)
        self.update_prime_counter(b_value)
        self.update_odd_or_even_counter(b_value)

    def set_default_values(self):
        self.max_number = -sys.maxsize
        self.min_number = sys.maxsize
        self.first_number = None
        self.last_number = None
        self.number_of_even_numbers = 0
        self.number_of_odd_numbers = 0
        self.number_of_prime_numbers = 0


class Sample:
    def __init__(self):
        self.set_default_values()

    def set_default_values(self):
        self.timestamp = dt.datetime.now()
        self.values = []
        self.random_values_stats = RandomValuesStats()
    
    def gen_stats(self):
        self.random_values_stats = RandomValuesStats()
        for sample_value in self.values:
            self.random_values_stats.take_sample(sample_value)

    def show_stats(self):
        print("---------------------------------------------------------------")
        print("sample size: {}".format(len(self.values)))
        print("timestamp: {}".format(dt.datetime.now()))
        print(self.random_values_stats)



sample = Sample()


def on_message(ws, message):
    data = json.loads(message)

    sample.values.append(data["b"])
    delta = dt.datetime.now() - sample.timestamp

    if delta.seconds >= SAMPLE_MAX_TIME_SECS:
        sample.gen_stats()
        sample.show_stats()
        sample.set_default_values()


def on_error(ws, error):
    print("error: ", error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    sample.timestamp = dt.datetime.now()
    print("Opened connection")


try:
    url = str(sys.argv[1])
except IndexError:
    url = "ws://209.126.82.146:8080"

if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close)
    ws.run_forever(dispatcher=rel)  
    rel.signal(2, rel.abort)  
    rel.dispatch()
