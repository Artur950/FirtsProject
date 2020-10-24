def generate_name():
    S_begin='JKLMNOPQ'
    S_end='ack'
    for i in S_begin:
        if i == 'O' or i == 'Q':
            print(i+'u'+S_end)
        else:
            print(i+S_end)


generate_name()