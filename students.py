import openpyxl
import collections


def read_excel_file(file_name):
    workbook = openpyxl.load_workbook(f"{file_name}")

    Row = collections.namedtuple("Row", "No Name Birth_Year Address")
    worksheet = workbook["Sheet1"]

    data = []
    is_header_row = True
    # count = 0
    for row in worksheet.rows:

        if is_header_row:
            is_header_row = False
            continue

        data.append(((Row(*row).No.value)
                        , (Row(*row).Name.value)
                        , (Row(*row).Birth_Year.value)
                        , (Row(*row).Address.value),))
        # if count >= 5:
        #     break
        #
        #     data.append(Row(*row))
        # count += 1

        # data.sort(key=lambda x: x[0], reverse=True)
    return data


def append_row(file_name, data):
    workbook = openpyxl.load_workbook("Excel_Example.xlsx")

    worksheet = workbook["Sheet1"]

    for row in data:
        worksheet.append(row)

    workbook.save(f"{file_name}")

    return workbook


def main():
    data_students = read_excel_file("Excel_Example.xlsx")
    # print(data_students)
    data_students.sort(key = lambda x:x[0], reverse=False)
    print(data_students)
    # for student in data_students:
    #     print(student)
    #
    # data = ((9, "Hoang", 1999, "Quang Nam"),)
    #
    # append_row("StudentsInfo.xlsx", data)


if __name__ == '__main__':
    main()
