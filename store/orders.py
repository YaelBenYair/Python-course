class Shipment:

    STATUSES = ('processing', 'shipped', 'delivered')
    counter = 0

    def __init__(self, address):
        self.address = address
        self.status = 0
        Shipment.counter += 1

    def change_status_to_next(self) -> bool:
        if self.status == len(Shipment.STATUSES) - 1:
            print('Bad status')
            return False
        self.status += 1
        return True


class Order:

    ORDERS_NUMBER = 0

    def __init__(self, customer_id: str, products: dict[str: float], price_dict: dict[str: int], address: str):

        Order.ORDERS_NUMBER += 1
        self.customer_id = customer_id
        self.products = products
        self.num_order = Order.ORDERS_NUMBER
        self.price_dict = price_dict

        self.shipment = Shipment(address)
        self.total_price = 0

    def __str__(self):
        return f"Order Detail:\n" \
               f"<ID> {self.customer_id}\n" \
               f"<Num order> {self.num_order}\n" \
               f"<Product> {self.products}\n" \
               f"<Total Price> {self.total_price}"

    def __repr__(self):
        return f"<ID> {self.customer_id} - <Num order> {self.num_order}"

    def get_total_price(self):

        sum_product = 0
        for sku in self.price_dict:
            sum_product += self.price_dict[sku]
        self.total_price = sum_product
        return sum_product

    def change_status(self):
        self.shipment.change_status_to_next()