import os
import pandas as pd

#my imports
import app.file_handlers
import app.data_handlers




def main(config: "Config", filename: str):
    """
    The central code of this application. Binds modules together, 
    checks the input variables, creates necessary directories, 
    cleans up mess and etc.

    Parameters:
    config -- a Config object with all needed configuration stored 
                                                                inside;
    excel_filename -- a string with filename of a table with data.
                    The app expects it to be either: .csv, .xls, .xlsx
                    Example: 'data.csv'
    """
    # if the file-path can't pass the check, this will raise an exception
    file_handlers.file_validation(file_location=config.DATA_LOCATION, 
                                                            filename=filename)

    location = config.get_result_location()
    # create folders (directories) for the results, if they don't exist
    if not os.path.exists(location):
        os.makedirs(location)

    df = pd.read_excel(os.path.join(config.DATA_LOCATION, filename),
                        header=config.HEADER_ROW,
                        index_col=config.INDEX_COLUMN)

    data_handlers.handle_data(df=df, config=config)
        
