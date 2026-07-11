import requests
import json

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




def get_series():

    url = "https://api.themoviedb.org/3/tv/popular"


    params = {

        "api_key": TMDB_KEY,

        "language": LANG

    }


    response = requests.get(
        url,
        params=params
    )


    data=response.json()


    return data.get(
        "results",
        []
    )




def show_series(item):


    print("----------------------")


    print(
        "Серіал:",
        item["name"]
    )


    print(
        "Рейтинг:",
        item["vote_average"]
    )


    print(
        "Опис:",
        item["overview"]
    )




def main():


    print(
        "START SERIES BOT"
    )


    database=load_database()


    series=get_series()



    for item in series:


        sid=item["id"]



        if sid in database:

            continue



        show_series(item)



        database.append(
            sid
        )



    save_database(database)



    print(
        "END SERIES BOT"
    )




if __name__=="__main__":

    main()
