from datetime import datetime, date, time, timedelta

######################################################################################################
######################################################################################################
#                                             Bar
class Bar:

    count_reservation = 1

    def __init__(self, table_id: int, capacity: int):
        self.table_id = table_id
        self.capacity = capacity
        self.occupied_seats = 0
        self.is_occupied = False
        self.reservation_time = time()
        self.end_reservation_time = time()
        self.location = 'bar'

        self.reservation_by_time: dict[int: list[datetime, datetime, int]] = {}

    def __str__(self):
        return f"\nNumber table: {self.table_id}\n" \
               f"Capacity: {self.capacity}\n" \
               f"Location: {self.location}\n" \
               f"Is occupied: {self.is_occupied}\n" \
               f"Occupied seats: {self.occupied_seats}\n" \
               f"Reservation start time: {self.reservation_time.strftime('%H:%M:%S')}\n" \
               f"End time reservation: {self.end_reservation_time.strftime('%H:%M:%S')}\n"

    def __repr__(self):
        return f"\nNumber table: {self.table_id}\n" \
               f"Capacity: {self.capacity}\n" \
               f"Occupied seats: {self.occupied_seats}\n" \
               f"Location: {self.location}\n"

    def reserve_a_table(self, limit: timedelta, num_guests: int) -> bool:
        # if the bar is occupied and there are no room at the bar
        if self.is_occupied and self.occupied_seats + num_guests > self.capacity:
            print("this  table is occupied and there is no room at the table")
            return False

        # if there are no room at the bar
        if self.occupied_seats + num_guests > self.capacity:
            print(f"There is no room at the table for the {num_guests} people")
            return False

        # There is space at the bar and the order is being made
        self.is_occupied = True
        self.reservation_time = datetime.now()
        self.end_reservation_time = limit + self.reservation_time
        self.occupied_seats += num_guests

        self.reservation_by_time[Bar.count_reservation] = [self.reservation_time,
                                                           self.end_reservation_time, num_guests]

        Bar.count_reservation += 1
        return True

    def time_left(self) -> bool | timedelta | list[list[int, timedelta]]:
        if len(self.reservation_by_time) == 0:
            return False
        if len(self.reservation_by_time) == 1:
            for num, details in self.reservation_by_time.items():
                return details[1] - datetime.now()

        # return the minimum time that left if there are more than one reservation
        small_time = None
        if len(self.reservation_by_time) > 1:
            for num, details in self.reservation_by_time:
                if small_time is None:
                    small_time = details[1] - datetime.now()
                elif details[1] - datetime.now() >= small_time:
                    small_time = details[1] - datetime.now()

            return small_time

    def time_left_and_reservation(self) -> bool | timedelta | list[list[int, timedelta]]:
        if len(self.reservation_by_time) == 0:
            return False
        if len(self.reservation_by_time) == 1:
            for num, details in self.reservation_by_time.items():
                return [details[1] - datetime.now(), details[2]]

        # return list of time that left if there are more than one reservation
        time_left_list = []
        if len(self.reservation_by_time) > 1:
            for num, details in self.reservation_by_time.items():
                time_left_list.append([details[2], details[1] - datetime.now()])
        return time_left_list

    def release_a_table(self, num_guests_leave):
        print("release_a_table")
        if num_guests_leave > self.occupied_seats:
            return False

        # delete from the dict the reservation of the num guests
        small_time = None
        release = 0
        for num, details in self.reservation_by_time.items():
            if details[2] == num_guests_leave:
                if small_time is None:
                    small_time = details[1]
                    release = num
                elif small_time < details[1]:
                    small_time = details[1]
                    release = num

        self.reservation_by_time.pop(release)
        self.occupied_seats -= num_guests_leave
        return True





######################################################################################################
######################################################################################################
#                                             TABLE


class Table:

    def __init__(self, table_id: int, capacity: int, location: str):

        date_time_now = datetime.now()

        self.table_id = table_id
        self.capacity = capacity
        self.occupied_seats = 0
        self.is_occupied = False
        self.reservation_time = time()
        self.end_reservation_time = time()
        self.location = location


    def __str__(self):
        return f"\nNumber table: {self.table_id}\n" \
               f"Capacity: {self.capacity}\n" \
               f"Location: {self.location}\n" \
               f"Is occupied: {self.is_occupied}\n" \
               f"Occupied seats: {self.occupied_seats}\n" \
               f"Reservation start time: {self.reservation_time.strftime('%H:%M:%S')}\n" \
               f"End time reservation: {self.end_reservation_time.strftime('%H:%M:%S')}\n"

    def __repr__(self):
        return f"\nNumber table: {self.table_id}\n" \
               f"Capacity: {self.capacity}\n" \
               f"Location: {self.location}\n"

    def is_available(self):
        pass

    def reserve_a_table(self, limit: timedelta, num_guests: int) -> bool:
        if self.is_occupied:
            print("this  table is occupied")
            return False

        # if there are no room at the table
        if self.occupied_seats + num_guests > self.capacity:
            print(f"There is no room at the table for the {num_guests} people")
            return False

        # There is room at the table and the order is being made
        self.is_occupied = True
        self.reservation_time = datetime.now()
        self.end_reservation_time = limit + self.reservation_time
        self.occupied_seats += num_guests

        return True

    def release_a_table(self, num_guests_leave):
        self.is_occupied = False
        self.reservation_time = time()
        self.end_reservation_time = time()
        self.occupied_seats -= num_guests_leave

    def time_left(self):
        if self.end_reservation_time == time():
            return None
        return self.end_reservation_time - datetime.now()

    def get_available_hour(self):
        return self.end_reservation_time




class TableReservationSystem:

    def __init__(self, name: str, table_list: list, location_table: list,
                 time_limit_occupy: timedelta, locations_list: tuple):

        self.name = name

        # How many tables do I have in the restaurant in total
        self.num_all_tables = len(table_list)

        self.num_table2table: dict[int: Table | Bar] = {}
        self.location2table: dict[str: list[Table | Bar]] = {}

        count_num_table = 1
        for capacity, location in zip(table_list, location_table):
            table = Table(count_num_table, capacity, location)
            self.num_table2table[count_num_table] = table
            if location not in self.location2table:
                self.location2table[location] = []
            self.location2table[location].append(table)
            count_num_table += 1

        self.time_limit_occupy = time_limit_occupy

        #all the locations in the restaurant
        self.locations_list = locations_list

    def add_bar(self, capacity_bar: list):
        for capacity in capacity_bar:
            bar = Bar(self.num_all_tables + 1, capacity)
            self.num_table2table[bar.table_id] = bar
            if bar.location not in self.location2table:
                self.location2table[bar.table_id] = []
            self.location2table[bar.table_id].append(bar)

    def make_reservation(self, table_id: int, num_guests: int) -> bool:
        if table_id not in self.num_table2table:
            print(f"the table num{table_id} not found")
            return False

        if self.num_table2table[table_id].reserve_a_table(self.time_limit_occupy, num_guests):
            print("The order has been placed")
            return True
        else:
            return False

    def release_a_table(self, table_id: int, num_guests_leave: int):
        if table_id not in self.num_table2table:
            return False, f"the table num{table_id} not found"

        if not self.num_table2table[table_id].is_occupied:
            return False, f"This table is available"

        if self.num_table2table[table_id].occupied_seats - num_guests_leave < 0 :
            return False, f"The number of guests leaving is greater than the number of guests seated"

        self.num_table2table[table_id].release_a_table(num_guests_leave)
        return True, f"Table number {table_id} has been released"

    def display_table_by_location(self, location_name: str):
        if location_name not in self.location2table:
            print("We dont have this location")
            return False
        print(f"Tables in area {location_name}: ")
        print(self.location2table[location_name])

    def display_table_by_id(self, table_id: int):
        print(self.num_table2table[table_id])

    def display_bar_reservation(self, bar_id):
        print(self.num_table2table[bar_id].reservation_by_time)

    def get_available_tables(self, num_guests: int):
        available_tables: list[Table] = []
        inx_t = None

        for num, table in self.num_table2table.items():

            # Enters only if the list is not empty
            if len(available_tables) > 0:
                for inx, t in enumerate(available_tables):

                    # Checks if the table is occupied and if it is a bar,
                    # checks if there is room for the number of guests
                    if not table.is_occupied or type(table) is Bar and \
                            table.occupied_seats < table.capacity and \
                            num_guests + table.occupied_seats < table.capacity:
                        if table.capacity >= t.capacity:
                            inx_t = inx+1
                        elif inx > 0 and available_tables[inx - 1].capacity < table.capacity < t.capacity:
                            inx_t = inx
                        elif t.capacity > table.capacity >= num_guests and inx == 0:
                            inx_t = inx

                # check if inx_t is in the end of the list
                if inx_t == len(available_tables):
                    available_tables.append(table)
                # check if the table is in range of the num guests
                elif inx_t is not None:
                    available_tables.insert(inx_t, table)

            else:
                if table.capacity >= num_guests and not table.is_occupied:
                    available_tables.append(table)

            inx_t = None

        return available_tables

    def get_soonest_available_tables(self, num_guests: int):
        available_tables_by_time: list[Table | Bar] = []
        inx_t = None

        for num, table in self.num_table2table.items():

            if len(available_tables_by_time) > 0:
                for inx, t in enumerate(available_tables_by_time):
                    if table.capacity >= num_guests:
                        # Checks if the table has not been booked yet
                        if table.time_left() is None:
                            inx_t = 0
                        elif t.time_left() is None:
                            inx_t = inx + 1
                        # Tests to order from the smallest to the largest
                        elif table.time_left() >= t.time_left():
                            inx_t = inx + 1
                        elif table.time_left() < t.time_left() and inx == 0:
                            inx_t = inx
                        elif inx > 0 and \
                                available_tables_by_time[inx-1].time_left() < table.time_left() < t.time_left():
                            inx_t = inx

                # check if inx_t is in the end of the list
                if inx_t == len(available_tables_by_time):
                    available_tables_by_time.append(table)
                elif inx_t is not None:
                    available_tables_by_time.insert(inx_t, table)
            # If it is the first variable and it is in the range
            elif type(table) is Bar and num_guests < table.capacity or \
                    type(table) is Table and table.capacity >= num_guests:
                available_tables_by_time.append(table)

            inx_t = None
        return available_tables_by_time

    def time_left(self, table_id):
        if table_id not in self.num_table2table:
            return False
        if type(self.num_table2table[table_id]) is Bar:
            return self.num_table2table[table_id].time_left_and_reservation()
        else:
            return self.num_table2table[table_id].time_left()


    def get_tables_time_limit(self):
        return self.time_limit_occupy

    def update_tables_time_limit(self, limit: timedelta):
        self.time_limit_occupy = limit













#
# LOCATION_TABLES = ('bar', 'Terrace', 'Indoors', 'Floor number', 'VIP room',
#                        'Near toilet', 'Near exit', 'Near kitchen')














