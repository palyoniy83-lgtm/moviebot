def movie_template(movie):


    title = movie.get(
        "title",
        movie.get("name","")
    )


    year = movie.get(
        "release_date",
        movie.get("first_air_date","")
    )[:4]


    rating = movie.get(
        "vote_average",
        0
    )


    poster = (
        "https://image.tmdb.org/t/p/w500"
        +
        str(movie.get("poster_path"))
    )


    description = movie.get(
        "overview",
        "Опис відсутній"
    )



    html = f"""

<center>

<img src="{poster}" width="300">

</center>


<h1>
{title} ({year})
</h1>


<hr>


<b>⭐ Рейтинг:</b>

{rating}


<br><br>


<b>📅 Рік:</b>

{year}


<br><br>


<h2>
Опис
</h2>


<p>
{description}
</p>


<h2>
Дивитися онлайн
</h2>


<div>

ВАШ_ПЛЕЄР_ТУТ

</div>


<h2>
Трейлер
</h2>


<div>

ВАШ_ТРАЙЛЕР_ТУТ

</div>

"""


    return html
