import requests
import json

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


    if "results" not in data:

        print("Помилка TMDB:")

        print(data)

        return []


    return data["results"]




def create_movie(movie):


    title = movie.get(
        "title",
        "Без назви"
    )


    html = movie_template(movie)



    create_article(

        title,

        html,

        "films"

    )



    print(
        "Додано:",
        title
    )




def main():


    print(
        "===== START MOVIE BOT ====="
    )


    database = load_database()


    movies = get_movies()



    if not movies:

        print(
            "Фільми не знайдені"
        )

        return



    count = 0



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


        count += 1




    save_database(database)



    print(
        "Додано нових фільмів:",
        count
    )


    print(
        "===== END MOVIE BOT ====="
    )




if __name__ == "__main__":

    main()
