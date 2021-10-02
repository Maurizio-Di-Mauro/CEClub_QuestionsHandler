import os
import re # regular expressions for removing whitespaces
from datetime import datetime

from jinja2 import Environment, PackageLoader, select_autoescape




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
    questions: [str] = []
    for index, row in df.itertuples():
        question: str = process_question(row)
        if question is not None:
            questions.append(question)

    with open(os.path.join(config.RESULTS_LOCATION, "questions.html"), "w") as f:
        f.write(template.render(questions=questions))


def process_question(question: str) -> str:
    if question is None:
        return None

    #if conversion raised an error, return None
    try:
        question = str(question).strip()
    except:
        return None

    # get rid of extra spaces between words
    question = re.sub(" +", " ", question)

    return question
