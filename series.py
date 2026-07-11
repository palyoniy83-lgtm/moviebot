import requests
import json

from config import TMDB_KEY, LANG
from ucoz import create_article


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



    data = response.json()



    if "results" not in data:

        print(data)

        return []



    return data["results"]




def series_template(item):


    title = item.get(
        "name",
        "Без назви"
    )


    year = item.get(
        "first_air_date",
        ""
    )[:4]



    poster = (

        "https://image.tmdb.org/t/p/w500"

        +

        str(
            item.get(
                "poster_path"
            )
        )

    )



    rating = item.get(
        "vote_average",
        0
    )



    description = item.get(
        "overview",
        ""
    )



    html = f"""

<center>

<img src="{poster}" width="300">

</center>


<h1>
{title} ({year})
</h1>


<p>

⭐ Рейтинг:
{rating}

</p>


<h2>
Опис
</h2>


<p>
{description}
</p>


<h2>
Дивитися онлайн
</h2>


ВАШ_ПЛЕЄР


"""



    return html




def create_series(item):


    title = item.get(
        "name"
    )


    html = series_template(item)



    create_article(

        title,

        html,

        "serials"

    )


    print(
        "Додано серіал:",
        title
    )




def main():


    print(
        "===== START SERIES BOT ====="
    )



    database = load_database()


    series = get_series()



    count = 0



    for item in series:


        series_id = item["id"]



        if series_id in database:

            print(
                "Пропуск:",
                item["name"]
            )

            continue




        create_series(item)



        database.append(
            series_id
        )



        count += 1




    save_database(database)



    print(
        "Нових серіалів:",
        count
    )


    print(
        "===== END SERIES BOT ====="
    )




if __name__ == "__main__":

    main()
