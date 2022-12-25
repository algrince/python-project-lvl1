import prompt


def welcome_user():
    '''Greets user with name from input'''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    greet = 'Hello, ' + name
    print(greet)


def generate_answer(bool):
    '''Returns "yes" or "no" for True or False'''
    return 'yes' if bool else 'no'
