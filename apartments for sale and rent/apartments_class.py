



class Apartment:
    def __init__(self, address: str, parking_type: str, rooms_num: int, size_in_sq_meters: int,
                 floor: int, monthly_municipal_tax: int, has_balcony: bool, is_penthouse: bool, is_villa: bool):
        self.__is_villa = is_villa
        self.__is_penthouse = is_penthouse
        self.__has_balcony = has_balcony
        self.__monthly_municipal_tax = monthly_municipal_tax
        self.__floor = floor
        self.__size_in_sq_meters = size_in_sq_meters
        self.__parking_type = parking_type
        self.__address = address
        self.__room_num = rooms_num

    def get_annual_municipal_tax(self) -> float:
        return self.__monthly_municipal_tax * 12

    def __str__(self):
        return f"Apartment address: {self.__address}\n" \
               f"Number op rooms: {self.__room_num}\n" \
               f"Apartment address: {self.deal_state}"




class ApartmentForSale(Apartment):

    deal_s = ('Open', 'Sold')

    def __init__(self, address: str, parking_type: str, rooms_num: int, size_in_sq_meters: int, floor: int,
                 monthly_municipal_tax: int, has_balcony: bool, is_penthouse: bool, is_villa: bool, sale_price: int):
        super().__init__(address, parking_type, rooms_num, size_in_sq_meters, floor, monthly_municipal_tax, has_balcony,
                         is_penthouse, is_villa)

        self.deal_state = ApartmentForSale.deal_s[0]
        self.sale_price = sale_price

    # def __str__(self):
    #     return f"Apartment address: {self.__address}\n" \
    #            f"Number op rooms: {self.__room_num}\n" \
    #            f"Apartment address: {self.deal_state}"

    def get_agency_fee(self):
        return self.sale_price * 0.02

    def get_sale_price(self):
        return self.sale_price

    def close_deal(self):
        if self.deal_state == ApartmentForSale.deal_s[1]:
            return False
        self.deal_state = ApartmentForSale.deal_s[1]

    def is_for_rent(self):
        return False

    def is_for_sale(self):
        return True
# apartment_id
# sale_price
# deal_state - open | closed (sold)
# dict - apartment_id to apartment

# get_agency_fee()
# close_deal()
# is_for_rent()
# is_for_sale()



class ApartmentForRent(Apartment):

    deal_s = ('Open', 'Rented')

    def __init__(self, address: str, parking_type: str, rooms_num: int, size_in_sq_meters: int,
                 floor: int, monthly_municipal_tax: int, has_balcony: bool, is_penthouse: bool, is_villa: bool,
                 rent_price_per_month: int):
        super().__init__(address, parking_type, rooms_num, size_in_sq_meters, floor, monthly_municipal_tax, has_balcony,
                         is_penthouse, is_villa)

        self.deal_state = ApartmentForRent.deal_s[0]
        self.rent_price_per_month = rent_price_per_month

    def get_agency_fee(self):
        return self.rent_price_per_month

    def get_annual_rent_price(self):
        return self.rent_price_per_month * 12

    def close_deal(self):
        if self.deal_state == ApartmentForRent.deal_s[1]:
            return False
        self.deal_state = ApartmentForRent.deal_s[1]

    def is_for_rent(self):
        return True

    def is_for_sale(self):
        return False
# apartment_id
# rent_price_per_month
# deal_state - open | closed (rented)
# dict - apartment_id to apartment

# get_agency_fee()
# get_annual_rent_price()
# close_deal()
# is_for_rent()
# is_for_sale()














