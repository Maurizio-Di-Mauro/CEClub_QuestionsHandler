import os
import pandas as pd

#my imports
import app.file_handlers
import app.data_handlers




def main(config: "Config"):
    """
    The central code of this application. Binds modules together, 
    checks the input variables, creates necessary directories, 
    cleans up mess and etc.

    Parameters:
    config -- a Config object with all needed configuration stored 
                                                                inside;
    """
    # if the file-path can't pass the check, this will raise an exception
    file_handlers.file_validation(file_location=config.DATA_LOCATION, 
                                                    filename=config.FILENAME)

    location = config.RESULTS_LOCATION
    # create folders (directories) for the results, if they don't exist
    if not os.path.exists(location):
        os.makedirs(location)

    if input("Do you need to print questions? Y/N: ") in ("N", "n"):
        config.set_is_testing(False)

    # prepare metafile
    file_handlers.prepare_metafile(config.get_meta_location())

    df = pd.read_excel(os.path.join(config.DATA_LOCATION, config.FILENAME),
                        header=config.HEADER_ROW,
                        index_col=config.INDEX_COLUMN)

    data_handlers.handle_data(df=df, config=config)
        
