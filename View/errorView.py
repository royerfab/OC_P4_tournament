import re


class InputCheckView:
    def __init__(self):
        self.error_handler = ErrorHandlerView()

    def check_string(self, message):
        while True:
            user_input = input(message)
            if re.search('^[\\w ]{3,}$', user_input):
                return user_input
            self.error_handler.display_error('Mauvais format')

    def check_int(self, message):
        while True:
            user_input = input(message)
            if user_input.strip().isdigit():
                return user_input
            self.error_handler.display_error('Mauvais format')

    def check_date(self, message):
        while True:
            user_input = input(message)
            if re.match("^\d{4}/\d{2}/\d{2}$", user_input):
                return user_input
            self.error_handler.display_error('Mauvais format')

    def check_sex(self, message):
        while True:
            user_input = input(message)
            if user_input == 'M' or user_input == 'F':
                return user_input
            self.error_handler.display_error('Mauvais format (M ou F)')

    def input_in_array_of_int(self, message, array):
        while True:
            user_input = int(input(message))
            if user_input in array:
                return user_input
            self.error_handler.display_error('numéro inconnu')

    def time_option(self):
        while True:
            print('Timing de la partie:')
            print('1: Bullet')
            print('2: Blitz')
            print('3: Rapid')
            user_input = input('Votre choix: ')
            if user_input == '1':
                return 'Bullet'
            elif user_input == '2':
                return 'Blitz'
            elif user_input == '3':
                return 'Rapid'
            else:
                self.error_handler.display_error('mauvais format')


class ErrorHandlerView:
    @staticmethod
    def display_error(error):
        print(f'\033[31mErreur\033[00m: {error}')
