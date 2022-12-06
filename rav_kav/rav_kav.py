from datetime import datetime, date, time, timedelta

class RavKav:

    rides = {'short': {'range': (0, 15), 'price': 5.5},
             'medium': {'range': (16, 40), 'price': 12},
             'long': {'range': (40, 1000), 'price': 40},
             }

    def __init__(self, holder_id: str, holder_name: str):
        self.__holder_id = holder_id
        self.__holder_name = holder_name
        self.__balance = 0
        self.__date_log: dict[date: int] = {}
        self.__log_types: dict[str: int] = {}

    def get_holder_id(self):
        return self.__holder_id

    def get_holder_name(self):
        return self.__holder_name

    def topup(self, amount_momey: int):
        if amount_momey <= 0:
            return False
        self.__balance += amount_momey

    @staticmethod
    def _km2type(km) -> str:
        for ride_type, ride_details in RavKav.rides.items():
            if ride_details['range'][0] <= km <= ride_details['range'][1]:
                return ride_type

    def ride(self, km: int):
        if km < 0:
            return False

        # Checking km type
        ride_type = self._km2type(km)

        sum_ride = RavKav.rides[ride_type]['price']

        # Checks if there is not enough money for the ride
        if self.__balance - sum_ride < 0:
            return False

        self.__balance -= sum_ride
        if date.today() not in self.__date_log:
            self.__date_log[date.today()] = 0
        self.__date_log[date.today()] += 1

        if ride_type not in self.__log_types:
            self.__log_types[ride_type] = 0
        self.__log_types[ride_type] += 1

        return True

    def get_current_balance(self):
        return self.__balance

    def get_rides_by_date(self, date_ride: date):
        if date_ride not in self.__date_log:
            return False
        return self.__date_log[date_ride]

    def get_rides_by_type(self, type_ride: str):
        if type_ride not in self.__log_types:
            return False
        return self.__log_types[type_ride]








if __name__ == '__main__':

    rav_kav = RavKav('534628153', 'Yael')
    rav_kav.topup(20)
    print("Balance: ", rav_kav.get_current_balance())
    print("Add ride: ", rav_kav.ride(41))  # false - don't have enough money
    print("Add ride: ", rav_kav.ride(10))
    print("Balance: ", rav_kav.get_current_balance())
    print(f"The number of rides on {date.today()} = ", rav_kav.get_rides_by_date(date.today()))
    print(f"The number of rides by type - medium = ", rav_kav.get_rides_by_type('medium'))
    print(f"The number of rides by type - short = ", rav_kav.get_rides_by_type('short'))
    print("holder name: ", rav_kav.get_holder_name(), "\nId: ", rav_kav.get_holder_id())
