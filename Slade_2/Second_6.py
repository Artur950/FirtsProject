# Написали программу которая проверяет является ли строка палиндромом "Чин зван мечем навзнич"
def is_palindrome():
    source_string = "Чин зван мечем навзнич"
    tmp_string = source_string.replace(' ', '')
    invert_string = ''.join(reversed(tmp_string))
    if tmp_string.casefold() == invert_string.casefold():
        print("Является палиндромом")
    else:
        print("Не является палиндромом")


is_palindrome()
