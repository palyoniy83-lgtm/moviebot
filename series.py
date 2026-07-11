import requests
import json
import os

from config import TMDB_KEY, LANG
from ucoz import create_article
from series_categories import get_series_category


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

        print("Помилка TMDB:")

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



    rating = item.get(
        "vote_average",
        0
    )



    poster_path = item.get(
        "poster_path"
    )



    if poster_path:

        poster = (
            "https://image.tmdb.org/t/p/w500/"
            +
            poster_path
        )

    else:

        poster = ""



    description = item.get(
        "overview",
        "Опис відсутній"
    )



    html = f"""

<div class="series-card">


<center>

<img src="{poster}"
style="width:300px;border-radius:10px;">

</center>



<h1>

{title} ({year})

</h1>


<hr>


<p>

<b>⭐ Рейтинг:</b>

{rating}/10

</p>



<h2>
Опис серіалу
</h2>


<p>

{description}

</p>



<h2>
Дивитися онлайн
</h2>


<div style="
background:#111;
padding:20px;
color:white;
text-align:center;
">


ТУТ БУДЕ ПЛЕЄР


</div>



<h2>
Трейлер
</h2>


<div>

ТУТ БУДЕ YOUTUBE

</div>



</div>

"""


    return html




def create_series(item):


    title = item.get(
        "name",
        "Без назви"
    )



    html = series_template(item)



    os.makedirs(
        "results/series",
        exist_ok=True
    )



    filename = title.replace(
        "/",
        "_"
    )



    path = (
        "results/series/"
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



    category = get_series_category(item)



create_article(

    title,

    html,

    category

)



    print(
        "Створено серіал:",
        title
    )




def main():


    print(
        "===== START SERIES BOT ====="
    )



    database = load_database()



    series = get_series()



    if not series:

        print(
            "Серіали не знайдені"
        )

        return



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
