# Вывели по очереди все подстроки меньшие на один символ строки "Съешь ещё этих мягких французских булок, да выпей чаю"
# И их же задом наперед
def generate_substring():
    source_string = "Съешь ещё этих мягких французских булок, да выпей чаю"
    start_index = 0

    while start_index < len(source_string):
        print(source_string[start_index:len(source_string)])
        start_index += 1

    invert_string = ''.join(reversed(source_string))
    end_index = 1

    while end_index < len(invert_string):
        print(invert_string[0:end_index])
        end_index += 1
    print(invert_string)


generate_substring()