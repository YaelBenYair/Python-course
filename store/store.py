from orders import Shipment, Order

class Customer:
    def __init__(self, customer_id, name, address, phone, email=None):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"<Customer>\n" \
               f"ID: {self.customer_id}" \
               f"Name: {self.name}\n" \
               f"Address: {self.address}\n" \
               f"Phone: {self.phone}"

    def __repr__(self):
        return f"<Customer> {self.name}"


class Product:
    def __init__(self, sku: str, category: str, brand: str,
                 qty: float, price: float,
                 model: str = None,
                 warranty_months: int = None):

        self.sku = sku
        self.category = category
        self.brand = brand
        self.model = model
        self.warranty_months = warranty_months
        self.price = price
        self.qty = qty

    def update_qty(self, diff: float):
        if diff + self.qty < 0:
            # error
            return None
        self.qty += diff

    def update_price(self, new_price):
        if new_price <= 0:
            # error
            return None
        self.price = new_price

    def __str__(self):
        return f"<Product>: Brand: {self.brand} Model: {self.model} SKU: {self.sku}"

    def __repr__(self):
        return f"<Product>: Brand: {self.brand}"

    def __eq__(self, other):
        return self.sku == other.sku


class Store:

    def __init__(self, store_name):
        self.store_name = store_name

        # id to customer
        self.customers: dict[str, Customer] = {}

        # sku to product
        self.inventory: dict[str, Product] = {}

        self.orders: dict[str, dict[int, Order]] = {}

        # order_product
        # orders
        # shipments

    def display_customers(self):
        print(self.customers)

    def add_customer(self, customer_id, name, address, phone, email=None):
        print(f"Adding customer {name}")
        new_customer = Customer(customer_id, name, address, phone, email)
        self.customers[customer_id] = new_customer

    # def add_customer2(self, customer: Customer):
    #     self.customers[customer.customer_id] = customer

    def add_product_to_inventory(self, sku: str, category: str, brand: str,
                                 qty: float, price: float,
                                 model: str = None,
                                 warranty_months: int = None):
        print(f"Adding product {brand}")
        new_product = Product(sku, category, brand,
                              qty, price, model, warranty_months)
        self.inventory[sku] = new_product

    def make_order(self, customer_id: str, sku2qty: dict[str: float], address: str):
        print("in make order")
        price_dict: dict[str, int] = {}
        count_num_product_in_stock = 0
        num_product = 0

        if customer_id not in self.customers:
            print("not in customer")
            return False

        for sku, qty in sku2qty.items():
            num_product += 1
            if sku in self.inventory and self.inventory[sku].qty - sku2qty[sku] >= 0:
                count_num_product_in_stock += 1
            price_dict[sku] = sku2qty[sku] * self.inventory[sku].price

        if count_num_product_in_stock != num_product:
            print("not in stock")
            return False

        customer_order = Order(customer_id, sku2qty, price_dict, address)
        num_order = customer_order.num_order
        print(f"Your number order is {num_order}")
        self.orders[customer_id] = {}
        self.orders[customer_id][num_order] = customer_order

        for sku in sku2qty:
            self.inventory[sku].qty -= sku2qty[sku]
        return num_order

    def get_price(self, customer_id: str, num_order: int):
        if num_order not in self.orders[customer_id]:
            return False
        return self.orders[customer_id][num_order].get_total_price()

    def change_status(self, customer_id: str, num_order: int):
        if num_order not in self.orders[customer_id]:
            return False
        self.orders[customer_id][num_order].change_status()

    def display_order(self, customer_id: str, num_order: int):
        print(self.orders[customer_id][num_order])


    # def add_qty(self, sku:str, qty: float):
    #     self.inventory[sku].update_qty(qty)
    #
    # def add_items(self, skus: list, quantities: list):
    #     for sku, qty in zip(skus, quantities):
    #         self.add_qty(sku, qty)
    #
    # def get_products_by_brand(self, brand) -> list[Product]:
    #     ret_val = list()
    #     for product in self.inventory.values():
    #         if product.brand == brand:
    #             ret_val.append(product)
    #     return ret_val
    #
    # def get_out_of_stock(self):
    #     pass
    #
    # def add_order(self):
    #     pass
