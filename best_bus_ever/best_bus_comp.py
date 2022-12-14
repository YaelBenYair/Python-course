from bus_route_and_achedulea import BusRoute

class BestBusCompany:

    def __init__(self):
        self._line_num2busroute: dict[int: BusRoute] = {}
        self._origin2busroute: dict[str: list[{int: BusRoute}]] = {}
        self._destination2busroute: dict[str: list[{int: BusRoute}]] = {}
        self._bus_stop2busroute: dict[str: BusRoute] = {}

    # Manager actions --------------
    # add route --------------------------------------------------------------------------------------------------------
    def add_route(self, line_num: int, origin: str, destination: str, stops: str):
        # check if the line number already exist
        if line_num in self._line_num2busroute:
            return False

        # check if there are already line with the same stops
        if stops in self._bus_stop2busroute:
            return False

        bus_route = BusRoute(line_num, origin, destination, stops)
        self._line_num2busroute[line_num] = BusRoute(line_num, origin, destination, stops)
        self._bus_stop2busroute[stops] = bus_route

        # can be more than one line with the same origin and the same destination
        if origin in self._origin2busroute:
            self._origin2busroute[origin] = []
        self._origin2busroute[origin].append({line_num: bus_route})

        if destination in self._destination2busroute:
            self._destination2busroute[destination] = []
        self._destination2busroute[destination].append({line_num: bus_route})

        return True

    # delete route -----------------------------------------------------------------------------------------------------
    def _delete_from_origin(self, line_num: int):
        inx_i = None
        for inx, i in enumerate(self._origin2busroute[self._line_num2busroute[line_num].get_origin()]):
            if line_num in i:
                inx_i = inx

        self._origin2busroute[self._line_num2busroute[line_num].get_origin()].pop(inx_i)

    def _delete_from_destin(self, line_num: int):
        inx_i = None
        for inx, i in enumerate(self._destination2busroute[self._line_num2busroute[line_num].get_destin()]):
            if line_num in i:
                inx_i = inx

        self._origin2busroute[self._line_num2busroute[line_num].get_destin()].pop(inx_i)

    def _delete_from_stops(self, line_num: int):
        stops = self._line_num2busroute[line_num].get_stops()
        self._bus_stop2busroute.pop(stops)

    def delete_route(self, line_num: int):
        if line_num not in self._line_num2busroute:
            return False

        self._delete_from_origin(line_num)
        self._delete_from_destin(line_num)
        self._delete_from_stops(line_num)
        self._line_num2busroute.pop(line_num)

        return True

    # update line ------------------------------------------------------------------------------------------------------
    def display_information_route_by_line(self, line_num: int):
        if line_num not in self._line_num2busroute:
            return False

        print(self._line_num2busroute[line_num])

    def update_origin(self, line_num: int, new_origin: str):
        self._line_num2busroute[line_num].change_origin(new_origin)

    def update_destin(self, line_num: int, new_destin: str):
        self._line_num2busroute[line_num].change_destination(new_destin)

    def updete_stops(self, line_num: int, new_stops: str):
        self._line_num2busroute[line_num].change_stops(new_stops)

    # add scheduled ----------------------------------------------------------------------------------------------------

    # Passenger actions --------------
    # search route -----------------------------------------------------------------------------------------------------
    def search_by_line(self, line_num: int):
        pass

    def search_by_origin(self, line_num: int):
        pass

    def search_by_destin(self, line_num: int):
        pass

    def search_by_bus_stop(self, line_num: int):
        pass













