import requests
import json

from template import movie_template
from config import TMDB_KEY, LANG


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


    html = movie_template(movie)


    print(html)



def main():


    print("START MOVIE BOT")


    database = load_database()


    movies = get_movies()



    for movie in movies:


        movie_id = movie["id"]


        if movie_id in database:

            continue



        create_movie(movie)



        database.append(
            movie_id
        )



    save_database(database)


    print("END MOVIE BOT")




if __name__ == "__main__":

    main()
