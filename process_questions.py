from app import main

from config import Config




if __name__ == '__main__':
    config = Config()
    main(config, "questions.xlsx")
    