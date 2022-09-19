test_msg = 'There are so many niggers out there, waiting for our wallets.'


class CustomException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"CustomException: banned word was found ( ."


try:
    if 'nigg' in test_msg:
        raise CustomException(test_msg)
    print('Everything okay.')
except CustomException as exception:
    print('Ohh, shame on you.')
