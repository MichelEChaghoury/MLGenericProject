import sys


class CustomException(Exception):
    """custom exception handling with error messaging

    Args:
        Exception (Exception): inheriting from the Exception class
    """

    def error_message_detail(self, error: str) -> str:
        """

        Args:
            error (str): the error text of the occured exception
            error_detail (sys): the sys module to extract details about the error

        Returns:
            str: the error message
        """
        _, _, exc_tb = sys.exc_info()

        file_name: str = exc_tb.tb_frame.f_code.co_filename if exc_tb is not None else 'unknown'
        line_number: int = exc_tb.tb_lineno if exc_tb is not None else 0
        error = str(error)

        error_message = f"""
        Error occured in python script name [{file_name}]
        line number [{line_number}]
        error message[{error}]
        """

        return error_message

    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = self.error_message_detail(error_message)

    def __str__(self):
        return self.error_message