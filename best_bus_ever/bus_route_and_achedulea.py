import random
import datetime


class BusRoute:

    sched_counter = 1

    def __init__(self, line_number: int, origin: str, destination: str, stops: list):
        self.__line_number = line_number
        self._origin = origin
        self._destination = destination
        self._stops = stops
        self._scheduled_rides: dict[int: ScheduledRide] = {}

    def __str__(self):
        return f"\n\nLine number: {self.__line_number}\n" \
               f"Origin: {self._origin}\n" \
               f"Destination: {self._destination}\n" \
               f"Stops: {self._stops}\n" \
               f"Scheduled rides: \n{self._scheduled_rides}\n"

    def __repr__(self):
        return self.__str__()

    def get_line_number(self):
        return self.__line_number

    def get_origin(self):
        return self._origin

    def get_stops(self):
        return self._stops

    def get_destin(self):
        return self._destination

    def add_scheduled_rides(self, origin_time: datetime, destination_time: datetime, driver_name: str):
        # id_sche = random.randint(10000, 100000)
        # while id_sche in self._scheduled_rides:
        #     id_sche = random.randint(10000, 100000)
            #  1 : 1, 12:45, 14:00, Tom
        self._scheduled_rides[BusRoute.sched_counter] = ScheduledRide(BusRoute.sched_counter, origin_time,
                                                                      destination_time, driver_name)

        BusRoute.sched_counter += 1

    def add_delay(self, id_s: int):
        if id_s not in self._scheduled_rides:
            raise Exception()
        self._scheduled_rides[id_s].add_delays()


    def display_sched(self):
        for id_n, sches in self._scheduled_rides.items():
            print(sches)

    def change_origin(self, new_origin: str):
        self._origin = new_origin

    def change_destination(self, new_destination: str):
        self._destination = new_destination

    def change_stops(self, new_stops: list):
        self._stops = new_stops


class ScheduledRide:

    def __init__(self, id_sche: int, origin_time: datetime, destination_time: datetime, driver_name: str):
        self._driver_name = driver_name
        self._destination_time = destination_time
        self._origin_time = origin_time
        self._id_sche = id_sche
        self._delays: dict[datetime: int] = {}

    def __str__(self):
        return f"{self.__repr__()}" \
               f"Driver_name: {self._driver_name}\n"

    def __repr__(self):
        return f"\nId: {self._id_sche}\n" \
               f"Origin time: {self._origin_time}\n" \
               f"Destination time: {self._destination_time}\n" \
               f"Delays: {self._delays}\n"

    def add_delays(self):
        date_delays = datetime.date.today()
        if date_delays not in self._delays:
            self._delays[date_delays] = 0

        self._delays[date_delays] += 1

    # def get_delays(self):
    #     return self._delays












