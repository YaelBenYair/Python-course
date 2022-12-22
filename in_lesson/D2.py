import datetime

class DateIterator:
    def __init__(self, date_d: datetime):
        self._date: datetime = date_d


    def __iter__(self):
        self.date_month = self._date.month
        self.date_plas = datetime.timedelta(days=1)
        self.iter_date = self._date
        return self

    def __next__(self):
        if self.date_month != self.iter_date.month:
            raise StopIteration()
        d = self.iter_date
        self.iter_date += self.date_plas
        return d

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value: datetime):
        self._date = value






if __name__ == '__main__':

    d = DateIterator(datetime.date(year=2022, month=12, day=2))

    for i in d:
        print(i)

    print("\noriginal date", d.date)



