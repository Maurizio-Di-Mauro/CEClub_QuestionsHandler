import os
from app import utility




class Config:
    """All my configurations are stored here, in Config"""
    IS_TESTING = True # If set to False, questions will be printed

    # In DATA_LOCATIONis stored location of excel tables directory.
    DATA_LOCATION = "data"
    RESULTS_LOCATION = "results"
    RESULTS_FILENAME = "questions.html"
    FILENAME = "questions.xlsx"
    META_FILENAME = "questions_meta.txt"

    # for jinja locations
    JINJA_APP_LOCATION = "app" # your application python package
    # folder with your Jinja templates for app
    JINJA_TEMPLATES_LOCATION = "templates"

    # configuration for pandas
    HEADER_ROW = 0 # index (not including skipped rows) of a header row
    INDEX_COLUMN = 0 # "Name" columns

    def __init__(self, filename: str = "", meta_filename: str = ""):
        if filename != "":
            self.FILENAME = filename
        if meta_filename != "":
            self.META_FILENAME = meta_filename

    def get_data_location(self) -> str:
        return os.path.join(self.DATA_LOCATION, self.FILENAME)

    def get_meta_location(self) -> str:
        return self.get_file_path(self.RESULTS_LOCATION, self.META_FILENAME)

    def get_results_file_path(self) -> str:
        return self.get_file_path(self.RESULTS_LOCATION, self.RESULTS_FILENAME)

    def get_file_path(self, dirname: str, filename: str) -> str:
        filename = utility.get_current_sunday().strftime("%d-%m-%y") + filename
        return os.path.join(dirname, filename)

    def set_is_testing(self, is_testing: bool = True):
        self.IS_TESTING = bool(is_testing)
