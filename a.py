def right_justify(s):
    str_len = len(s)
    count = 70 - str_len
    print(count)
    i=1
    cat = " "
    while i < count:
        cat = " "+cat
        print(cat)
        i=i+1
    print(s)
right_justify("shireesha")