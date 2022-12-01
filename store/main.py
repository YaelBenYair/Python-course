# from lesson8.store.store import Store
# from lesson8.store.orders import Shipment
from orders import Shipment
from store import Store


if __name__ == '__main__':

    # create a store
    gadget_store = Store('Ivory')

    # create a new customer
    gadget_store.add_customer('123123123', 'Valeria', 'netanya', '0456456')
    gadget_store.add_customer('333333333', 'Ziv Attias', 'Yaffo', '0545555555')

    gadget_store.display_customers()

    # create a product
    gadget_store.add_product_to_inventory("aa34v", "laptop", "Apple",
                                          10, 8000, "MacBook Pro 15'", 12)
    gadget_store.add_product_to_inventory("45ghf3", "phone", "Samsumg",
                                          23, 3500, "Galaxy 22", 12)

    # print(Shipment.counter)

    num_order = gadget_store.make_order('333333333', {"aa34v": 2, "45ghf3": 4}, 'address')

    print(gadget_store.get_price('333333333', num_order))

    gadget_store.display_order('333333333', num_order)