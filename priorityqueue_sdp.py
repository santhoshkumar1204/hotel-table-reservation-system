import queue
from datetime import datetime

class Reservation:
    sequence_number = 0  # Class variable to keep track of the order of reservations

    def __init__(self, customer_name, reservation_time):
        self.customer_name = customer_name
        self.reservation_time = reservation_time
        self.sequence = Reservation.sequence_number
        Reservation.sequence_number += 1
    
    def __lt__(self, other):
        return self._compare_to(other)

    def _compare_to(self, other):
        #  reservation time
        if self.reservation_time == other.reservation_time:
            # sequence number (earlier reservations first)
            return self.sequence < other.sequence
        return self.reservation_time < other.reservation_time

# Priority Queue
reservation_queue = queue.PriorityQueue()

# Function to add a reservation
def add_reservation(customer_name, reservation_time_str):
    reservation_time = convert_to_datetime(reservation_time_str)
    reservation = Reservation(customer_name, reservation_time)
    reservation_queue.put(reservation)
    print(f"Reservation for {customer_name} at {reservation_time.strftime('%Y-%m-%d %I:%M %p')} added.")

# Function to convert string to datetime
def convert_to_datetime(time_str):
    return datetime.strptime(time_str, "%Y-%m-%d %I:%M %p")

# Function to allocate a table
def allocate_table():
    if not reservation_queue.empty():
        next_reservation = reservation_queue.get()
        print(f"Table allocated to {next_reservation.customer_name} for {next_reservation.reservation_time.strftime('%Y-%m-%d %I:%M %p')}.")
    else:
        print("No reservations to allocate.")

# Adding reservations
add_reservation("Alice", "2024-06-05 06:00 PM")
add_reservation("Bob", "2024-06-05 06:00 PM")
add_reservation("Charlie", "2024-06-05 06:00 PM")
add_reservation("David", "2024-06-05 06:00 PM")
add_reservation("Eve", "2024-06-05 06:00 PM")

# Allocating tables
allocate_table()
allocate_table()
allocate_table()
allocate_table()
allocate_table()
