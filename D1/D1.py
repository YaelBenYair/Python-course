import csv
import datetime
import os
from pprint import pprint
from csv import DictReader


# from os import listdir

# def csv_find_files(path, end_file = ".csv"):
#     filenames = listdir(path)
#     return [filename for filename in filenames if filename.endswith(end_file)]

# 1 --------------------------------------------------------------------------------------------------------------------


def csv_details(path):
    if not os.path.exists(path):
        return False

    file2deteils: dict[str: list] = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".csv"):
                path_file = os.path.join(root, file)
                with open(path_file) as fh:
                    clu = fh.readline()
                    clu = clu.split(";")
                    count_linse = 0
                    for line in fh:
                        count_linse += 1
                file2deteils[file] = [f"Amount of columns: {len(clu)}", f"amount of rows: {count_linse}"]

    return file2deteils


if __name__ == '__main__':
    path = 'C:\\Users\\DELL\\OneDrive\\שולחן העבודה\\f_name'
    pprint(csv_details(path))


# 2 --------------------------------------------------------------------------------------------------------------------


def aapl_filse(path):
    counter = 0
    vol = []
    high_price = []
    low_price = []
    line_in_csv = []
    with open(path) as csv_file:
        reader = DictReader(csv_file)

        for item in reader:
            # Inserts the date of each row
            date = item['Date']
            date = datetime.datetime.strptime(date, "%d-%m-%Y")

            # enter the first year in variable
            if counter == 0:
                date_year = date.year

            if date.year == date_year:
                vol.append(float(item['Volume']))
                high_price.append(float(item['High']))
                low_price.append(float(item['Low']))
                counter = 1
            else:
                # When we come to a new year, we enter all the details and reset the variables for the next year
                line_in_csv.append({'Year': date_year,
                                    'Avg Price': (sum(high_price) + sum(low_price)) / (len(high_price) + len(low_price)),
                                    'Min Price': min(low_price), 'Max Price': max(high_price),
                                    'Avg Volume': sum(vol) / len(vol), 'Min Volume': min(vol), 'Max Volume': max(vol)})
                high_price = []
                low_price = []
                vol = []
                date_year = date.year

    with open('files\\PL.csv', "w", newline="") as csv_f:
        writer = csv.DictWriter(csv_f, ['Year',  'Avg Price', 'Min Price', 'Max Price', 'Avg Volume',
                                        'Min Volume', 'Max Volume'])
        writer.writeheader()
        for row in line_in_csv:
            writer.writerow(row)


if __name__ == '__main__':
    aapl_filse('files\\AAPL.csv')

















# def aapl_filse(path):
#     counter = 0
#     low = 0
#     high = 0
#     sum_volume = 0
#     li = []
#     with open(path) as csv_file:
#         reader = DictReader(csv_file)
#
#         for item in reader:
#             date = item['Date']
#             date = datetime.datetime.strptime(date, "%d-%m-%Y")
#             if counter == 0:
#                 date_year = date.year
#                 low = float(item['Volume'])
#             if date.year == date_year:
#                 counter += 1
#                 if float(item['Volume']) >= high:
#                     high = float(item['Volume'])
#                 if float(item['Volume']) <= low:
#                     low = float(item['Volume'])
#                 sum_volume += float(item['Volume'])
#             else:
#                 li.append({'Year': date_year, 'Avg Volume': sum_volume/counter, 'Min Volume': low, 'Max Volume': high})
#                 low = float(item['Volume'])
#                 high = float(item['Volume'])
#                 counter = 1
#                 date_year = date.year




    # print(li)
    # with open('files\\PL.csv', "w") as csv_f:
    #     writer = csv.DictWriter(csv_f, ['Year', 'Avg Volume', 'Min Volume', 'Max Volume'])
    #     writer.writeheader()
    #     new_row = {'Year': date_year, 'Avg Volume': sum_volume/counter, 'Min Volume': low, 'Max Volume': high}
    #     writer.writerow(new_row)





