import os




class Config:
    """All my configurations are stored here, in Config"""
    DATA_LOCATION = "data" #here is stored location of excel tables directory.
    RESULTS_LOCATION = "results"
    META_LOCATION = "meta" #final directory name for meta files
    QUESTIONS_LOCATION = "html" #final directory name for questions files

    #for jinja locations
    JINJA_APP_LOCATION = "app" #your application python package
    JINJA_TEMPLATES_LOCATION = "templates" #folder with your templates in app
