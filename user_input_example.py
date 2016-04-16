
def salute():
    name = input("What is your name? ")
    return 'Hello, {}'.format(name)

def print_salute():
    print(salute())

if __name__ == '__main__':
    print_salute()