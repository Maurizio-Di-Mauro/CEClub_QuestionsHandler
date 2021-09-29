import os




class Config:
    """All my configurations are stored here, in Config"""
    DATA_LOCATION = "data" #here is stored location of excel tables directory.
    RESULTS_LOCATION = "results"

    # for jinja locations
    JINJA_APP_LOCATION = "app" #your application python package
    JINJA_TEMPLATES_LOCATION = "templates" #folder with your templates in app

    # configuration for pandas
    HEADER_ROW = 0 # index (not including skipped rows) of a header row

    def get_result_location(self) -> str:
        return os.path.join(self.RESULTS_LOCATION)
