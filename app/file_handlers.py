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


def read_metadata(metafile: str) -> [str]:
    metadata: [str] = []
    with open(metafile, 'r') as f:
        for line in f:
            metadata.append(line.rstrip())
    return metadata


def render_results(questions: [str],  filename: str, metafile: str, template):
    with open(filename, "w") as f:
        f.write(template.render(questions=questions))
