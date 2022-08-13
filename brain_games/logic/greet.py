import prompt


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    greet = 'Hello, ' + name + '!'
    print(greet)
    return name
