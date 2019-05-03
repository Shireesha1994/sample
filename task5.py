def do_twice(f)
    f()
    f()

def print_twice():
    print('+','-','-','-','+', end='')
    print('-','-','-','+', end='')
    for i in range (5):
        print('\n / \n',end='')


do_twice(print_twice)

