from table_management import Table, TableReservationSystem
from datetime import datetime, date, time, timedelta


if __name__ == '__main__':


    locations_tables = ('bar', 'terrace', 'indoors', 'floor number', 'vip room',
                        'near toilet', 'near exit', 'near kitchen')
    limit = timedelta(hours=1, minutes=30)
    restaurant = TableReservationSystem('Mozes', [4, 3, 5, 2, 2, 3, 2, 4, 2],
                                        ['terrace', 'terrace', 'indoors', 'near toilet', 'vip room',
                                         'near toilet', 'indoors', 'near exit', 'terrace'],
                                        limit, locations_tables)

    restaurant.add_bar([10])

    restaurant.display_table_by_location(locations_tables[1])
    restaurant.make_reservation(1, 3)
    restaurant.display_table_by_id(1)

    restaurant.make_reservation(10, 2)
    restaurant.display_table_by_id(10)
    restaurant.display_bar_reservation(10)

    # restaurant.make_reservation(10, 10)

    restaurant.make_reservation(10, 7)
    restaurant.display_table_by_id(10)
    # restaurant.display_bar_reservation(10)


    # available_tables = restaurant.get_available_tables(2)
    # print("The available tables:", available_tables)

    print(restaurant.time_left(10))
    restaurant.release_a_table(10, 7)
    restaurant.display_bar_reservation(10)
    restaurant.display_table_by_id(10)

    print(restaurant.get_soonest_available_tables(3))

    print(restaurant.get_tables_time_limit())


















