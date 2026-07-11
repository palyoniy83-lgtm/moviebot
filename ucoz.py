import json
import os


FILE = "ucoz_articles.json"



def load_articles():

    if not os.path.exists(FILE):

        return []


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)




def save_articles(data):

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )




def create_article(title, html, category):


    articles = load_articles()


    article = {

        "title": title,

        "category": category,

        "content": html

    }



    articles.append(article)



    save_articles(
        articles
    )


    print(
        "Створено матеріал:",
        title
    )
