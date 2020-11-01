def is_palindrome():
    source_string = "Чин зван мечем навзнич"
    invert_string = ''.join(reversed(source_string))
    if source_string == invert_string[::-1]:
        print("Является палиндромом")
    else:
        print("Не является палиндромом")


is_palindrome()