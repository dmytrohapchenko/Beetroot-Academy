class Validate:
    def __init__(self, email):
        self.email = email

    def email_check(self):
        if (type(self.email) == str and
                '@' in self.email and
                8 <= len(self.email) <= 36):
            return True
        return False

    def printer(self):
        if self.email_check():
            print('Everything is ok')
        else:
            print('Something is wrong')


validate = Validate('dmytrohapchenko@gmail.com')
validate.printer()
