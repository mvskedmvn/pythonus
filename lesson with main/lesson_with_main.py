def hello(name=''):
    print(f'Hello {name}')

def enter_age(age=''):
    print(f'age {age}')

def main():
    name = input("Enter your name: ")
    hello(name = name)
    input_age = input('Enter your age: ')
    enter_age(age = input_age)

if __name__ == '__main__':
    main()