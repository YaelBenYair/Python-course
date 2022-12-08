import random
from apartments_class import ApartmentForSale, ApartmentForRent


# def add_apartment_for_sale():
#     pass
#
#
# def add_apartment_for_rent():
#     pass


if __name__ == '__main__':

    apartment1 = ApartmentForRent('mapiley egoz', 'parking lot', 4, 80, 4, 50, False, False, False, 4000)
    apartment2 = ApartmentForSale('rabin', 'roofed parking', 6, 150, 0, 100, True, False, True, 2_560_000)

    print("apartment1")
    print(apartment1)
    print("Is for rent: ", apartment1.is_for_rent())
    print("get_annual_rent_price: ", apartment1.get_annual_rent_price())
    print("get_annual_municipal_tax: ", apartment1.get_annual_municipal_tax())
    print("get_agency_fee: ", apartment1.get_agency_fee())
    print(" ")

    print("apartment1")
    apartment1.close_deal()
    print(apartment1)
    print()

    print("apartment2")
    print(apartment2)
    print("Is for rent: ", apartment2.is_for_rent())
    print("get_annual_rent_price: ", apartment2.get_sale_price())
    print("get_annual_municipal_tax: ", apartment2.get_annual_municipal_tax())
    print("get_agency_fee: ", apartment2.get_agency_fee())

    print(" ")
    print("apartment2")
    apartment2.close_deal()
    print(apartment2)





