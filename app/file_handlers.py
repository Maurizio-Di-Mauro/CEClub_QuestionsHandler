import os

# importing my exceptions
from .errors import NotTableFileError




def file_validation(file_location: str, filename: str):
    #checks whether it is an excel table (or csv) and its existence
    if not os.path.exists( os.path.join(file_location, filename) ):
        #If there is no such file, raise FileNotFoundError
        raise FileNotFoundError
    if not filename.endswith(('.xls', '.xlsx', '.csv')):
        # if it is not an excel file, raise NotTableFileError
        raise NotTableFileError(filename)
