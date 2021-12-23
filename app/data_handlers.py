import os
import re # regular expressions for removing whitespaces
from datetime import datetime, timedelta

from jinja2 import Environment, PackageLoader, select_autoescape

# my imports
from . import file_handlers, utility




def handle_data(df: "DataFrame", config: "Config"):
    # set configuration for jinja
    jinja_env = Environment(
        loader=PackageLoader(config.JINJA_APP_LOCATION, 
                            config.JINJA_TEMPLATES_LOCATION),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    # load template
    template = jinja_env.get_template('questions_template.html')

    # process the data
    df.dropna(inplace=True) # skip empty rows
    timestamps: [str] = []
    questions: [str] = []
    for index, row in df.itertuples():
        timestamp: datetime = index.to_pydatetime()
        # skip the question if it is from previous week
        if timestamp < utility.get_last_sunday():
            continue
        question: str = process_question(row)
        if question is not None:
            questions.append(question)

    if len(questions) == 0:
        return

    file_handlers.render_results(
        questions=questions,
        filename=config.get_results_file_path(), 
        metafile=config.get_meta_location(),
        template=template
    )


def process_question(question: str) -> str:
    if question is None:
        return None

    #if conversion raised an error, return None
    try:
        question = str(question).strip()
    except:
        return None

    # get rid of extra space characters between words
    question = re.sub(r"\s+", " ", question)

    # Ignore one-word and two-word questions
    if len(question.split()) < 3:
        return None

    # Ignore digits-only or "nonletter symbols" only questions
    test_question: str = re.sub(" ", "", question)
    if re.fullmatch(r"[\d\W_]+", test_question):
        return None

    # Ignore questions that are only composed of one or two characters
    test_question = test_question.lower()
    if len(set(test_question)) < 3:
        return None

    return question
