def person(name, surname, birth, city, email, phone):
    return ' '.join([name, surname, birth, city, email, phone])


print(person(input('Enter your name: '), input('Enter your surname: '), input('Enter your birth date: '),
             input('Enter your city: '), input('Enter your email: '), input('Enter you phone number: ')))
