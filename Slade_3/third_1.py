#Напишите функцию которая принимает аргументы 2, 123.4567, 10000, 12345.67
# и возвращает строку 'file_002 :   123.46, 1.00e+04, 1.23e+04'
# половина
def arguments(file_name, first_number, second_number, third_number):
    f = open("file_00" + str(file_name), "w+")
    f.write(str(first_number)+"\n")
    f.write(str(second_number)+"\n")
    f.write(str(third_number)+"\n")
    print(filename + )
    f.close()


arguments(2, 123.4567, 10000, 12345.67)