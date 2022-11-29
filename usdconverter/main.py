class UsdConverter:
    def __init__(self):
        self.rate_usd = {}

    def add_rate(self, rate_name: str, num_rate: float):
        self.rate_usd[rate_name] = num_rate
        print("Added exchange rate")

    def print_rate(self, rate_name: str) -> bool:
        if rate_name in self.rate_usd:
            print(f"The {rate_name} rate: {self.rate_usd.get(rate_name)}")
            return True
        else:
            print(f"The exchange rate {rate_name} not found")
            return False

    def update_rate(self, rate_name: str, num_rate: float):
        self.add_rate(rate_name, num_rate)
        print("The exchange rate update")

    def convert_from_usd(self, currency: str, amnt: float):
        if currency in self.rate_usd:
            return amnt * self.rate_usd[currency]
        else:
            print(f"Currency {currency} not found")
            return None

    def convert_from_rate(self, currency: str, amnt: float):
        """

        :param currency:
        :param amnt:
        :return:
        """
        if currency in self.rate_usd:
            return amnt / self.rate_usd[currency]
        else:
            print(f"Currency {currency} not found")
            return None


# 1 USD = 3.16 NIS
# 1 USD = 113.73 Japanese yen
# 1 USD = 0.89 Euro


if __name__ == '__main__':
    converter = UsdConverter()

    converter.add_rate('NIS', 3.16)
    converter.add_rate('YEN', 113.73)
    converter.add_rate('EURO', 0.89)

    print("10,000 from usd to yen: ", converter.convert_from_usd('YEN', 10_000))
    print("10,000 yen to usd: ", converter.convert_from_rate('YEN', 10_000))
