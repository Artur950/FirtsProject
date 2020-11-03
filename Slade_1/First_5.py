# Создали функцию, которая считает, сколько символов состовляет прямоугольную форму
def count_the_characters():
    count_characters1 = ("###", "###", "###")
    count_characters2 = ("22222222", "22222222")
    count_characters3 = ("------------------")
    count_characters4 = ("", "")

    counter = 0
    for s in count_characters1:
        counter = counter + len(s)
    print('count_characters1 = ("###", "###", "###")->' + str(counter))

    counter = 0
    for s in count_characters2:
        counter = counter + len(s)
    print('count_characters2 = ("22222222", "22222222")->' + str(counter))

    counter = 0
    for s in count_characters3:
        counter = counter + len(s)
    print('count_characters3 = ("------------------")->' + str(counter))

    counter = 0
    for s in count_characters4:
        counter = counter + len(s)
    print('count_characters4 = ("", "")->' + str(counter))


count_the_characters()


