import requests
import json
import os

from config import TMDB_KEY, LANG
from template import movie_template
from ucoz import create_article
from categories import get_category


DATABASE = "database.json"



def load_database():

    try:
        with open(
            DATABASE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []



def save_database(data):

    with open(
        DATABASE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )



def get_movies():

    url = "https://api.themoviedb.org/3/movie/popular"


    params = {

        "api_key": TMDB_KEY,

        "language": LANG

    }


    response = requests.get(
        url,
        params=params
    )


    data = response.json()


    return data.get(
        "results",
        []
    )



def create_movie(movie):


    title = movie.get(
        "title",
        "Без назви"
    )


    html = movie_template(movie)


    category = get_category(movie)



    os.makedirs(
    "results/movies",
    exist_ok=True
)


    filename = title.replace(
        "/",
        "_"
    )


    path = (
    "results/movies/"
    +
    filename
    +
    ".html"
)



    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)



    create_article(

        title,

        html,

        category

    )


    print(
        "Створено:",
        title
    )


    print(
        "Категорія:",
        category
    )



def main():


    print(
        "===== START MOVIE BOT ====="
    )


    database = load_database()


    movies = get_movies()



    for movie in movies:


        movie_id = movie["id"]



        if movie_id in database:

            print(
                "Пропуск:",
                movie["title"]
            )

            continue



        create_movie(movie)



        database.append(
            movie_id
        )



    save_database(database)



    print(
        "===== END MOVIE BOT ====="
    )



if __name__ == "__main__":

    main()
