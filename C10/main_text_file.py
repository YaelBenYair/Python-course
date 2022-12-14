from C10.text_file import CsvFile, TxtFile, JsonFile

if __name__ == '__main__':
    csv_file = CsvFile("D:\\Full Stack Python\\Python_Course\\C10\\files\\text.csv", ';')
    csv_file2 = CsvFile('D:\\Full Stack Python\\Python_Course\\C10\\files\\text_4.csv', ",")
    txt = TxtFile("D:\\Full Stack Python\\Python_Course\\C10\\files\\alice_in_wonderland.txt")
    txt2 = TxtFile("D:\\Full Stack Python\\Python_Course\\C10\\files\\txt12.txt")
    txt3 = TxtFile("D:\\Full Stack Python\\Python_Course\\C10\\files\\txt34.txt")
    json_file = JsonFile("D:\\Full Stack Python\\Python_Course\\C10\\files\\example_2.json")
    json_file2 = JsonFile("D:\\Full Stack Python\\Python_Course\\C10\\files\\example_2 - Copy.json")
    # files_list = [csv_file, txt]
    # for f in files_list:
    #     print(f.get_content())
    print("file size csv: ", csv_file.get_file_size())
    print("number of row: ", csv_file.get_rows_num())
    print("number of columns: ", csv_file.get_columns_num())
    print("get row: ", csv_file.get_row(2))
    print("get column: ", csv_file.get_column(1))
    print("get cell: ", csv_file.get_cell(1, 2))
    print("content: ", csv_file.get_content())
    print(" + : ", csv_file + csv_file2)
    print()

    print("txt words num: ", txt.get_words_num())
    print("txt words avg: ", txt.get_avg_word_len())
    # print(" + : ", txt2 + txt3)
    # print(" + : ", txt2 + json_file2)
    print()

    print("json 1 is list?: ", json_file.is_list())
    print("json 1 is object?: ", json_file.is_object())
    print("json 2 is list?: ", json_file2.is_list())
    print("json 2 is object?: ", json_file2.is_object())
    # csv_file = CsvFile("/Users/valeria/src/morning-ninjas/lesson9/files/data/AAPL.csv")
