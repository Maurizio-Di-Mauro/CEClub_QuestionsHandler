import os
from datetime import datetime

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


def prepare_metafile(metafile: str):
    # checks existence of metafile
    if not (os.path.exists(metafile)):
        with open(metafile, "w"):
            # just create an empty metafile
            pass



def is_question_printed(timestamp: datetime, metafile: str) -> bool:
    str_ts: str = timestamp.strftime('%d-%m-%Y, %H:%M:%S')
    with open(metafile, 'r') as f:
        for line in f:
            # loop through lines
            if str_ts == line.rstrip():
                # if there is such timestamp, stop looping
                return True
        return False
