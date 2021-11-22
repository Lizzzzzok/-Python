class Exception:
    def __init__(self):
        self.numbers = []

    def create(self):
        print('To exit the code press !.')
        while True:
            try:
                number = int(input('Enter a value: '))
                self.numbers.append(number)
                print('Current list: ', self.numbers)
            except:
                print('You entered invalid value. To continue press ?, to stop !.')
                sym = input('Enter: ')
                if sym == '!':
                    return 'Finish. Your list:', self.numbers
                else:
                    print(Exception.create(attempt))


attempt = Exception()
print(attempt.create())
