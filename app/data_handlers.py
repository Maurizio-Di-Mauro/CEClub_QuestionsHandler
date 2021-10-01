import os
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
    questions: [str] = []
    for index, row in df.itertuples():
        question: str = process_question(row)
        questions.append(question)

    pages: [[str]] = form_pages(questions)
    with open(os.path.join(config.RESULTS_LOCATION, "questions.html"), "w") as f:
        f.write(template.render(pages=pages))


def process_question(question: str) -> str:
    if question is None:
        return None

    #if conversion raised an error, return None
    try:
        question = str(question).strip()
    except:
        print("there was an error in row")
        return None

    return question


def form_pages(questions: [str]) -> [[str]]:
    amount = len(questions)
    # round up without using any libraries
    num_of_pages_needed: int = int(amount/12) + (amount%12 > 0)

    pages: [[str]] = []
    start_index = 0
    end_index = amount if amount < 12 else 12

    for i in range(num_of_pages_needed):
        pages.append(questions[start_index:end_index])
        start_index += 12
        if end_index + 12 > amount:
            end_index = amount
        else:
            end_index += 12
    return pages
