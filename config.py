import os
from datetime import datetime




class Config:
    """All my configurations are stored here, in Config"""
    DATA_LOCATION = "data" #here is stored location of excel tables directory.
    RESULTS_LOCATION = "results"
    RESULTS_FILENAME = "questions.html"
    FILENAME = "questions.xlsx"
    META_FILENAME = "questions_meta.txt"

    # for jinja locations
    JINJA_APP_LOCATION = "app" #your application python package
    JINJA_TEMPLATES_LOCATION = "templates" #folder with your templates in app

    # configuration for pandas
    HEADER_ROW = 0 # index (not including skipped rows) of a header row
    INDEX_COLUMN = 0 # "Name" columns

    def __init__(self, filename: str = "", meta_filename: str = ""):
        if filename != "":
            self.FILENAME = filename
        if meta_filename != "":
            self.META_FILENAME = meta_filename

    def get_meta_location(self) -> str:
        return os.path.join(self.RESULTS_LOCATION, self.META_FILENAME)

    def get_results_filename(self) -> str:
        filename: str = datetime.now().strftime('%d-%m-%YT%H:%M:%S') + "_" + \
                                                        self.RESULTS_FILENAME
        return os.path.join(self.RESULTS_LOCATION,filename)
