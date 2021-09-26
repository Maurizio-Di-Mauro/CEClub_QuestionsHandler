# define Python user-defined exceptions
class MyBaseError(Exception):
    """Base class for other exceptions"""
    def __init__(self, message, base_message=None, *args):
        self.base_message = base_message
        self.message = message

    def __str__(self):
        if self.base_message is None:
            return self.message
        return self.message + " '" + str(self.base_message) + "'"


class NotTableFileError(MyBaseError):
    """Exception raised for errors in checking for the excel tables.
    
    Attributes:
        filename -- input file which caused the error (e.g., it is not an excel)
        message -- explanation of the error
    """
    def __init__(self, filename: str, message: str =\
            "The file extension is not supported. Use .csv, .xls, .xlsx files"):
        self.filename: str = filename
        self.message: str = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.filename} -> {self.message}'