import datetime

from bus_route_and_achedulea import *
from BestBusCompanyExceptions import *

class BestBusCompany:

    def __init__(self):
        self._line_num2busroute: dict[int: BusRoute] = dict()
        self._origin2busroute: dict[str: list[BusRoute]] = {}
        self._destination2busroute: dict[str: list[BusRoute]] = {}
        self._bus_stop2busroute: dict[str: list[BusRoute]] = {}

    # Manager actions --------------
    # add route --------------------------------------------------------------------------------------------------------
    def _check_exists(self, val, s_dict):
        if val not in s_dict:
            raise BusDetaileNotExistsError(val)

    def _add_to_bus_stop_dict(self, stops: list, bus_r: BusRoute):
        for stop in stops:
            if stop not in self._bus_stop2busroute:
                self._bus_stop2busroute[stop] = []
            self._bus_stop2busroute[stop].append(bus_r)

    def _add_to_origin_destin_dict(self, origin: str, bus_r: BusRoute, self_dict):
        if origin not in self_dict:
            self_dict[origin] = []
        self_dict[origin].append(bus_r)

    def add_route(self, line_num: int, origin: str, destination: str, stops: str):
        # check if the line number already exist
        if line_num in self._line_num2busroute:
            raise BusDetaileNotExistsError(line_num)

        bus_route = BusRoute(line_num, origin, destination, stops.split(","))
        self._line_num2busroute[line_num] = bus_route

        self._add_to_bus_stop_dict(stops.split(","), bus_route)

        # can be more than one line with the same origin and the same destination
        self._add_to_origin_destin_dict(origin, bus_route, self._origin2busroute)

        self._add_to_origin_destin_dict(destination, bus_route, self._destination2busroute)


        return True

    # delete route -----------------------------------------------------------------------------------------------------

    def _delete_from_origin(self, line_num: int):
        inx_i = None
        origin = self._line_num2busroute[line_num].get_origin()
        for inx, i in enumerate(self._origin2busroute[origin]):
            if line_num == i.get_line_number():
                inx_i = inx

        self._origin2busroute[origin].pop(inx_i)

    def _delete_from_destin(self, line_num: int):
        inx_i = None
        destin = self._line_num2busroute[line_num].get_destin()
        for inx, i in enumerate(self._destination2busroute[destin]):
            if line_num == i.get_line_number():
                inx_i = inx

        self._destination2busroute[destin].pop(inx_i)

    def _delete_from_stops(self, line_num: int):
        inx_i = None
        for key in self._bus_stop2busroute:
            for inx, i in enumerate(self._bus_stop2busroute[key]):
                if line_num == i.get_line_number():
                    inx_i = inx
            if inx_i is not None:
                self._bus_stop2busroute[key].pop(inx_i)

    def delete_route(self, line_num: int):
        self._check_exists(line_num, self._line_num2busroute)

        self._delete_from_origin(line_num)
        self._delete_from_destin(line_num)
        self._delete_from_stops(line_num)
        self._line_num2busroute.pop(line_num)

        return True

    # update line ------------------------------------------------------------------------------------------------------
    def display_information_route_by_line(self, line_num: int):
        self._check_exists(line_num, self._line_num2busroute)
        print(self._line_num2busroute[line_num])

    def update_origin(self, line_num: int, new_origin: str):
        self._delete_from_origin(line_num)
        self._line_num2busroute[line_num].change_origin(new_origin)
        bus_r = self._line_num2busroute[line_num]
        self._add_to_origin_destin_dict(new_origin, bus_r, self._origin2busroute)


    def update_destin(self, line_num: int, new_destin: str):
        self._delete_from_destin(line_num)
        self._line_num2busroute[line_num].change_destination(new_destin)
        bus_r = self._line_num2busroute[line_num]
        self._add_to_origin_destin_dict(new_destin, bus_r, self._destination2busroute)

    def update_stops(self, line_num: int, new_stops: str):
        self._delete_from_stops(line_num)
        self._line_num2busroute[line_num].change_stops(new_stops.split(","))
        bus_r = self._line_num2busroute[line_num]
        self._add_to_bus_stop_dict(new_stops.split(","), bus_r)

    # add scheduled ----------------------------------------------------------------------------------------------------
    def get_scheduled_line(self, line_num: int):
        self._check_exists(line_num, self._line_num2busroute)
        return self._line_num2busroute[line_num].display_sched()

    def add_scheduled(self, line_num: int, origin_time: datetime, destination_time: datetime, driver_name: str):
        self._check_exists(line_num, self._line_num2busroute)
        self._line_num2busroute[line_num].add_scheduled_rides(origin_time, destination_time, driver_name)

    # Passenger actions --------------
    # search route -----------------------------------------------------------------------------------------------------
    def search_by_line(self, line_num: int):
        self._check_exists(line_num, self._line_num2busroute)
        print(self._line_num2busroute[line_num])


    def search_by_origin(self, origin: str):
        self._check_exists(origin, self._origin2busroute)
        print(self._origin2busroute[origin])


    def search_by_destin(self, destin: str):
        self._check_exists(destin, self._destination2busroute)
        print(self._destination2busroute[destin])


    def search_by_bus_stop(self, stop: str):
        self._check_exists(stop, self._bus_stop2busroute)
        print(self._bus_stop2busroute[stop])


    def report_delay(self, line_num: int, sche_id: int):
        self._check_exists(line_num, self._line_num2busroute)
        self._line_num2busroute[line_num].add_delay(sche_id)



    def get_lins_by_num(self):
        return self._line_num2busroute





#
#
# if __name__ == '__main__':
#
#     bus_c = BestBusCompany()
#     print(bus_c.add_route(16, 'Tayasim', 'Opera', 'school,park,sea,xxx'))
#     print(bus_c.add_route(32, 'bbb', 'abc', 'xxx,lll,ggg'))
#     # print(bus_c.get_lins_by_num())
#     bus_c.add_scheduled(16, datetime.time(12, 40), datetime.time(13, 40), "Tom")
#     # print(bus_c.search_by_line(16))
#     print(bus_c.search_by_origin('Tayasim'))
#     print()
#     bus_c.report_delay(16, 1)
#     print(bus_c.search_by_line(16))
#     bus_c.report_delay(16, 1)
#     bus_c.report_delay(16, 1)
#     print()
#     print(bus_c.search_by_line(16))
#     # print(bus_c.by_stops())
#     # print(bus_c.by_origin())
#     # bus_c.delete_route(32)
#     print()
#     # print(bus_c.get_lins_by_num())
#     # print(bus_c.by_stops())
#     # print(bus_c.by_origin())






